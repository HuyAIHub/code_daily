def adjacentElementProduct(inputArray):
    # cho 1 mảng hãy tìm 2 số liền kề lớn nhất
    finnalArray = [] # create a emptyArray
    for i in range(len(inputArray)-1):
        finnalArray.append(inputArray[i]*inputArray[i+1])
    result = max(finnalArray)
    return print("gia tri lon nhat la:",result)
inputArray =  [3,3]
adjacentElementProduct(inputArray)


