    #imports
import os
    # global varriables
A=[]
i=0


    # starting logic for the script
to_do = input(str("mode program? new/edit "))
if to_do == "new":

    #input of tasks and specify amount

    k = int(input('Amount of tasks? '))
    for i in range(k):
        print ('task',(i+1))
        k = input('')
        A.append(k)

    #output conversion of the list to string
    output = ("\n".join(A))
    print ("\n".join(A))

    # creating a file name and saving it
    ending = input(str("save? y/n "))
    if ending == "y":
        filename = input(str("Filename? "))
        file = open(filename +".txt","a")
        file.write(output)
        file.close()
        print("saved")

    # edit mode looking up a file in a working directory for outside gonna need a path and import os

else:
    print("edit mode")
    to_edit=input(str("File name?"))
    file = open(to_edit +'.txt' , "r")
    print(file.read())
    rewrite = input(str("Rewrite/delete? rw/d"))
    if rewrite == "rw":
         k = int(input('Amount of tasks? '))  
         for i in range(k):
            print ('task',(i+1))
            k = input('')
            A.append(k)

            output = ("\n".join(A))
            print ("\n".join(A))

    # creating a file name and saving it
         ending = input(str("save? y/n "))
         if ending == "y":
            filename = input(str("Filename? "))
            file = open(filename +".txt","w")
            file.write(output)
            file.close()
            print("saved")

    else:
        delete = str(input('Delete y/n? '))
        if delete == "y":
            #filename = input(str("Filename? "))
            file.close()
            os.remove(to_edit + '.txt')
            print("removed")
