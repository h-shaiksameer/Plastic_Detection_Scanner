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
    "Learning Module": (-2, 0),
    "Upcoming Features": (-2, -1)
}

# Define node shapes and colors
shape_styles = {
    "oval": {"shape": "o", "color": "lightblue"},
    "parallelogram": {"shape": "s", "color": "lightgreen"},
    "diamond": {"shape": "D", "color": "orange"},
    "rectangle": {"shape": "h", "color": "lightcoral"}
}

# Increase figure size for clarity
plt.figure(figsize=(12, 8))

# Draw nodes with specific shapes, ensuring text fits inside
for node, (shape, label) in nodes.items():
    nx.draw_networkx_nodes(
        G, pos, nodelist=[node], node_shape=shape_styles[shape]["shape"],
        node_color=shape_styles[shape]["color"], node_size=5000, alpha=0.9
    )
    # Draw node name inside the shape
    nx.draw_networkx_labels(G, {node: pos[node]}, labels={node: node}, font_size=10, font_weight="bold")

    # Position the description slightly away from the node
    x_offset = 0.6 if pos[node][0] >= 0 else -0.6  # Dynamic horizontal offset
    y_offset = -0.3  # Lower vertical offset for better readability
    plt.text(
        pos[node][0] + x_offset, pos[node][1] + y_offset, label, fontsize=9,
        ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
    )

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, width=1.5, alpha=0.8)

plt.title("PSA Platform - Modern Flow Diagram", fontsize=14, fontweight="bold")
plt.show()
