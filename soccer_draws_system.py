import json
from nitrogen import NitrogenApi
import time

USE_TEST_DATA = True

games_json = None

if USE_TEST_DATA is True:
    with open('test_upcoming_games_json.txt') as data_file:    
        games_json = json.load(data_file)
else:
    NITRO_API = NitrogenApi()
    NITRO_API.login('flot989', 'Thr0wAway1')
    time.sleep(1)
    games_json = NITRO_API.find_upcoming_games()
    time.sleep(1)
    NITRO_API.logout()

for event in games_json['data']:
    print('EVENT: ' + event['event_id'])
    for period in event['period']:
        print('\t' + 'PERIOD: ' + period['period_id'])
        if 'moneyLine' in period and period['moneyLine'] is not None:
            for line in period['moneyLine']:
                if 'drawPrice' in line:
                    print('\t\t' + 'Found avail draw bet @ ' + line['drawPrice'])
