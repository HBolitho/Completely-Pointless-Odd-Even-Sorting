stop = False
flag = False

while(stop == False):
    type_Num = int(input("Input a number"))
  
    if type_Num > 0:
        flag = False
    else:
        flag == True

    if flag == False:
        if type_Num%2 ==0:
            print("Number is Even")
        else:
            print("Number is Odd")
    else:
        print("Number is invalid")
    
    quitting = input("Do you want to quite the application (Y/N)")
    if quitting == 'Y':
        stop = True
        break




    
    
    
    
    
