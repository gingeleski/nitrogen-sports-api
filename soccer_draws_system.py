import json
from nitrogen import NitrogenApi
import time

# Global constants
NITRO_API = None
MINUTES_TO_SECONDS = 3600

# Nitrogen credentials
NITROGEN_USERNAME = 'flot989'
NITROGEN_PASSWORD = 'Thr0wAway1'

# Betting system parameters
RETRY_WAIT_TIME = 20 * MINUTES_TO_SECONDS
BETTING_UNIT = 0.002
MIN_ODDS = 2.85
MAX_ODDS = 3.45
MAX_BET_TIER = 13
BANKROLL_GOAL = None  # infinity

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
                            return {'event_id': event_id,
                                    'period_id': period_id,
                                    'bet_type': 'moneyline_draw',
                                    'bet_id': '-1'}
    return None

def get_bet_amount(tier_num):
    """
    Get appropriate bet amount for given tier

    Args:
        tier_num (int)
    """

    bet_amount = BETTING_UNIT
    if tier_num >= 2:
        bet_amount *= 2.0
        if tier_num >= 3:
            bet_amount *= 2.0
            if tier_num >= 4:
                bet_amount *= 1.5
                if tier_num >= 5:
                    bet_amount *= 1.5
                    if tier_num >= 6:
                        bet_amount *= 1.5
                        if tier_num >= 7:
                            bet_amount *= 1.5
                            if tier_num >= 8:
                                bet_amount *= 1.5
                                if tier_num >= 9:
                                    bet_amount *= 1.5
                                    if tier_num >= 10:
                                        bet_amount *= 1.5
                                        if tier_num >= 11:
                                            bet_amount *= 1.5
                                            if tier_num >= 12:
                                                bet_amount *= 1.5
                                                if tier_num >= 13:
                                                    bet_amount *= 1.5
    return bet_amount

def continue_betting():
    """
    Indicates whether betting should continue
    """

    return True


if __name__ == '__main__':

    games_json = None
    bet_in_progress = False
    current_bet_tier = 1
    current_bet = 1 * BETTING_UNIT

    NITRO_API = NitrogenApi()
    NITRO_API.login(NITROGEN_USERNAME, NITROGEN_PASSWORD)
    time.sleep(1)

    transaction_dump = NITRO_API.get_transactions()
    STARTING_BALANCE = transaction_dump['transactionData']['balance']
    time.sleep(1)

    NITRO_API.logout()

    last_balance = STARTING_BALANCE

    while True:

        if bet_in_progress is False:

            while True:
                NITRO_API = NitrogenApi()
                NITRO_API.login('flot989', 'Thr0wAway1')
                time.sleep(1)
                games_json = NITRO_API.find_upcoming_games()
                time.sleep(1)
                NITRO_API.logout()

                next_bet = find_next_bet(games_json)

                if next_bet is not None:
                    break
                    
                time.sleep(RETRY_WAIT_TIME)

            # TODO next steps

            # POST /php/query/betslip_addBet.php HTTP/1.1
            # event_id=711667105&period_id=387060156&bet_type=moneyline_draw&bet_id=-1

            # adjust risk to current_bet
            # POST /php/query/betslip_bet_adjustRisk.php HTTP/1.1
            # bet_id=16635862&risk=0.05000

            # POST /php/query/betslip_get_place.php HTTP/1.1

            # POST /php/query/betslip_confirm.php HTTP/1.1
            # betslip_type=straight&teaser_id=0&coupon_id=

        else:
            TRANSACTION_DUMP = NITRO_API.get_transactions()
            BALANCE = TRANSACTION_DUMP['transactionData']['balance']
            INPLAY = TRANSACTION_DUMP['transactionData']['inplay']

            if INPLAY == 0.0:
                bet_in_progress = False
                if BALANCE > last_balance:
                    # Last bet was won
                    pass  # TODO
                elif BALANCE == last_balance:
                    # Last bet was pushed
                    pass  # TODO
                else:
                    # Last bet was lost
                    pass  # TODO

        if continue_betting() is False:
            break
        else:
            time.sleep(RETRY_WAIT_TIME)
