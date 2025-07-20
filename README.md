# **Knowledge Graph-Enhanced Therapeutic Agent (KgTxAgent)**

## **Overview**
This research project develops an enhanced therapeutic reasoning agent that integrates PrimeKG (Precision Medicine Knowledge Graph) with the TxAgent framework for improved biomedical decision-making. The project combines structured knowledge representation with large language model capabilities to create a more comprehensive and contextually-aware therapeutic reasoning system. The enhanced agent leverages the rich biomedical relationships encoded in PrimeKG to provide evidence-based therapeutic recommendations across multiple biological scales.

## **Key Features**

* **Knowledge Graph Integration Pipeline:** Incorporates PrimeKG as the core knowledge foundation, utilizing its 17,080 diseases and 4,050,249 biomedical relationships to enhance therapeutic reasoning capabilities beyond traditional text-based approaches.

* **Multi-Scale Biomedical Reasoning:** Integrates relationships spanning molecular, cellular, tissue, and organ levels from PrimeKG to provide comprehensive therapeutic analysis that considers the full spectrum of biological interactions and disease mechanisms.

* **Enhanced Entity Linking System:** Implements advanced biomedical entity recognition and linking capabilities that connect textual mentions to PrimeKG entities, enabling more accurate knowledge retrieval and contextual understanding for therapeutic queries.

* **Graph-Aware Decision Making:** Utilizes sophisticated graph traversal algorithms and multi-hop reasoning across PrimeKG's structure to identify relevant therapeutic pathways, drug-disease associations, and potential contraindications for evidence-based recommendations.

* **Precision Medicine Integration:** Leverages PrimeKG's comprehensive disease coverage and drug association data to support personalized treatment recommendations, drug repurposing opportunities, and precision medicine applications.

## **Rich Dataset**
PrimeKG (Precision Medicine Knowledge Graph) serves as the primary knowledge source, integrating data from 20 high-quality biomedical resources including disease ontologies (MONDO, HPO), drug databases (DrugBank, SIDER), protein interaction networks (STRING, BioGRID), and pathway databases (KEGG, Reactome). The knowledge graph contains 17,080 diseases with 4,050,249 relationships across ten major biological scales. Additionally, the project utilizes the original TxAgent framework's biomedical reasoning capabilities and integrates clinical case studies for validation and performance evaluation.

## **Model Architectures**
This research project enhances the TxAgent architecture with knowledge graph-aware components. The core system utilizes transformer-based models for natural language understanding while incorporating graph neural networks for processing PrimeKG's structure and relationships. The enhanced architecture includes a Knowledge Graph Encoder that processes biomedical entities and their relationships, an Entity Linking Module for accurate biomedical entity recognition, and a Graph-Aware Reasoning Engine that combines knowledge graph embeddings with language model representations. The Multi-Modal Fusion Layer integrates structured knowledge from PrimeKG with unstructured clinical text to provide comprehensive therapeutic understanding and evidence-based decision making.

## **Knowledge Graph Integration**
The project implements sophisticated knowledge graph querying and reasoning mechanisms to leverage PrimeKG's comprehensive biomedical knowledge. The system performs entity linking to map clinical mentions to PrimeKG entities, executes multi-hop graph traversals to identify relevant therapeutic pathways, and utilizes graph-guided generation to ensure recommendations are grounded in established biomedical knowledge. The integration enables the agent to access detailed drug-disease associations, biological pathway information, and mechanism-based therapeutic insights that significantly enhance the accuracy and reliability of therapeutic recommendations compared to traditional text-only approaches.

**P.S.** You can use the original TxAgent repository at https://github.com/mims-harvard/TxAgent and PrimeKG documentation at https://www.nature.com/articles/s41597-023-01960-3 to understand the foundational components and knowledge graph structure that this research project builds upon.




## 🚀 Getting Started

### 📁 Clone the Repository

```bash
git clone https://github.com/75Dineshchandra/KgTxAgent.git
cd KgTxAgent


This repository provides a clean, modular framework to work with:

- **PrimeKG** (Precision Medicine Knowledge Graph) — for disease-drug-gene relationships
- **ToolUniverse** — plug-and-play FDA tools (structured response)
- **openFDA API Explorers** — raw API response demonstrations for real-world queries

---

## 📦 Installation

Make sure you have Python 3.8+ installed, then:

```bash
git clone https://github.com/75Dineshchandra/KgTxAgent.git
cd KgTxAgent
pip install -r requirements.txt
```

---

## 📁 Repository Structure

```
src/
├── Code/
│   ├── Datadownloader/                 # PrimeKG downloader
│   ├── Tools/
│   │   ├── openfda/                    # API response test scripts + guides
│   │   └── tool_universe/             # Modular reusable FDA tools
│   └── PrimeKG/                        # Graph builder, queries, notebooks
├── logs/                               # Logs from PrimeKG downloader
├── reports/                            # Analysis or results (optional)
```

---

## 🧬 PrimeKG Downloader

Downloads and prepares the full PrimeKG dataset.

```bash
python src/Code/Datadownloader/primekg_downloader.py
```

Outputs:
- `.tab/.csv` files in: `src/Code/data/primekg/`
- Logs in: `logs/primekg_download.log`

---

## 🔧 Modular Tools — ToolUniverse

Reusable tools for extracting structured data from openFDA (modular, embeddable).

| Tool | Script | Guide |
|------|--------|-------|
| Adverse Reactions | `test_tool_Adverse_Reactions.py` | `test_tool_Adverse_Reactions.md` |
| Dosage Info | `test_tool_Dosage_and_Storage.py` | `test_tool_Dosage_and_Storage.md` |
| Drug Ingredients | `test_tool_drug_ingredients.py` | `test_tool_drug_ingredients.md` |
| Brand/Generic Name | `test_tool_FDA_get_brand_name_generic_name.py` | — |
| Clinical Pharmacology | `test_tool_FDA_get_clinical_pharmacology_by_drug_name.py` | — |

> 🔍 See the full list in `tools_description.md`

These tools return structured JSON responses and can be used programmatically in LLMs or automation.

---

## 🔍 API Response Explorers — openFDA Test Scripts

These scripts hit the real openFDA REST API and return **full raw results** for:

- Drug labeling
- Device events
- Food recalls
- Drug adverse events

Run them like this:

```bash
python src/Code/Tools/openfda/test/test_device_events.py
python src/Code/Tools/openfda/test/test_drug_labeling.py
```

Each script prints actual FDA event reports or metadata. Good for:
- Demos
- Exploration
- QA evaluation of raw fields

---

## What’s Included

-  Safe, resumable PrimeKG downloader
-  Modular FDA tools (ToolUniverse)
-  Raw FDA response scripts (openFDA)
-  Full documentation in matching Markdown files
- Simple install & usage

---

- Based on [PrimeKG (Harvard)](https://github.com/mims-harvard/PrimeKG)
- Powered by [openFDA API](https://open.fda.gov)

