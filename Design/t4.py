# import matplotlib.pyplot as plt
# import networkx as nx

# # Define nodes with their shapes and descriptions
# nodes = {
#     "Home Page": ("oval", "Entry Point"),
#     "Request Service Page": ("parallelogram", "User Inquiry"),
#     "Explore Services Page": ("parallelogram", "Navigation"),
#     "Learning Module": ("parallelogram", "Educational Content"),
#     "Upcoming Features": ("oval", "Future Enhancements"),
#     "Login System": ("diamond", "Access Control"),
#     "PSA Platform": ("rectangle", "Main Processing"),
#     "Image Processing": ("rectangle", "Plastic Analysis"),
#     "Report Generation": ("rectangle", "Generate Report")
# }

# # Define directed edges (connections between components)
# edges = [
#     ("Home Page", "Request Service Page"),
#     ("Home Page", "Explore Services Page"),
#     ("Home Page", "Learning Module"),
#     ("Home Page", "Upcoming Features"),
#     ("Explore Services Page", "Login System"),
#     ("Login System", "PSA Platform"),
#     ("PSA Platform", "Image Processing"),
#     ("Image Processing", "Report Generation"),
#     ("PSA Platform", "Learning Module")
# ]

# # Create directed graph
# G = nx.DiGraph()
# G.add_edges_from(edges)

# # Define positions for structured layout
# pos = {
#     "Home Page": (0, 4),
#     "Request Service Page": (-3, 3),
#     "Explore Services Page": (-1, 3),
#     "Learning Module": (1, 3),
#     "Upcoming Features": (3, 3),
#     "Login System": (0, 2),
#     "PSA Platform": (0, 1),
#     "Image Processing": (2, 0),
#     "Report Generation": (2, -1)
# }

# # Define node shapes and colors
# shape_styles = {
#     "oval": {"shape": "o", "color": "lightblue"},
#     "parallelogram": {"shape": "s", "color": "lightgreen"},
#     "diamond": {"shape": "D", "color": "orange"},
#     "rectangle": {"shape": "h", "color": "lightcoral"}
# }

# # Increase figure size for clarity
# plt.figure(figsize=(14, 9))

# # Draw nodes with enhanced size
# for node, (shape, label) in nodes.items():
#     nx.draw_networkx_nodes(
#         G, pos, nodelist=[node], node_shape=shape_styles[shape]["shape"],
#         node_color=shape_styles[shape]["color"], node_size=7500, alpha=0.9
#     )
#     # Draw node name inside the shape
#     nx.draw_networkx_labels(
#         G, {node: pos[node]}, labels={node: node}, font_size=10, font_weight="bold"
#     )

#     # Position descriptions inside the shape
#     y_offset = -0.3 if node != "Upcoming Features" else -0.1  # Prevents text overlap
#     plt.text(
#         pos[node][0], pos[node][1] + y_offset, label, fontsize=9,
#         ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
#     )

# # Draw edges with arrows both in the **middle** and at the **end**
# for edge in edges:
#     start, end = edge
#     mid_x, mid_y = (pos[start][0] + pos[end][0]) / 2, (pos[start][1] + pos[end][1]) / 2

#     # Draw main edge with arrow at the end
#     nx.draw_networkx_edges(G, pos, edgelist=[(start, end)], edge_color="black", arrows=True, width=2, alpha=0.8, arrowstyle='-|>')

#     # Draw extra arrow in the middle
#     plt.annotate(
#         "→", xy=(mid_x, mid_y), xytext=(mid_x, mid_y), fontsize=12,
#         ha='center', va='center', fontweight="bold", color="black"
#     )

# # Add bullet points **below** the "Upcoming Features" node
# upcoming_x, upcoming_y = pos["Upcoming Features"]
# plt.text(
#     upcoming_x, upcoming_y - 0.5,  # Move text below the node
#     "- Energy Output Prediction\n- Environmental Impact\n- Cost-Benefit Analysis\n- Multilingual Support",
#     fontsize=9, ha='center', va='top',
#     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
# )

