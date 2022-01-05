def swapFiledata():
    file1=input("Enter the first file :")
    file2=input("Enter the second file :")
    data_a=open(file1 , "r")
    data1=data_a.read()
    data_b=open(file2 , "r")
    data2=data_b.read()
    with open(file1,"w") as a:
        a.write(data2)
    with open(file2,"w") as b:
        b.write(data1)
swapFiledata()        