import llm
from llm.default_plugins.openai_models import Chat, Completion, SharedOptions
import json
import requests

# Hardcoded models for now
def get_inference_models():
    return [
        {"id": "meta-llama/llama-3.2-1b-instruct/fp-8", "aliases": ["inf-1b"]},
        {"id": "meta-llama/llama-3.2-3b-instruct/fp-8", "aliases": ["inf-3b"]},
        {"id": "meta-llama/llama-3.1-8b-instruct/fp-8", "aliases": ["inf-8b-fp8"]},
        {"id": "meta-llama/llama-3.1-8b-instruct/fp-16", "aliases": ["inf-8b-fp16"]},
        {"id": "meta-llama/llama-3.2-11b-instruct/fp-16", "aliases": ["inf-11b"]},
        {"id": "mistralai/mistral-nemo-12b-instruct/fp-8", "aliases": ["inf-mistral"]},
        {"id": "meta-llama/llama-3.1-70b-instruct/fp-8", "aliases": ["inf-70b"]},
        # {"id": "meta-llama/llama-3.1-70b-instruct/bf-16", "aliases": ["inf-70b-bf16"]},
        {"id": "Gryphe/MythoMax-L2-13b", "aliases": ["inf-mythomax"]},
    ]

class InferenceChat(Chat):
    needs_key = "inference"
    key_env_var = "INFERENCE_KEY"

    def __str__(self):
        return "Inference: {}".format(self.model_id)

@llm.hookimpl
def register_models(register):
    key = llm.get_key("", "inference", "LLM_INFERENCE_KEY")
    if not key:
        return

    models = get_inference_models()
    for model_definition in models:
        model_id = "inference/{}".format(model_definition["id"])
        model_name = model_definition["id"]
        aliases = model_definition.get("aliases", []) # Extract aliases or use empty list if none

        chat_model = InferenceChat(
            model_id=model_id,
            model_name=model_name,
            api_base="https://api.inference.net/v1",  # Corrected API base
            headers={"HTTP-Referer": "https://llm.datasette.io/", "X-Title": "LLM"},
        )
        register(chat_model, aliases=aliases) # Pass aliases to register()

class DownloadError(Exception):
    pass
