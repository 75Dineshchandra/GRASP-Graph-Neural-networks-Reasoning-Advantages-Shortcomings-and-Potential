# test_tool_FDA_get_user_safety_warning_by_drug_names.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_user_safety_warning_by_drug_names"
    # Testing with various drug names known to have user safety warnings MENTHOL
    drug_names_to_test = [
        "MENTHOL",         # Common NSAID with GI/cardiovascular warnings
    ]

    for drug_name in drug_names_to_test:
        arguments = {
            "drug_name": drug_name
        }

        print(f"Executing tool: {tool_name} with arguments: {arguments}")

        try:
            query = {
                "name": tool_name,
                "arguments": arguments
            }
            result = tooluni.run(query)
            if result:
                print(f"Response for drug '{drug_name}':", result)
            else:
                print(f"No user safety warning found for drug: '{drug_name}'. This might mean the specific drug name is not indexed with a user safety warning in the FDA API, or the warning is phrased differently.")
        except Exception as e:
            print(f"An error occurred for drug '{drug_name}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
