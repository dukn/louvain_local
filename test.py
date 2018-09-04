from louvain_local import *
import matplotlib.pyplot as plt
import networkx as nx


elist = eval(open('edge.list').read())

G = nx.Graph()
G.add_edges_from(elist)

print (len(G.nodes()), 'nodes')
print (len(G.edges()), 'edges')

partition = get_clusters(G)

pos = nx.spring_layout(G)

nx.draw(G, pos, node_size = 50, node_color=list(partition.values())); plt.show()

plt.show()
