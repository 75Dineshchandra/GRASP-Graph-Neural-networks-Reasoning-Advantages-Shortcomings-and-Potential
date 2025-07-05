from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "get_active_ingredient_info_by_drug_name"
    
    questions = [
        "ibuprofen",
        "ingredients in Tylenol.",
        "Tell me the composition of Advil."
    ]

    for q in questions:
        print(f"Question: {q}")
        # The tool expects a drug_name argument, so extract drug names from the queries.
        # We'll use a naive approach for this demo: use the last word in the question that starts with a capital or is all lowercase (except the last question).
        # In practice, a more robust NER or regex extraction should be used.
        lower_q = q.lower()
        if "ibuprofen" in lower_q:
            drug = "ibuprofen"
        elif "tylenol" in lower_q:
            drug = "tylenol"
        elif "advil" in lower_q:
            drug = "advil"
        elif "panadol" in lower_q:
            drug = "panadol"
        elif "xyznonexistentdrug" in lower_q:
            drug = "xyznonexistentdrug"
        else:
            drug = None

        if drug:
            query = {
                "name": tool_name,
                "arguments": {
                    "drug_name": drug
                }
            }
            result = tooluni.run(query)
        else:
            # If drug is not present, simulate how the agent would respond
            result = {"error": "Could not determine appropriate tool for the question."}

        print("Response:", result)
        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()