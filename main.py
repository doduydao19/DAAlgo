from Object import harbour as hObj
from transport import transport_windows
from sort_container import sortContainer
import os

def find_distance(source, dest, data):
    for d in data:
        for h in d:
            if h[0] == source and h[1] == dest:
                return int(h[2])

def input_Harbours():
    file_name = "harbours_relation.txt"
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
        f.close()
    for d in data:
        print(d)
    print("Danh sánh các cảng biển hiện tại:")
    print(sorted(all_harbour))

    har_name = input("Nhập tên cảng muốn xuất phát: ")

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
            for d in range(0, len(destinations)):
                if destinations[d] != destinations[h]:
                    dist = find_distance(destinations[d], destinations[h], data)
                    harbours.append(hObj.inputHarbour(destinations[d], destinations[h], dist, False))

        for d in range(0, len(destinations)):
            dist = find_distance(destinations[d], har_name, data)
            harbours.append(hObj.inputHarbour(destinations[d], har_name, dist, False))
        return harbours
    else:
        return None

def output_harbours(harbours):
    fileName = "data1.txt"
    with open(fileName, "wt", encoding="utf-8") as f:
        for h in harbours:
            print(h.infoHarbour())
            text = h.infoHarbour()
            f.write(text)

def output_containers(harbours):
    folderName = "data"
    if os.path.isdir(folderName) == False:
        os.mkdir(folderName)
    for h in harbours:
        if h.no_container != 0:
            fileName = folderName + "/" + h.dst
            with open(fileName, "w", encoding="utf-8") as f:
                f.write(h.infoContainer())

def input_auto():
    transport_windows.make_route_auto("A", "E")

def output_auto():
    sortContainer.sort_container()

def main():
    print("Ấn 1 để nhập thủ công, ấn 2 để nhập từ file.")
    choose = int(input("Lựa chọn là: "))

    if choose == 1:
        hs = input_Harbours()
        output_harbours(hs)
        output_containers(hs)

    if choose == 2:
        input_auto()
        output_auto()

if __name__ == '__main__':
    main()
