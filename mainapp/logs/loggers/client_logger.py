import logging
import sys

formatter = logging.Formatter('%(asctime)s %(levelname)-10s %(module)-10s %(message)s')

applog_hand = logging.FileHandler('logs/log_files/client_logs.log',
                                  encoding='utf-8')

applog_hand.setFormatter(formatter)
logger = logging.getLogger('client')
logger.setLevel(logging.INFO)
logger.addHandler(applog_hand)

if __name__ == '__main__':
    logger.info('test info')
    logger.critical('test error')