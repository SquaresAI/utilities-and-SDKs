
# SDK Overview

The Squares AI SDK provides developers with the tools to integrate AI-powered features into their applications.

## Features

- **Model Management**: List, upload, and fine-tune models.
- **Dataset Management**: Manage datasets for training or inference.
- **Decentralized GPU Management**: Leverage GPU nodes for scalable model training.

## Example Usage

### Authentication

Authenticate with your API key:

```python
from squares_sdk import SquaresClient

client = SquaresClient(api_key="YOUR_API_KEY")
```

### Listing Models

Retrieve all available models:

```python
models = client.models.list()
for model in models:
    print(model.name)
```

### Uploading Datasets

Upload datasets for model training:

```python
client.datasets.upload(file_path="./dataset.csv", name="Sample Dataset")
```

### Fine-tuning Models

Fine-tune a model:

```python
client.models.fine_tune(model_id="12345", dataset_id="67890", epochs=5)
```

For detailed guides, refer to the [CLI Guide](cli_guide.md) or [Integration Examples](integration_examples.md).
