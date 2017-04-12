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

        self.polling_sid = None
        self.ping_count = 0

    def login(self):
        """
        Login
        """
        #username = 'YOUR_USERNAME'
        username = 'flot989'
        #password = 'YOUR_PASSWORD'
        password = 'Thr0wAway1'
        login_url = BASE_URL + 'php/login/login.php'
        payload = {'username': username, 'password': password, 'otp': '', 'captcha_code': ''}
        requests.post(login_url, data=payload, verify=False)

    def ping(self):
        """
        TODO TODO
        Send the server heartbeat / keep-alive / ping
        """
        unix_time = int(time.time())
        ping_url = BASE_URL + PING_URL_START + '&t=' + str(unix_time) + '-' + str(self.ping_count)
        self.ping_count += 1
        requests.post(ping_url)

# The following is debug/test while developing this API...
if __name__ == '__main__':
    NITRO_API = NitrogenApi()
    NITRO_API.login()
