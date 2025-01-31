


class BinaryNum:
    def __init__(self, num: int):
        self.num = num
        self.binary_num = list()
        
        tmp = num
        while tmp > 0:
            self.binary_num.append(True if tmp % 2 == 1 else False)
            tmp = tmp >> 1
        self.binary_num = self.binary_num[::-1]
        
    def __str__(self):
        return "".join(['1' if x else '0' for x in self.binary_num])
    
    def print_decimal(self):
        tmp = self.binary_num[::-1]
        count = 0
        for i in range(len(tmp)):
            count += tmp[i] * 2**i
        print(count)
    
    def __len__(self):
        return len(self.binary_num)

    def __iter__(self):
        return iter(self.binary_num)
    
    # def __next__(self):
    #     return 
    
    def add_pad(self, pad: list):
        print(self.binary_num)
        self.binary_num = pad + self.binary_num

def pad_nums(bnum1, bnum2):
    assert(type(bnum1) == BinaryNum and type(bnum2) == BinaryNum)
    if len(bnum1) > len(bnum2):
        bnum2.add_pad([0 for i in range(len(bnum1)-len(bnum2))])
    if len(bnum1) < len(bnum2):
        bnum1.add_pad([0 for i in range(len(bnum2)-len(bnum1))])
    return bnum1, bnum2
        

def num_from_binary_num(binary_num):
    num = 0
    index = 0

    for x in binary_num[::-1]:
        num += 2**index if x else 0
        index+=1
    return num



# Pi     = Ai xor Bi
# Gi     = Ai and Bi
# C(i+1) = Gi or (Pi and Ci)
# Si     = Pi xor Ci
def carry_look_ahead_add(bnum1, bnum2):
    bnum1.add_pad([False])
    bnum2.add_pad([False])
    bnum1, bnum2 = pad_nums(bnum1, bnum2)
    

    def xor(bit1, bit2):
        return True if (bit1 and not bit2) or (not bit1 and bit2) else False
    
    counter = 0
    propagate = [True if xor(x[0], x[1]) else False for x in zip(bnum1, bnum2)]
    generate  = [True if x[0] and x[1] else False for x in zip(bnum1, bnum2)]
    
    # carry_plus is indexed '+1' offset
    carry_plus = []
    carry_plus.append(True if generate[0] else False)
    for i in range(1, len(bnum1)):
        carry_plus.append(True if generate[i] or (propagate[i] and carry_plus[i-1]) else False)
    
    sum = ['1' if xor(x[0], x[1]) else '0' for x in zip(propagate, carry_plus)]

    output = num_from_binary_num(sum)
    print(output)


    



if __name__ == "__main__":
    x = BinaryNum(int(input("first number to add: ")))
    y = BinaryNum(int(input("second number to add: ")))

    carry_look_ahead_add(x, y)


    
    