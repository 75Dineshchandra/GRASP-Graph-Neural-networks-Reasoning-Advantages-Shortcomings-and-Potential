# test_tool_OT_get_target_synonyms_by_ensemblID.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "OpenTargets_get_target_synonyms_by_ensemblID"
    
    # Example argument: Ensembl ID for 'TP53' gene (ENSG00000141510)
    arguments = {
        "ensemblId": "ENSG00000141510" 
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