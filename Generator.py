def runFunc(num,total):
    current=0
    doubleNumber=1
    arr=[]

    outfile = open('data.txt','w')

    while(current<total):
        if doubleNumber >= num:
            doubleNumber=1

        for i in range(1,num):
            current+=1
            if(current > total):
                break
            if(i==doubleNumber):
                arr.append(i)
                current += 1
            arr.append(i)
        doubleNumber+=1
    print(arr)

    string_ints = [str(int) for int in arr]

    str_of_ints = ",".join(string_ints)

    print(str_of_ints)

    outfile.write(str_of_ints)
    outfile.close()


runFunc(4,10)