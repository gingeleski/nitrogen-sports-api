import cfscrape
import requests
import time

BASE_URL = 'https://nitrogensports.eu/'
PING_URL_START = 'socket.io/?EIO=3&transport=polling'

class NitrogenApi():
    """
    Interface to programmatically interact with Nitrogen Sports
    """

    def __init__(self):
        """
        Constructor
        """

        self.session = None
        self.polling_sid = None
        self.ping_interval = -1
        self.ping_count = 0

    def session_check(self):
        """
        Check for session existence
        """
        if self.session is None:
            self.session = cfscrape.CloudflareScraper()
            self.pass_cloudflare()

    def pass_cloudflare(self):
        """
        Complete the Cloudflare check for this session

        TODO
        """
        self.session.get(BASE_URL, verify=False)

    def login(self):
        """
        Login
        """
        self.session_check()
        username = 'flot989'
        password = 'Thr0wAway1'
        login_url = BASE_URL + 'php/login/login.php'
        payload = {'username': username, 'password': password, 'otp': '', 'captcha_code': ''}
        self.session.post(login_url, data=payload, verify=False)

    def ping(self):
        """
        Send the server heartbeat / keep-alive / ping
        """
        unix_time = int(time.time())
        ping_url = BASE_URL + PING_URL_START + '&t=' + str(unix_time)
        ping_url = ping_url + '-' + str(self.ping_count)
        if self.ping_count == 0:
            req = self.session.get(ping_url, verify=False)
            poll_info_json = req.json()
            self.polling_sid = poll_info_json['sid']
            self.ping_interval = poll_info_json['pingInterval']
        else:
            ping_url = ping_url + '&sid=' + self.polling_sid
        self.ping_count += 1

    def keep_alive(self, duration=None):
        """
        Keep the session alive by pinging at a normal interval

        Args:
            duration: how long to keep alive, in seconds
        """
        now = int(time.time())
        start_time = now
        next_time = now
        if duration == None or now - start_time > duration:
            pass  # TODO

    def find_upcoming_games(self, sport='Soccer'):
        """
        Request upcoming games for the given sport
        """
        games_url = BASE_URL + 'php/query/findgames_upcomming.php'
        payload = {'sport': sport}
        req = self.session.post(games_url, data=payload, verify=False)
        if req.status_code == requests.codes.ok:
            return req.json()
        return None

# The following is debug/test while developing this API...
if __name__ == '__main__':
    NITRO_API = NitrogenApi()
    NITRO_API.login()
    time.sleep(0.5)
    NITRO_API.ping()
