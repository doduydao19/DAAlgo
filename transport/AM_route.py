import pandas
import networkx
import numpy as np



data_route = pandas.read_excel("/Users/lehuy/Downloads/Daa/routeData.xlsx", header = None)

edgeList_route = data_route.values.tolist()


GRoute = networkx.DiGraph()

for i in range(len(edgeList_route)):
    if i > 1:
        GRoute.add_edge(edgeList_route[i][0], edgeList_route[i][1], weight=edgeList_route[i][2])

A = networkx.adjacency_matrix(GRoute).A


print(A)
print(A.shape)


