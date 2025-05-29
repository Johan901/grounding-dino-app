from transformers import AutoTokenizer

AutoTokenizer.from_pretrained("bert-base-uncased", cache_dir="./bert-cache")
