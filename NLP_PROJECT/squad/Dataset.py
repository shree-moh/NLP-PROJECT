from datasets import load_dataset

dataset = load_dataset(
    "json",
    data_files={
        "train": "../squad/Data/train-v2.0.json",
        "validation": "../squad/Data/dev-v2.0.json"
    },
    field="data"
)
