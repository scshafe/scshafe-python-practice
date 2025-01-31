


class BinaryNum:

    def __init__(self, num):
        num = int(num)
        self.num = num
        self.binary_num = list()
        
        tmp = num
        while tmp > 0:
            self.binary_num.append(True if tmp % 2 == 1 else False)
            tmp = tmp >> 1
        self.binary_num = self.binary_num[::-1]
        

    def __str__(self):
        return "".join(['1' if x else '0' for x in self.binary_num])





def int_to_binary(num):
    binary_num = list()
    while num > 0:
        binary_num.append(True if num % 2 == 1 else False)
        num = num >> 1
    binary_num[::-1]



if __name__ == "__main__":

    x = BinaryNum(input("first number to add: "))
    y = BinaryNum(input("second number to add: "))

    print(x)
    print(y)

    # x_binary = int_to_binary(x)
    # y_binary = int_to_binary(y)

    
    