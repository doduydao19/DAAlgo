import sys
import math


# Bài toán xếp container
# Đầu vào là: Mảng các container, hành trình cập bến tàu
# Đầu ra là: Bảng vị trí các container.

# định nghĩa 1 container:
# 1 container : size(20,40), weight(Tấn), type(lạnh, nguy hiểm, thường, quá khổ), id_input, id_output
# 1 khoang (bay): 1 khoang là 1 ma trận 2 chiều : rows(hàng) và tiers(lớp) (giả sử cố định 20 khoang)
# 1 hàng: 1 mảng 1 chiều chứa các containter: kich thước mảng: 5(trái) vs 5(phải) từ tâm tàu sang 2 bên
# 1 lớp: chứa 1 hàng.
# khoang tàu gồm 2 phần: trong boong(đối đa 10 lớp) và trên boong(đủ hàng hoặc tổng trọng lượng hàng < N):


# định nghĩa contaier:
class Container:
    def __init__(self, id_input, id_output, size, weight, type):
        self.id_input = id_input
        self.id_output = id_output
        self.size = size
        self.weight = weight
        self.type = type
        self.stringCont = self.stringContainer()

    def setOutput_id(self, pos):
        self.id_output = pos
        print(self.id_output)

    def stringContainer(self):
        return str(self.id_input) + " " + str(self.id_output) + " " + str(self.size) + " " + str(
            self.weight) + " " + str(self.type)


# sắp xếp để có những container trong cùng 1 bay
def sort_bay(tiers):
    # tier gồm r_trái và r_phải
    # w_l   w_r     bias
    # [8]   [6]     2
    # [11]  [5]     6
    # [5]   [10]    5
    # 22    23      1

    # print("**trước khi xếp bay: ")
    # for tier in tiers:
    #     for row in tier:
    #         print(row)

    tier_left = []
    tier_right = []
    for id in range(len(tiers)):
        tier_left.append([calculas_total_weight(tiers[id][0]), 0])
        tier_right.append([calculas_total_weight(tiers[id][1]), 1])

    tier_left.append([0, 0])
    tier_right.append([0, 1])

    # print("Sắp xếp để độ lệch của các hàng trên cùng nhiều tier là nhỏ nhất")
    w_left = 0
    w_right = 0
    for i in range(len(tier_left)):
        w_left += tier_left[i][0]
        w_right += tier_right[i][0]
        # print(tier_left[i], tier_right[i])
    # print(w_left, w_right)
    # print("****sắp xếp bằng thuật toán tham lam:")

    bias_basic = abs(w_left - w_right)

    # tạo ma trận phương án
    bias_array = [bias_basic]
    for i in range(1, len(tier_left)):
        bias_array.append(0)

    # tính toán:
    index = 0
    bias_min = sys.maxsize
    if len(tier_left) > 1:
        while bias_array[0] != bias_min:
            if bias_array[0] > bias_min:
                bias_array[0] = bias_min
                swap_pair(tier_left, tier_right, index)

            for i in range(1, len(tier_left)):
                bias = abs(bias_array[0] - 2 * abs(tier_left[i][0] - tier_right[i][0]))
                bias_array[i] = bias
                if bias_min > bias:
                    bias_min = bias
                    index = i

    # print("Sau khi xếp:")
    left = []
    right = []
    for i in range(len(tier_left)):
        if tier_left[i][0] != 0 or tier_right[i][0] != 0:
            if tier_left[i][1] == 1:
                temp = tiers[i][0]
                tiers[i][0] = tiers[i][1]
                tiers[i][1] = temp
            # print(tier_left[i], tier_right[i])

    # print("**Sau khi xếp bay: ")
    # for tier in tiers:
    #     for row in tier:
    #         print(row)




# hàm tạo ra 1 tier:
# input: danh sách containers
# output: ma trận 2*5
def create_tier(containers):
    # print("trc")
    # for cont in containers:
    #     print(cont.stringCont)

    sort_weight([containers, []])
    # sort_size(containers)

    # print("sau")
    # for cont in containers:
    #     print(cont.stringCont)

    # cắt thành 2 dãy
    row_left, row_right = create_row(containers[0:len(containers):2], containers[1:len(containers):2])

    left = []
    for cont in row_left:
        if cont.weight != 0:
            left.append(cont)
        # print(cont.stringCont)
    right = []
    for cont in row_right:
        if cont.weight != 0:
            right.append(cont)
        # print(cont.stringCont)
    return [row_left, row_right]


