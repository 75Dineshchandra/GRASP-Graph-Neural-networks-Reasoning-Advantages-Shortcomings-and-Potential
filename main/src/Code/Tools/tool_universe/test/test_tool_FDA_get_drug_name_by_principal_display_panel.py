# test_tool_FDA_get_drug_name_by_principal_display_panel.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_name_by_principal_display_panel"
    # Example: Retrieve drug name based on a simpler term on the principal display panel.
    # The previous error suggested issues with parsing complex phrases like "active ingredient: ibuprofen".
    # Trying a single, common word like "pain" to see if the tool functions with simpler inputs.
    arguments = {
        "display_panel_content": "pain"
    }

    print(f"Executing tool: {tool_name} with arguments: {arguments}")

    try:
        query = {
            "name": tool_name,
            "arguments": arguments
        }
        result = tooluni.run(query)
        if result:
            print("Response:", result)
        else:
            print(f"No drug name found for display panel content: '{arguments['display_panel_content']}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
