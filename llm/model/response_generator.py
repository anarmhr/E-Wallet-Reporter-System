import openai
import llm.model.rag as rag
from llm.model.model_definition import GPT
from llm.model.prompt import Prompt

openai.api_key = "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"

with open('./llm/model/config/base-rules.txt') as f:
    base_rules = '\n'.join(f.readlines())

llm_model = GPT('gpt-4o')


def generate_sql_response(user_request):
    rag_knowledge = rag.query_chroma(user_request)
    prompt = Prompt(base_rules=base_rules, rag_context=rag_knowledge, user_request=user_request)
    return llm_model.generate_response(str(prompt))



