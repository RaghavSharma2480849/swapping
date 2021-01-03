def swapping():
    file1 = input('enter the first file name ')
    file2 = input('enter the second file name ')
    data1 = open(file1, 'r')
    data2 = open(file2, 'r')
    with open(file1, 'w') as a:
        a.write(data1)
    with open(file2, 'w') as b:
        b.write(data2)

swapping()