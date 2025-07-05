# %%
#installing tooluniverse package
pip install tooluniverse

# %% [markdown]
# Loading Tool Universe

# %%
# Import the ToolUniverse class from the tooluniverse.execute_function module
from tooluniverse.execute_function import ToolUniverse

# Create an instance of the ToolUniverse class
# This likely sets up the core environment to use and manage various tools (APIs, wrappers, etc.)
tooluni = ToolUniverse()

# Load all available tools into the tool universe instance
# This may initialize tool metadata, endpoints, authentication, and prepare tools for execution
tooluni.load_tools()


# %% [markdown]
# Tool Categorization by Source Module

# %%
import json

# Paths to the tool definition JSON files
tool_files = {
    'opentarget': '/home/ubuntu/.local/lib/python3.8/site-packages/tooluniverse/data/opentarget_tools.json',
    'fda_drug_label': '/home/ubuntu/.local/lib/python3.8/site-packages/tooluniverse/data/fda_drug_labeling_tools.json',
    'special_tools': '/home/ubuntu/.local/lib/python3.8/site-packages/tooluniverse/data/special_tools.json',
    'monarch': '/home/ubuntu/.local/lib/python3.8/site-packages/tooluniverse/data/monarch_tools.json',
}

# Count and print number of tools in each group
for group, path in tool_files.items():
    with open(path, 'r') as f:
        tools = json.load(f)
        print(f"{group} group has {len(tools)} tools.")


# %% [markdown]
# Registered Tool Functions and Descriptions

# %%
# Retrieve all tool names and their corresponding descriptions from the loaded tool universe
tools, descs = tooluni.refresh_tool_name_desc()

# Print a header to indicate the beginning of the tool listing
print("\n=== All Available Tools ===")

# Iterate over each tool name and its matching description
for name, desc in zip(tools, descs):
    # Print the tool name followed by its description
    print(f"{name}\n  ➤ {desc}\n")


# %% [markdown]
# Grouped Tool Descriptions by Domain
# 

# %%
from collections import defaultdict

# Create a dictionary to group tools by their domain (e.g., FDA, Pubmed, Monarch)
category_map = defaultdict(list)

# Iterate through each tool name and description
for name, desc in zip(tools, descs):
    # Extract the domain prefix from the tool name (e.g., "fda_get_drug_info" → "FDA")
    domain = name.split('_')[0].upper()
    
    # Group the tool under the corresponding domain
    category_map[domain].append((name, desc))

# Print tools grouped by domain, with counts and formatted display
for domain, tool_list in category_map.items():
    print(f"\n=== {domain} Tools ({len(tool_list)} tools) ===")
    for name, desc in tool_list:
        print(f"- {name}: {desc}")


# %% [markdown]
# ### Significance of Each Domain
# 
# get_ → Think of this as "just give me the info."
# It’s used for quick, straightforward lookups — like asking, “What’s the description of this disease?”
# 
# retrieve_ → A more detailed version of get_.
# It often brings back richer or more structured information — like pulling a full report instead of a summary.
# 
# drug_ → Tools that focus specifically on drugs.
# These might include side effects, approvals, or how a drug interacts with other things.
# 
# target_ → Tools about biological targets (like genes or proteins).
# Helpful for understanding what a drug is aimed at in the body.
# 
# search_ → Used to look for something when you don’t know the exact name.
# Like typing a few letters into Google and getting suggestions.
# 
# multi_ → Tools that deal with multiple types of information at once — like drugs and diseases and genes.
# 
# callagent / tool_ / finish → These are special tools used by AI agents behind the scenes to plan or complete a task.

# %%
# Define the tool query as a dictionary.
# You're calling a tool named 'get_active_ingredient_info_by_drug_name'
# and passing 'ibuprofen' as the input drug name.
query = {
    "name": "get_active_ingredient_info_by_drug_name",
    "arguments": {
        "drug_name": "ibuprofen"
    }
}

# Use the ToolUniverse to run the query and fetch the result.
output = tooluni.run(query)

# Print the result of the tool's execution
print(output)


# %% [markdown]
# 🔬 Querying Active Ingredient Information for a Drug
# 
# This cell uses a tool from the ToolUniverse to retrieve active ingredient information for a specific drug — in this case, **ibuprofen**.
# 
# - The tool name: `get_active_ingredient_info_by_drug_name`
# - The input argument: `"drug_name": "ibuprofen"`
# - The `run()` function executes the tool with the provided input and returns detailed information, such as:
#   - Active ingredient(s)
#   - Drug formulation details
#   - Associated metadata (if available)
# 
# This is a practical way to fetch structured biomedical data using natural language-friendly API wrappers.
# 

# %%
# Define a list of sample tool queries with different use cases
sample_queries = [
    {
        "name": "get_target_enabling_packages_by_ensemblID",
        "arguments": {
            "keyword": "machine learning"  # May be an incorrect argument for this tool
        }
    },
    {
        "name": "FDA_get_active_ingredient_info_by_drug_name",
        "arguments": {
            "drug_name": "acetaminophen"
        }
    },
    {
        "name": "arxiv_search_paper_by_topic",
        "arguments": {
            "topic": "reinforcement learning"
        }
    },
    {
        "name": "Wikipedia_summary",
        "arguments": {
            "query": "Graph Neural Networks"
        }
    }
]

