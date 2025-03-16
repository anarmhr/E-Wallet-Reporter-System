import ollama
import openai
import rag
model_name = 'codeLlama:7b'

openai.api_key = "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"

BASE_RULE = '''
    1. You need to only answer the questions that request an SQL query.
    2. The response should be in a json-format:
    {
        "sql": "sql query",
        "info": "additional info that the model gives"
        "need_clarification": true or false
    }
    3. If you think the request is irrelevant or ambiguous then refuse to answer it.
    4. When refusing the sql field should be null and the info field should contain the reason behind the refusal.
    5. If the user request is ambiguous try to ask a question to clarify it. In this case sql is null and need_clarification is true
'''
user_request = input()

rag_knowledge = rag.query_chroma(user_request)

prompt = BASE_RULE + f'\nSystem-generated context: {rag_knowledge}\n' + ('user request: ' + user_request)
print('Thinking...')

response = openai.chat.completions.create(
    messages=[
        {
            'role': 'assistant',
            'content': prompt
        }
    ],
    model='gpt-4.5-preview'
)

print(response.choices[0].message.content)
