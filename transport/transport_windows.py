import pandas as pd
from pathlib import Path
import os
import platform


class Dijkstra:
    def __init__(self, start, end, time, harbours):
        self.start = start.upper()
        self.end = end.upper()
        self.time = time
        self.harbours = harbours

        self.train_map = self.make_train_map(harbours)

        self.route = self.dijk()

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

    def lowest_cost(self, costs, processed):
        lowest = float('inf')
        station_name = None
        for station in costs.keys():
            cost = costs[station]
            if cost < lowest and station not in processed:
                station_name = station
                lowest = cost
        return station_name

    def dijk(self):
        parents = {x: self.start for x in self.train_map[self.start].keys()}
        costs = self.train_map[self.start]
        # print("costs = ", costs)
        processed = []
        for station in self.train_map.keys():
            if station not in costs.keys():
                costs[station] = float('inf')
        # print("costs = ", costs)
        current_stop = self.lowest_cost(costs, processed)
        while current_stop is not None:
            cost = costs[current_stop]
            # print(self.train_map[current_stop])
            neighbours = self.train_map[current_stop]
            for n in neighbours.keys():
                new_cost = cost + neighbours[n]
                if new_cost < costs[n]:
                    costs[n] = new_cost
                    parents[n] = current_stop
            processed.append(current_stop)
            current_stop = self.lowest_cost(costs, processed)
        print('Time to get from {0} to {1} is: {2} KM.'.format(self.start, self.end, costs[self.end]))
        last = self.end
        route = [self.end]
        while last != self.start:
            last = parents[last]
            route += [last]
        # print('Stops along the way: {0}'.format(route))

        return route


def makeDijkstra(harbours):
    l_h = set([h[0] for h in harbours])
    l_h = sorted(list(l_h))

    start = "A"
    end = "E"

    # sort harbour theo cot thoi gian tra hang
    for s_h in l_h:
        for e_h in l_h:
            D = Dijkstra(s_h, e_h, '10am', harbours)

            print(D.route[::-1])

    D = Dijkstra('A', 'E', '10am', harbours)

    # print(D.route)
    return start, end, reversed(D.route)


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
    outDijk = open(path_out + 'outDijk.txt', 'w', encoding="utf-8")

    har = get_info_har(harbours, s)

    f = open(path_out + 'route.txt', 'w', encoding="utf-8")
    for i in route:
        har = get_info_har(harbours, i)
        print(i)
        f.write(har[0] + "\t" + har[4])
        f.write("\n")
    f.close()


if __name__ == '__main__':
    path = "D:/GitHub/DAAlgo/data.txt"
    harbours = inputHarbours(path)

    s, e, route = makeDijkstra(harbours)

    # path_out = "D:/GitHub/DAAlgo/"
    #
    # output_route(path_out, s, e, route, harbours)
