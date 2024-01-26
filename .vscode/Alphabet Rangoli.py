def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    size_alpha = alphabet[:size]
    max_length = ((size*2)-1)+((size*2)-2)
    temp = ''
    temp1 = ''
    temp2 = ''
    x = []
    for i in reversed(range(0,size)):
        temp = temp1 + size_alpha[i] + temp2
        print(temp.center(max_length,"-"))
        x.append(temp.center(max_length,"-"))
        temp1 = temp1 + size_alpha[i].ljust(2,"-")
        temp2 = size_alpha[i].rjust(2,"-") + temp2
    for  j in reversed(range(0,size-1)):
        print(x[j])