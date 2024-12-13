import argparse
from utilities_and_sdks.cli_tools.cli_main import execute_command

def main():
    parser = argparse.ArgumentParser(description="Squares AI CLI Usage Example")
    parser.add_argument('--command', type=str, required=True, help="Command to execute on Squares AI platform")
    parser.add_argument('--options', type=str, help="Additional options for the command", default="")
    args = parser.parse_args()
    
    # Execute the CLI command
    result = execute_command(command=args.command, options=args.options)
    
    # Print the result
    print("Command Execution Result:")
    print(result)

if __name__ == "__main__":
    main()
