
A=[]

def ListToString(s):
    s = ""
    return (s.join(A))

to_do = input(str("mode program? new/edit"))
if to_do == "new":
    k = int(input('Amount of tasks? '))
    for i in range(k):
        print ('page',(i+1))
        k = input('')
        A.append(k)
        print(A) 

        ending = input(str("save? y/n"))
        if ending == "y":
            file = open("To-do.txt","a")
            ListToString(s)
            file.write(s)
            file.close()
            print("saved")


else:
    print("cya")

