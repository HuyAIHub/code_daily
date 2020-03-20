def shapearea(n):
    area = 1
    while n >1 :
        area = area + (n-1)*4
        n=n-1
    return print(area)
n = 3
shapearea(n)
