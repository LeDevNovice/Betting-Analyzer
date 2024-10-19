import logging
import sys

from data.fetch_data import fetch_data_from_elasticsearch

def setup_logging():
    """Configure logging for app"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    try:
        # Data retrievment and formating
        raw_data = fetch_data_from_elasticsearch()
    except Exception as e:
        logger.exception("An error occured during execution.")
        sys.exit(1)

if __name__ == '__main__':
    main()