# plt.title("PSA Platform - Design/Architecture", fontsize=14, fontweight="bold")
# plt.show()

import matplotlib.pyplot as plt
import networkx as nx

# Define nodes with their shapes and descriptions
nodes = {
    "Home Page": ("oval", "Entry Point"),
    "Request Service Page": ("parallelogram", "User Inquiry"),
    "Explore Services Page": ("parallelogram", "Navigation"),
    "Learning Module": ("parallelogram", "Educational Content"),
    "Upcoming Features": ("oval", "Future Enhancements"),
    "Login System": ("diamond", "Access Control"),
    "PSA Platform": ("rectangle", "Main Processing"),
    "Image Processing": ("rectangle", "Plastic Analysis"),
    "Report Generation": ("rectangle", "Generate Report")
}

# Define directed edges (connections between components)
edges = [
    ("Home Page", "Request Service Page"),
    ("Home Page", "Explore Services Page"),
    ("Home Page", "Learning Module"),
    ("Home Page", "Upcoming Features"),
    ("Explore Services Page", "Login System"),
    ("Login System", "PSA Platform"),
    ("PSA Platform", "Image Processing"),
    ("Image Processing", "Report Generation"),
    ("PSA Platform", "Learning Module")
]

# Create directed graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Define positions for structured layout
pos = {
    "Home Page": (0, 4),
    "Request Service Page": (-3, 3),
    "Explore Services Page": (-1, 3),
    "Learning Module": (1, 3),
    "Upcoming Features": (3, 3),
    "Login System": (0, 2),
    "PSA Platform": (0, 1),
    "Image Processing": (2, 0),
    "Report Generation": (2, -1)
}

# Define node shapes and colors
shape_styles = {
    "oval": {"shape": "o", "color": "lightblue"},
    "parallelogram": {"shape": "s", "color": "lightgreen"},
    "diamond": {"shape": "D", "color": "orange"},
    "rectangle": {"shape": "h", "color": "lightcoral"}
}

# Increase figure size for clarity
plt.figure(figsize=(14, 9))

# Draw nodes with enhanced size
for node, (shape, label) in nodes.items():
    nx.draw_networkx_nodes(
        G, pos, nodelist=[node], node_shape=shape_styles[shape]["shape"],
        node_color=shape_styles[shape]["color"], node_size=8000, alpha=0.9
    )
    
    # Reduce font size **only for long labels**
    font_size = 10 if len(node) <= 15 else 9

    # Adjust label position for better fit
    nx.draw_networkx_labels(
        G, {node: pos[node]}, labels={node: node}, font_size=font_size, font_weight="bold"
    )

    # Adjust description box size and padding
    y_offset = -0.3 if node != "Upcoming Features" else -0.1
    plt.text(
        pos[node][0], pos[node][1] + y_offset, label, fontsize=9,
        ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.4')
    )

# Draw edges with arrows **at both the middle and the end**
for edge in edges:
    start, end = edge
    mid_x, mid_y = (pos[start][0] + pos[end][0]) / 2, (pos[start][1] + pos[end][1]) / 2

    # Main edge with arrow at the end
    nx.draw_networkx_edges(G, pos, edgelist=[(start, end)], edge_color="black", arrows=True, width=2, alpha=0.8, arrowstyle='-|>')

    # Extra arrow in the middle
    plt.annotate(
        "→", xy=(mid_x, mid_y), xytext=(mid_x, mid_y), fontsize=12,
        ha='center', va='center', fontweight="bold", color="black"
    )

# Add bullet points **below** the "Upcoming Features" node
upcoming_x, upcoming_y = pos["Upcoming Features"]
plt.text(
    upcoming_x, upcoming_y - 0.5,  # Move text below the node
    "- Energy Output Prediction\n- Environmental Impact\n- Cost-Benefit Analysis\n- Multilingual Support",
    fontsize=9, ha='center', va='top',
    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
)

plt.title("PSA Platform - Design/Architecture", fontsize=14, fontweight="bold")
plt.show()
