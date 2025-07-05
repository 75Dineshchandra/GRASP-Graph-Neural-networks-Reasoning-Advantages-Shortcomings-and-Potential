# test_tool_FDA_get_drug_names_by_information_for_owners_or_caregivers.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_information_for_owners_or_caregivers"
    # Example: Retrieve drug names based on information for owners or caregivers, e.g., "storage instructions"
    arguments = {
        # Corrected the argument name from "owners_caregivers_info" to "field_info"
        "field_info": "storage instructions"
    }

    print(f"Executing tool: {tool_name} with arguments: {arguments}")

    try:
        query = {
            "name": tool_name,
            "arguments": arguments
        }
        result = tooluni.run(query)
        print("Response:", result)
    except Exception as e:
        print(f"An error occurred: {e}")

    print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
