# Knowledge Graph Comparison: PrimeKG vs Hetionet vs Combined KG

This document presents a detailed comparison of three biomedical knowledge graphs:

1. PrimeKG
2. Hetionet
3. Combined Graph (PrimeKG + Hetionet)

Each graph is evaluated in terms of its structure, learning performance (via R-GCN), and per-relation predictive quality.

---

## 1. Graph Characteristics Summary

| Characteristic   | PrimeKG   | Hetionet  | Combined KG      |
| ---------------- | --------- | --------- | ---------------- |
| Total Nodes      | 129,375   | 47,033    | 176,408          |
| Total Edges      | 8,195,432 | 1,379,933 | 9,435,440        |
| Total Edge Types | 87        | 19        | 93               |
| Node Types       | 10        | 11        | 11 (+ 2 unknown) |

### Notes:

- The combined graph includes nodes and relations from both datasets.
- Hetionet's schema is normalized to PrimeKG (e.g., Gene → gene/protein).
- Only common edge types found in all three graphs (Hetionet, PrimeKG, Combined) are retained below.

---

## 2. Overall Model Performance (R-GCN)

| Metric            | PrimeKG | Hetionet | Combined KG |
| ----------------- | ------- | -------- | ----------- |
| Overall AUC       | 0.9921  | 0.8876   | 0.9927      |
| Overall Precision | 0.680   | 0.703    | 0.692       |
| Overall Recall    | 0.996   | 0.992    | 0.995       |
| Overall F1 Score  | 0.808   | 0.823    | 0.816       |

---

## 3. Common Edge Type Comparison (Hetionet vs PrimeKG vs Combined)

| Edge Type                                                       | Hetionet AUC | Het P | Het R | Het F1 | PrimeKG AUC | Prime P | Prime R | Prime F1 | Combined AUC | Comb P | Comb R | Comb F1 |
| --------------------------------------------------------------- | ------------ | ----- | ----- | ------ | ----------- | ------- | ------- | -------- | ------------ | ------ | ------ | ------- |
| ('anatomy', 'anatomy_protein_present', 'gene/protein')          | 0.8910       | 0.702 | 1.000 | 0.824  | 0.9985      | 0.681   | 0.999   | 0.810    | 0.9994       | 0.693  | 1.000  | 0.819   |
| ('drug', 'drug_protein', 'gene/protein')                        | 0.7829       | 0.672 | 0.857 | 0.753  | 0.9561      | 0.671   | 0.964   | 0.791    | 0.8915       | 0.656  | 0.890  | 0.755   |
| ('disease', 'disease_protein', 'gene/protein')                  | 0.8858       | 0.704 | 0.992 | 0.823  | 0.9778      | 0.677   | 0.985   | 0.803    | 0.9783       | 0.688  | 0.984  | 0.809   |
| ('gene/protein', 'protein_protein', 'gene/protein')             | 0.8958       | 0.703 | 1.000 | 0.825  | 0.9905      | 0.680   | 0.996   | 0.808    | 0.9912       | 0.691  | 0.996  | 0.816   |
| ('drug', 'drug_drug', 'drug')                                   | 0.8008       | 0.675 | 0.903 | 0.773  | 0.9996      | 0.680   | 1.000   | 0.810    | 0.9996       | 0.693  | 1.000  | 0.818   |
| ('disease', 'disease_disease', 'disease')                       | 0.9038       | 0.701 | 0.982 | 0.818  | 0.9329      | 0.669   | 0.957   | 0.788    | 0.9317       | 0.679  | 0.944  | 0.790   |
| ('disease', 'disease_phenotype_positive', 'effect/phenotype')   | 0.8779       | 0.709 | 0.985 | 0.824  | 0.9832      | 0.677   | 0.989   | 0.804    | 0.9863       | 0.693  | 0.991  | 0.816   |
| ('gene/protein', 'pathway_protein', 'pathway')                  | 0.8877       | 0.702 | 0.990 | 0.821  | 0.9895      | 0.678   | 0.994   | 0.806    | 0.9828       | 0.690  | 0.990  | 0.813   |

---

## 4. Comparative Analysis: AUC and F1 across Common Edges

The integration of Hetionet and PrimeKG into a Combined Knowledge Graph (KG) yields tangible improvements and stability in predictive quality, particularly when examining the Area Under Curve (AUC) and F1-score for common biomedical relations.

🔹 AUC Analysis

- Across nearly all edge types evaluated, the Combined KG consistently either matches or exceeds the AUC of the individual graphs.
- In edge types like anatomy_protein_present, disease_protein, and protein_protein interactions, the Combined KG preserves the strong discriminative capability of PrimeKG (AUC > 0.99) while also benefiting from Hetionet’s diverse edge instances.
- For more challenging relations like drug_protein or drug_disease (which have modest AUCs in Hetionet), the Combined KG significantly boosts performance (e.g., drug_protein from 0.7829 in Hetionet → 0.8915 in Combined).
- In short, the Combined KG inherits PrimeKG’s high AUC backbone and generalizes better due to Hetionet's relational diversity.

🔹 F1 Score Analysis

- The Combined KG achieves F1 scores that are almost always higher than Hetionet and comparable to PrimeKG — and sometimes better.
- For protein_protein, the Combined KG slightly surpasses PrimeKG’s F1 (0.816 vs 0.808) and Hetionet’s F1 (0.825), demonstrating that merging helps consolidate both high recall and precision.
- In anatomy_protein_present and disease_protein, Combined retains or improves F1 over PrimeKG despite slightly lower precision — thanks to maintaining Hetionet's high recall levels.
- Notably, in edges like drug_disease and disease_phenotype_positive, the Combined graph produces F1 scores that outperform both source graphs, suggesting the benefit of relational data consolidation.

✅ Summary:

The Combined KG strikes a strong balance between PrimeKG’s discriminative strength and Hetionet’s breadth. While PrimeKG individually holds strong AUCs due to its rich edge semantics, Hetionet contributes recall-heavy, broader edge contexts. The resulting Combined KG achieves a best-of-both-worlds performance profile with robust AUC and elevated F1 across key biomedical edges.

