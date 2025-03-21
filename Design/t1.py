import matplotlib.pyplot as plt
import networkx as nx

# Define the main platform sections
sections = [
    "Home Page", "Request Service Page", "Explore Services Page", 
    "PSA Platform", "Learning Module", "Upcoming Features"
]

# Subsections for 'Explore Services Page'
explore_services = [
    "Plastic Suitability Detection", "Report Generation", "User Authentication"
]

# Define main platform connections
connections = [
    ("Home Page", "Request Service Page"),
    ("Home Page", "Explore Services Page"),
    ("Explore Services Page", "PSA Platform"),
    ("PSA Platform", "Learning Module"),
    ("Learning Module", "Upcoming Features"),
]

# Define additional sub-flows for "Explore Services Page"
explore_connections = [
    ("Explore Services Page", "Plastic Suitability Detection"),
    ("Explore Services Page", "Report Generation"),
    ("Explore Services Page", "User Authentication"),
]

# Create a directed graph
G = nx.DiGraph()

# Add main platform sections
G.add_edges_from(connections)

# Add sub-sections for Explore Services Page
G.add_edges_from(explore_connections)

# Define node positions for better structure
pos = {
    "Home Page": (0, 3),
    "Request Service Page": (-2, 2), 
    "Explore Services Page": (2, 2), 
    "PSA Platform": (2, 1), 
    "Learning Module": (2, 0), 
    "Upcoming Features": (2, -1),
    
    # Sub-sections for Explore Services
    "Plastic Suitability Detection": (4, 2.5),
    "Report Generation": (4, 2),
    "User Authentication": (4, 1.5)
}

# Define color schemes for different components
node_colors = {
    "Home Page": "skyblue",
    "Request Service Page": "lightcoral",
    "Explore Services Page": "gold",
    "PSA Platform": "limegreen",
    "Learning Module": "orange",
    "Upcoming Features": "violet",
    
    # Sub-sections
    "Plastic Suitability Detection": "deepskyblue",
    "Report Generation": "dodgerblue",
    "User Authentication": "steelblue"
}

# Draw the graph
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, 
        node_color=[node_colors[node] for node in G.nodes], 
        edge_color="gray", 
        node_size=3000, 
        font_size=9, 
        font_weight="bold", 
        arrows=True, 
        arrowsize=15)

# Add title
plt.title("PSA Platform - Multi-Directional Flowchart", fontsize=12, fontweight="bold")

# Show the graph
plt.show()
