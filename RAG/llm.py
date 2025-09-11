from huggingface_hub import InferenceClient
from prompts import prompt
from config import HF_TOKEN

client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.3", token= HF_TOKEN)

from langchain_core.runnables import Runnable

class HuggingFaceChatRunnable(Runnable):
    def __init__(self, client, prompt_template, temperature, max_tokens):
        self.client = client
        self.prompt_template = prompt_template
        self.temperature = temperature
        self.max_tokens = max_tokens

    def invoke(self, inputs: dict) -> str:
        prompt_str = self.prompt_template.format(**inputs)

        response = self.client.chat_completion(
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_str}],
            temperature = self.temperature,
            max_tokens = self.max_tokens)
        return response.choices[0].message["content"]

chat = HuggingFaceChatRunnable(client, prompt_template=prompt, temperature= 0.2, max_tokens= 1024)