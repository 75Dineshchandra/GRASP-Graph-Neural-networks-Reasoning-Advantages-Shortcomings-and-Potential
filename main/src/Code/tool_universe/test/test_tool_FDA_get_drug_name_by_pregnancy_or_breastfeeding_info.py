# test_tool_FDA_get_drug_name_by_pregnancy_or_breastfeeding_info.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_name_by_pregnancy_or_breastfeeding_info"
    # Example: Retrieve drug names based on "excretion in human milk" information
    arguments = {
        "pregnancy_info": "If pregnant or breast-feeding, ask a health professional before use"
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
