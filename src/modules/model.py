# watsonx_model.py
import os
import logging
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

logger = logging.getLogger(__name__)

def watsonx_model():
    logger.info("Connecting to IBM Foundation Models.")
    model_id = ModelTypes.LLAMA_2_70B_CHAT
    credentials = {
        "url": "https://eu-de.ml.cloud.ibm.com",
        "apikey": os.getenv('IBM_IAM_API_KEY')
    }

    parameters = {
        GenParams.TEMPERATURE: 0.25,
        GenParams.MAX_NEW_TOKENS: 512,
        GenParams.REPETITION_PENALTY: 1.1,
        GenParams.STOP_SEQUENCES: ["\n\n"],
        GenParams.RANDOM_SEED: 25
    }

    return Model(
        model_id=model_id,
        params=parameters,
        credentials=credentials,
        project_id=os.getenv('watsonx_project_id')
    )