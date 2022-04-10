import logging

from app_logging import logger
from common.house import House

if __name__ == '__main__':
    logger.init(logging.DEBUG, '.', 'app_logging')

    try:
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')
        my_house = House()
        my_house.bedroom.add_beds(1)
        my_house.kitchen.add_fridge(2)
    except ValueError as v:
        logging.exception(msg='ValueError', exc_info=v)
    except Exception as e:
        logging.exception(msg='Exception', exc_info=e)
