# test_tool_OpenTargets_get_drug_chembId_by_generic_name.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "OpenTargets_get_drug_chembId_by_generic_name"
    
    # CORRECTED argument name: 'drugName', based on the latest error message.
    # Example argument: Drug generic name 'ibuprofen'
    arguments = {
        "drugName": "ibuprofen" # Changed from 'drugGenericName' to 'drugName'
    }

    print(f"--- Running Demo for Tool: {tool_name} ---")
    print(f"Arguments: {arguments}")
    print("-" * 60)

    query = {
        "name": tool_name,
        "arguments": arguments
    }
    try:
        result = tooluni.run(query)
        print("Response:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error during tool execution for '{tool_name}' with arguments {arguments}: {e}")
        print("Please ensure 'tooluniverse' is installed and configured correctly.")

    print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()