import os
import logging
from dotenv import load_dotenv
from langchain.vectorstores import ElasticsearchStore

logger = logging.getLogger(__name__)

def vector_store():
    load_dotenv('configs/.env')
    logger.info("Initialising ElasticSearch vector store.")
    return ElasticsearchStore(
        es_cloud_id=os.getenv('CLOUD_ID'),
        es_user=os.getenv('CLOUD_USERNAME'),
        query_field="text_field",
        vector_query_field="vector_query_field.predicted_value",
        es_password=os.getenv('CLOUD_PASSWORD'),
        index_name=os.getenv('INDEX_NAME'),
        strategy=ElasticsearchStore.ApproxRetrievalStrategy(query_model_id=os.getenv('QUERY_MODEL_ID'))
    )
