# **Knowledge Graph-Enhanced Therapeutic Agent (KgTxAgent)**

## **Overview**
This research project develops an enhanced therapeutic reasoning agent that integrates **PrimeKG** (Precision Medicine Knowledge Graph) with the **TxAgent** framework for improved biomedical decision-making. The system combines structured biomedical knowledge with natural language understanding to provide evidence-based therapeutic recommendations across multiple biological scales.

## **Key Features**

- **Knowledge Graph Integration Pipeline**: Leverages PrimeKG’s 17,080 diseases and 4,050,249 relationships.
- **Multi-Scale Biomedical Reasoning**: Covers molecular to organ-level interactions.
- **Enhanced Entity Linking System**: Maps clinical mentions to PrimeKG entities.
- **Graph-Aware Decision Making**: Multi-hop traversal and path reasoning for therapy suggestions.
- **Precision Medicine Ready**: Supports drug repurposing and patient-specific treatment strategies.

## **Rich Dataset**
PrimeKG is sourced from 20+ biomedical datasets such as MONDO, HPO, DrugBank, SIDER, STRING, KEGG, and Reactome. The dataset captures over 4M relationships and integrates disease, drug, and gene-level interactions. Additional validation is supported by the original TxAgent clinical reasoning capabilities.

## **Model Architectures**
The system enhances the TxAgent framework with:

- **Transformer Models** for language understanding.
- **Graph Neural Networks (GNNs)** for structured reasoning over PrimeKG.
- **Knowledge Graph Encoder**
- **Entity Linking Module**
- **Graph-Aware Reasoning Engine**
- **Multi-Modal Fusion Layer**

These modules allow seamless fusion of textual and graph-based biomedical knowledge.

## **Knowledge Graph Integration**
The pipeline includes:

- Entity resolution and linking to PrimeKG nodes.
- Multi-hop query traversal for drug-disease-pathway chains.
- Graph-guided generation and explanation tracing.

> 📎 Repositories and references:
> - [TxAgent GitHub](https://github.com/mims-harvard/TxAgent)
> - [PrimeKG Paper](https://www.nature.com/articles/s41597-023-01960-3)

---

## 🚀 Getting Started

### 📁 Clone the Repository

```bash
git clone https://github.com/75Dineshchandra/KgTxAgent.git
cd KgTxAgent
```

---

## 📦 Installation

Ensure you have Python 3.8+ installed:

```bash
pip install -r requirements.txt
```

---

## 📁 Repository Structure

```
src/
├── Code/
│   ├── Datadownloader/                 # PrimeKG downloader
│   ├── Tools/                        # Reports and summaries
=======
│       ├── openfda/                    # API response test scripts + guides
│       └── tool_universe/             # Modular reusable FDA tools
│       └── PrimeKG/                        # Graph builder, queries, notebooks
├── logs/                               # Logs from PrimeKG downloader
├── reports/                            # Analysis or results (optional)
```

---

## 🧬 PrimeKG Downloader

To download and prepare PrimeKG:

```bash
python src/Code/Datadownloader/primekg_downloader.py
```

Outputs:
- CSV/TAB files in: `src/Code/data/primekg/`
- Log file: `logs/primekg_download.log`

---

## 📚 Tool Documentation

Each modular tool is documented with a corresponding Markdown guide to help you understand inputs, outputs, and usage. Browse the links below for full documentation.

### 🛠 ToolUniverse Tools (`src/Code/Tools/tool_universe/`)

| Tool Name           | Markdown Guide                                                                                     |
|---------------------|----------------------------------------------------------------------------------------------------|
| Adverse Reactions   | [test_tool_Adverse_Reactions.md](src/Code/Tools/tool_universe/test/test_tool_Adverse_Reactions.md) |
| Dosage and Storage  | [test_tool_Dosage_and_Storage.md](src/Code/Tools/tool_universe/test/test_tool_Dosage_and_Storage.md) |
| Drug Ingredients    | [test_tool_Drug_Ingredients.md](src/Code/Tools/tool_universe/test/test_tool_Drug_Ingredients.md)   |
| Warnings            | [test_tool_Warnings.md](src/Code/Tools/tool_universe/test/test_tool_Warnings.md)                  |


                                                        |

### 🌐 openFDA API Test Scripts (`src/Code/Tools/openfda/test/`)

| Test Script            | Markdown Guide                                                                                 |
|------------------------|------------------------------------------------------------------------------------------------|
| Device Events          | [device_events_test_guide.md](src/Code/Tools/openfda/test/device_events_test_guide.md)         |
| Drug Adverse Events    | [drug_adverse_events_test_guide.md](src/Code/Tools/openfda/test/drug_adverse_events_test_guide.md) |
| Drug Labeling          | [drug_labeling_test_guide.md](src/Code/Tools/openfda/test/drug_labeling_test_guide.md)         |
| Drug NDC Info          | [drug_ndc_test_guide.md](src/Code/Tools/openfda/test/drug_ndc_test_guide.md)                   |
| Drug Recalls           | [drug_recalls_test_guide.md](src/Code/Tools/openfda/test/drug_recalls_test_guide.md)           |
| Food Recalls           | [food_recalls_test_guide.md](src/Code/Tools/openfda/test/food_recalls_test_guide.md)           |


> 🔍 See the full list in: [tools_description.md](src/Code/Tools/tool_universe/tools_description.md)
---

## 📘 PrimeKG Scripts & Visualizations

These scripts and guides help you build, explore, and query the PrimeKG biomedical graph using Python and Jupyter — no graph database required.

| File / Script                             | Description                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [`Build_graph.py`](src/Code/PrimeKG/Build_graph.py) | 📦 Loads PrimeKG CSVs, builds a NetworkX graph, enriches with drug/disease features, adds BERT similarity links, and visualizes subgraphs interactively. Saves `.pkl` and `.png`. |
| [`build_graph.md`](src/Code/PrimeKG/build_graph.md) | 📘 Detailed markdown guide covering graph construction, feature enrichment, size stats, node type distribution, BERT-based similarity, and visual query examples. |
| [`KG_Query.ipynb`](src/Code/PrimeKG/KG_Query.ipynb) | 🔍 Interactive notebook to run entity-level queries like gene–disease–drug paths, similarity lookups, and multi-hop graph traversal using NetworkX. |
| [`PrimeKG_Full_Query_Detailed.md`](src/Code/PrimeKG/PrimeKG_Full_Query_Detailed.md) | 📖 Query blueprint with detailed disease, drug, and gene examples — shows how to match entities from features CSVs, extract `node_index`, and query relations using pandas + NetworkX. |

> 🗃️ All CSV data lives in `src/Code/data/primekg/`.  
> 📊 Graph exports and neighborhood subgraphs are saved in `outputs/`.  
> 🖼️ Visualizations include `primekg_full_graph.png`, drug–gene graphs, BERT clusters, and shortest path diagrams.

---
## ✅ What's Included

- ✅ PrimeKG dataset + querying tools  
- ✅ Knowledge-graph enhanced therapeutic reasoning  
- ✅ FDA-compliant structured toolkits  
- ✅ Real-world openFDA pipeline testing  
- ✅ Complete documentation for each module  

---

- 📘 Based on [PrimeKG (Harvard)](https://github.com/mims-harvard/PrimeKG)  
- 💊 Powered by [openFDA](https://open.fda.gov)  
- 🤖 Language Reasoning via [TxAgent](https://github.com/mims-harvard/TxAgent)
