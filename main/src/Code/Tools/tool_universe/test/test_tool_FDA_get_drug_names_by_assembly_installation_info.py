# test_tool_FDA_get_drug_names_by_assembly_installation_info.py

from tooluniverse.execute_function import ToolUniverse
import json

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_assembly_installation_info"
    
    # Trying multiple terms that might appear in assembly/installation instructions
    assembly_terms = [ "prepare"]
    
    print(f"--- Running Demo for Tool: {tool_name} with multiple arguments ---")
    print("-" * 60)

    for term in assembly_terms:
        arguments = {
            "field_info": term 
        }
        print(f"\nAttempting with Arguments: {arguments}")
        print("-" * 40)

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
    print("Note: Consistent 'No matches found!' suggests data sparsity for 'assembly_or_installation_instructions' in the FDA API.")

if __name__ == "__main__":
    run_tool_demo()