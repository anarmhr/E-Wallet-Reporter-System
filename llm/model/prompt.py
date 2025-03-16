class Prompt:
    def __init__(self, base_rules, rag_context, user_request):
        self.base_rules = base_rules
        self.rag_context = rag_context
        self.user_request = user_request

    def __str__(self):
        return f'''
                   I. Base rules: {self.base_rules}
                   II. Additional context: {self.rag_context}
                   III. User request: {self.user_request}
                '''
