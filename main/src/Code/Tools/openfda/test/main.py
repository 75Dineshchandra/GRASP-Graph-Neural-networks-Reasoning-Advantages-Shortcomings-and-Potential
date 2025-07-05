# main.py

from test_device_events import run_demo as run_device_events
from test_drug_adverse_events import run_demo as run_drug_adverse_events
from test_drug_labeling import run_demo as run_drug_labeling
from test_drug_ndc import run_demo as run_drug_ndc
from test_drug_recalls import run_demo as run_drug_recalls
from test_foodrecalls import run_demo as run_food_recalls

if __name__ == "__main__":
    print("\n==== DEVICE EVENTS DEMO ====\n")
    run_device_events()

    print("\n==== DRUG ADVERSE EVENTS DEMO ====\n")
    run_drug_adverse_events()

    print("\n==== DRUG LABELING DEMO ====\n")
    run_drug_labeling()

    print("\n==== DRUG NDC INFO DEMO ====\n")
    run_drug_ndc()

    print("\n==== DRUG RECALLS DEMO ====\n")
    run_drug_recalls()

    print("\n==== FOOD RECALLS DEMO ====\n")
    run_food_recalls()
