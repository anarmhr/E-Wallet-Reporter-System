import json

import datasets
import pandas as pd

from transformers import LlamaTokenizer, TrainingArguments, Trainer
from datasets import Dataset

model_name = "codellama/CodeLlama-7b-hf"

tokenizer = LlamaTokenizer.from_pretrained(model_name)

model = LlamaTokenizer.from_pretrained(
    model_name,
    device_map="auto"
)


def tokenize_dataset(data_path):
    with open(data_path, 'r', encoding='utf-8') as file:
        dataset = pd.read_json('sql_dataset.jsonl', lines=True, dtype=str)

    dataset['text'] = dataset['text'].apply(lambda x: tokenizer.encode(x))
    dataset['sql'] = dataset['sql'].apply(lambda x: tokenizer.encode(x))

    return dataset


training_args = TrainingArguments(
    output_dir="codellama-finetuned",
    evaluation_strategy="steps",
    save_strategy="steps",
    save_steps=500,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,
    optim="adamw_torch",
    learning_rate=2e-5,
    num_train_epochs=3,
    logging_dir="logs",
    logging_steps=100,
    no_cuda=True
)

train_data = datasets.Dataset.from_pandas(tokenize_dataset('sql_dataset.jsonl'))

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
)

