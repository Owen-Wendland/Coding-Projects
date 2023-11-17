from math import log


def ConvertToBinary (number):
    Num = number
    binAge = []
    for i in range(int(log(number,2)+1)):
        if (Num%2 ==1):
            binAge.insert(0,1)
            Num = Num - 1
         
        else:
            binAge.insert(0,0)
        Num = Num/2
    return(binAge)
while(True):
    print("enter num to be converted to bin")
    a = input()
    if(a == 'q'):
        break
    print(ConvertToBinary(int(a)))
