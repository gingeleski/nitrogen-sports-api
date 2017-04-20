import datetime
import json
import logging
from nitrogen import NitrogenApi
import os
import time


# Global constants
MINUTES_TO_SECONDS = 3600

# Nitrogen credentials
NITROGEN_USERNAME = 'flot989'
NITROGEN_PASSWORD = 'Thr0wAway1'

# Betting system parameters
LOG_FILENAME = 'soccer_draws.log'
RETRY_WAIT_TIME = 20 * MINUTES_TO_SECONDS
BUFFER_TIME_BEFORE_GAMES = 5 * MINUTES_TO_SECONDS
BETTING_UNIT = 0.001
MIN_ODDS = 2.85
MAX_ODDS = 3.45
MAX_BET_TIER = 13
BANKROLL_GOAL = None  # infinity

logging.basicConfig(level=logging.INFO)
logging_initialized = False


def init_logging():
    """
    Initial setup of logger
    """

    try:
        os.remove(LOG_FILENAME)
    except OSError:
        pass

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(LOG_FILENAME)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log(msg):
    """
    Log given message with timestamp

    Args:
        msg (str): Message to log
    """

    if logging_initialized is False:
        init_logging()

    logger = logging.getLogger(__name__)
    logger.info(msg)

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

    MIN_CUTOFF = int(time.time()) + BUFFER_TIME_BEFORE_GAMES

    for event in games_json['data']:
        event_id = event['event_id']
        for period in event['period']:
            period_id = period['period_id']
            if 'moneyLine' in period and period['moneyLine'] is not None:
                if 'cutoffDateTime' in period and int(period['cutoffDateTime']) >= MIN_CUTOFF:
                    for line in period['moneyLine']:
                        if 'drawPrice' in line and line['drawPrice'] is not None:
                            draw_price = float(line['drawPrice'])
                            if draw_price >= MIN_ODDS and draw_price <= MAX_ODDS:
                                log('Found bet at odds ' + str(draw_price) + ', event ID ' + event_id + ', period ID ' + period_id + '.')
                                return {'event_id': event_id,
                                        'period_id': period_id,
                                        'bet_type': 'moneyline_draw',
                                        'bet_id': '-1'}
    log('Did not find suitable next bet.')
    return None

def get_bet_amount(tier_num):
    """
    Get appropriate bet amount for given tier

    Args:
        tier_num (int)

    Returns:
        (float) Appropriate bet amount in Bitcoin
    """

    bet_amount = 1 * BETTING_UNIT
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

def login(NITRO_API):
    """
    Login wrapper with logging
    """

    log('Started new session, logging in as ' + NITROGEN_USERNAME + ' ...')
    NITRO_API.login(NITROGEN_USERNAME, NITROGEN_PASSWORD)
    time.sleep(1)
    return NITRO_API

def logout(NITRO_API):
    """
    Logout wrapper with logging
    """

    log('Logging out.')
    NITRO_API.logout()
    return NITRO_API


if __name__ == '__main__':

    log('Starting Nitrogen soccer draws betting system.')

    games_json = None
    bet_in_progress = False
    current_bet_tier = 1

    NITRO_API = NitrogenApi()
    NITRO_API = login(NITRO_API)

    transaction_dump = NITRO_API.get_transactions()
    STARTING_BALANCE = transaction_dump['transactionData']['balance']
    log('Starting account balance is ' + str(STARTING_BALANCE) + ' BTC.')
    time.sleep(1)

    NITRO_API = logout(NITRO_API)
    time.sleep(1)

    last_balance = STARTING_BALANCE

    while True:

        if bet_in_progress is False:

            while True:
                NITRO_API = login(NITRO_API)
                games_json = NITRO_API.find_upcoming_games()
                time.sleep(1)

                next_bet = find_next_bet(games_json)

                if next_bet is None:
                    NITRO_API = logout(NITRO_API)
                    log('Sleeping for ' + RETRY_WAIT_TIME + ' seconds...')
                    time.sleep(RETRY_WAIT_TIME)
                else:
                    break

            # add bet for the indicated event and period
            log('Adding bet...')
            res = NITRO_API.add_bet(next_bet['event_id'], next_bet['period_id'], 'moneyline_draw')
            if 'data' in res:
                bet_id = res['data'][0]['bet'][0]['bet_id']
                log('Success, bet ID is ' + str(bet_id) + '.')
                time.sleep(1)

                # adjust risk to appropriate amount
                current_bet = get_bet_amount(current_bet_tier)
                log('Adjusting risk to ' + str(current_bet) + ' BTC...')
                NITRO_API.adjust_risk(bet_id, str(current_bet))
                time.sleep(1)

                log('Placing betslip...')
                NITRO_API.place_betslip()
                time.sleep(1)

                log('Confirming betslip...')
                NITRO_API.confirm_betslip()
                time.sleep(1)

                bet_in_progress = True
                log('Bet in progress.')

                # update last known balance since we've spent money
                TRANSACTION_DUMP = NITRO_API.get_transactions()
                last_balance = TRANSACTION_DUMP['transactionData']['balance']
                log('Available account balance is now ' + str(last_balance) + ' BTC.')
                time.sleep(1)
            else:
                log('** Something went wrong adding bet. **')
                raise RuntimeError('Something went wrong adding bet.')

        else:
            NITRO_API = login(NITRO_API)
            TRANSACTION_DUMP = NITRO_API.get_transactions()
            BALANCE = TRANSACTION_DUMP['transactionData']['balance']
            INPLAY = TRANSACTION_DUMP['transactionData']['inplay']

            if INPLAY == 0.0:
                bet_in_progress = False
                if BALANCE > last_balance:
                    current_bet_tier = 1
                    log('Detected WIN, reset bet tier to 1.')
                elif BALANCE < last_balance:
                    current_bet_tier += 1
                    log('Detected LOSS, progress bet tier to ' + str(current_bet_tier) + '.')
                last_balance = BALANCE

        NITRO_API = logout(NITRO_API)

        if continue_betting() is False:
            log('continue_betting is false, betting system is ending.')
            break
        else:
            log('Sleeping for ' + str(RETRY_WAIT_TIME) + ' seconds.')
            time.sleep(RETRY_WAIT_TIME)
