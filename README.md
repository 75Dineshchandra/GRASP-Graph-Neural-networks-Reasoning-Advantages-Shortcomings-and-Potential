
# 📘 PrimeTxAgent: Therapeutic Reasoning via Knowledge Graphs using PrimeKG

**Proposed by**: Dinesh Chandra Gaddam and Ganesh Kumar Boini  
**Advisor**: Dr. Amir Jafari  
**Program**: M.S. Data Science, The George Washington University  
**Contact**: [dineshchandra.gaddam@gwu.edu](mailto:dineshchandra.gaddam@gwu.edu)  
**GitHub**: [75Dineshchandra](https://github.com/75Dinesh)

---

## 🎯 Objective

The aim of **PrimeTxAgent** is to develop a biomedical reasoning agent that performs **therapeutic inference** using a structured, explainable **knowledge graph (KG)** derived from the **PrimeKG** dataset. Inspired by Harvard's **TxAgent**, this system incorporates **multi-hop reasoning** across graph paths and integrates curated biomedical tools for drug-disease-treatment evaluation.

---

## 🧬 Dataset

We use the [**PrimeKG**](https://github.com/mims-harvard/PrimeKG) dataset, which consists of over **4 million biomedical relations** involving drugs, diseases, phenotypes, genes, pathways, anatomical sites, and more.

In addition, curated biomedical APIs from **ToolUniverse**, **OpenFDA**, and **Open Targets** may be integrated to supplement external reasoning and enrich entity context.

---

## 🤖 Rationale

Most LLM-based agents rely on **textual retrieval** and suffer from **lack of explainability**. PrimeTxAgent leverages **graph-based reasoning** to perform transparent, structured, and multi-relational drug-disease inference. This enables:

- Graph-based explainability
- Integration with biomedical ontologies (e.g., MONDO, DrugBank)
- Enhanced interpretability over LLM-based black-box agents

---

## ⚙️ Approach

### ✅ Phase 1 – Graph Construction
- Parse and enrich PrimeKG files
- Build graph database using **NetworkX** or **Neo4j**
- Merge node-level descriptions from drug/disease features

### ✅ Phase 2 – Tool Integration
- Wrap biomedical APIs like **DrugChecker**, **SideEffectLinker**, **PathwayAnalyzer**
- Adapt scripts from **ToolUniverse**

### ✅ Phase 3 – Agent Development
- Create a reasoning engine that:
  - Extracts relevant subgraphs
  - Performs path-based multi-hop reasoning
  - Verifies hypotheses using external tools

### ✅ Phase 4 – Evaluation
- Benchmark on **DrugPC**, **TreatmentPC**, and **DescriptionPC** tasks
- Evaluate precision, coverage, and explainability

### ✅ Phase 5 – Optional LLM Integration
- Add **LLM-based interface** (RAG or function-calling)
- Enable user-friendly querying via natural language

---

## 📅 Timeline

| Week  | Milestone                                           |
| ----- | --------------------------------------------------- |
| 1–2   | Study PrimeKG structure and ToolUniverse tooling    |
| 3–6   | Graph building and metadata enrichment              |
| 7–10  | Tool integration and script wrapping                |
| 11–14 | Build multi-hop agent (e.g., Drug → Gene → Disease) |
| 15–16 | Evaluation + Presentation prep                      |

---

## 👥 Team Suitability

- Ideal for 2–3 students
- Background in Biomedical AI, Knowledge Graphs, or NLP
- Python, Neo4j, NetworkX, API integration experience preferred

---

## ⚠️ Challenges

- 📦 **Tool Wrapping**: Over 200 tools in ToolUniverse—requires selective integration
- 🔁 **Multi-Hop Reasoning**: Path explosion and scalability must be optimized
- 🧠 **LLM Interface**: Requires careful management of prompt context and memory

---

## 📂 PrimeKG File Documentation

### 1. `kg.csv` — Core KG File

| Column               | Meaning                                                |
| -------------------- | ------------------------------------------------------ |
| `relation`           | Type of relation (e.g., drug_disease)                 |
| `display_relation`   | Abbreviated relation name (e.g., ppi)                  |
| `x_id`, `x_type`     | Source node ID and type (e.g., drug, gene/protein)     |
| `x_name`, `x_source` | Name and origin of the node (e.g., TP53, NCBI)         |
| `y_id`, `y_type`     | Target node ID and type                                |
| `y_name`, `y_source` | Name and origin of the target                          |

### 2. `nodes.csv` — Node Metadata

| Column        | Meaning                        |
| ------------- | ------------------------------ |
| `node_index`  | Graph index                    |
| `node_id`     | Identifier (NCBI, MONDO, etc.) |
| `node_type`   | Type of entity                 |
| `node_name`   | Display label                  |
| `node_source` | Origin database                |

### 3. `edges.csv` — Simplified Edge List

| Column               | Meaning       |
| -------------------- | ------------- |
| `relation`           | Relation type |
| `x_index`, `y_index` | Node indices  |

### 4. `disease_features.csv` — Disease Metadata

| Field                 | Description                            |
| --------------------- | -------------------------------------- |
| `mondo_name`          | Name of disease (from MONDO)           |
| `mondo_definition`    | Official MONDO definition              |
| `umls_description`    | Unified Medical Language System desc.  |
| `orphanet_definition` | Rare disease summary                   |
| `mayo_symptoms`, etc. | Clinical data scraped from Mayo Clinic |

### 5. `drug_features.csv` — Drug Metadata

| Field                 | Description                            |
| --------------------- | -------------------------------------- |
| `description`         | Summary of the drug                    |
| `indication`          | What it treats                         |
| `mechanism_of_action` | How it works                           |
| `pharmacodynamics`    | Effects on body                        |
| `category`, `atc_*`   | Drug classification (e.g., ATC system) |

### 6–9. Other Files

| File                               | Purpose                                           |
| ---------------------------------- | ------------------------------------------------- |
| `kg_raw.csv`, `kg_giant.csv`       | Variants of the full graph without node indexing  |
| `kg_grouped_diseases.csv`          | Clustered disease groups based on name similarity |
| `kg_grouped_diseases_bert_map.csv` | BERT-embedding clusters for disease sets          |

---

## 🔗 Useful Links

- 📘 [PrimeKG GitHub](https://github.com/mims-harvard/PrimeKG)
- 🧪 [ToolUniverse](https://github.com/mims-harvard/ToolUniverse)
