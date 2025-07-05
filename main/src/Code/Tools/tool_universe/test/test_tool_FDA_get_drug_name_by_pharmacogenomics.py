# test_tool_FDA_get_drug_name_by_pharmacogenomics.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_name_by_pharmacogenomics"
    # Example: Retrieve drug name based on pharmacogenomics information like "CYP2D6 polymorphism"
    arguments = {
        "pharmacogenomics": "CYP2D6 polymorphism"
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
