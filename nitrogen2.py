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
        self.ping_count = 0

    def session_check(self):
        """
        Check for session existence
        """
        if self.session is None:
            self.session = requests.Session()

    def do_cloudflare(self):
        """
        Complete the Cloudflare check for this session
        
        TODO
        """
        pass

    def login(self):
        """
        Login
        """
        self.session_check()
        #username = 'YOUR_USERNAME'
        username = 'flot989'
        #password = 'YOUR_PASSWORD'
        password = 'Thr0wAway1'
        login_url = BASE_URL + 'php/login/login.php'
        payload = {'username': username, 'password': password, 'otp': '', 'captcha_code': ''}
        self.session.post(login_url, data=payload, verify=False)

    def ping(self):
        """
        Send the server heartbeat / keep-alive / ping

        TODO fix
        """
        unix_time = int(time.time())
        ping_url = BASE_URL + PING_URL_START + '&t=' + str(unix_time) + '-' + str(self.ping_count)
        self.session.post(ping_url, verify=False)
        self.ping_count += 1

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
