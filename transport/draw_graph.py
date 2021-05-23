import networkx as nx
import matplotlib.pyplot as plt

edges = [['A','D'], ['A', 'C'], ['B', 'D'], ['D','E'], ['B', 'C'], ['E', 'F'], ['A', 'F'], ['E', 'B'],['C', 'E'], ['F', 'B'],['C', 'F'],['A', 'B'], ['D', 'A'], ['F','A']]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()

nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
node_size=500,node_color='pink',alpha=0.9,\
labels={node:node for node in G.nodes()})

nx.draw_networkx_edge_labels(G,pos,edge_labels={('A','D'):'100',('A','C'):'250',('B','D'):'347', ('D','E'):'1450',('B','C'):'640',('E','F'):'741',('A','F'):'645',('E','B'):'380', ('C','E'):'140', ('F','B'):'250',('C','F'):'87',('A','B'):'142',('D','A'):'210',('F','A'):'221'},font_color='red')



plt.axis('off')
plt.show()


# plt.savefig("/Users/lehuy/Desktop/graph")


