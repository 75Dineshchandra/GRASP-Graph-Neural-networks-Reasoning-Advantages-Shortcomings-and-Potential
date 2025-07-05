

# test_tool_FDA_get_drug_name_by_document_id.py
from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "FDA_get_drug_name_by_document_id"
    # Examples: Using actual SPL Set IDs from FDA DailyMed/OpenFDA data.
    # These are more likely to yield results than a generic document_id placeholder.
    # Note: The 'document_id' argument in the tool likely maps to 'id' or 'set_id' in the FDA API.
    # Found some examples from DailyMed announcements and OpenFDA documentation.
    document_ids_to_test = [
        "40adee5c-9e61-46c5-addc-071557d8d21d" 
    ]

    for doc_id in document_ids_to_test:
        arguments = {
            "document_id": doc_id
        }

        print(f"Executing tool: {tool_name} with arguments: {arguments}")

        try:
            query = {
                "name": tool_name,
                "arguments": arguments
            }
            result = tooluni.run(query)
            if result:
                print(f"Response for Document ID '{doc_id}':", result)
            else:
                print(f"No drug name found for Document ID: '{doc_id}'. This could mean the ID is not active, or the API does not return a drug name for this specific ID through this query.")
        except Exception as e:
            print(f"An error occurred for Document ID '{doc_id}': {e}")

        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()
