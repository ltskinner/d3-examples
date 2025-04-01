
import pandas as pd
import json

# Load CSVs
nodes_df = pd.read_csv("nodes.csv")
edges_df = pd.read_csv("edges.csv")

print(nodes_df.head())
print(edges_df.head())

# Assume nodes have 'id', and edges have 'source' and 'target'
def build_tree(nodes, edges, root_id):
    node_dict = {
        int(row['id']): {"id": int(row['id']), "children": []} for _, row in nodes.iterrows()}
    for _, edge in edges.iterrows():
        source = edge['source']
        target = edge['target']
        node_dict[source]['children'].append(node_dict[target])
    return node_dict[root_id]

tree_data = build_tree(nodes_df, edges_df, root_id=1)  # replace with your actual root node ID

# Save as embedded JSON
with open("tree_data.json", "w") as f:
    json.dump(tree_data, f, indent=2)
