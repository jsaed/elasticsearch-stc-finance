import sys
import json
import logging
from modules.elasticsearch import vector_store
from modules.model import watsonx_model
from modules.prompt import promptTemplate

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def similarity_search(vector_store, user_query, include_keys=None, exclude_keys=["big_chunk"]):
    search_results = vector_store.similarity_search(user_query, k=2)

    filtered_results = [
        {
            "chunk": result.page_content,
            "metadata": {
                key: value for key, value in result.metadata.items()
                if (include_keys is None or key in include_keys) and (exclude_keys is None or key not in exclude_keys)
            }
        }
        for result in search_results
    ]

    return json.dumps(filtered_results, indent=4)

def main():

    if len(sys.argv) > 1:
        user_query=' '.join(sys.argv[1:])
    else:
        user_query=input("User query: ")
    
    vs = vector_store()
    logger.info("Retrieving similarity search results from.")
    results = similarity_search(vs, user_query=user_query)
    logger.info(results)
    model = watsonx_model()

    # prompt_prefix = "According to Pages. {}".format(" ".join(item["metadata"]["page"] for item in results))
    prompt = "{}".format(promptTemplate.format(context=results, user_query=user_query))

    model_response = model.generate_text(prompt=prompt)
    print(model_response)
    
if __name__ == '__main__':
    main()