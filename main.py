from Object import harbour
from transport import transport_windows
from sort_container import Dao_test
import os

def input_Harbours():
    no_harbour = int(input("Nhap so luong cang:"))
    harbours = []
    for h in range(no_harbour):
        print("Nhap cang thu", h+1)
        harbours.append(harbour.inputHarbour())
    return harbours

def output_harbours(harbours):
    fileName = "data.txt"
    with open(fileName, "w", encoding="utf-8") as f:
        for h in harbours:
            print(h.infoHarbour())
            f.write(h.infoHarbour())

def output_containers(harbours):
    folderName = "data"
    os.mkdir(folderName)
    for h in harbours:
        fileName = folderName + "/" + h.name
        with open(fileName, "w", encoding="utf-8") as f:
            f.write(h.infoContainer())

def main():
    hs = input_Harbours()
    output_harbours(hs)
    output_containers(hs)

if __name__ == '__main__':
    main()