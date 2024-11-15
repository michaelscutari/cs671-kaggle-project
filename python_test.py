from huggingface_hub import HfApi
api = HfApi()
print(api.list_models(limit=5))

import transformers