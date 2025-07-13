#%%
#%%
import pandas as pd
import os

# Change working directory to where your files are
os.chdir("/home/ubuntu/primekg")

# List of all your CSV files and labels
files = {
    "README.txt": "📘 README",
    "nodes.csv": "🧠 Nodes",
    "kg.csv": "📊 KG",
    "kg_raw.csv": "📊 KG Raw",
    "kg_grouped.csv": "📦 KG Grouped",
    "kg_grouped_diseases.csv": "🧬 KG Grouped Diseases",
    "kg_grouped_diseases_bert_map.csv": "🧬 KG Diseases BERT Map",
    "kg.giant.csv": "🗺️ KG Giant",
    "edges.csv": "🔗 Edges",
    "drug_features.csv": "💊 Drug Features",
    "disease_features.csv": "🦠 Disease Features"
}

# Load and preview each file
for file, label in files.items():
    print(f"\n--- {label} ({file}) ---")
    try:
        if file.endswith(".txt"):
            with open(file, "r") as f:
                print(f.read().strip()[:1000])  # Show first 1000 chars
        else:
            df = pd.read_csv(file)
            print(df.head())
    except Exception as e:
        print(f"❌ Failed to load {file}: {e}")

# %%
import networkx as nx

# Load main files again for clarity
nodes_df = pd.read_csv("nodes.csv")
kg_df = pd.read_csv("kg.csv", low_memory=False)

# Initialize a directed graph
G = nx.DiGraph()

# Add all nodes
for _, row in nodes_df.iterrows():
    G.add_node(
        row["node_index"],
        node_id=row["node_id"],
        node_type=row["node_type"],
        node_name=row["node_name"],
        node_source=row["node_source"]
    )

# Add all edges with relation info
for _, row in kg_df.iterrows():
    G.add_edge(
        row["x_index"],
        row["y_index"],
        relation=row["relation"],
        display_relation=row["display_relation"]
    )

print(f"✅ Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

#%%
# Load feature files
drug_df = pd.read_csv("drug_features.csv")
disease_df = pd.read_csv("disease_features.csv")

# Add features to drug nodes
for _, row in drug_df.iterrows():
    idx = row["node_index"]
    if idx in G:
        for col in drug_df.columns[1:]:  # skip node_index
            G.nodes[idx][col] = row[col]

# Add features to disease nodes
for _, row in disease_df.iterrows():
    idx = row["node_index"]
    if idx in G:
        for col in disease_df.columns[1:]:
            G.nodes[idx][col] = row[col]

print("✅ Drug and disease features enriched into graph.")

#%%
# Optional: Add BERT similarity edges between grouped diseases
bert_map_df = pd.read_csv("kg_grouped_diseases_bert_map.csv")
print("✅ BERT disease groupings loaded.")

bert_edge_count = 0
for _, row in bert_map_df.iterrows():
    disease_id = row["node_id"]
    group_ids = str(row["group_id_bert"]).split("_")

    for gid in group_ids:
        if gid != disease_id and G.has_node(int(disease_id)) and G.has_node(int(gid)):
            G.add_edge(int(disease_id), int(gid), relation="bert_group", display_relation="BERT similarity")
            bert_edge_count += 1

print(f"✅ BERT edges added: {bert_edge_count:,}")

#%%
from collections import Counter
import networkx as nx
import random

print("🔍 Running PrimeKG Graph Health Check...\n")

# 🎯 1. Size
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"📏 Graph Size: {num_nodes:,} nodes, {num_edges:,} edges")

#%%
# 🔬 2. Type Counts
node_types = [data["node_type"] for _, data in G.nodes(data=True) if "node_type" in data]
type_counts = Counter(node_types)
print("\n🧬 Node Type Counts:")
for k, v in type_counts.items():
    print(f"  - {k}: {v:,}")


#%%
# 🧩 3. Connectivity
if isinstance(G, nx.DiGraph):
    weak_cc = nx.number_weakly_connected_components(G)
    strong_cc = nx.number_strongly_connected_components(G)
    print(f"\n🔗 Connectivity (Directed Graph):")
    print(f"  - Weakly Connected Components: {weak_cc}")
    print(f"  - Strongly Connected Components: {strong_cc}")
else:
    cc = nx.number_connected_components(G)
    print(f"\n🔗 Connectivity (Undirected Graph): {cc} connected components")


#%%
# 🔄 4. Try Random Path Check
print("\n🔄 Path Check: Trying 1 random gene → disease...")
genes = [n for n, d in G.nodes(data=True) if d.get("node_type") == "gene/protein"]
diseases = [n for n, d in G.nodes(data=True) if d.get("node_type") == "disease"]

src = random.choice(genes)
tgt = random.choice(diseases)

