import argparse
import os
import requests

API_ENDPOINT = "https://api.squareslabs.ai/datasets/upload"

def validate_file(file_path):
    """Ensure the file exists and is a valid dataset file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not file_path.endswith(('.csv', '.json')):
        raise ValueError("Only .csv or .json files are allowed for dataset uploads.")

def upload_dataset(file_path, api_key):
    """Uploads a dataset to the Squares AI platform."""
    validate_file(file_path)
    headers = {'Authorization': f"Bearer {api_key}"}
    with open(file_path, 'rb') as f:
        response = requests.post(API_ENDPOINT, files={'file': f}, headers=headers)
    if response.status_code == 200:
        print(f"Dataset uploaded successfully: {response.json()['dataset_id']}")
    else:
        print(f"Failed to upload dataset: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Upload a dataset to Squares AI.")
    parser.add_argument("file_path", help="Path to the dataset file.")
    parser.add_argument("api_key", help="Your API key for authentication.")
    args = parser.parse_args()
    try:
        upload_dataset(args.file_path, args.api_key)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
