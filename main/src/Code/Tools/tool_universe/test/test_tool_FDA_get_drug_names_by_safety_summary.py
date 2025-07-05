# test_tool_FDA_get_drug_names_by_safety_summary.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_safety_summary"
    # Testing with more general terms related to safety summaries.
    summary_texts_to_test = [ "risk"   ]

    for text in summary_texts_to_test:
        arguments = {
            "summary_text": text
        }

        print(f"Executing tool: {tool_name} with arguments: {arguments}")

        try:
            query = {
                "name": tool_name,
                "arguments": arguments
            }
            result = tooluni.run(query)
            if result:
                print(f"Response for summary text '{text}':", result)
            else:
                print(f"No drug names found for safety summary text: '{text}'.")
        except Exception as e:
            print(f"An error occurred for summary text '{text}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
