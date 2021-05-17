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
def create_position_all_bays():
    return []


def input():
    return

def output():
    return

def main():
    # danh sách các container và hành trình
    data = input()
    p = create_position_all_bays(data)
    output(p)
    return

if __name__ == '__main__':
    main()
