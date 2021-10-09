d={}
while(1):
    print("----------Birthday App----------")
    print("1. Show Birthday")
    print("2. Add to Birthday list")
    print("3. exit")
    inp=int(input("Enter choice "))
    if(inp==3):
        print("Thank you!")
        break
    elif(inp==1):
        if(len(d.keys())==0):
            print("Nothing to show!")
            continue
        name=input("enter name- ")
        print(d.get(name,"Not Found!"))
    elif(inp==2):
        name=input("enter name- ")
        d[name]=input("enter birtday- ")
        print("Birthday Added")
    else:
        print("Wrong input!")
