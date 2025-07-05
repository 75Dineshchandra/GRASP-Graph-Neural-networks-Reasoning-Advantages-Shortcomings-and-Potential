# test_tool_OpenTargets_target_disease_evidence.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "OpenTargets_target_disease_evidence"
    
    # Corrected argument names: 'efoId' and 'ensemblId'
    # This tool requires both disease EFO ID and target Ensembl ID.
    # Example: Disease 'diabetes mellitus' (EFO_0000540) and Target 'TP53' (ENSG00000141510)
    arguments = {
        "efoId": "EFO_0000540",
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