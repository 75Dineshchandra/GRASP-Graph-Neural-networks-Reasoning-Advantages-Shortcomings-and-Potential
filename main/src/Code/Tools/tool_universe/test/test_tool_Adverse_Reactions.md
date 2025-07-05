# Test Tool 2: Adverse Reactions (Side Effects) Lookup

This test script demonstrates the use of the `get_adverse_reactions_by_drug_name` tool from the ToolUniverse. The tool queries the FDA drug label database for known adverse reactions (side effects) associated with a given drug. Below is a breakdown of test questions, the exact results returned by the tool, and explanations of what each output means.

---

## Tool Used

- **Name:** `get_adverse_reactions_by_drug_name`
- **Purpose:** Retrieve a list of documented side effects (adverse reactions) for a specified drug, using FDA label data.

---

## Questions and Exact Answers

### 1. **Question:** ibuprofen

**Exact Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 241},
  "results": [
    {
      "openfda.brand_name": ["Ibuprofen"],
      "openfda.generic_name": ["IBUPROFEN"],
      "adverse_reactions": [
        "ADVERSE REACTIONS The most frequent type of adverse reaction occurring with ibuprofen tablets is gastrointestinal. In controlled clinical trials the percentage of patients reporting one or more gastrointestinal complaints ranged from 4% to 16%. In controlled studies when ibuprofen tablets were compared to aspirin and indomethacin in equally effective doses, the overall incidence of gastrointestinal complaints was about half that seen in either the aspirin- or indomethacin-treated patients. Adverse reactions observed during controlled clinical trials at an incidence greater than 1% are listed in the table. Those reactions listed in Column one encompass observations in approximately 3,000 patients. More than 500 of these patients were treated for periods of at least 54 weeks. Still other reactions occurring less frequently than 1 in 100 were reported in controlled clinical trials and from marketing experience. These reactions have been divided into two categories: Column two of the table lists reactions with therapy with ibuprofen tablets where the probability of a causal relationship exists: for the reactions in Column three, a causal relationship with ibuprofen tablets has not been established. Reported side effects were higher at doses of 3200 mg/day than at doses of 2400 mg or less per day in clinical trials of patients with rheumatoid arthritis. The increases in incidence were slight and still within the ranges reported in the table. Incidence Greater than 1% (but less than 3%) Probable Causal Relationship Precise Incidence Unknown (but less than 1%) Probable Causal Relationship* Precise Incidence Unknown (but less than 1%) Causal Relationship Unknown* *Reactions are classified under 'Probable Causal Relationship (PCR)' if there has been one positive rechallenge or if three or more cases occur which might be causally related. Reactions are classified under 'Causal Relationship Unknown' if seven or more events have been reported but the criteria for PCR have not been met. † Reactions occurring in 3% to 9% of patients treated with ibuprofen. (Those reactions occurring in less than 3% of the patients are unmarked). GASTROINTESTINAL Nausea†, epigastric pain†, heartburn†, diarrhea, abdominal distress, nausea and vomiting, indigestion, constipation, abdominal cramps or Pain, fullness of GI tract (bloating and flatulence) Gastric or duodenal ulcer with bleeding and/or perforation, gastrointestinal hemorrhage, melena, gastritis, hepatitis, jaundice, abnormal liver function tests; pancreatitis CENTRAL NERVOUS SYSTEM Dizziness†, headache, nervousness Depression, insomnia, confusion, emotional liability, somnolence, aseptic meningitis with fever and coma (see PRECAUTIONS ) Paresthesias, hallucinations, dream abnormalities, pseudo-tumor cerebri DERMATOLOGIC Rash† (including maculopapular type), pruritus Vesiculobullous eruptions, urticaria, erythema multiforme, Stevens- Johnson syndrome, alopecia Toxic epidermal necrolysis, photoallergic skin reactions SPECIAL SENSES Tinnitus Hearing loss, amblyopia (blurred and/or diminished vision, scotomata and/or changes in color vision) (see PRECAUTIONS ) Conjunctivitis, diplopia, optic neuritis, cataracts HEMATOLOGIC Neutropenia, agranulocytosis, aplastic anemia, hemolytic anemia (sometimes Coombs positive), thrombocytopenia with or without purpura, eosinophilia, decreases in hemoglobin and hematocrit (see PRECAUTIONS ) Bleeding episodes (eg epistaxis, menorrhagia) METABOLIC/ENDOCRINE Decreased appetite Gynecomastia, hypoglycemic reaction, acidosis CARDIOVASCULAR Edema, fluid retention (generally responds promptly to drug discontinuation) (see PRECAUTIONS ) Congestive heart failure in patients with marginal cardiac function, elevated blood pressure, palpitations Arrhythmias (sinus tachycardia, sinus bradycardia) ALLERGIC Syndrome of abdominal pain, fever, chills, nausea and vomiting; anaphylaxis; bronchospasm (see CONTRAINDICATIONS ) Serum sickness, lupus erythematosus syndrome. Henoch- Schonlein vasculitis, angioedema RENAL Acute renal failure (see PRECAUTIONS ), decreased creatinine clearance, polyuria, azotemia, cystitis, Hematuria Renal papillary necrosis MISCELLANEOUS Dry eyes and mouth, gingival ulcer, rhinitis Postmarketing Experience The following adverse reactions have been identified during postapproval use of ibuprofen. Because these reactions are reported voluntarily from a population of uncertain size, it is not always possible to reliably estimate their frequency or establish a causal relationship to drug exposure. Skin and Appendages: Exfoliative dermatitis, Stevens-Johnson syndrome (SJS), toxic epidermal necrolysis (TEN), and fixed drug eruption (FDE)."
      ],
      "warnings_and_cautions": null
    }
    // ... (other results omitted for brevity)
  ]
}
```

**Answer Breakdown (Detailed Explanation):**

**Summary of Tool Output:**  
The output from ToolUniverse is a direct extraction of the official FDA drug label for ibuprofen, specifically the "adverse reactions" section. The response includes:
- A large block of text summarizing side effect data collected from clinical trials, postmarketing surveillance, and medical case reports.
- Side effects are grouped by frequency and organ system, and include both common and rare reactions.
- The meta field shows that there are 241 total label entries for ibuprofen, but the tool outputs the first available detailed entry.

**Detailed Explanation:**  
- **Clinical Trial Data:** The response explains that adverse reactions (side effects) were collected during controlled clinical trials. Gastrointestinal issues (nausea, pain, heartburn, diarrhea) are the most frequent. 4-16% of patients report GI complaints.
- **Comparison to Other Drugs:** Ibuprofen causes fewer GI issues than aspirin or indomethacin in trials.
- **Side Effect Frequency:**  
  - **More than 1%:** Nausea, epigastric pain, heartburn, diarrhea, etc.  
  - **Less than 1%:** Ulcers, bleeding, hepatitis, pancreatitis, and other rare but serious events.
- **Organ System Categories:**  
  - **GI:** Nausea, vomiting, ulcers, GI bleeding, hepatitis, jaundice.
  - **CNS:** Dizziness, headache, depression, insomnia, confusion, somnolence, aseptic meningitis.
  - **Skin:** Rash, pruritus, severe skin reactions (SJS, TEN).
  - **Blood:** Neutropenia, anemia, bleeding, decreases in hemoglobin/hematocrit.
  - **Heart:** Edema, fluid retention, heart failure, arrhythmias.
  - **Allergy:** Anaphylaxis, bronchospasm, serum sickness, angioedema.
  - **Kidney:** Acute renal failure, decreased clearance, hematuria, necrosis.
  - **Miscellaneous:** Dry eyes/mouth, gingival ulcers, rhinitis.
- **Postmarketing Experience:** Lists additional rare events reported after the drug was widely used—often severe skin reactions.
- **Significance:**  
  - This FDA-sourced answer is the gold standard for adverse reaction information.  
  - It is comprehensive (including both common and rare side effects) and is used by doctors, pharmacists, and patients to understand the risks of ibuprofen.
  - The answer is direct and unfiltered from the official label, ensuring accuracy and completeness, although it can be verbose and technical.

---

### 2. **Question:** List adverse reactions of Tylenol.

**Exact Answer:**
```json
{
  "code": "NOT_FOUND",
  "message": "No matches found!"
}
```

**Answer Breakdown (Case-II):**
- **Why no answer?**
  - The tool could not find adverse reactions for "Tylenol" in the FDA label database.
  - **Possible reasons:**
    - "Tylenol" is a brand name for acetaminophen. FDA data might be indexed under the generic name ("acetaminophen"), not "Tylenol."
    - The FDA label data may not include an "adverse_reactions" section for this brand in its current index.
    - Some drugs/brands are not in the FDA dataset if they are not approved, discontinued, or are registered under a different name.
- **What to do:**  
  - Try the generic name ("acetaminophen") or check if the brand is present under another tool (e.g., if you want ingredients, use the active ingredient tool).
  - This is a common issue in drug databases: the generic name is prioritized, and side effects are typically listed only under the generic.

---

### 3. **Question:** Does Advil cause drowsiness?

**Exact Answer:**
```json
{
  "code": "NOT_FOUND",
  "message": "No matches found!"
}
```

**Answer Breakdown (Case-II):**
- **Why no answer?**
  - "Advil" (a brand name for ibuprofen) did not return results for adverse reactions.
  - Like Tylenol, this could be because the FDA data is indexed under the generic name ("ibuprofen"), not the brand ("Advil").
  - The dataset may not contain an "adverse_reactions" entry for this brand or spelling.
- **What to do:**  
  - Use the generic name ("ibuprofen") for better results with this tool.
  - Drug safety databases often only include side effect listings for generics, not for every marketed brand.

---

### 4. **Question:** Which side effects are associated with Panadol?

**Exact Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 2},
  "results": [
    {
      "openfda.brand_name": ["PANADOL PM"],
      "openfda.generic_name": ["ACETAMINOPHEN AND DIPHENHYDRAMINE HCL"],
      "adverse_reactions": [
        "Allergy alert: acetaminophen may cause severe skin reactions. Symptoms may include: skin reddening blisters rash If a skin reaction occurs, stop use and seek medical help right away."
      ],
      "warnings_and_cautions": null
    },
    {
      "openfda.brand_name": ["PANADOL PM"],
      "openfda.generic_name": ["ACETAMINOPHEN AND DIPHENHYDRAMINE HCL"],
      "adverse_reactions": [
        "Allergy alert: acetaminophen may cause severe skin reactions. Symptoms may include: skin reddening blisters rash If a skin reaction occurs, stop use and seek medical help right away."
      ],
      "warnings_and_cautions": null
    }
  ]
}
```

