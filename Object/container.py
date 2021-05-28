class Container:
    def __init__(self, id_input, id_output, size, weight, type):
        self.id_input = id_input
        self.id_output = id_output
        self.size = size
        self.weight = weight
        self.type = type

    def setOutput_id(self, pos):
        self.id_output = pos
        print(self.id_output)

    def stringContainer(self):
        return str(self.id_input) + " " + str(self.id_output) + " " + str(self.size) + " " + str(
            self.weight) + " " + str(self.type)


def inputContainer():
    id_container_input = input("Nhap Container ID:")
    id_container_output = -1
    size_container = input("Nhap Kich Thuoc Container:")
    weight_container = input("Nhap Trong Luong Container:")
    type_container = input("Nhap Loai Container:")
    return Container(id_container_input, id_container_output, size_container, weight_container, type_container)

def printContainer(container):
    print(container.stringContainer())

# def main():
#     c = inputContainer()
#     printContainer(c)
#
# if __name__ == '__main__':
#     main()