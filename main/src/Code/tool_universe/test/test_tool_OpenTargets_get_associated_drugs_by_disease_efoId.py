# test_tool_OpenTargets_get_associated_drugs_by_disease_efoId.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "OpenTargets_get_associated_drugs_by_disease_efoId"
    
    # Corrected arguments: 'efoId' and added 'size'
    # Example argument: EFO ID for 'diabetes mellitus' (EFO_0000540)
    arguments = {
        "efoId": "EFO_0000540",
        "size": 10 # Added required 'size' parameter with a default value
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