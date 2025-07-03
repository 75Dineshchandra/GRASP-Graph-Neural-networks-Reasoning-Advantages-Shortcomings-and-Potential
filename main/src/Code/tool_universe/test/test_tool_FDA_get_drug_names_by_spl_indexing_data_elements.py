# test_tool_FDA_get_drug_names_by_spl_indexing_data_elements.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_names_by_spl_indexing_data_elements"
    # The previous error indicated a parsing issue with multi-word phrases.
    # Trying a simpler, single-word term like "warning" to see if it yields results.
    # Note: This field typically refers to structured indexing elements like
    # "pharmacologic_class", "substance", etc., rather than free text.
    # This test aims to see if simple text search is supported at all.
    arguments = {
        "spl_indexing_data_elements": "warning"
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
            print(f"No drug names found for SPL indexing data element: '{arguments['spl_indexing_data_elements_info']}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
