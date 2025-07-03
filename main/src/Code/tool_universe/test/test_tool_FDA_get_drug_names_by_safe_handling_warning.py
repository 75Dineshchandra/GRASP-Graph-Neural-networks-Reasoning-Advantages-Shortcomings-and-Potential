# test_tool_FDA_get_drug_names_by_safe_handling_warning.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_safe_handling_warning"
    # Testing with multiple terms related to safe handling warnings.
    # The previous error for "cytotoxic" suggests the need for broader or more common terms.
    safe_handling_warnings_to_test = [ "disposal", ]

    for warning_info in safe_handling_warnings_to_test:
        arguments = {
            "safe_handling_warning": warning_info
        }

        print(f"Executing tool: {tool_name} with arguments: {arguments}")

        try:
            query = {
                "name": tool_name,
                "arguments": arguments
            }
            result = tooluni.run(query)
            if result:
                print(f"Response for safe handling warning info '{warning_info}':", result)
            else:
                print(f"No drug names found for safe handling warning info: '{warning_info}'.")
        except Exception as e:
            print(f"An error occurred for safe handling warning info '{warning_info}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
