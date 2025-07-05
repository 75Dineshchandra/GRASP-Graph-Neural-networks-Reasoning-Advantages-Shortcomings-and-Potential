# Test Tool 3: Warnings Lookup — uses get_warnings_by_drug_name to query FDA drug labels for official warnings.

This test script demonstrates the use of the `get_warnings_by_drug_name` tool from the ToolUniverse. The tool queries the FDA drug label database for official warnings (including boxed/black box warnings, allergy, liver, pregnancy, and interaction warnings) for a given drug. Below you’ll find each test question, the exact answer from ToolUniverse, and a breakdown of what the result means or why you might not get an answer.

---

## Tool Used

- **Name:** `get_warnings_by_drug_name`
- **Purpose:** Retrieve all regulatory warnings (including black box, allergy, liver, overdose, and other medical risks) for a given drug, using FDA drug label data.

---

## Questions and Exact Answers

### 1. **Question:** ibuprofen

**Exact Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 1143},
  "results": [
    {
      "openfda.brand_name": ["Ibuprofen Dye Free"],
      "openfda.generic_name": ["IBUPROFEN"],
      "warnings": [
        "Warnings Allergy alert: Ibuprofen may cause a severe allergic reaction, especially in people allergic to aspirin. Symptoms may include: rash facial swelling asthma (wheezing) hives skin reddening shock blisters If an allergic reaction occurs, stop use and seek medical help right away. Stomach bleeding warning: This product contains an NSAID, which may cause severe stomach bleeding. The chance is higher if you: take more or for a longer time than directed take a blood thinning (anticoagulant) or steroid drug have had stomach ulcers or bleeding problems have 3 or more alcoholic drinks every day while using this product are age 60 or older take other drugs containing prescription or nonprescription NSAIDs [aspirin, ibuprofen, naproxen, or others] Heart attack and stroke warning: NSAIDs, except aspirin, increase the risk of heart attack, heart failure, and stroke. These can be fatal. The risk is higher if you use more than directed or for longer than directed. Do not use if you have ever had an allergic reaction to any other pain reliever/fever reducer right before or after heart surgery Ask a doctor before use if stomach bleeding warning applies to you you have a history of stomach problems, such as heartburn you have high blood pressure, heart disease, liver cirrhosis, kidney disease, asthma, or had a stroke you are taking a diuretic you have problems or serious side effects from taking pain relievers or fever reducers Ask a doctor or pharmacist before use if you are under a doctor's care for any serious condition taking aspirin for heart attack or stroke, because ibuprofen may decrease this benefit of aspirin taking any other drug When using this product take with food or milk if stomach upset occurs Stop use and ask a doctor if you experience any of the following signs of stomach bleeding: feel faint have bloody or black stools vomit blood have stomach pain that does not get better you have symptoms of heart problems or stroke: chest pain slurred speech leg swelling trouble breathing weakness in one part or side of body pain gets worse or lasts more than 10 days fever gets worse or lasts more than 3 days redness or swelling is present in the painful area any new symptoms appear If pregnant or breast-feeding, ask a health professional before use. It is especially important not to use ibuprofen at 20 weeks or later in pregnancy unless definitely directed to do so by a doctor because it may cause problems in the unborn child or complications during delivery. Keep out of reach of children. In case of overdose, get medical help or contact a Poison Control Center right away."
      ],
      "boxed_warning": null
    },
    {
      "openfda.brand_name": ["care one ibuprofen"],
      "openfda.generic_name": ["IBUPROFEN"],
      "warnings": [
        "Warnings Allergy alert: Ibuprofen may cause a severe allergic reaction, especially in people allergic to aspirin. Symptoms may include: • hives • facial swelling • asthma (wheezing) • shock • skin reddening • rash • blisters If an allergic reaction occurs, stop use and seek medical help right away. Stomach bleeding warning: This product contains an NSAID, which may cause severe stomach bleeding. The chance is higher if you • are age 60 or older • have had stomach ulcers or bleeding problems • take a blood thinning (anticoagulant) or steroid drug • take other drugs containing prescription or nonprescription NSAIDs [aspirin, ibuprofen, naproxen, or others] • have 3 or more alcoholic drinks every day while using this product • take more or for a longer time than directed Heart attack and stroke warning: NSAIDs, except aspirin, increase the risk of heart attack, heart failure, and stroke. These can be fatal. The risk is higher if you use more than directed or for longer than directed. Do not use • if you have ever had an allergic reaction to ibuprofen or any other pain reliever/fever reducer • right before or after heart surgery ..."
      ],
      "boxed_warning": null
    },
    {
      "openfda.brand_name": ["Ibuprofen"],
      "openfda.generic_name": ["IBUPROFEN"],
      "warnings": [
        "WARNINGS Cardiovascular Effects Cardiovascular Thrombotic Events Clinical trials of several COX-2 selective and nonselective NSAIDs ... Elderly patients are at greater risk for serious gastrointestinal events (see WARNINGS )."
      ],
      "boxed_warning": [
        "Cardiovascular Thrombotic Events Nonsteroidal anti-inflammatory drugs (NSAIDs) cause an increased risk of serious cardiovascular thrombotic events, including myocardial infarction and stroke, which can be fatal. This risk may occur early in treatment and may increase with duration of use [see Warnings and Precautions ]. Ibuprofen tablets are contraindicated in the setting of coronary artery bypass graft (CABG) surgery [see Contraindications and Warnings ]. Gastrointestinal Risk NSAIDs cause an increased risk of serious gastrointestinal adverse events including bleeding, ulceration, and perforation of the stomach or intestines, which can be fatal. These events can occur at any time during use and without warning symptoms. Elderly patients are at greater risk for serious gastrointestinal events (see WARNINGS )."
      ]
    }
    // ... (other results omitted for brevity)
  ]
}
```

**Answer Breakdown (Case I):**
- The tool returned multiple FDA official warning sections for various ibuprofen products.
- **Summary of output:**  
  - Includes warnings about severe allergic reactions, risk of stomach bleeding (especially NSAID-related), heart attack and stroke risk, not to use after heart surgery, and special cautions for those with certain health conditions.
  - Pregnancy warning: Do not use ibuprofen at 20 weeks or later unless directed by a doctor.
  - Boxed/black box warning (found in one result): Increased risk of serious cardiovascular events (heart attack, stroke) and gastrointestinal events (bleeding, ulcers, perforation).
- **Explanation:**  
  - This is an authoritative, detailed FDA warning summary for ibuprofen, covering all major health risks, interactions, overdose, and contraindications.

---

### 2. **Question:** List warnings associated with Tylenol.

**Exact Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 97},
  "results": [
    {
      "openfda.brand_name": ["TYLENOL Extra Strength"],
      "openfda.generic_name": ["ACETAMINOPHEN"],
      "warnings": [
        "Warnings Liver warning This product contains acetaminophen. Severe liver damage may occur if you take more than 4,000 mg of acetaminophen in 24 hours with other drugs containing acetaminophen 3 or more alcoholic drinks every day while using this product Allergy alert: acetaminophen may cause severe skin reactions. Symptoms may include: skin reddening blisters rash If a skin reaction occurs, stop use and seek medical help right away. Do not use with any other drug containing acetaminophen (prescription or nonprescription). If you are not sure whether a drug contains acetaminophen, ask a doctor or pharmacist. if you are allergic to acetaminophen or any of the inactive ingredients in this product Ask a doctor before use if you have liver disease Ask a doctor or pharmacist before use if you are taking the blood thinning drug warfarin Stop use and ask a doctor if pain gets worse or lasts more than 10 days fever gets worse or lasts more than 3 days new symptoms occur redness or swelling is present These could be signs of a serious condition. If pregnant or breast-feeding, ask a health professional before use. Keep out of reach of children. Overdose warning In case of overdose, get medical help or contact a Poison Control Center right away. (1-800-222-1222) Quick medical attention is critical for adults as well as for children even if you do not notice any signs or symptoms."
      ],
      "boxed_warning": null
    }
    // ... (other Tylenol products omitted for brevity)
  ]
}
```

