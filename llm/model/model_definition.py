import ollama
import openai


class LLMModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def set_model(self, model_name):
        self.model_name = model_name

    def generate_response(self, prompt):
        pass


class GPT(LLMModel):
    def __init__(self, model_name):
        super().__init__(model_name)

    def generate_response(self, prompt):
        response = openai.chat.completions.create(
            messages=[
                {
                    'role': 'assistant',
                    'content': prompt
                }
            ],
            model=self.model_name
        )

        return response.choices[0].message.content


class CodeLlama(LLMModel):
    def __init__(self, model_name):
        super().__init__(model_name)

    def generate_response(self, prompt):
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ])

        return response['message']