**Answer Breakdown (Case-I):**
- The tool found entries for "PANADOL PM," which contains acetaminophen (and diphenhydramine).
- The main side effect documented is a severe skin allergy warning for acetaminophen.
- This is a correct result, as it alerts users to a rare but serious potential reaction. This is vital information for patients with known allergies.

---

## General Overview of the Tool

### **What argument does it take?**
- **Argument:** `drug_name` (string).  
  Example: `{"drug_name": "ibuprofen"}`

### **How does it answer?**
- The tool looks up the FDA drug label database for the given drug name (brand or generic).
- It retrieves the "adverse_reactions" section from the FDA label for that drug.
- Returns a detailed list of side effects (sometimes very long, direct from FDA label text).
- If the drug name is not found, or if there is no adverse reactions section for that brand/generic, it returns an error message.

### **Combined Overview of the Four Questions in test_tool_2.py**

- **Generic names (like "ibuprofen") return detailed, official adverse reaction lists**—these are comprehensive and come straight from the FDA.
- **Brand names (like "Tylenol" or "Advil") may not yield answers** if the FDA’s label database indexes the information only under the generic name. In such cases, the tool returns a "no matches found" error.
- **Combination products (like "PANADOL PM") are found if indexed, and their side effect warnings reflect all active ingredients.**
- **If the answer is not found, it is usually because:**  
  - The brand/generic is not present in the FDA dataset.
  - The name doesn’t match exactly what’s in the FDA database (try generic names).
  - The label does not contain an "adverse_reactions" section.

---

## Simple Metrics

| Metric         | Description                                       | Example/Result                      |
|----------------|---------------------------------------------------|-------------------------------------|
| Coverage       | % of drugs with adverse reactions found           | High for common generics, lower for brands |
| Precision      | How exact is the answer? (FDA label, so very high)| Exact FDA label info                |
| Error Rate     | % of queries with no results                      | Medium if using only brand names    |
| Response Time  | Speed of answer                                   | Near-instant (API-dependent)        |

---

## In Simple Terms

- This tool gives you official side effect lists from the FDA for drugs you ask about.
- For best results, use the generic name (like "ibuprofen" or "acetaminophen").
- If you use a brand name and get no result, try again with the generic.
- The answers are thorough, direct, and meant for both patients and health professionals.