**Answer Breakdown (Case I):**
- The tool returned multiple FDA warning sections for Tylenol products (acetaminophen).
- **Summary of output:**  
  - Main warnings: Severe liver damage (if over 4,000mg in 24 hours, combining with other acetaminophen-containing drugs, or with heavy alcohol use), severe skin reactions (rash, redness, blisters), and not to use with other acetaminophen drugs.
  - Overdose: Immediate medical attention required.
  - Additional: Caution if you have liver disease, are using warfarin, or if symptoms persist or worsen.
- **Explanation:**  
  - This is a comprehensive FDA warning summary for acetaminophen, highlighting overdose, interaction, and allergy risks.

---

### 3. **Question:** Are there any black box warnings for Advil?

**Exact Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 36},
  "results": [
    {
      "openfda.brand_name": ["Advil Dual Action with Acetaminophen, Travel BASIX"],
      "openfda.generic_name": ["IBUPROFEN, ACETAMINOPHEN TABLET, FILM COATED"],
      "warnings": [
        "Warnings ... (multiple warnings about liver damage, allergies, stomach bleeding, heart attack, stroke, etc.)"
      ],
      "boxed_warning": null
    }
    // ... (other Advil products omitted for brevity)
  ]
}
```

**Answer Breakdown (Case I):**
- The tool returned FDA warning sections for Advil and related products (ibuprofen and combinations).
- **Summary of output:**  
  - Warnings include liver damage (acetaminophen component), NSAID allergy and stomach bleeding, heart attack and stroke risk, pregnancy and overdose instructions.
  - **No boxed warning field was present for these specific Advil products.**
- **Explanation:**  
  - FDA warnings for Advil focus on the same risks as ibuprofen and acetaminophen. No "black box" warning is listed for these Advil products, but all major risks are represented in the warnings section.

---

### 4. **Question:** What warnings are given for Panadol?

**Exact Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 9},
  "results": [
    {
      "openfda.brand_name": ["PANADOL PM"],
      "openfda.generic_name": ["ACETAMINOPHEN AND DIPHENHYDRAMINE HCL"],
      "warnings": [
        "Warnings Liver warning: This product contains acetaminophen. Severe liver damage may occur if you take more than 4,000 mg of acetaminophen in 24 hours with other drugs containing acetaminophen 3 or more alcoholic drinks every day while using this product Allergy alert: acetaminophen may cause severe skin reactions. Symptoms may include: skin reddening blisters rash ..."
      ],
      "boxed_warning": null
    },
    {
      "openfda.brand_name": ["PANADOL"],
      "openfda.generic_name": ["ACETAMINOPHEN"],
      "warnings": [
        "Warnings Liver warning: This product contains acetaminophen. Severe liver damage may occur if your child takes more than 5 doses in 24 hours, which is the maximum daily amount with other drugs containing acetaminophen Allergy alert: acetaminophen may cause severe skin reactions. Symptoms may include: skin reddening blisters rash ..."
      ],
      "boxed_warning": null
    }
    // ... (other Panadol products omitted for brevity)
  ]
}
```

