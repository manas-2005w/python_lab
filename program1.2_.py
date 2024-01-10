def calculator():
    checker="Y"
    while(checker=="Y" or checker=="y"):
        firstinput= float(input("Enter first number: "))
        secondinput= float(input("Enter second number: "))
        print()
        operation=int(input("Chose among operations(1=+)(2=-)(3=*)(4=/)(5=%)(6=//)(7=**): "))
        if(operation==1):
            print(firstinput+secondinput)
        elif(operation==2):
            if(firstinput>secondinput):
                print(firstinput-secondinput)
            else:
                print(secondinput-firstinput)
        elif(operation==3):
            print(firstinput*secondinput)
        elif(operation==4):
            if(firstinput>secondinput):
                print(firstinput/secondinput)
            else:
                print(secondinput/firstinput)
        elif(operation==5):
            if(firstinput>secondinput):
                print(firstinput%secondinput)
            else:
                print(secondinput%firstinput)
          #print(firstinput%secondinput)
        elif(operation==6):
            if(firstinput>secondinput):
                print(firstinput//secondinput)
            else:
                print(secondinput//firstinput)
          #print(firstinput//secondinput)
        elif(operation==7):
             print(firstinput**secondinput)
        else:
            if firstinput>secondinput:
                print(firstinput,"is greater than",secondinput)
            elif firstinput==secondinput:
                print(firstinput,"is equal to",secondinput)
            else:
                print(secondinput,"is greater than",firstinput)
        checker=str(input("Do you want to conitnue:(y/n) "))

calculator()