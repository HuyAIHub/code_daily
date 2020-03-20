def giaithua(n):
    s = 1
    while n > 1 :
        s = s*n
        n= n-1
    return print(s)
n = int(input("số bạn muốn nhập : "))
giaithua(n)