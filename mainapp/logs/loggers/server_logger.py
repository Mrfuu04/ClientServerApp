import logging
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter('%(asctime)s %(levelname)-10s %(module)-10s %(message)s')

applog_hand = TimedRotatingFileHandler(
    'logs/log_files/server_logs.log', when="midnight", interval=1, backupCount=30, encoding='utf-8')

applog_hand.setFormatter(formatter)
logger = logging.getLogger('server')
logger.setLevel(logging.INFO)
logger.addHandler(applog_hand)

if __name__ == '__main__':
    logger.info('test info')
    logger.critical('test error')
