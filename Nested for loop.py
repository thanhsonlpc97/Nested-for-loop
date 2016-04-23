print("    %3d%3d%3d%3d%3d%3d%3d%3d%3d " % (1, 2, 3, 4, 5, 6, 7, 8, 9))
print("-------------------------------")
for i in range(1, 10):
    print("%d  |" %(i), end='' )
    for j in range(1, 10):
        print("%3d" %(i*j), end='')
    print('')
