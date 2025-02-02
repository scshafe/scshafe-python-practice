

class BinaryNum:
    def __init__(self, num: int):
        self.num = num
        self.binary_num = list()
        
        tmp = num
        while tmp > 0:
            self.binary_num.append(True if tmp % 2 == 1 else False)
            tmp = tmp >> 1
        # self.binary_num = self.binary_num
        
    def __str__(self):
        return "".join(['1' if x else '0' for x in self.binary_num])
    
    def print_decimal(self):
        tmp = self.binary_num
        count = 0
        for i in range(len(tmp)):
            count += tmp[i] * 2**i
        print(count)
    
    def __len__(self):
        return len(self.binary_num)

    def __iter__(self):
        return iter(self.binary_num)
    
    def add_pad(self, pad: list):
        self.binary_num = self.binary_num + pad

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

    for x in binary_num:
        num += 2**index if x else 0
        index+=1
    return num


def print_bool_arr_as_binary(message, array):
    print(message, "".join(['1' if x else '0' for x in array]))

# Pi     = Ai xor Bi
# Gi     = Ai and Bi
# C(i+1) = Gi or (Pi and Ci)
# Si     = Pi xor Ci
def carry_look_ahead_add(bnum1, bnum2):
    bnum1.add_pad([False])
    bnum2.add_pad([False])
    bnum1, bnum2 = pad_nums(bnum1, bnum2)
    

    def xor(bit1, bit2):
        return bit1 != bit2
    
    counter = 0
    propagate = [xor(x[0], x[1]) for x in zip(bnum1, bnum2)]
    counter += 4 * len(bnum1)
    generate  = [True if x[0] and x[1] else False for x in zip(bnum1, bnum2)]
    counter += len(bnum1)

    # print_bool_arr_as_binary("propagate: ", propagate)
    # print_bool_arr_as_binary("generate:  ", generate)
    
    carry = []
    carry.append(False)
    for i in range(1, len(bnum1)+1):
        carry.append(True if generate[i-1] or (propagate[i-1] and carry[i-1]) else False)

        # this must be calculated for each carry bit without using recursion because they must all be
        # accessible at the same time. If they use the previous carry bit in the calculation
        # that is essentially the same as the ripple-adder circuit.
        counter += 2**i

    # print_bool_arr_as_binary("carry:     ", carry)

    sum = [True if xor(a,b) else False for a,b in zip(propagate, carry)]
    counter += 4 * len(propagate)

    output = num_from_binary_num(sum)

    print("\ngates used: ", counter)
    print(output)


    



if __name__ == "__main__":
    x = BinaryNum(int(input("first number to add: ")))
    y = BinaryNum(int(input("second number to add: ")))

    carry_look_ahead_add(x, y)


    
    