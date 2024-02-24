
def binary(number, memory):
    bin_number = bin(number)[2:]
    NewString = ""
    NewString2 = ""
    memoryToBin = str('0' * memory)
    length1 = len(memoryToBin)
    length2 = len(bin_number)
    length = length1 - length2
    counter = 0
    counter2 = 0
    Checker = False

    while(counter < length):
        NewString += '0'
        counter += 1

    NewString += bin_number

    for digit in NewString:
        if digit == '0':
            NewString2 += '1'
        else:
            NewString2 += '0'

    NewStringLength = len(NewString2)
    A_bin = int(NewString2)
    B_bin = A_bin

    while(counter2 < NewStringLength and Checker == False):
        if(B_bin % 10 == 0):
            Checker = True
        else:
            B_bin = int(B_bin / 10)
            A_bin = A_bin - 10**counter2
            counter2 += 1
    ten = 10 ** counter2
    A_bin += ten
    return A_bin

print(binary(42, 8))