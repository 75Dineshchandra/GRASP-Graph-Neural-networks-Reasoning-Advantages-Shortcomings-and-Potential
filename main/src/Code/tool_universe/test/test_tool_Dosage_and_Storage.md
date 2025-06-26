# Test Tool 4: Dosage and Storage Instructions Lookup — uses get_dosage_and_storage_information_by_drug_name to query FDA drug labels for dosage and storage directions.

This test script demonstrates the use of the `get_dosage_and_storage_information_by_drug_name` tool from ToolUniverse. The tool queries the FDA drug label database for official dosage instructions and, if available, storage or supply information for a given drug. Below you’ll find each test question, the exact answer from ToolUniverse, and a breakdown of what the result means or why you might not get an answer.

---

## Tool Used

- **Name:** `get_dosage_and_storage_information_by_drug_name`
- **Purpose:** Retrieve dosage instructions and storage/supply information for a given drug, using FDA drug label data.

---

## Questions and Exact Answers

### 1. **Question:** ibuprofen

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 1167},
  "results": [
    {
      "openfda.brand_name": ["Ibuprofen Dye Free"],
      "openfda.generic_name": ["IBUPROFEN"],
      "dosage_and_administration": [
        "Directions do not take more than directed the smallest effective dose should be used adults and children 12 years and over: take 1 tablet every 4 to 6 hours while symptoms persist if pain or fever does not respond to 1 tablet, 2 tablets may be used do not exceed 6 tablets in 24 hours, unless directed by a doctor children under 12 years: ask a doctor"
      ],
      "how_supplied": null
    },
    {
      "openfda.brand_name": ["care one ibuprofen"],
      "openfda.generic_name": ["IBUPROFEN"],
      "dosage_and_administration": [
        "Directions • do not take more than directed • the smallest effective dose should be used adults and children 12 years and older • take 1 tablet every 4 to 6 hours while symptoms persist • if pain or fever does not respond to 1 tablet, 2 tablets may be used • do not exceed 6 tablets in 24 hours, unless directed by a doctor children under 12 years • ask a doctor"
      ],
      "how_supplied": null
    },
    {
      "openfda.brand_name": ["Ibuprofen"],
      "openfda.generic_name": ["IBUPROFEN"],
      "dosage_and_administration": [
        "DOSAGE AND ADMINISTRATION Carefully consider the potential benefits and risks of ibuprofen tablets and other treatment options before deciding to use ibuprofen tablets. Use the lowest effective dose for the shortest duration consistent with individual patient treatment goals (see WARNINGS ). After observing the response to initial therapy with ibuprofen tablets, the dose and frequency should be adjusted to suit an individual patient's needs. Do not exceed 3200 mg total daily dose. If gastrointestinal complaints occur, administer ibuprofen tablets with meals or milk. Rheumatoid arthritis and osteoarthritis, including flare-ups of chronic disease Suggested Dosage: 1200 mg to 3200 mg daily (300 mg qid; 400 mg, 600 mg or 800 mg tid or qid). Individual patients may show a better response to 3200 mg daily, as compared with 2400 mg, although in well-controlled clinical trials patients on 3200 mg did not show a better mean response in terms of efficacy. Therefore, when treating patients with 3200 mg/day, the physician should observe sufficient increased clinical benefits to offset potential increased risk. The dose should be tailored to each patient, and may be lowered or raised depending on the severity of symptoms either at time of initiating drug therapy or as the patient responds or fails to respond. In general, patients with rheumatoid arthritis seem to require higher doses of ibuprofen tablets than do patients with osteoarthritis. The smallest dose of ibuprofen tablets that yields acceptable control should be employed. A linear blood level doseresponse relationship exists with single doses up to 800 mg (See CLINICAL PHARMACOLOGY for effects of food on rate of absorption). The availability of three tablet strengths facilitates dosage adjustment. In chronic conditions, a therapeutic response to therapy with ibuprofen tablets is sometimes seen in a few days to a week but most often is observed by two weeks. After a satisfactory response has been achieved, the patient's dose should be reviewed and adjusted as required. Mild to moderate pain: 400 mg every 4 to 6 hours as necessary for relief of pain. In controlled analgesic clinical trials, doses of ibuprofen tablets greater than 400 mg were no more effective than the 400 mg dose. Dysmenorrhea For the treatment of dysmenorrhea, beginning with the earliest onset of such pain, ibuprofen tablets should be given in a dose of 400 mg every 4 hours as necessary for the relief of pain."
      ],
      "how_supplied": [
        "HOW SUPPLIED Ibuprofen tablets USP are available in the following strengths, colors and sizes: Ibuprofen Tablets USP, 400 mg are white to off-white, film-coated, oval shaped tablets debossed with ‘I4’ on one side and plain on the other side. Bottles of 100 NDC 59651-360-01 Bottles of 500 NDC 59651-360-05 Ibuprofen Tablets USP, 600 mg are white to off-white, film-coated, capsule shaped tablets debossed with ‘I6’ on one side and plain on the other side. Bottles of 100 NDC 59651-361-01 Bottles of 500 NDC 59651-361-05 Ibuprofen Tablets USP, 800 mg are white to off-white, film-coated, capsule shaped tablets debossed with ‘I8’ on one side and plain on the other side. Bottles of 100 NDC 59651-362-01 Bottles of 500 NDC 59651-362-05 Store at 20° to 25°C (68° to 77°F) [see USP Controlled Room Temperature]. Avoid excessive heat 40ºC (104ºF). Dispense with Medication Guide available at: www.aurobindousa.com/medication-guides. Distributed by: Aurobindo Pharma USA, Inc. 279 Princeton-Hightstown Road East Windsor, NJ 08520 Manufactured by: Aurobindo Pharma Limited Hyderabad–500 032, India Revised: 08/2024 Dispense with Medication Guide available at: www.aurobindousa.com/medication-guides."
      ]
    }
    // ... (other results omitted for brevity)
  ]
}
```

**Answer Breakdown (Case I):**
- The tool listed several versions of FDA label dosage instructions for ibuprofen.
- Typical adult/child 12+ dose: 1 tablet every 4–6 hours; max 6 tablets/24 hours unless directed by a doctor.
- For arthritis and chronic pain: Up to 3200 mg/day, titrated per doctor.
- Pediatric dosing: "Ask a doctor."
- Storage (from "how_supplied" field): Store at 20–25°C (68–77°F), avoid excessive heat, original packaging.
- **Summary:** The tool provides both patient-friendly and professional instructions, including special advice for arthritis, pain, and storage.

---

### 2. **Question:** How much Tylenol should I take?

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 97},
  "results": [
    {
      "openfda.brand_name": ["TYLENOL Extra Strength"],
      "openfda.generic_name": ["ACETAMINOPHEN"],
      "dosage_and_administration": [
        "Directions do not take more than directed (see overdose warning ) adults and children 12 years and over take 2 tablets every 6 hours while symptoms last do not take more than 6 tablets in 24 hours, unless directed by a doctor do not use for more than 10 days unless directed by a doctor children under 12 years ask a doctor"
      ],
      "how_supplied": null
    }
    // ... (other Tylenol products omitted for brevity)
  ]
}
```
**Answer Breakdown (Case I):**
- For adults/children 12+: 2 tablets every 6 hours, max 6 tablets in 24 hours.
- Do not use for more than 10 days unless directed by a doctor.
- Children under 12: ask a doctor.
- **Summary:** Clear patient dosing guidance, with warnings about exceeding dose or duration.

