import logging
import logging.config

logging.config.fileConfig('SchoolBeauty/logging.conf')

logger = logging.getLogger('root')

logger.info('root logger init...')