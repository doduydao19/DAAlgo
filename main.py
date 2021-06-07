from Object import harbour as hObj
from transport import transport_windows
from sort_container import Dao_test
import os

def find_har(har, data, dest, id, max):
    if id >= max:
        return
    else:
        for d in data:
            for h in d:
                if h[0] == har:
                    if h in dest:
                        continue
                    else:
                        dest.append(h)
                        id += 1
                        # print(h)
                        find_har(h[1], data, dest, id, max)

                # if h[1] == har:
                #     dest.add(h)
                #     id += 1
                #     find_har(h[0], data, dest, id, max)

def find_distance(source, dest, data):
    for d in data:
        for h in d:
            if h[0] == source and h[1] == dest:
                return int(h[2])

def input_Harbours():
    file_name = "quanhegiuacaccang.txt"
    with open(file_name, "r", encoding="utf-8") as f:
        data = []
        harbour = []
        all_harbour = set()
        no_rel = 0
        for line in f:
            line = line.strip("\n")
            # print(line)
            if line != "":
                har = line.split("\t")
                harbour.append(har)
                all_harbour.add(har[0])
                all_harbour.add(har[1])
            else:
                no_rel += len(harbour)
                data.append(harbour)
                harbour = []
    for d in data:
        print(d)
    print("Danh sánh các cảng biển hiện tại:")
    print(sorted(all_harbour))
    har_name = input("Nhập tên cảng muốn xuất phát: ")
    # # print(har_name)
    # dest = list()
    # find_har(har_name, data, dest, 0, no_rel)
    # dest_name = set()
    # for d in dest:
    #     dest_name.add(d[0])
    #     dest_name.add(d[1])
    # dest_name.remove(har_name)
    # print("Các cảng có thể đi tới là:")
    # print(sorted(dest_name))

    if har_name != None:
        print("Nhập tên các cảng muốn tới (\"None\" để dừng):")
        destinations = []
        id = 0
        while id < len(all_harbour):
            h = input("Tên cảng: ")
            if h != "None":
                destinations.append(h)
                id+=1
            else:
                if len(destinations) != 0:
                    break
                else:
                    print("Chưa có cảng nào được nhập vào. Vui lòng nhập lại")
        pass
        print(destinations)
        harbours = []
        for h in range(len(destinations)):
            print("Nhập cảng thứ", h + 1)
            dist = find_distance(har_name, destinations[h], data)
            harbours.append(hObj.inputHarbour(har_name, destinations[h], dist, True))
            for d in range(h+1,len(destinations)):
                dist = find_distance(destinations[h], destinations[d], data)
                harbours.append(hObj.inputHarbour(destinations[h], destinations[d], dist, False))
        return harbours
    else:
        return None

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
    # output_containers(hs)

if __name__ == '__main__':
    main()