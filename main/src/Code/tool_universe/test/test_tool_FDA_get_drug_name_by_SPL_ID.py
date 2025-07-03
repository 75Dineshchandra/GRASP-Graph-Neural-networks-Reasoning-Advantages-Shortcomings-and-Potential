# test_tool_FDA_get_drug_name_by_SPL_ID.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_name_by_SPL_ID"
    
    # CORRECTED argument name based on error message: 'field_info'
    # Keeping the SPL ID as the value, as the tool description implies
    arguments = {
        "field_info": "0a97b20e-8515-46b0-94e8-89c03265882c" 
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

if __name__ == "__main__":
    run_tool_demo()