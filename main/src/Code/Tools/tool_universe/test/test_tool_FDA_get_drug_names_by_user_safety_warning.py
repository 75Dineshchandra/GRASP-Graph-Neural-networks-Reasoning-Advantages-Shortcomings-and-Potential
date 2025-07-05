# test_tool_FDA_get_drug_names_by_user_safety_warning.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_user_safety_warning"
    # Testing with various common user safety warning phrases.
    user_safety_warnings_to_test = [
        
        "allergic reaction",
        "stomach bleeding",
        "kidney problems"
    ]

    for warning_info in user_safety_warnings_to_test:
        arguments = {
            "safety_warning": warning_info
        }

        print(f"Executing tool: {tool_name} with arguments: {arguments}")

        try:
            query = {
                "name": tool_name,
                "arguments": arguments
            }
            result = tooluni.run(query)
            if result:
                print(f"Response for user safety warning info '{warning_info}':", result)
            else:
                print(f"No drug names found for user safety warning info: '{warning_info}'.")
        except Exception as e:
            print(f"An error occurred for user safety warning info '{warning_info}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
