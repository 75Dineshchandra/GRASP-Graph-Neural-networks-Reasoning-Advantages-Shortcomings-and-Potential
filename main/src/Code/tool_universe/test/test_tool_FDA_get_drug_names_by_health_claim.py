# test_tool_FDA_get_drug_names_by_health_claim.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_health_claim"
    # Testing with multiple common health-related terms that might appear as claims or indications.
    # Note: Finding direct "health claims" can be challenging as the FDA API's indexing
    # for this specific field might require very precise phrasing or may not categorize
    # general health benefits as "claims" in the same way.
    health_claims_to_test = [  
        "immune support",
    ]

    for claim in health_claims_to_test:
        arguments = {
            "health_claim": claim
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
                print(f"No results found for health claim: '{claim}'.")
        except Exception as e:
            print(f"An error occurred for health claim '{claim}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
