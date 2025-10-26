import networkx as nx
import matplotlib.pyplot as plt

S = [
    [2, 3, 5, 4, 1, 0], # a row
    [4, 5, 3, 2, 0, 1], # b row
    [5, 4, 0, 1, 3, 2], # a^2 row
    [1, 0, 4, 5, 2, 3], # ab row
    [3, 2, 1, 0, 5, 4], # ba row
    [0, 1, 2, 3, 4, 5]  # b^2 row
]
elements = ["a", "b", "a^2", "ab", "ba", "b^2"]
n = len(elements)

print(f"Semigroup Size |S| = {n}")
if n != 6:
    print("ERROR: The semigroup does not have the expected 6 elements. Calculation aborted.")
    exit()

vertices = [(i, j, S[i][j]) for i in range(n) for j in range(n)]
n_vertices = len(vertices)
print(f"Number of vertices: {n_vertices}")

G = nx.Graph()
G.add_nodes_from(range(n_vertices))

for i in range(n_vertices):
    for j in range(i + 1, n_vertices):
        v1 = vertices[i]
        v2 = vertices[j]
        common = sum(1 for a, b in zip(v1, v2) if a == b)
        if common == 1:
            G.add_edge(i, j)

degrees = sorted(dict(G.degree()).values())
unique_degrees = set(degrees)
is_regular_graph = len(unique_degrees) == 1

print("\n--- Regularity Report (S defined by multiplication table) ---")
print(f"Is Γ(S) a regular graph? {is_regular_graph}")
if is_regular_graph:
    print(f"Common degree: {degrees[0]}")
else:
    print(f"Degree set: {sorted(list(unique_degrees))}")

print("\nGenerating graph visualization...")
labels = {i: f"({elements[v[0]]}, {elements[v[1]]}, {elements[v[2]]})"
          for i, v in enumerate(vertices)}
plt.figure(figsize=(16, 16))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, labels=labels, with_labels=True, node_size=800, font_size=8, node_color="skyblue", edge_color="gray")
plt.title("Generalized Latin Square Graph Γ(S4)", size=20)
plt.show()