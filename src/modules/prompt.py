promptTemplate = """<s>[INST] <<SYS>>
Provide a comprehesive answer to the given user query based on the provided context.
<</SYS>>

Ensure your answer always references the following metadatas from the provided context dictionary: `chapter`, `source`, and `page`:

[context]: {context} 

[user_query]: {user_query} [/INST]
"""

# promptTemplate = """<<SYS>>
# You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. Provide a comprehensive and thorough response.

# Generate the next agent response by answering the user_query based on the provided context. Ensure your response always references the following metadatas from the provided context dictionary: `chapter`, `source`, and `page`.
# <</SYS>>

# [INST] [context]: {context} [/INST] [user_query]: {user_query}"""