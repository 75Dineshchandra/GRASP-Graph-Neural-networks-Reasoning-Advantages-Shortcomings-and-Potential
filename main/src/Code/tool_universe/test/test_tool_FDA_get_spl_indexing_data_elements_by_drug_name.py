# test_tool_FDA_get_spl_indexing_data_elements_by_drug_name.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_spl_indexing_data_elements_by_drug_name"
    # Example: Retrieve SPL indexing data elements for "PHENYTOIN SODIUM"
    arguments = {
        "drug_name": "PHENYTOIN SODIUM"
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
