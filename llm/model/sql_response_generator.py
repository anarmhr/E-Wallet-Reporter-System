import json

from dtos import SqlResponse
from rabbit_mq import RabbitMQ

import openai
import llm.model.rag as rag
from llm.model.model_definition import GPT
from llm.model.prompt import Prompt

rabbit_mq = RabbitMQ()

openai.api_key = "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"

with open('./config/base-rules.txt') as f:
    base_rules = '\n'.join(f.readlines())

llm_model = GPT('gpt-4o')


def generate_sql_response(user_query):
    rag_knowledge = rag.query_chroma(user_query)
    prompt = str(Prompt(base_rules=base_rules, rag_context=rag_knowledge, user_request=user_query))
    return json.loads(
        llm_model.generate_response(prompt)
    )


res = generate_sql_response('show users')
print(SqlResponse.model_validate(res))

