import logging

logging.basicConfig(
    filename='logs.log',
    filemode='a',
    level=logging.INFO,
    encoding='utf_8',
    format='%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)