# Run each query using ToolUniverse and print the results
for q in sample_queries:
    print(f"\n🔍 Running: {q['name']}")
    try:
        # Attempt to execute the query using the loaded tools
        result = tooluni.run(q)
        print(result)
    except Exception as e:
        # Catch and report any error (e.g., invalid tool name, argument mismatch)
        print(f"❌ Failed to run {q['name']}: {e}")


# %% [markdown]
# 🧪 Running Sample Tool Queries Across Multiple Domains
# 
# This block demonstrates how to programmatically run a list of diverse tool queries using the `ToolUniverse` interface.
# 
# Each entry in the `sample_queries` list contains:
# - A **tool name** indicating what function to call
# - A dictionary of **arguments** relevant to the tool's purpose
# 
# The tools being tested here span across different domains:
# - **Biomedical** (`FDA_get_active_ingredient_info_by_drug_name`)
# - **Bioinformatics** (`get_target_enabling_packages_by_ensemblID`)
# - **Scientific search** (`arxiv_search_paper_by_topic`)
# - **General knowledge** (`Wikipedia_summary`)
# 
# The `try...except` block ensures graceful handling of tools that might throw an error due to:
# - Incorrect arguments
# - Missing tools
# - Backend/API issues
# 
# This is a useful pattern when building AI agents or pipelines that work with heterogeneous tools.
# 

# %% [markdown]
# #### Querying by Groups

# %%
# -------------------------------
# MOCK FUNCTIONS for Testing
# Replace these with actual tool functions if available
# -------------------------------

def get_HPO_ID_by_phenotype(phenotype): return {"phenotype": phenotype, "HPO_ID": "HP:XXXX"}
def get_disease_phenotype_overlap(d1, d2): return {"disease1": d1, "disease2": d2, "shared_phenotypes": ["HP:0000001", "HP:0000002"]}
def get_gene_phenotypes(gene): return {"gene": gene, "phenotypes": ["HP:0000001", "HP:0000003"]}

def get_drug_targets(drug): return {"drug": drug, "targets": ["GeneA", "GeneB"]}
def get_gene_drug_interactions(gene): return {"gene": gene, "interacting_drugs": ["DrugX", "DrugY"]}
def get_disease_pathways(disease): return {"disease": disease, "pathways": ["PathwayA", "PathwayB"]}

def get_drug_gene_interactions_by_drug_name(drug): return {"drug": drug, "genes": ["Gene1", "Gene2"]}
def get_pathway_nodes_by_disease_name(disease): return {"disease": disease, "nodes": ["Node1", "Node2"]}
def get_gene_ontology_terms(gene): return {"gene": gene, "GO_terms": ["GO:0008150", "GO:0003674"]}

# -------------------------------
# QUERY EXECUTION
# -------------------------------

# Monarch Tools
monarch_queries = {
    "get_HPO_ID_by_phenotype": ["chronic cough", "muscle weakness", "hearing loss"],
    "get_disease_phenotype_overlap": [("Asthma", "COPD"), ("Autism", "Epilepsy"), ("Diabetes", "Hypertension")],
    "get_gene_phenotypes": ["CFTR", "TP53", "BRCA1"]
}

# Open Targets Tools
open_targets_queries = {
    "get_drug_targets": ["Metformin", "Ibuprofen", "Loratadine"],
    "get_gene_drug_interactions": ["EGFR", "BRAF", "TNF"],
    "get_disease_pathways": ["Parkinson's disease", "Lung cancer", "Crohn's disease"]
}

# openFDA KG Tools
openfda_kg_queries = {
    "get_drug_gene_interactions_by_drug_name": ["Warfarin", "Clopidogrel", "Tamoxifen"],
    "get_pathway_nodes_by_disease_name": ["Alzheimer's disease", "Type 2 diabetes", "Colorectal cancer"],
    "get_gene_ontology_terms": ["FOXP2", "MYH7", "APP"]
}

# -------------------------------
# RUN AND COLLECT RESULTS
# -------------------------------

import pprint

def run_queries(tool_name, tool_fn, queries):
    results = []
    for query in queries:
        if isinstance(query, tuple):
            result = tool_fn(*query)
        else:
            result = tool_fn(query)
        results.append({"input": query, "output": result})
    return {tool_name: results}

final_results = {}

print(" Results:")

# Monarch
final_results.update(run_queries("get_HPO_ID_by_phenotype", get_HPO_ID_by_phenotype, monarch_queries["get_HPO_ID_by_phenotype"]))
final_results.update(run_queries("get_disease_phenotype_overlap", get_disease_phenotype_overlap, monarch_queries["get_disease_phenotype_overlap"]))
final_results.update(run_queries("get_gene_phenotypes", get_gene_phenotypes, monarch_queries["get_gene_phenotypes"]))


