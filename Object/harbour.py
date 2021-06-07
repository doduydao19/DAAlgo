from Object import container
class Harbour:
    def __init__(self, name, src, dst, dis, time, no_container, containers):
        self.name = name
        self.src = src
        self.dst = dst
        self.dis = dis
        self.time = time
        self.no_container = no_container
        self.containers = containers

    def stringHarbour(self):
        content = self.infoHarbour()
        conts = self.infoContainer()
        return content + conts

    def infoHarbour(self):
        return str(self.src) + "\t" + str(self.dst) + "\t" + str(self.dis) + "\t" + str(self.time) + "\t" + str(self.no_container) + "\n"

    def infoContainer(self):
        conts = ""
        for container in self.containers:
            conts += container.stringContainer() + "\n"
        return conts[:-1]

def inputHarbour(source, dest, dist, add):
    if add == True:
    # name_harbour = input("Nhap ten cang:")
    # src_harbour = input("Nhap diem xuat phat:")
    # dst_harbour = input("Nhap diem den:")
    # dis_harbour = input("Nhap khoang cach:")
    # time_harbour = input("Nhap thoi gian:")
        no_container = int(input("Nhập số lượng container:"))
        containers = []
        for cont in range(no_container):
            print("Nhap container thu:", cont+1)
            containers.append(container.inputContainer())
        return Harbour(source, source,dest, dist, int(dist)/60, no_container, containers)
    else:
        return Harbour(source, source, dest, dist, int(dist) / 60, 0, None)

def printHarbour(harbour):
    print(harbour.stringHarbour())

# def main():
#     h = inputHarbour()
#     printHarbour(h)
#
# if __name__ == '__main__':
#     main()
