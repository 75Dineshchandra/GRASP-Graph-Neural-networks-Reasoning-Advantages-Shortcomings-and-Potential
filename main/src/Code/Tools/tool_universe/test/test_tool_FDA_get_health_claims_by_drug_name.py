# test_tool_FDA_get_health_claims_by_drug_name.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_health_claims_by_drug_name"
    # Testing with a new set of drug names, including some supplements,
    # which might have more explicit "health claims" in their labeling
    #'VITAMIN C,THIAMIN,RIBOFLAVIN,NIACIN,VITAMIN B6,FOLATE,BIOTIN,PANTOTHENIC ACID,MAGNESIUM,ZINC,SODIUM
    drug_names_to_test = [
        "THIAMIN"          # Sleep aid
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
                print(f"Response for '{drug_name}':", result)
            else:
                print(f"No health claims found for '{drug_name}'.")
        except Exception as e:
            print(f"An error occurred for '{drug_name}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