src_name = G.nodes[src]["node_name"]
tgt_name = G.nodes[tgt]["node_name"]

print(f"  - From gene: {src_name}")
print(f"  - To disease: {tgt_name}")

try:
    path = nx.shortest_path(G, source=src, target=tgt)
    readable_path = [G.nodes[n].get("node_name", str(n)) for n in path]
    print(f"  ✅ Path found ({len(path)} steps):")
    print("    → " + " → ".join(readable_path))
except nx.NetworkXNoPath:
    print("  ❌ No path found between them.")

#%%
# 📈 5. Degree Distribution
degrees = [deg for _, deg in G.degree()]
print("\n📈 Degree Distribution:")
print(f"  - Min Degree: {min(degrees)}")
print(f"  - Max Degree: {max(degrees)}")
print(f"  - Average Degree: {sum(degrees) / len(degrees):.2f}")


#%%

import plotly.graph_objects as go
import networkx as nx

def draw_neighbors_interactive(entity_name):
    # Map names to node IDs
    node_map = {data['node_name']: n for n, data in G.nodes(data=True)}
    node = node_map.get(entity_name)
    
    if node is None:
        print("Entity not found.")
        return
    
    # Get neighbors + subgraph
    neighbors = list(G.neighbors(node))
    sub_nodes = [node] + neighbors
    subgraph = G.subgraph(sub_nodes)

    # Spring layout
    pos = nx.spring_layout(subgraph, seed=42)

    # Node coordinates and hover text
    node_x, node_y, hovertext = [], [], []
    for n in subgraph.nodes():
        x, y = pos[n]
        node_x.append(x)
        node_y.append(y)
        node_data = G.nodes[n]
        hovertext.append(f"{node_data['node_name']}<br>({node_data['node_type']})")

    # Edges
    edge_x, edge_y = [], []
    for u, v in subgraph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[G.nodes[n]['node_name'] for n in subgraph.nodes()],
        hovertext=hovertext,
        hoverinfo='text',
        textposition="top center",
        marker=dict(
            color='skyblue',
            size=20,
            line=dict(width=2, color='darkblue')
        )
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(
                text=f"🧠 Interactive Neighborhood of '{entity_name}'",
                font=dict(size=22)
            ),
            showlegend=False,
            hovermode='closest',
            margin=dict(b=40, l=40, r=40, t=60),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
            height=800
        )
    )

    fig.show()

# ✅ Try it:
draw_neighbors_interactive("asthma")


#%%
import plotly.graph_objects as go
import networkx as nx

# --- Helper Functions ---

def get_node(name):
    return next((n for n, d in G.nodes(data=True) if d.get("node_name") == name), None)

def draw_interactive_subgraph(node_names, title="Subgraph"):
    name_to_index = {data["node_name"]: n for n, data in G.nodes(data=True)}
    indices = [name_to_index[name] for name in node_names if name in name_to_index]
    subgraph = G.subgraph(indices)

    if not subgraph.nodes:
        print("⚠️ No valid nodes to draw.")
        return

    pos = nx.spring_layout(subgraph, seed=1)
    node_x, node_y, hovertext = [], [], []

    for n in subgraph.nodes():
        x, y = pos[n]
        node_x.append(x)
        node_y.append(y)
        d = G.nodes[n]
        hovertext.append(f"{d['node_name']}<br>({d['node_type']})")

    edge_x, edge_y = [], []
    for u, v in subgraph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[G.nodes[n]['node_name'] for n in subgraph.nodes()],
        hovertext=hovertext,
        hoverinfo='text',
        textposition="top center",
        marker=dict(
            color='skyblue',
            size=20,
            line=dict(width=2, color='darkblue')
        )
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(
                text=title,
                font=dict(size=22)
            ),
            showlegend=False,
            hovermode='closest',
            margin=dict(b=40, l=40, r=40, t=60),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
            height=800
        )
    )

    fig.show()

def get_drugs_for_disease(disease_name):
    disease_node = get_node(disease_name)
    return [G.nodes[n]['node_name'] for n in G.neighbors(disease_node)
            if G.nodes[n]['node_type'] == 'drug'] if disease_node else []

def get_genes_for_disease(disease_name):
    disease_node = get_node(disease_name)
    return [G.nodes[n]['node_name'] for n in G.neighbors(disease_node)
            if G.nodes[n]['node_type'] == 'gene/protein'] if disease_node else []

def draw_shortest_path(entity1, entity2):
    name_to_node = {data['node_name']: n for n, data in G.nodes(data=True)}
    src = name_to_node.get(entity1)
    tgt = name_to_node.get(entity2)
    if not src or not tgt or not nx.has_path(G, src, tgt):
        print(f"❌ No path found between '{entity1}' and '{entity2}'")
        return
    path = nx.shortest_path(G, src, tgt)
    readable_path = [G.nodes[n]["node_name"] for n in path]
    print(f"✅ Shortest path ({len(path)} steps): {' → '.join(readable_path)}")
    draw_interactive_subgraph(readable_path, title=f"Shortest Path: {entity1} → {entity2}")

