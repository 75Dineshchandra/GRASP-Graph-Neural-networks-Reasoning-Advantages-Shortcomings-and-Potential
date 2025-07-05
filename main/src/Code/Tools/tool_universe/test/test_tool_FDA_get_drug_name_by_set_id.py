# test_tool_FDA_get_drug_name_by_set_id.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_name_by_set_id"
    # Example: Retrieve drug name based on a known SPL Set ID for Digoxin.
    # This ID was found on DailyMed and is expected to yield a result.
    arguments = {
        "set_id": "f3d29508-e7cc-47ff-845d-b5375ee30407" # Specific SET ID for Digoxin
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
            print(f"No drug name found for Set ID: '{arguments['set_id']}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