**Answer Breakdown (Case I):**
- The tool returned FDA warning sections for Panadol products (acetaminophen and combinations).
- **Summary of output:**  
  - Main warnings: Severe liver damage risk (especially overdose/combination), severe skin reactions, allergy alerts, not to use with other acetaminophen drugs, and overdose danger.
  - Includes both adult and child dosing/overdose warnings.
- **Explanation:**  
  - These warnings are direct from FDA labels for Panadol and highlight the most serious health risks of its active ingredients.

---

## General Overview of the Tool

**Purpose:**  
`get_warnings_by_drug_name` retrieves all FDA warnings for a given drug, including allergy, liver, pregnancy, interaction, overdose, and black box warnings. It’s designed to provide patients, clinicians, and developers with authoritative safety information for medications.

**Arguments:**  
- `drug_name` (string): The brand or generic name of the drug (e.g., "ibuprofen", "Tylenol").

**How It Answers:**  
- Looks up the FDA drug label database for the provided name.
- Returns the "warnings" section(s) and, if present, the "boxed_warning" (black box warning) field.
- If the drug is a combination product (like Panadol PM), warnings about all active components are included.
- If the drug is not found or does not have warnings in the database, `results` will be empty or missing.

**Combined Summary of the Four Questions:**
- For all four drugs tested (ibuprofen, Tylenol, Advil, Panadol), the tool returned detailed FDA warnings for each product or its generic equivalent.
- Common themes: allergy alerts (especially for NSAIDs and acetaminophen), severe liver damage warnings, stomach bleeding, heart attack and stroke risk, pregnancy cautions, and overdose instructions.
- Some products (like Advil) did not have a "boxed_warning" even when the underlying ingredient (ibuprofen) does—this reflects how FDA warnings are sometimes attached to generic or specific formulations.
- All warnings are authoritative and sourced directly from FDA labels, making this tool highly reliable for safety lookups.

---