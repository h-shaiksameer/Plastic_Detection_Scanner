import matplotlib.pyplot as plt
import networkx as nx

# Define nodes with their shapes and descriptions
nodes = {
    "Home Page": ("oval", "Entry Point"),
    "Request Service Page": ("parallelogram", "User Inquiry"),
    "Explore Services Page": ("parallelogram", "Navigation"),
    "Login System": ("diamond", "Access Control"),
    "PSA Platform": ("rectangle", "Main Processing"),
    "Image Processing": ("rectangle", "Plastic Analysis"),
    "Report Generation": ("rectangle", "Generate Report"),
    "Learning Module": ("parallelogram", "Educational Content"),
    "Upcoming Features": ("oval", "Future Enhancements")
}

# Define directed edges (connections between components)
edges = [
    ("Home Page", "Request Service Page"),
    ("Home Page", "Explore Services Page"),
    ("Explore Services Page", "Login System"),
    ("Login System", "PSA Platform"),
    ("PSA Platform", "Image Processing"),
    ("Image Processing", "Report Generation"),
    ("PSA Platform", "Learning Module"),
    ("Learning Module", "Upcoming Features")
]

# Create directed graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Define positions for a modern layout
pos = {
    "Home Page": (0, 4),
    "Request Service Page": (-2, 3),
    "Explore Services Page": (2, 3),
    "Login System": (2, 2),
    "PSA Platform": (2, 1),
    "Image Processing": (4, 0),
    "Report Generation": (4, -1),
    "Learning Module": (0, 0),
    "Upcoming Features": (0, -1)
}

# Define node shapes and colors
shape_styles = {
    "oval": {"shape": "o", "color": "lightblue"},
    "parallelogram": {"shape": "s", "color": "lightgreen"},
    "diamond": {"shape": "D", "color": "orange"},
    "rectangle": {"shape": "h", "color": "lightcoral"}
}

# Increase figure size
plt.figure(figsize=(12, 8))

# Draw nodes with specific shapes and ensure text fits inside
for node, (shape, label) in nodes.items():
    nx.draw_networkx_nodes(
        G, pos, nodelist=[node], node_shape=shape_styles[shape]["shape"],
        node_color=shape_styles[shape]["color"], node_size=6000, alpha=0.9
    )
    plt.text(
        pos[node][0], pos[node][1], label, fontsize=8, ha='center', 
        fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
    )

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, width=1.5, alpha=0.8)

# Draw node labels inside the shapes
nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold", font_color="black")

plt.title("PSA Platform - Modern Flow Diagram", fontsize=14, fontweight="bold")
plt.show()
