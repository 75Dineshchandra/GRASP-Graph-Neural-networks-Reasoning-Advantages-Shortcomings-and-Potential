# test_tool_OpenTargets_get_diseases_phenotypes_by_target_ensembl.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "OpenTargets_get_diseases_phenotypes_by_target_ensembl"
    
    # Corrected argument name: 'ensemblId'
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
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error during tool execution for '{tool_name}' with arguments {arguments}: {e}")
        print("Please ensure 'tooluniverse' is installed and configured correctly.")

    print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()