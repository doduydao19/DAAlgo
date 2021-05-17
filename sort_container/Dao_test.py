# Bài toán xếp container
# Đầu vào là: Mảng các container, hành trình cập bến tàu
# Đầu ra là: Bảng vị trí các container.

# định nghĩa 1 container:
# 1 container : size(20,40), weight(Tấn), type(lạnh, nguy hiểm, thường, quá khổ), id_input, id_output
# 1 khoang (bay): 1 khoang là 1 ma trận 2 chiều : rows(hàng) và tiers(lớp) (giả sử cố định 20 khoang)
# 1 hàng: 1 mảng 1 chiều chứa các containter: kich thước mảng: 5(trái) vs 5(phải) từ tâm tàu sang 2 bên
# 1 lớp: chứa 1 hàng.
# khoang tàu gồm 2 phần: trong boong(đối đa 10 lớp) và trên boong(đủ hàng hoặc tổng trọng lượng hàng < N):


#định nghĩa contaier:
class Container:
    def __init__(self, id_input):
        self.id_input

        # ...

# tạo mảng 2 chiều cho khoang: row và tier
def create_bay():
    return []

# 1 tier gồm row_trái và row_phải
# w_r_trái = w_r_phải
def create_tier():
    return []

#tạo mảng 1 chiều
def create_row():
    return []

# sắp xếp để có những container phù hợp ở trong boong (10 lớp)
def sort_in_boong():
    return []

# sắp xếp để có những container  phù hợp trên trong boong
def sort_on_boong():
    return []

# kiểm tra xem tổng trọng lượng hàng hóa đã đủ hay chưa?
def isFull():
    return False

# sinh ra vị trí của các bay cho phù hợp trên con tàu để tàu không lệch.
def create_position_all_bays(data):
    # đầu vào là data mảng n mảng con 1 mảng con gồm 3 phần tử:
    # Ptu 1: id của cảng
    # Ptu 2: số lượng các container
    # Ptu 3: tổng trọng lượng của các container
    # Ptu 4: mảng các container (ở dạng danh sách)
    
    for harbour in data:
        id_harbour = harbour[0]
        no_containers = harbour[1]
        weight_total = harbour[2]
        container = harbour[3]
        create_bay(container)
    
    return []


def input(f_data_harbour):
    data = []
    with open(f_data_harbour, "r", encoding = "utf-8") as file:
        nameFolder = f_data_harbour[:-4]
        for line in file:
            info = line.strip('\n').split('\t')
            # tách lấy id cảng và số lượng container của cảng đó
            id_harbour = info[0]
            no_container = info[1]
            # lấy thông tin của các container của cảng
            f_harbour = nameFolder + "/" + str(id_harbour)+".txt"
            containers_in_harbour = []
            total_weight = 0
            with open(f_harbour, "r", encoding="utf-8") as file_harbour:
                for row in file_harbour:
                    data_container = row.strip('\n').split('\t')
                    container = Container(data_container[0], data_container[1], data_container[2], data_container[3], data_container[4])
                    total_weight += data_container[3]
                    containers_in_harbour.append(container)
            data.append([id_harbour, no_container, total_weight, containers_in_harbour])
    return data

def output():
    return

def main():
    # danh sách các container và hành trình
    f_data_harbour = "data_harbour.txt"
    data = input(f_data_harbour)
    p = create_position_all_bays(data)
    output(p)
    return

if __name__ == '__main__':
    main()
