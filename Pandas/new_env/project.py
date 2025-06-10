import pandas as pd
from faker import Faker
import random
import networkx as nx
import matplotlib.pyplot as plt

# Initialize Faker
fake = Faker()

# Generate fake employee data
data = {
    "Employee_ID": [fake.unique.random_number(digits=5) for _ in range(5)],
    "Name": [fake.name() for _ in range(5)],
    "Department": [random.choice(["HR", "Finance", "IT", "Manufacturing", "Sales", "Operations"]) for _ in range(5)],
    "Salary": [random.randint(30_000, 120_000) for _ in range(5)],
    "Years_Experience": [random.randint(1, 15) for _ in range(5)],
    "Location": [fake.city() for _ in range(5)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("employee_data.csv", index=False)

# Download (if using Google Colab)
# try:
#     from google.colab import files
#     files.download("employee_data.csv")
#     print("✅ employee_data.csv downloaded!")
# except:
#     print("📁 CSV saved locally as 'employee_data.csv'")

relations = {
    "Department": "works in",
    "Salary": "has salary of",
    "Years_Experience": "has experience of",
    "Location": "is located in"
}

triples = []
for _, row in df.iterrows():
    source = row["Name"]
    for col, relation in relations.items():
        target = row[col]
        triples.append({"Source": source, "Relation": relation, "Target": target})


# print("The values are ",triples)  
# Convert to DataFrame
triples_df = pd.DataFrame(triples)

# print(triples_df)


with open("employee_data.metta", "w") as f:
    for src, rel, tgt in zip(triples_df["Source"], triples_df["Relation"], triples_df["Target"]):
        f.write(f"({src} {rel} {tgt})\n")

print("Data saved to employee_data.metta")


# Initialize a directed graph
G = nx.DiGraph()

# Add edges to the graph based on predefined source, target and relations
for _, row in triples_df.iterrows():
    source = row['Source']
    target = row['Target']
    relation = row['Relation']

    G.add_node(source)
    G.add_node(target)
    G.add_edge(source, target, relation=relation)

# Visualize the knowledge graph with colored nodes
# Calculate node degrees
node_degrees = dict(G.degree)
# Assign colors based on node degrees
node_colors = ['grey' if degree == max(node_degrees.values()) else 'lightpink' for degree in node_degrees.values()]

# Adjust the layout for better spacing
pos = nx.spring_layout(G, seed=50, k=5)

labels = nx.get_edge_attributes(G, 'relation')

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color=node_colors, font_size=8, arrowsize=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
# plt.show()

plt.savefig("knowledge_graph.png", dpi=300)
print("Knowledge graph saved as knowledge_graph.png")
