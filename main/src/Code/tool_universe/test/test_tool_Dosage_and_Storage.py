from tooluniverse.execute_function import ToolUniverse

def run_tool_demo():
    tooluni = ToolUniverse()
    tooluni.load_tools()

    tool_name = "get_dosage_and_storage_information_by_drug_name"
    questions = [
        "ibuprofen",
        "How much Tylenol should I take?",
        "What is the recommended dose for Advil?",
        "How should Panadol be stored?"
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