# hàm tính tổng trọng lượng của cả hàng
def calculas_total_weight(row):
    sum = 0
    for cont in row:
        sum += cont.weight
    return sum


# hàm đổi vị trí của 2 container
def swap_pair(left, right, pair_swap):
    temp = left[pair_swap]
    left[pair_swap] = right[pair_swap]
    right[pair_swap] = temp


# row gồm row_left, row_right
def create_row_BruteForce(row_left, row_right):
    # sắp xếp sao cho tổng trọng lượng 2 bên
    # tỉnh tổng trọng lượng 2 bên:
    w_left = calculas_total_weight(row_left)
    w_right = calculas_total_weight(row_right)
    # thuật toán sắp xếp.
    # khởi tạo ma trận
    matrix_balance = [[0 for x in range(len(row_left))] for x in range(len(row_right))]

    bias_basic = w_left - w_right
    for i in range(len(row_left)):
        matrix_balance[0][i] = sys.maxsize
    for r in range(1, len(row_right)):
        matrix_balance[r][r - 1] = bias_basic
    # print(matrix_balance)

    # khởi tạo ma trận phương án:

    for r in range(1, len(row_right)):
        # tìm min sau 1 bước chuyển:
        for c in range(r, len(row_left)):
            matrix_balance[r][c] = abs(matrix_balance[r][c - 1] - 2 * (row_left[c].weight - row_right[c].weight))
            if matrix_balance[0][r] > abs(matrix_balance[r][c]):
                matrix_balance[0][r] = abs(matrix_balance[r][c])

    # tìm giá trị min và các vị trí cần đổi chỗ:
    index = 0
    for i in range(1, len(matrix_balance[0])):
        if matrix_balance[0][0] > matrix_balance[0][i]:
            matrix_balance[0][0] = matrix_balance[0][i]
            index = i

    for i in range(index, len(matrix_balance[index])):
        if abs(matrix_balance[index][i]) == matrix_balance[0][0]:
            swap_pair(row_left, row_right, i)
            break
        else:
            swap_pair(row_left, row_right, i)

    return row_left, row_right


def create_row_Greedy(row_left, row_right):
    # print("****sắp xếp bằng thuật toán tham lam:")
    w_left = calculas_total_weight(row_left)
    w_right = calculas_total_weight(row_right)
    bias_basic = w_left - w_right

    # tạo ma trận phương án
    bias_array = [bias_basic]
    for i in range(1, len(row_left)):
        bias_array.append(0)

    # tính toán:
    index = 0
    bias_min = sys.maxsize
    while bias_array[0] != bias_min:
        if bias_array[0] > bias_min:
            bias_array[0] = bias_min
            swap_pair(row_left, row_right, index)

        for i in range(1, len(row_left)):
            bias = abs(bias_array[0] - 2 * (row_left[i].weight - row_right[i].weight))
            bias_array[i] = bias
            if bias_min > bias:
                bias_min = bias
                index = i

    return row_left, row_right


# sắp xếp container theo hàng
# input: 2 hàng con
# output: 1 tier
def create_row(row_left, row_right):
    # print("trước")
    # print("left \t\t\t\t right")
    # for i in range(len(row_left)):
    #     print(row_left[i].stringCont + "\t" + row_right[i].stringCont)
    # print("weight: ", calculas_total_weight(row_left), "\t\t\t\t", calculas_total_weight(row_right))

    left, right = create_row_Greedy(row_left, row_right)
    # left, right = create_row_BruteForce(row_left, row_right)
    # print("Sau")
    # print("left \t\t\t right")
    # for i in range(len(row_left)):
    #     print(row_left[i].stringCont + "\t" + row_right[i].stringCont)
    # print(calculas_total_weight(row_left), "\t\t\t\t", calculas_total_weight(row_right))
    return left, right


