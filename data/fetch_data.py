import pandas as pd
from elasticsearch import Elasticsearch
from elastic_transport import TransportError
from elasticsearch.helpers import scan
from typing import Any
from config.settings import Config
import logging

logger = logging.getLogger(__name__)

def fetch_data_from_elasticsearch() -> pd.DataFrame:
    """
    Retrieve data from Elasticsearch data and return them in Panda Dataframe format.

    :raises ConnectionError: Connection error to Elasticsearch instance.
    :raises ValueError: No data retrieved.
    """
    try:
        # Elasticsearch client configuration
        es = Elasticsearch('http://localhost:9200')

        # Elasticsearch request to retrieve all the data from the index
        query = {
            "query": {
                "match_all": {}
            }
        }

        logger.info("Starting data retrievement from Elasticsearch index '%s'", Config.ES_INDEX)

        # Use of scan to use Elasticsearch scroll option
        results = scan(client=es, index=Config.ES_INDEX, query=query)
        data_list = [res['_source'] for res in results]
        data = pd.DataFrame(data_list)

        if data.empty:
            logger.error("No data retrieved from Elasticsearch.")
            raise ValueError("No data retrieved from Elasticsearch.")

        logger.info("Successfully retrieved %d documents from Elasticsearch index.", len(data))
        return data

    except TransportError as e:
        logger.exception("An error has occured during Elasticsearch connection.")
        raise ConnectionError(f"Elasticsearch connection error: {e}") from e

    except Exception as e:
        logger.exception("An error occured during data retrievement.")
        raise e
