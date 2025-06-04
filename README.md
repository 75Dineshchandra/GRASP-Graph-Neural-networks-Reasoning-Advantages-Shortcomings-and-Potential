

## PrimeTxAgent: Therapeutic Reasoning via Knowledge Graphs using PrimeKG
### Proposed by: Dinesh Chandra Gaddam
#### Email: dineshchandra.gaddam@gwu.edu
#### Advisor: Amir Jafari
#### The George Washington University, Washington DC  
#### Data Science Program

## 1 Objective:  
 
    The goal of this project is to build a biomedical knowledge graph-based agent that performs therapeutic reasoning by integrating PrimeKG with tool-based biomedical reasoning similar to Harvard’s TxAgent. 
    We will build a graph-based knowledge engine that enables multi-hop reasoning over PrimeKG and integrates with curated biomedical tools (from ToolUniverse) for drug-disease-treatment inference.
    


## 2 Dataset:  

    PrimeKG will be used as the core knowledge graph. It includes over 4 million relationships across drugs, diseases, genes, phenotypes, and clinical guidelines. 
    Additional data may be pulled from OpenFDA, Open Targets, and drug ontology APIs as used in the ToolUniverse repository.
    

## 3 Rationale:  

    Current LLM-based therapeutic agents often rely on textual retrieval. This project brings graph-based reasoning into the loop by using PrimeKG to provide structured, explainable, and multi-relational 
    drug-disease inference. It mirrors TxAgent but grounds reasoning on graph paths and knowledge embeddings, enhancing interpretability and integration with biomedical ontologies.
    

## 4 Approach:  

    The project will follow these phases:
    **Phase 1 – Graph Construction**: Parse and load PrimeKG into a graph database (e.g., Neo4j or NetworkX).
    **Phase 2 – Tool Wrapping**: Integrate biomedical tools (e.g., DrugChecker, InteractionScorer) using scripts adapted from ToolUniverse.
    **Phase 3 – Agent Development**: Create a hybrid reasoning engine that uses PrimeKG for subgraph extraction and external tools for evidence verification.
    **Phase 4 – Evaluation**: Benchmark the system on DrugPC, TreatmentPC, and DescriptionPC tasks to assess reasoning accuracy and coverage.
    **Phase 5 – Optional LLM Integration**: If time allows, wrap the system in an LLM interface with RAG-style querying.
    

## 5 Timeline:  

    **Weeks 1–2**: Study PrimeKG schema, install ToolUniverse, define task objectives.
    **Weeks 3–6**: Build graph database and run KG sanity checks (degree stats, drug clusters, etc.).
    **Weeks 7–10**: Integrate at least 5 tools from ToolUniverse and enable function calls.
    **Weeks 11–14**: Implement and test multi-hop reasoning agent (e.g., Drug → Gene → Disease → Phenotype).
    **Weeks 15–16**: Run benchmarks and finalize results for presentation.
    

## 6 Expected Number Students:  

    This project is suitable for a team of 2-3 students with expertise in biomedical AI, NLP, or graph neural networks.
    

## 7 Possible Issues:  

    **Tool Integration Complexity**: ToolUniverse has over 200 tools—deciding which to integrate and managing input/output formats can be time-consuming.
    **Graph Reasoning**: Performing explainable multi-hop traversal over a massive KG requires careful pruning and optimization.
    **LLM Interfacing**: If RAG or function-calling is integrated, latency and context handling can become bottlenecks.
    

## Contact
- Author: Amir Jafari
- Email: [ajafari@gmail.com](mailto:ajafari@email.gwu.edu)
- GitHub: [Dinesh](https://github.com/75Dineshchandra)
