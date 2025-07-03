# test_tool_FDA_get_drug_names_by_dear_health_care_provider_letter_info.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_dear_health_care_provider_letter_info"
    # Changed example to a more general term like "safety"
    # as specific phrases like "new safety warning" might not be directly indexed.
    arguments = {
        "letter_info": "safety"
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
