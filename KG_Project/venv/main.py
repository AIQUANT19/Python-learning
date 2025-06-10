import nltk
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download resources (only first time)
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Create a small custom dataset with sentences

data = {
    "sentence": [
        "John is the father of Alice.",
        "Mary is the mother of Alice.",
        "Alice is the sister of Bob.",
        "John is married to Mary.",
        "Bob is the son of Mary.",
        "Alice likes painting.",
        "Bob likes football.",
        "Mary likes gardening.",
        "John likes fishing.",
        "Alice is the aunt of Charlie.",
        "Charlie is the son of Bob.",
        "Charlie likes video games.",
        "Mary is the grandmother of Charlie.",
        "John is the grandfather of Charlie.",
    ],
    "source": [
        "John",
        "Mary",
        "Alice",
        "John",
        "Bob",
        "Alice",
        "Bob",
        "Mary",
        "John",
        "Alice",
        "Charlie",
        "Charlie",
        "Mary",
        "John"
    ],
    "target": [
        "Alice",
        "Alice",
        "Bob",
        "Mary",
        "Mary",
        "painting",
        "football",
        "gardening",
        "fishing",
        "Charlie",
        "Bob",
        "video games",
        "Charlie",
        "Charlie"
    ],
    "relation": [
        "father of",
        "mother of",
        "sister of",
        "married to",
        "son of",
        "likes",
        "likes",
        "likes",
        "likes",
        "aunt of",
        "son of",
        "likes",
        "grandmother of",
        "grandfather of"
    ]
}
# Save as a Python file
with open("graph_data.metta", "w") as f:
    for src, rel, tgt in zip(data["source"], data["relation"], data["target"]):
        f.write(f"({src} {rel} {tgt})\n")

print("Data saved to graph_data.metta")


# Create a DataFrame
df = pd.DataFrame(data)    # Organizes our data in a table-like format for easy processing
print(df)


# NLP Preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    words = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(text) if word.isalnum() and word.lower() not in stop_words]
    return ' '.join(words)

# Apply preprocessing to sentences in the dataframe
df['processed_sentence'] = df['sentence'].apply(preprocess_text)
print(df)

# Initialize a directed graph
G = nx.DiGraph()

# Add edges to the graph based on predefined source, target and relations
for _, row in df.iterrows():
    source = row['source']
    target = row['target']
    relation = row['relation']

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














# # Sample text
# text = "Albert Einstein was a theoretical physicist. He developed the theory of relativity."

# # Preprocessing
# stop_words = set(stopwords.words("english"))
# lemmatizer = WordNetLemmatizer()

# sentences = sent_tokenize(text)
# words = [word_tokenize(sent) for sent in sentences]
# filtered_words = [[lemmatizer.lemmatize(w.lower()) for w in sent if w.isalnum() and w.lower() not in stop_words] for sent in words]

# # Dummy relation extraction (just linking words for demo)
# G = nx.Graph()
# for sent in filtered_words:
#     for i in range(len(sent)-1):
#         G.add_edge(sent[i], sent[i+1])

# # Draw graph
# nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
# plt.show()
