





def int_to_binary(num):
    binary_num = list()
    while num > 0:
        binary_num.append('1' if num % 2 == 1 else '0')
        num = num >> 1
    return "".join(binary_num[::-1])



if __name__ == "__main__":

    x = int(input("first number to add: "))
    y = int(input("second number to add: "))

    print("output is: ", x+y)

    x_binary = int_to_binary(x)
    y_binary = int_to_binary(y)

    
    