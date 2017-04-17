import json
from nitrogen import NitrogenApi
import time

USE_TEST_DATA = True

def find_next_bet(games_json):
    """
    Find next bet to place

    Args:
        games_json (dict): JSON response from #get_upcoming_games
    """

    for event in games_json['data']:
        for period in event['period']:
            if 'moneyLine' in period and period['moneyLine'] is not None:
                for line in period['moneyLine']:
                    if 'drawPrice' in line and line['drawPrice'] is not None:
                        draw_price = float(line['drawPrice'])
                        if draw_price >= 2.8 and draw_price <= 3.2:
                            print('Found draw bet @ ' + str(draw_price))


if __name__ == '__main__':

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

    find_next_bet(games_json)

    # TODO next steps

    # POST /php/query/betslip_addBet.php HTTP/1.1
    # event_id=711667105&period_id=387060156&bet_type=moneyline_draw&bet_id=-1

    # POST /php/query/betslip_bet_adjustRisk.php HTTP/1.1
    # bet_id=16635862&risk=0.05000

    # POST /php/query/betslip_get_place.php HTTP/1.1

    # POST /php/query/betslip_confirm.php HTTP/1.1
    # betslip_type=straight&teaser_id=0&coupon_id=
