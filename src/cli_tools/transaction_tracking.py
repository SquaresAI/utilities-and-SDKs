import argparse
import requests

API_ENDPOINT = "https://api.squares-ai.io/transactions/"

def track_transaction(transaction_id, api_key):
    """Tracks the status of a transaction."""
    headers = {'Authorization': f"Bearer {api_key}"}
    response = requests.get(f"{API_ENDPOINT}{transaction_id}", headers=headers)
    if response.status_code == 200:
        transaction = response.json()
        print(f"Transaction ID: {transaction['id']}")
        print(f"Status: {transaction['status']}")
        print(f"Details: {transaction['details']}")
    else:
        print(f"Failed to track transaction: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Track a transaction in Squares AI.")
    parser.add_argument("transaction_id", help="The ID of the transaction to track.")
    parser.add_argument("api_key", help="Your API key for authentication.")
    args = parser.parse_args()
    try:
        track_transaction(args.transaction_id, args.api_key)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
