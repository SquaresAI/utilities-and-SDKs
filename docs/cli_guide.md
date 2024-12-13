
# CLI Guide for Utilities and SDKs

This guide explains how to effectively use the CLI tools provided by the Squares AI platform.

## Installation

Ensure you have Python 3.8+ installed. 

## Usage

The CLI provides commands to interact with Squares AI services, manage models, and datasets.

### List Available Models

```bash
squares-cli models list
```

### Upload a Dataset

```bash
squares-cli datasets upload --file dataset.csv --name "My Dataset"
```

### Fine-tune a Model

```bash
squares-cli models fine-tune --model-id 12345 --dataset-id 67890 --epochs 10
```

For a complete list of commands, run:

```bash
squares-cli --help
```

## Configuration

CLI settings are stored in a config file located at `~/.squares-cli/config.yaml`. Example:

```yaml
api_key: YOUR_API_KEY
base_url: https://api.squareslabs.ai
timeout: 30
```

For more details, refer to the [SDK Overview](sdk_overview.md).