def find_drugs_sharing_side_effects(drug_name):
    drug_node = get_node(drug_name)
    if drug_node is None: return []
    side_effects = [n for n in G.neighbors(drug_node)
                    if G.nodes[n]['node_type'] == 'effect/phenotype']
    shared = set()
    for se in side_effects:
        for neighbor in G.neighbors(se):
            if neighbor != drug_node and G.nodes[neighbor]["node_type"] == "drug":
                shared.add(G.nodes[neighbor]["node_name"])
    return list(shared)
#%%
# --- Link asthma to BERT-similar diseases ---
bert_map_df = pd.read_csv("kg_grouped_diseases_bert_map.csv")
asthma_node = get_node("asthma")

asthma_cluster = bert_map_df[
    bert_map_df["group_name_bert"].str.contains("asthma", case=False)
]

bert_cluster_edge_count = 0
if asthma_node is not None and not asthma_cluster.empty:
    for _, row in asthma_cluster.iterrows():
        target_id = row["node_id"]
        if G.has_node(target_id):
            G.add_edge(asthma_node, target_id,
                       relation="bert_related",
                       display_relation="BERT cluster approx")
            bert_cluster_edge_count += 1

print(f"✅ Linked 'asthma' to {bert_cluster_edge_count} BERT-clustered diseases.\n")


#%%
# --- Run All Queries on a Sample Entity ---

entity = "asthma"
drug_query = "albuterol"

# 1. Drugs
print(f"\n💊 Drugs used for '{entity}':")
drugs = get_drugs_for_disease(entity)
print(drugs[:10])
draw_interactive_subgraph([entity] + drugs[:10], title="Drugs for Disease")

# 2. Genes
print(f"\n🧬 Genes linked to '{entity}':")
genes = get_genes_for_disease(entity)
print(genes[:10])
draw_interactive_subgraph([entity] + genes[:10], title="Genes for Disease")

# 3. Shortest path
print(f"\n🔗 Shortest path from 'TP53' to '{entity}':")
draw_shortest_path("TP53", entity)

# 4. BERT group (linked manually above)
print(f"\n🧠 BERT-similar diseases to '{entity}':")
bert_siblings = [G.nodes[n]['node_name']
                 for n in G.successors(asthma_node)
                 if G[asthma_node][n]["relation"] == "bert_related"]
if bert_siblings:
    print(bert_siblings[:10])
    draw_interactive_subgraph([entity] + bert_siblings, title="BERT-Similar Diseases (Asthma)")
else:
    print("❌ No BERT-linked diseases found.")

# 5. Shared side effect drugs
print(f"\n⚠️ Drugs that share side effects with '{drug_query}':")
shared = find_drugs_sharing_side_effects(drug_query)
if shared:
    print(shared[:10])
    draw_interactive_subgraph([drug_query] + shared[:10], title="Shared Side Effects")
else:
    print("❌ No shared side-effect drugs found.")

# %%
#save graph
# %%
# Save the current state of the graph to a file
import pickle

graph_path = "primekg_graph.pkl"
with open(graph_path, "wb") as f:
    pickle.dump(G, f)

print(f"✅ Graph saved to: {graph_path}")

#%%
#Full Graph Visualization
# %%
# Load the graph and generate full visualization
import pickle
import networkx as nx
import matplotlib.pyplot as plt

# Load the saved graph
with open("primekg_graph.pkl", "rb") as f:
    G = pickle.load(f)

print(f"✅ Graph loaded with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

# Try Graphviz layout if possible (for better large-scale layout)
try:
    from networkx.drawing.nx_agraph import graphviz_layout
    print("⚡ Using Graphviz layout (sfdp)")
    pos = graphviz_layout(G, prog="sfdp")
except ImportError:
    print("🐢 Falling back to spring layout (slower for large graphs)")
    pos = nx.spring_layout(G, k=0.005, iterations=30, seed=42)

# Plot and save
plt.figure(figsize=(80, 80))  # Extra large canvas
nx.draw(
    G,
    pos,
    node_size=2,
    edge_color="gray",
    width=0.1,
    node_color="blue",
    alpha=0.4,
    with_labels=False
)

plt.title("Full PrimeKG Graph", fontsize=36)
plt.tight_layout()
plt.savefig("primekg_full_graph.png", dpi=300)
plt.close()
print("✅ Full graph image saved to: primekg_full_graph.png")

# %%

# %%