---

### 3. **Question:** What is the recommended dose for Advil?

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 36},
  "results": [
    {
      "openfda.brand_name": ["Advil Dual Action with Acetaminophen, Travel BASIX"],
      "openfda.generic_name": ["IBUPROFEN, ACETAMINOPHEN TABLET, FILM COATED"],
      "dosage_and_administration": [
        "Directions \u200bDirections Do not take more than directed adults and children 12 years and over take 2 caplets every 8 hours while symptoms persist children under 12 years ask a doctor do not take more than 6 caplets in 24 hours, unless directed by a doctor"
      ],
      "how_supplied": null
    },
    {
      "openfda.brand_name": ["Advil"],
      "openfda.generic_name": ["IBUPROFEN"],
      "dosage_and_administration": [
        "Directions • do not take more than directed • the smallest effective dose should be used • adults and children 12 years and over: take 1 tablet every 4 to 6 hours while symptoms persist • if pain or fever does not respond to 1 tablet, 2 tablets may be used • do not exceed 6 tablets in 24 hours, unless directed by a doctor • children under 12 years: ask a doctor"
      ],
      "how_supplied": null
    }
    // ... (other Advil products omitted for brevity)
  ]
}
```
**Answer Breakdown (Case I):**
- Most Advil products: Adults/children 12+: 1 tablet every 4–6 hours (if 1 doesn't work, use 2), max 6 tablets/24 hours.
- Some combo products (e.g., Dual Action): 2 caplets every 8 hours, up to 6/day.
- Pediatric dosing: ask a doctor.
- **Summary:** The tool provides both branded and combination Advil dosing details.

---

### 4. **Question:** How should Panadol be stored?

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 9},
  "results": [
    {
      "openfda.brand_name": ["PANADOL PM"],
      "openfda.generic_name": ["ACETAMINOPHEN AND DIPHENHYDRAMINE HCL"],
      "dosage_and_administration": [
        "Directions do not take more than directed (see overdose warning) adults and children 12 years of age and over: take 2 caplets at bedtime, if needed, or as directed by a doctor do not give to children under 12 years of age"
      ],
      "how_supplied": null
    },
    {
      "openfda.brand_name": ["PANADOL"],
      "openfda.generic_name": ["ACETAMINOPHEN"],
      "dosage_and_administration": [
        "Directions: this product does not contain directions or complete warnings for adult use do not take more than directed (see overdose warning) find right dose in chart. If possible use weight to dose; otherwise, use age if needed, repeat dose every 4 hours while symptoms persist or as directed by a doctor do not take more than 5 doses in 24 hours, unless directed by a doctor use only with enclosed pre-marked measuring syringe for accuracy. Do not use any other dosing device. Age Weight Dosage under 2 yrs under 24 lbs ask a doctor 2-3 yrs 24-35 lbs 5 mL"
      ],
      "how_supplied": null
    }
    // ... (other Panadol products omitted for brevity)
  ]
}
```
**Answer Breakdown (Case I):**
- All Panadol answers give dosage, but "how_supplied" (true storage info) is missing (null) from the FDA label entries returned.
- Dosage: Adults/children 12+: 2 caplets at bedtime or as directed; pediatric and liquid forms: use supplied cup/syringe and dose by weight/age.
- **Summary:** The tool returns FDA label dosage info, but storage instructions are not always present in the data.

---

## General Overview of the Tool

**Purpose:**  
- The `get_dosage_and_storage_information_by_drug_name` tool provides official FDA dosage instructions and, if available, storage/supply information for a given drug.

**Arguments:**  
- `drug_name` (string): The brand or generic name of the drug (e.g., "ibuprofen", "Tylenol").

**How It Answers:**  
- Looks up the FDA drug label database for the provided name.
- Returns the "dosage_and_administration" section(s) and, if present, the "how_supplied" section.
- If the drug is not found or does not have these sections in the FDA label, the result may be empty or missing.

**Combined Summary of 4 Questions:**
- For all four drugs tested (ibuprofen, Tylenol, Advil, Panadol), the tool returned detailed patient-friendly and/or professional dosage instructions per FDA label.
- Pediatric dosing is always "ask a doctor" unless a weight/age chart is provided.
- Storage instructions ("how_supplied") are only present for some products (e.g., ibuprofen tablets). Most results focus on dosing, not physical storage.
- The tool answers with exactly what the FDA label provides, including directions, warnings about maximum dose, and special instructions for children or for longer-term use.

---