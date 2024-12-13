# Utilities and SDKs for Squares AI

This repository contains the utilities and SDKs for developers to interact with the Squares AI platform. 
It provides tools to streamline integration, command-line utilities, and client SDKs for seamless interaction.

## Features

- Python SDK for interacting with Squares AI
- Command-line tools for managing models and datasets
- Easy integration with the Squares AI Core Platform

## Getting Started

### Prerequisites

- Python 3.8 or above
- Docker (for containerized execution)
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SquaresAI/utilities-and-SDKs.git
   cd utilities-and-SDKs
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application (example CLI command):

   ```bash
   python cli-tools/cli_main.py
   ```

### Using Docker

Build and run the application using Docker:

```bash
docker-compose up --build
```

This will start the SDK service on `http://localhost:8080`.

## File Structure

- `python-sdk/`: Contains the Python SDK code.
- `cli-tools/`: Contains command-line tools for model and dataset management.
- `helpers/`: Utility functions used by the SDK and CLI tools.

## Contributing

We welcome contributions! Please fork the repository, make your changes, and submit a pull request.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.