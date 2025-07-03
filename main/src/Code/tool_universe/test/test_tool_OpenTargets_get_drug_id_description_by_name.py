# test_tool_OpenTargets_get_drug_id_description_by_name.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "OpenTargets_get_drug_id_description_by_name"
    
    # Preemptive correction: Assuming 'drugName' (camelCase) based on similar patterns
    # Example argument: Drug name 'ibuprofen'
    arguments = {
        "drugName": "ibuprofen" # Corrected from 'name' to 'drugName' based on pattern
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