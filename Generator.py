def runFunc(num,total):
    current=0
    doubleNumber=1
    output_list=[]

    outfile = open('result.txt','w')

    while(current<total):
        if doubleNumber >= num:
            doubleNumber=1

        for i in range(1,num):
            current+=1
            if(current > total):
                break
            if(i==doubleNumber):
                output_list.append(i)
                current += 1
            output_list.append(i)
        doubleNumber+=1
    #print(output_list)
    
    #converting list of integers to string
    str_output = [str(int) for int in output_list]
    str_output = ",".join(str_output)

    #print(str_output)

    outfile.write(str_output)
    outfile.close()


runFunc(4,10)
