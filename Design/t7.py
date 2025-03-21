import matplotlib.pyplot as plt
import networkx as nx

# --- Enhanced Code for Improved Understanding ---

def create_psa_platform_diagram():
    """
    Creates and displays a diagram representing the PSA (Plastic Sorting Analysis) Platform's architecture.

    This function defines the components (nodes) of the platform, their relationships (edges),
    and visualizes them using NetworkX and Matplotlib. It also includes detailed descriptions
    for each component and uses a clear, organized layout.
    """

    # 1. Define Nodes (Components) with Shapes and Descriptions
    #    - Each node represents a distinct part of the PSA platform.
    #    - The tuple contains: (shape_type, description)
    nodes = {
        "Home Page": ("oval", "Entry point for users to access the platform."),
        "Request Service Page": ("parallelogram", "Allows users to submit requests for plastic analysis."),
        "Explore Services Page": ("parallelogram", "Provides an overview of available services and features."),
        "Learning Module": ("parallelogram", "Offers educational content about plastic sorting and analysis."),
        "Upcoming Features": ("oval", "Highlights planned future enhancements (see detailed description below)."),
        "Login System": ("diamond", "Manages user authentication and access control."),
        "PSA Platform": ("rectangle", "The core processing engine for plastic analysis."),
        "Image Processing": ("rectangle", "Analyzes images to identify and classify plastic types."),
        "Report Generation": ("rectangle", "Creates detailed reports based on the analysis results.")
    }

    # 2. Define Edges (Relationships)
    #    - Edges represent the flow of interaction or data between components.
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

    # 3. Create a Directed Graph
    #    - A directed graph (DiGraph) is used to show the direction of relationships.
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # 4. Define Node Positions for a Clear Layout
    #    - This dictionary specifies the (x, y) coordinates for each node.
    #    - A well-organized layout improves readability.
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

    # 5. Define Node Shape Styles and Colors
    #    - This dictionary maps shape types (e.g., "oval") to visual properties.
    shape_styles = {
        "oval": {"shape": "o", "color": "lightblue"},
        "parallelogram": {"shape": "s", "color": "lightgreen"},
        "diamond": {"shape": "D", "color": "orange"},
        "rectangle": {"shape": "h", "color": "lightcoral"}
    }

    # 6. Customize the Plot
    #    - Increase figure size for better visibility.
    plt.figure(figsize=(14, 9))

    # 7. Draw Nodes with Labels and Descriptions
    for node, (shape, description) in nodes.items():
        # Draw the node shape
        nx.draw_networkx_nodes(
            G, pos, nodelist=[node], node_shape=shape_styles[shape]["shape"],
            node_color=shape_styles[shape]["color"], node_size=7000, alpha=0.9
        )

        # Draw the node name (label) inside the shape
        nx.draw_networkx_labels(
            G, {node: pos[node]}, labels={node: node}, font_size=10, font_weight="bold"
        )

        # Draw the node description inside the shape
        y_offset = -0.3  # Adjust vertical position of the description
        if node == "Upcoming Features":
            # Special handling for the "Upcoming Features" node's detailed description
            text = "Future Enhancements\n- Energy Output Prediction\n- Environmental Impact\n- Cost-Benefit Analysis\n- Multilingual Support"
        else:
            text = description

        plt.text(
            pos[node][0], pos[node][1] + y_offset, text, fontsize=9,
            ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
        )

    # 8. Draw Edges with Arrows
    nx.draw_networkx_edges(G, pos, edge_color="black", arrows=True, width=2, alpha=0.8, arrowstyle='-|>')

    # 9. Add Title and Display the Plot
    plt.title("PSA Platform - Design/Architecture​", fontsize=14, fontweight="bold")
    plt.axis('off')  # Hide the axis
    plt.show()

# --- Run the function to create the diagram ---
create_psa_platform_diagram()
