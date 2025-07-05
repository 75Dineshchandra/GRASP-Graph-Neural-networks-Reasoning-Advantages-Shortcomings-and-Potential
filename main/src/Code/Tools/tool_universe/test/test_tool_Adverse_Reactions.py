from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "get_adverse_reactions_by_drug_name"
    questions = [
        "ibuprofen",
        "List adverse reactions of Tylenol.",
        "Does Advil cause drowsiness?",
        "Which side effects are associated with Panadol?"
    ]

    for q in questions:
        print(f"Question: {q}")
        drug = None
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

        if drug:
            query = {
                "name": tool_name,
                "arguments": {
                    "drug_name": drug
                }
            }
            result = tooluni.run(query)
        else:
            result = {"error": "Could not determine appropriate tool for the question."}

        print("Response:", result)
        print("-" * 60)

if __name__ == "__main__":
    run_tool_demo()