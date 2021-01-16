
A=[]
i=0



to_do = input(str("mode program? new/edit"))
if to_do == "new":
    k = int(input('Amount of tasks? '))
    for i in range(k):
        print ('page',(i+1))
        k = input('')
        A.append(k)

    output = ("\n".join(A))
    print ("\n".join(A))
    ending = input(str("save? y/n"))
    if ending == "y":
        filename = input(str("Filename"))
        file = open(filename +".txt","a")
        file.write(output)
        file.close()
        print("saved")


else:
    print("edit mode")
    to_edit=input(str("File name?"))
    file = open(to_edit + ".txt", "r")
    print(file)

