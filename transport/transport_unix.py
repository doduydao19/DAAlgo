import pandas as pd
from pathlib import Path
import os



class Dijkstra:
   

    def __init__(self, start, end, time="10am"):

        self.start = start.upper()
        self.end = end.upper()
        self.time = time
        self.train_map = {}
        self.load_data()
        self.dijk()

    def load_data(self):
        file_str = Path('.').absolute()
        file_str = str(file_str.joinpath('routeData.xlsx'))
        train_df = pd.read_excel(file_str)
        train_df.columns = ['start', 'destination', 'distance', 'time']
        for station in set(train_df['start']):
            connected_stations_df = train_df[train_df['start'] == station]
            connected_stations = {connected_stations_df.iloc[x, 1]: connected_stations_df.iloc[x, 3]
                                  for x in range(0, connected_stations_df.shape[0])}
            self.train_map[station] = connected_stations

    def lowest_cost(self, costs, processed):
        lowest = float("inf")
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
        processed = []
        for station in self.train_map.keys():
            if station not in costs.keys():
                costs[station] = float('inf')
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
        print('Time to get from {0} to {1} is: {2} minutes.'.format(
            self.start, self.end, costs[self.end]))
        last = self.end
        route = [self.end]
        while last != self.start:
            last = parents[last]
            route += [last]
        # print('Stops along the way: {0}'.format(route))
        outDijk = open('outDijk.txt', 'w')
        outDijk.write('Time to get from {0} to {1} is: {2} minutes.'.format(
            self.start, self.end, costs[self.end]))
        outDijk.write('\n')
        for i in reversed(route):
            # print(i)
            outDijk.write(i)
            if i != route[0]:
                outDijk.write("->")
        # outDijk.write(str(cost))
        outDijk.close()
        f = open('data.txt', 'w')
        for i in reversed(route):
            print(i)
            f.write(i)
            if i!= route[0]:
                f.write("\n")
        f.close()
        # print(costs)

#in ra so cac container trong cac cang
list_dir = os.listdir('port')

temp = os.getcwd()

for file in list_dir:

    if file == "A.txt":
        f = open(temp + "/" + "port" + "/" + file, 'r')
        countA = 0

        for line in f:
            if line != "\n":
                countA +=1
        f.close()



    if file == "B.txt":
        f = open(temp + "/" + "port" + "/" + file, 'r')
        countB = 0

        for line in f:
            if line != "\n":
                countB +=1
        f.close()



    if file == "C.txt":
        f = open(temp + "/" + "port" + "/" + file, 'r')
        countC = 0

        for line in f:
            if line != "\n":
                countC +=1
        f.close()



    if file == "D.txt":
        f = open(temp + "/" + "port" + "/" + file, 'r')
        countD = 0

        for line in f:
            if line != "\n":
                countD +=1
        f.close()



    if file == "E.txt":
        f = open(temp + "/" + "port" + "/" + file, 'r')
        countE = 0

        for line in f:
            if line != "\n":
                countE +=1
        f.close()



    if file == "F.txt":
        f = open(temp + "/" + "port" + "/" + file, 'r')
        countF = 0

        for line in f:
            if line != "\n":
                countF +=1
        f.close()



if __name__ == '__main__':

    # start = "HARROW & WEALDSTONE"
    # end = "WATERLOO"
    # time = "10am"
    Dijkstra('A', 'F', '3')
    # a = Dijkstra('A', 'E', '10am')
    # print(a.train_map)
    # print(tem)
    # result = temp.time_check()

    with open('data.txt', "r+") as f:
        content = f.read()
        output = ("output.txt","x")

        with open("output.txt", "w") as o:



            for line in content:
                if "A" in line:
                    line = "A" + "  " + str(countA)
                    o.write(line)
                    if line != line[0]:
                        o.write("\n")
                if "B" in line:
                    line = "B" + "  " + str(countB)
                    o.write(line)
                    if line!= line[0]:
                        o.write("\n")
                if "C" in line:
                    line = "C" + "  " + str(countC)
                    o.write(line)
                    if line != line[0]:
                        o.write("\n")
                if "D" in line:
                    line = "D" + "  " + str(countD)
                    o.write(line)
                    if line!= line[0]:
                        o.write("\n")
                if "E" in line:
                    line = "E" + "  " + str(countE)
                    o.write(line)
                    if line!= line[0]:
                        f.write("\n")
                if "F" in line:
                    line = "F" + "  " + str(countF)
                    o.write(line)
                    if line != line[0]:
                        o.write("\n")
                        
    