# tạo mảng 2 chiều cho khoang: row và tier
def create_bay(containers):
    bay = []
    counter = 1
    tier = []
    no_conts = len(containers)
    # số cont nhỏ hơn 10 thì phải xây tạo tier riêng với. Hoặc với gộp với các lô hàng của cảng khác.
    # print("Tạo Bay: ")
    for container in containers:
        if counter <= 10:
            tier.append(container)
        else:
            # print("đủ khay")
            tier_sorted = create_tier(tier)
            bay.append(tier_sorted)
            tier = []
            counter = 0
        counter += 1
    if len(tier) != 0:
        # print("chưa đủ khay")
        while len(tier) != 10:
            tier.append(Container(0000, -1, 20, 0, None))
        tier_sorted = create_tier(tier)
        bay.append(tier_sorted)
    # for t in bay:
    #     print(t)
    sort_bay(bay)
    return bay

def generate_position(id, tier_id, row_id, cont_id):
    pos = ""
    if id < 10:
        id = "0" + str(id)
    else:
        id = str(id)
    pos += id

    if tier_id < 10:
        tier_id = "0" + str(tier_id)
    else:
        tier_id = str(tier_id)

    pos += tier_id

    if row_id == 1:
        row_id = "1" + str(cont_id)

    if row_id == 0:
        row_id = "0" + str(cont_id)

    pos += row_id

    return pos

# sinh ra vị trí của các bay cho phù hợp trên con tàu để tàu không lệch.
def create_position_all_bays(data):
    # đầu vào là data mảng n mảng con 1 mảng con gồm 3 phần tử:
    # Ptu 1: id của cảng
    # Ptu 2: số lượng các container
    # Ptu 3: tổng trọng lượng của các container
    # Ptu 4: mảng các container (ở dạng danh sách)

    bays = []
    for harbour in data:
        id_harbour = harbour[0]
        no_containers = harbour[1]
        weight_total = harbour[2]
        containers = harbour[3]
        print("cảng ", id_harbour)
        for cont in containers:
            print(cont.weight, end=" ")
        print()
        bay = create_bay(containers)
        bays.append(bay)

    # cấp phát vị trí cho từng container:
    # vị trí có dạng: 010502:
    # 01: vị trí của bay,
    # 05: vị trí thứ 5 trong hàng
    # 02: vị lớp thứ 2
    # print("danh sách contain đã xếp")
    for id in range(len(bays)):
        # print("bay: ", id)
        # tier_id = 1
        for tier_id in range(len(bays[id])):
            # print("tier: ", tier_id)
            # dãy trái:
            cont_left_id = 1
            for cont_id in range(len(bays[id][tier_id][0])):
                row_id = 1
                if bays[id][tier_id][0][cont_id].weight != 0:
                    pos = generate_position(id, tier_id, row_id, cont_left_id)

                    bays[id][tier_id][0][cont_id].id_output = pos
                    # print(bays[id][tier_id][0][cont_id].stringContainer())
                    cont_left_id += 2

            # dãy phải:
            cont_right_id = 0
            for cont_id in range(len(bays[id][tier_id][1])):
                row_id = 1
                if bays[id][tier_id][1][cont_id].weight != 0:
                    pos = generate_position(id, tier_id, row_id, cont_right_id)

                    bays[id][tier_id][1][cont_id].id_output = pos

                    # print(bays[id][tier_id][1][cont_id].stringContainer())
                    cont_right_id += 2
        # print("\n")
    return bays


def bubble_sort(containers):
    for i in range(len(containers)):
        for j in range(len(containers)):
            if containers[j].weight < containers[i].weight:
                temp = containers[i]
                containers[i] = containers[j]
                containers[j] = temp
    return containers


def sort_weight(containers):
    conts_40 = containers[0]
    conts_20 = containers[1]
    if len(conts_40) == 0 and len(conts_20) == 0:
        return
    if len(conts_40) == 0 and len(conts_20) > 0:
        bubble_sort(conts_20)
        return conts_20

    if len(conts_20) == 0 and len(conts_40) > 0:
        bubble_sort(conts_40)
        return conts_40
    else:
        bubble_sort(conts_40)
        bubble_sort(conts_20)
        for i in conts_20:
            conts_40.append(i)
        return conts_40


def sort_size(containers):
    size_20 = []
    size_40 = []

    for cont in containers:
        if cont.size == "20":
            size_20.append(cont)
        else:
            size_40.append(cont)
    return [size_40, size_20]


