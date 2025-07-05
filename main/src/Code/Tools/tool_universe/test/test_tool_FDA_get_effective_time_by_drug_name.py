# test_tool_FDA_get_effective_time_by_drug_name.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_effective_time_by_drug_name"
    
    # Example: Trying 'ibuprofen' as another common drug.
    # The 'No matches found!' error for 'paracetamol' indicates potential data sparsity
    # or indexing issues in the FDA API for the 'effective_time' field.
    arguments = {
        "drug_name": "ibuprofen" 
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
    print("Note: 'No matches found!' might indicate data sparsity for 'effective_time' in the FDA API, not a parameter error.")

if __name__ == "__main__":
    run_tool_demo()