


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
    
    def __len__(self):
        return len(self.binary_num)
    
    def add_pad(self, pad):
        self.binary_num = pad + self.binary_num


def pad_nums(bnum1, bnum2):
    assert(type(bnum1) == BinaryNum and type(bnum2) == BinaryNum)
    if len(bnum1) > len(bnum2):
        bnum2.add_pad([0 for i in range(len(bnum1)-len(bnum2))])
    if len(bnum1) < len(bnum2):
        bnum1.add_pad([0 for i in range(len(bnum2)-len(bnum1))])
    return bnum1, bnum2
        


def carry_look_ahead_add(bnum1, bnum2):
    bnum1, bnum2 = pad_nums(bnum1, bnum2)
    print(bnum1)
    print(bnum2)





if __name__ == "__main__":

    x = BinaryNum(input("first number to add: "))
    y = BinaryNum(input("second number to add: "))

    carry_look_ahead_add(x, y)

    # x_binary = int_to_binary(x)
    # y_binary = int_to_binary(y)

    
    