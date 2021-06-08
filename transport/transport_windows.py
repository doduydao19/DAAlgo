import pandas as pd
from pathlib import Path
import os
import platform
import sys
import operator
sys.setrecursionlimit(1000)

class MinPath:
    def __init__(self, start, end, time, harbours):
        self.start = start.upper()
        self.end = end.upper()
        self.time = time
        self.harbours = harbours

        self.train_map = self.make_train_map(harbours)

        # self.route = self.dijk()

    def find_adj(self, name_harbour):
        list_h_adj = []
        for h in self.harbours:
            if h[0] == name_harbour:
                list_h_adj.append([h[1], float(h[2])])
        return list_h_adj

    def make_train_map(self, harbours):
        train_map = {}
        for h in harbours:
            start = h[0]
            end = h[1]
            dist = float(h[2])
            val = {}
            list_h_adj = self.find_adj(start)
            if list_h_adj != None:
                for h_adj in list_h_adj:
                    val[h_adj[0]] = h_adj[1]
            train_map[start] = val
        # print(train_map)
        return train_map

    # train_map{}: key = start
    # value = {} key =


    def try_node(self, current, n, visited, neighbor, route, dist, f):
        if self.start == self.end:
            return -1 
        if route[current] == self.end:

            for i in range(0, n):
                f.write(route[i] + "\t")
            f.write(str(dist[n - 1]) + "\n")

        while len(neighbor[current]) > 0:
            x = (neighbor[current])[0][1]
            route[current + 1] = neighbor[current].pop(0)[0]
            if route[current + 1] not in visited and route[current + 1] != self.start:
                dist.append(x + dist[current])

                visited.append(route[current + 1])
                if current + 1 == n - 1 and route[current + 1] == self.end:

                    neighbor[current + 1] = self.find_adj(route[current + 1])
                    return self.try_node(current + 1 , n, visited, neighbor, route, dist, f)
                elif current + 1 == n - 1 and route[current + 1] != self.end:
                    visited.remove(route[current + 1])
                    dist.pop(current + 1)
                elif current + 1 < n - 1 and route[current + 1] == self.end:
                    visited.remove(route[current + 1])
                    dist.pop(current + 1)

                elif current + 1 < n:
                    neighbor[current + 1] = self.find_adj(route[current + 1])
                    return self.try_node(current + 1 , n, visited, neighbor, route, dist, f)

                if current + 1 > len(visited):
                    visited.remove(route[current + 1])
                    dist.pop(current + 1)
        if current > 0:
            visited.remove(route[current])
            dist.pop(current)
            return self.try_node(current - 1 , n, visited, neighbor, route, dist, f)


    def find_min_path(self, harbours, path_out):
        train_map = self.make_train_map(harbours)
        node = list(train_map.keys())
        n = len(node)
        # danh dau trang thai
        visited = []
        # bang phuong an
        route = ["NULL"]*(n+1)
        route[0] = self.start

        neighbor = ["NULL"]*(n)
        visited.append(self.start)
        current_dist = 0
        current = 0

        dist = []
        dist.append(float(0))
        neighbor[current] = self.find_adj(route[current])
        result = []
        min = float('inf')
        temp = -1

        f = open(path_out + 'outTrans.txt', 'w', encoding="utf-8")
        self.try_node(current, n, visited, neighbor, route, dist, f)
        f.close()
        
        out_file = open(path_out + 'outTrans.txt', 'r', encoding="utf-8")

        for line in out_file:
            result.append(line.strip("\n").split("\t"))
        out_file.close()

        for i in range(0, len(result)):
            if float(result[i][n]) < min:
                min = float(result[i][n])
                temp = i

        file = open(path_out + 'outTrans.txt', 'w', encoding="utf-8")
        
        if temp != -1:
            # print(result[temp])
            file.write("Shortest path from " + self.start + " to " + self.end + ": " + str(result[temp][n]) + " km\n" + "Route: ")
            for i in range(0, n):
                file.write(result[temp][i])
                if i != n - 1:
                    file.write(" -> ")
        else:
            print("No route!")
            file.write("No route!")
        file.close()

        output = open(path_out + 'output.txt', 'w', encoding="utf-8")
        
        if temp != -1:
            for i in range(0, n):
                output.write(result[temp][i] + "\n")
        output.close()
        out_route = []
        if temp != -1:
            out_route = result[temp][:n]

        return self.start, self.end, (out_route)

def inputHarbours(path):
    with open(path, "r", encoding="utf-8") as f:
        harbours = []
        for line in f:
            harbour = line.strip("\n").split("\t")
            harbours.append(harbour)

    # for h in harbours:
    #     print(h)
    return harbours


def get_info_har(harbours, name_har):
    for h in harbours:
        if h[0] == name_har:
            return h


def output_route(path_out, s, e, route, harbours):
    # outTrans = open(path_out + 'outTrans.txt', 'w', encoding="utf-8")

    # har = get_info_har(harbours, s)

    f = open(path_out + 'route.txt', 'w', encoding="utf-8")
    for i in route:
        har = get_info_har(harbours, i)
        print(i)
        f.write(har[0] + "\t" + har[4])
        f.write("\n")
    f.close()


def make_route_auto(source, dest):
    path = "data.txt"
    # path = "D:/DAAlgo/data.txt"
    path_out = "D:/GitHub/DAAlgo/"
    # path_out = "D:/DAAlgo/"

    harbours = inputHarbours(path)

    D = MinPath(source, dest, "10am", harbours)
    D.find_min_path(harbours, path_out)
    s, e, route = D.find_min_path(harbours, path_out)
    output_route(path_out, s, e, route, harbours)

# if __name__ == '__main__':
#     make_route_auto("A", "E")