import argparse
import requests

API_BASE = "https://api.squareslabs.ai/models/"

def deploy_model(model_file, api_key):
    """Deploys a model to Squares AI."""
    headers = {'Authorization': f"Bearer {api_key}"}
    with open(model_file, 'rb') as f:
        response = requests.post(f"{API_BASE}deploy", files={'file': f}, headers=headers)
    if response.status_code == 200:
        print(f"Model deployed successfully: {response.json()['model_id']}")
    else:
        print(f"Deployment failed: {response.text}")

def list_models(api_key):
    """Lists all deployed models."""
    headers = {'Authorization': f"Bearer {api_key}"}
    response = requests.get(f"{API_BASE}list", headers=headers)
    if response.status_code == 200:
        models = response.json()
        for model in models:
            print(f"Model ID: {model['id']}, Name: {model['name']}")
    else:
        print(f"Failed to fetch models: {response.text}")

def delete_model(model_id, api_key):
    """Deletes a model by its ID."""
    headers = {'Authorization': f"Bearer {api_key}"}
    response = requests.delete(f"{API_BASE}{model_id}", headers=headers)
    if response.status_code == 200:
        print(f"Model deleted successfully.")
    else:
        print(f"Failed to delete model: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Manage models in Squares AI.")
    parser.add_argument("--deploy", help="Path to the model file for deployment.")
    parser.add_argument("--list", action="store_true", help="List all deployed models.")
    parser.add_argument("--delete", help="ID of the model to delete.")
    parser.add_argument("api_key", help="Your API key for authentication.")
    args = parser.parse_args()
    
    try:
        if args.deploy:
            deploy_model(args.deploy, args.api_key)
        elif args.list:
            list_models(args.api_key)
        elif args.delete:
            delete_model(args.delete, args.api_key)
        else:
            print("No valid command provided. Use --help for guidance.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
