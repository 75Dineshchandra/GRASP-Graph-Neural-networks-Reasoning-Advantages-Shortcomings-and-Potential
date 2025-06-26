# Test Tool 1: Active Ingredient Lookup — uses get_active_ingredient_info_by_drug_name to query FDA drug labels for the active ingredients of a drug.

This test script demonstrates the use of the `get_active_ingredient_info_by_drug_name` tool from ToolUniverse. The tool queries the FDA drug label database for the active ingredient(s) found in a given drug product. Below, each test question is documented with the exact ToolUniverse answer, followed by an answer breakdown and a general overview of how the tool works.

---

## Tool Used

- **Name:** `get_active_ingredient_info_by_drug_name`
- **Purpose:** Retrieve the active ingredient(s) present in a given brand or generic drug, as described on official FDA drug labels.

---

## Questions and Exact Answers

### 1. **Question:** What are the active ingredients in ibuprofen?

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 914},
  "results": [
    {
      "openfda.brand_name": ["Ibuprofen Dye Free"],
      "openfda.generic_name": ["IBUPROFEN"],
      "active_ingredient": [
        "Active ingredient (in each white tablet) Ibuprofen USP, 200 mg (NSAID)* *nonsteroidal anti-inflammatory drug"
      ]
    },
    // ...more similar results omitted for brevity
  ]
}
```

**Answer Breakdown (Case I):**
- **Summary:** The tool provided several FDA label entries for ibuprofen, each listing "Ibuprofen" as the active ingredient, with dosage (usually 200 mg per tablet for OTC forms), and clarifying it is a nonsteroidal anti-inflammatory drug (NSAID).
- **Explanation:** This confirms that for all standard ibuprofen products, the only active ingredient is ibuprofen itself.

---

### 2. **Question:** List the ingredients of Tylenol.

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 97},
  "results": [
    {
      "openfda.brand_name": ["TYLENOL Extra Strength"],
      "openfda.generic_name": ["ACETAMINOPHEN"],
      "active_ingredient": ["Active ingredient (in each tablet) Acetaminophen 500 mg"]
    },
    // ...more Tylenol products omitted for brevity
  ]
}
```

**Answer Breakdown (Case I):**
- **Summary:** The tool returned several Tylenol product entries, all listing "Acetaminophen" as the sole active ingredient, with dosage varying by product (325 mg, 500 mg, 650 mg, etc).
- **Explanation:** Tylenol’s active ingredient is acetaminophen, regardless of strength or formulation.

---

### 3. **Question:** Tell me the composition of Advil.

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 36},
  "results": [
    {
      "openfda.brand_name": ["Advil Dual Action with Acetaminophen, Travel BASIX"],
      "openfda.generic_name": ["IBUPROFEN, ACETAMINOPHEN TABLET, FILM COATED"],
      "active_ingredient": [
        "Active ingredients Acetaminophen 250 mg Ibuprofen 125 mg (NSAID*) *nonsteroidal anti-inflammatory drug"
      ]
    },
    {
      "openfda.brand_name": ["JUNIOR STRENGTH ADVIL"],
      "openfda.generic_name": ["IBUPROFEN"],
      "active_ingredient": [
        "ACTIVE INGREDIENT (IN EACH TABLET) Ibuprofen 100 mg (NSAID)* *nonsteroidal anti-inflammatory drug"
      ]
    },
    {
      "openfda.brand_name": ["Advil"],
      "openfda.generic_name": ["IBUPROFEN"],
      "active_ingredient": [
        "Active ingredient (in each tablet) Ibuprofen 200 mg (NSAID)* *nonsteroidal anti-inflammatory drug Purpose Pain reliever/Fever reducer"
      ]
    },
    // ...other Advil variants omitted
  ]
}
```

**Answer Breakdown (Case I):**
- **Summary:** The tool found multiple Advil formulations, including single-ingredient products (ibuprofen) and combination products (ibuprofen + acetaminophen, ibuprofen + pseudoephedrine). Most Advil products list ibuprofen as the only active ingredient.
- **Explanation:** Advil’s main active ingredient is ibuprofen, but combination products may include other actives such as acetaminophen or pseudoephedrine.

---

### 4. **Question:** Which substances are present in Panadol?

**Exact ToolUniverse Answer:**
```json
{
  "meta": {"skip": 0, "limit": 5, "total": 9},
  "results": [
    {
      "openfda.brand_name": ["PANADOL PM"],
      "openfda.generic_name": ["ACETAMINOPHEN AND DIPHENHYDRAMINE HCL"],
      "active_ingredient": [
        "Active ingredients (in each caplet) Acetaminophen 500 mg Diphenhydramine HCl 25 mg"
      ]
    },
    {
      "openfda.brand_name": ["PANADOL"],
      "openfda.generic_name": ["ACETAMINOPHEN"],
      "active_ingredient": [
        "Active ingredient (in each 5 mL) Acetaminophen 160 mg"
      ]
    }
    // ...other Panadol products omitted
  ]
}
```

**Answer Breakdown (Case I):**
- **Summary:** The tool found Panadol products with acetaminophen as the main active ingredient, and combination products (e.g., Panadol PM) with acetaminophen + diphenhydramine.
- **Explanation:** Panadol is primarily acetaminophen, but some variants include other active ingredients for specific uses (e.g., sleep aid).

---

### 5. **Question:** What are the active ingredients in xyznonexistentdrug?

**Exact ToolUniverse Answer:**
```json
{
  "code": "NOT_FOUND",
  "message": "No matches found!"
}
```

**Answer Breakdown (Case II):**
- **Why no answer?**  
  - The tool could not find any FDA label for "xyznonexistentdrug". This likely means:
    - The drug name is misspelled or does not exist.
    - The drug is not FDA-approved or not in the FDA label database.
    - It could be a research, discontinued, or foreign-market drug not covered by this tool.
- **What to do:**  
  - Double-check the spelling, or try the generic name. If still not found, the drug may not be covered by FDA labeling or is not available in the US market.

---

## General Overview

**Purpose:**  
The `get_active_ingredient_info_by_drug_name` tool is used for retrieving the active ingredient(s) in a drug as per official FDA product labeling.

**Arguments:**  
- `drug_name` (string): The brand or generic name of the drug (e.g., "ibuprofen", "Tylenol").

**How It Answers:**  
- Looks up the FDA drug label database for the provided name.
- Returns the "active_ingredient" field(s) for all matching products/formulations.
- For combination drugs, lists all actives and their dosages.
- If the drug is not found, returns a "No matches found!" error.

**Combined Summary of 4 Questions:**
- Generic and brand names for common OTC drugs (ibuprofen, Tylenol, Advil, Panadol) return detailed active ingredient lists.
- Combination products (e.g., Panadol PM, Advil Dual Action) list all active substances.
- If a drug is not found, it is likely because it is not FDA-approved, is a research/foreign drug, or is misspelled.
- The tool is best for ingredient lookup, not for side effects, warnings, or dosage details.

---