
# Integration Examples for SDK

This document provides practical examples of how to use the Squares AI SDK in real-world applications.

## Example 1: Listing Models

```python
from squares_sdk import SquaresClient

client = SquaresClient(api_key="YOUR_API_KEY")

# Fetch available models
models = client.models.list()
for model in models:
    print(f"Model ID: {model.id}, Name: {model.name}, Status: {model.status}")
```

## Example 2: Fine-tuning a Model

```python
from squares_sdk import SquaresClient

client = SquaresClient(api_key="YOUR_API_KEY")

# Start fine-tuning
response = client.models.fine_tune(
    model_id="12345",
    dataset_id="67890",
    epochs=10,
    learning_rate=0.001
)
print("Fine-tuning started:", response)
```

## Example 3: Downloading Model Output

```python
from squares_sdk import SquaresClient

client = SquaresClient(api_key="YOUR_API_KEY")

# Download the model
client.models.download(model_id="12345", file_path="./model_output.bin")
print("Model downloaded successfully!")
```

For more information, refer to the full [SDK Overview](sdk_overview.md).
