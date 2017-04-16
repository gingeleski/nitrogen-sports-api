import cfscrape
import json
import requests
import time

# Suppress HTTPS warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

BASE_URL = 'https://nitrogensports.eu/'
PING_URL_START = 'socket.io/?EIO=3&transport=polling'

class NitrogenApi():
    """
    Interface to programmatically interact with Nitrogen Sports
    """

    def __init__(self, auto_start_session=True):
        """
        Constructor
        """

        self.session = None
        self.polling_sid = None
        self.ping_interval = -1
        self.ping_count = 0
        if auto_start_session is True:
            self.new_session()

    def new_session(self):
        """
        Launch a new session
        """

        self.session = cfscrape.CloudflareScraper()
        self.pass_cloudflare()

    def pass_cloudflare(self):
        """
        Complete the Cloudflare check for this session
        """

        self.session.get(BASE_URL, verify=False)

    def login(self):
        """
        Login
        """

        username = 'flot989'
        password = 'Thr0wAway1'
        login_url = BASE_URL + 'php/login/login.php'
        payload = {'username': username, 'password': password, 'otp': '', 'captcha_code': ''}
        self.session.post(login_url, data=payload, verify=False)

    def logout(self):
        """
        Logout
        """

        logout_url = BASE_URL + 'php/login/logout.php'
        req = self.session.post(logout_url, verify=False)
        if req.status_code != requests.codes.ok:
            raise RuntimeError('Response to #logout not OK')

    def ping(self):
        """
        Send the server heartbeat / keep-alive / ping
        """

        unix_time = int(time.time())
        ping_url = BASE_URL + PING_URL_START + '&t=' + str(unix_time)
        ping_url = ping_url + '-' + str(self.ping_count)
        req = None
        if self.ping_count == 0:
            req = self.session.get(ping_url, verify=False)
            poll_info_json = json.loads(req.text[req.text.find('{'):])
            self.polling_sid = poll_info_json['sid']
            self.ping_interval = poll_info_json['pingInterval'] / 1000
        else:
            ping_url = ping_url + '&sid=' + self.polling_sid
            if self.ping_count < 3:
                req = self.session.get(ping_url, verify=False)
            else:
                req = self.session.post(ping_url, verify=False)
        self.ping_count += 1

    def keep_alive(self, duration=None):
        """
        Keep the session alive by pinging at a normal interval

        Args:
            duration: how long to keep alive, in seconds
        """

        now = int(time.time())
        if duration is not None:
            end_time = now + duration
        else:
            end_time = None
        next_time = now
        looping = True
        while looping is True:
            if duration is not None and now > end_time:
                looping = False
            elif now >= next_time:
                self.ping()
                next_time = now + self.ping_interval
            time.sleep(1)
            now = int(time.time())

    def get_betslip(self):
        """
        Get current betslip
        """

        get_url = BASE_URL + 'php/query/betslip_get.php'
        req = self.session.post(get_url, verify=False)
        if req.status_code == requests.codes.ok:
            return req.json()
        else:
            raise RuntimeError('Response to #get_betslip not OK')

    def find_upcoming_games(self, sport='Soccer'):
        """
        Request upcoming games for the given sport
        """

        games_url = BASE_URL + 'php/query/findgames_upcomming.php'
        payload = {'sport': sport}
        req = self.session.post(games_url, data=payload, verify=False)
        if req.status_code == requests.codes.ok:
            return req.json()
        else:
            raise RuntimeError('Response to #find_upcoming_games not OK')


# The following is debug/test while developing this API...
if __name__ == '__main__':
    NITRO_API = NitrogenApi()
    NITRO_API.login()
    time.sleep(1)
    NITRO_API.get_betslip()
    time.sleep(1)
    NITRO_API.logout()
