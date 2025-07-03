# test_tool_FDA_get_drug_names_by_disposal_info.py
from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_disposal_info"
    # Trying a more general term for disposal information
    arguments = {
        "disposal_info": "disposal" # Changed from "flush list" to "disposal"
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
        if result:
            print(json.dumps(result, indent=2))
        else:
            print("No data returned or empty response.")
    except Exception as e:
        print(f"Error during tool execution for '{tool_name}' with arguments {arguments}: {e}")
        print("Please ensure 'tooluniverse' is installed and configured correctly.")

    print("-" * 60)
    print("Note: Consistent 'No matches found!' may indicate sparse data in the FDA API for disposal information.")

if __name__ == "__main__":
    run_tool_demo()