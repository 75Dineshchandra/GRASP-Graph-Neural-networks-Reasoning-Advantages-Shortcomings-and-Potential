from test.test_tool_drug_ingredients import run_tool_demo as run_tool_1
from test.test_tool_Adverse_Reactions import run_tool_demo as run_tool_2
from test.test_tool_Warnings import run_tool_demo as run_tool_3
from test.test_tool_Dosage_and_Storage import run_tool_demo as run_tool_4

if __name__ == "__main__":
    print("==== Running tool test for active ingredient info ====\n")
    run_tool_1()

    print("\n==== Running tool test for adverse reactions (side effects) ====\n")
    run_tool_2()

    print("\n==== Running tool test for warnings ====\n")
    run_tool_3()

    print("\n==== Running tool test for dosage and storage instructions ====\n")
    run_tool_4()