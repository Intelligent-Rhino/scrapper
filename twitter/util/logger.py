"""
@Author: SolHuang
@E-mail: szhuang2021@gmail.com
@Time: 2021/04/15 11:48
@Description: logger
"""

import logging.config
from util.path_util import PathUtil
import os

PROJECT_ROOT_PATH = PathUtil.get_root()
print('PROJECT_ROOT_PATH====>',PROJECT_ROOT_PATH)

# logger configuration path
LOG_CONFIG_PATH = os.path.join(PROJECT_ROOT_PATH, 'utils', 'conf', 'logging.conf')
if not os.path.exists(os.path.join(PROJECT_ROOT_PATH, 'logs')):
    os.mkdir(os.path.join(PROJECT_ROOT_PATH, 'logs'))
LOG_PATH = os.path.join(PROJECT_ROOT_PATH, 'logs', 'twitter-scrapper.log')
print('LOG_PATH ===>',LOG_PATH)

logging.config.fileConfig(LOG_CONFIG_PATH, defaults={'log_file_name': LOG_PATH})

# create logger
logger = logging.getLogger('twitter-scrapper')
logger_kafka = logging.getLogger('kafka')
logger_kafka.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


#logger.propagate = False
# logger_kafka.propagate = False


if __name__ == '__main__':
    pass
