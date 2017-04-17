import json
from nitrogen import NitrogenApi
import time

# Constants
MINUTES_TO_SECONDS = 3600

# Betting System Parameters
USE_TEST_DATA = True
RETRY_WAIT_TIME = 20 * MINUTES_TO_SECONDS
BETTING_UNIT = 0.002
MIN_ODDS = 2.85
MAX_ODDS = 3.45

def find_next_bet(games_json):
    """
    Find next bet to place

    Args:
        games_json (dict): JSON response from #get_upcoming_games

    Returns:
        None: Indicates there is no suitable bet available yet

        Bet object: Info on a suitable bet to do next
            {
                event_id (str),
                period_id (str),
                bet_type (str),
                bet_id (str)
            }
    """

    for event in games_json['data']:
        event_id = event['event_id']
        for period in event['period']:
            period_id = period['period_id']
            if 'moneyLine' in period and period['moneyLine'] is not None:
                for line in period['moneyLine']:
                    if 'drawPrice' in line and line['drawPrice'] is not None:
                        draw_price = float(line['drawPrice'])
                        if draw_price >= MIN_ODDS and draw_price <= MAX_ODDS:
                            return {event_id, period_id, 'moneyline_draw', '-1'}
    return None

def continue_betting():
    """
    Indicates whether betting should continue
    """
    return True


if __name__ == '__main__':

    games_json = None
    bet_in_progress = False

    while True:

        if bet_in_progress is False:

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

            next_bet = find_next_bet(games_json)

            if next_bet is None:
                time.sleep(RETRY_WAIT_TIME)
            else:
                pass  # TODO next steps

                # POST /php/query/betslip_addBet.php HTTP/1.1
                # event_id=711667105&period_id=387060156&bet_type=moneyline_draw&bet_id=-1

                # POST /php/query/betslip_bet_adjustRisk.php HTTP/1.1
                # bet_id=16635862&risk=0.05000

                # POST /php/query/betslip_get_place.php HTTP/1.1

                # POST /php/query/betslip_confirm.php HTTP/1.1
                # betslip_type=straight&teaser_id=0&coupon_id=

        else:
            pass  # TODO check for result of this bet - win? lose?

        if continue_betting() is False:
            break
