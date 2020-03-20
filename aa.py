statues = [1,2,3,1,2,1]

mum = zip(statues[:-1], statues[1:])
diff_statues = [y-x for x, y in zip(statues[:-1], statues[1:])]
    print(x,y)
print(statues[:-1])
print(statues[1:])
print(list(mum))