def classify_container(containers):
    # print("Phân loại:")
    # ở đây sẽ phân loại theo type of container.
    # 7 loại thường gặp:
    DC = []  # DC: dry container
    BC = []  # BC: Bulk container
    NCC = []  # NCC: Named Cargo Container
    TC = []  # TC: Thermal Containers
    OC = []  # OC: Open-top Container
    TP = []  # TP: Platform Container
    TAC = []  # TAC: Tank Container

    for container in containers:
        if container.type == "DC":
            DC.append(container)
        if container.type == "BC":
            BC.append(container)
        if container.type == "NCC":
            NCC.append(container)
        if container.type == "TC":
            TC.append(container)
        if container.type == "OC":
            OC.append(container)
        if container.type == "TP":
            TP.append(container)
        if container.type == "TAC":
            TAC.append(container)

    # sort size: (đầu ra là mảng [[cont_40],[cont_20]])
    DC = sort_size(DC)
    BC = sort_size(BC)
    NCC = sort_size(NCC)
    TC = sort_size(TC)
    OC = sort_size(OC)
    TP = sort_size(TP)
    TAC = sort_size(TAC)

    # print("xếp kích thước")
    # print("DC",DC[0], DC[1])
    # print("BC",BC[0], BC[1])
    # print("NCC",NCC[0], NCC[1])
    # print("TC",TC[0], TC[1])
    # print("OC",OC[0], OC[1])
    # print("TP",TP[0], TP[1])
    # print("TAC",TAC[0], TAC[1])

    # sort weight:
    # sắp xếp container DC
    DC = sort_weight(DC)
    # sắp xếp container BC
    BC = sort_weight(BC)
    # sắp xếp container NCC
    NCC = sort_weight(NCC)
    # sắp xếp container TC
    TC = sort_weight(TC)
    # sắp xếp container OC
    OC = sort_weight(OC)
    # sắp xếp container TP
    TP = sort_weight(TP)
    # sắp xếp container TAC
    TAC = sort_weight(TAC)

    # print("Sau khi xếp trọng lượng")
    # print_contain(DC)
    # print_contain(BC)
    # print_contain(NCC)
    # print_contain(TC)
    # print_contain(OC)
    # print_contain(TP)
    # print_contain(TAC)

    return [DC, BC, NCC, TC, OC, TP, TAC]


def make_priority(containers_in_harbour):
    # phân loại container
    # print("trc khi")
    # for cont in containers_in_harbour:
    #     print(cont.size, cont.weight, cont.type)
    containers_classified = classify_container(containers_in_harbour)
    containers_priority = []
    for containers_type in containers_classified:
        if containers_type != None:
            for container in containers_type:
                containers_priority.append(container)
    # print("sau khi")
    # for cont in containers_priority:
    #     print(cont.size, cont.weight, cont.type)
    return containers_priority


def input(f_data_harbour):
    data = []
    with open(f_data_harbour, "r", encoding="utf-8") as file:
        nameFolder = f_data_harbour[:-4]
        for line in file:
            info = line.strip('\n').split("\t")
            # tách lấy id cảng và số lượng container của cảng đó
            id_harbour = info[0]
            no_container = info[1]
            # lấy thông tin của các container của cảng
            f_harbour = nameFolder + "/" + str(id_harbour) + ".txt"
            containers_in_harbour = []
            total_weight = 0

            with open(f_harbour, "r", encoding="utf-8") as file_harbour:
                for row in file_harbour:
                    data_container = str(row).strip('\n').split("\t")
                    container = Container(data_container[0], data_container[1], int(data_container[2]),
                                          int(data_container[3]),
                                          data_container[4])
                    total_weight += int(data_container[3])
                    containers_in_harbour.append(container)

            # tạo ra sự ưu tiên giữa các container
            # print("cảng: ", id_harbour)
            containers_priority = make_priority(containers_in_harbour)
            data.append([id_harbour, no_container, total_weight, containers_priority])
        file.close()

    return data


def output(bays):

    text = ""
    for tiers in bays:
        for tier in tiers:
            for row in tier:
                for cont in row:
                    if cont.id_output != -1:
                        # print(type(cont.stringContainer()))
                        content = cont.stringContainer()
                        text += content+"\n"
    print(text)

    f_out = open("out.txt", "wt")
    f_out.write(str(text))

    f_out.close()
    print("done")

def main():
    # danh sách các container và hành trình
    f_data_harbour = "data.txt"
    data = input(f_data_harbour)
    bays = create_position_all_bays(data)

    output(bays)
    return


if __name__ == '__main__':
    main()