# Open Targets
final_results.update(run_queries("get_drug_targets", get_drug_targets, open_targets_queries["get_drug_targets"]))
final_results.update(run_queries("get_gene_drug_interactions", get_gene_drug_interactions, open_targets_queries["get_gene_drug_interactions"]))
final_results.update(run_queries("get_disease_pathways", get_disease_pathways, open_targets_queries["get_disease_pathways"]))


# openFDA KG Tools
final_results.update(run_queries("get_drug_gene_interactions_by_drug_name", get_drug_gene_interactions_by_drug_name, openfda_kg_queries["get_drug_gene_interactions_by_drug_name"]))
final_results.update(run_queries("get_pathway_nodes_by_disease_name", get_pathway_nodes_by_disease_name, openfda_kg_queries["get_pathway_nodes_by_disease_name"]))
final_results.update(run_queries("get_gene_ontology_terms", get_gene_ontology_terms, openfda_kg_queries["get_gene_ontology_terms"]))

# -------------------------------
# DISPLAY
# -------------------------------
pprint.pprint(final_results)


# %% [markdown]
# #### 🧠 Overview: Executing Biomedical KG Tool Functions Across Domains
# 
# 
# This cell demonstrates the execution of various mock biomedical tool functions, grouped by data source or domain. Each function simulates a typical query you might perform using a biomedical API or knowledge graph.
# 
# 🧪 Tool Groups & Their Purpose
# Monarch Tools:
# Focus on phenotypes, diseases, and genes. These tools help link symptoms (phenotypes) to genes or find overlapping features between diseases.
# 
# Open Targets Tools:
# Explore relationships between drugs, targets (genes/proteins), and diseases, which is key for drug discovery and disease treatment research.
# 
# openFDA KG Tools (Knowledge Graph Queries):
# These tools interact with structured knowledge graph data:
# 
# get_drug_gene_interactions_by_drug_name
# → Retrieves gene targets for a drug.
# 
# get_pathway_nodes_by_disease_name
# → Fetches biological pathway components related to a disease.
# 
# get_gene_ontology_terms
# → Lists standardized functions and processes associated with a gene.
# 
# These queries operate over interconnected biomedical entities (like a graph of nodes and edges), making them ideal for tasks like: Relationship extraction, Graph traversal, Reasoning over biomedical data

# %% [markdown]
# #### Summary

# %% [markdown]
# 🧰 ToolUniverse Overview
# 
# **ToolUniverse** is a unified interface that connects to a wide range of biomedical tools and APIs, many of which operate on structured knowledge graph (KG) data. It allows researchers and developers to execute queries related to diseases, genes, drugs, phenotypes, and more using simple commands.
# 
# ---
# 
# 📂 Tool Sources & Categories
# 
# ToolUniverse integrates tools from multiple specialized sources:
# 
# - **Monarch**: Works with phenotypes, diseases, and genes using ontologies like HPO.
# - **Open Targets**: Focuses on drug–gene–disease relationships to support drug discovery.
# - **openFDA KG Tools**: Provides access to structured drug data based on FDA labeling.
# - **Special Tools**: Includes AI-driven utilities for summarization, search, and agent reasoning.
# 
# ---
# 
# ⚙️ Tool Name Prefixes (What They Mean)
# 
# Tool names follow a predictable pattern. The prefix hints at the tool’s purpose:
# 
# - `get_` → Quick lookup (e.g., `get_disease_description`)
# - `retrieve_` → Detailed fetch (e.g., `retrieve_pathway_nodes`)
# - `drug_`, `target_`, `disease_` → Specialized tools for specific biomedical entities
# - `search_` → Performs searches by keyword or concept
# - `multi_` → Involves multiple types of entities (e.g., drug + disease)
# - `tool_`, `callagent`, `finish` → Internal tools for reasoning workflows
# 
# ---
# 
# 🔍 Example Tool Use Cases
# 
# - `get_HPO_ID_by_phenotype`: Get the HPO ID for a human phenotype like "muscle weakness"
# - `get_drug_targets`: List genes targeted by a specific drug (e.g., Ibuprofen)
# - `get_gene_ontology_terms`: Get biological functions linked to a gene
# - `arxiv_search_paper_by_topic`: Find recent papers on a research topic
# - `Wikipedia_summary`: Get a short summary of a concept like "Graph Neural Networks"
# 
# ---
# 
# 🧠 Knowledge Graph Relevance
# 
# Many tools operate over knowledge graphs:
# - **Entities** (nodes): drugs, genes, diseases, phenotypes
# - **Relationships** (edges): "treats", "interacts with", "has phenotype"
# 
# This enables:
# - Semantic search
# - Biological reasoning
# - Multi-step tool chaining (e.g., drug → gene → disease → treatment)
# 
# ---
# 
# 🛠️ How to Use a Tool
# 
# Tools are executed using a dictionary-style query:
# ```python
# query = {
#     "name": "get_drug_targets",
#     "arguments": {"drug": "Aspirin"}
# }
# output = tooluni.run(query)
# 


