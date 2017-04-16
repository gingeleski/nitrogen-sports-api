from nitrogen import NitrogenApi
import time

NITRO_API = NitrogenApi()
NITRO_API.login('flot989', 'Thr0wAway1')
time.sleep(1)
games = NITRO_API.find_upcoming_games()
print(games)
time.sleep(1)
NITRO_API.logout()
