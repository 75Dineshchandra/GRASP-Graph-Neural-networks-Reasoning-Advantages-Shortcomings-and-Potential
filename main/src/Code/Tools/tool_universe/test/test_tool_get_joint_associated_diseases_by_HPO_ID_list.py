# test_tool_get_joint_associated_diseases_by_HPO_ID_list.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "get_joint_associated_diseases_by_HPO_ID_list"
    # Focusing on the two most cardinal features of Marfan Syndrome for a more precise query:
    # HP:0000581 - Ectopia lentis (Dislocated lens)
    # HP:0002616 - Aortic root dilatation (Enlargement of the aorta)
    arguments = {
        "HPO_ID_list": ["HP:0000581", "HP:0002616"]
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
