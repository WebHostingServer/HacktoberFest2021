while(True):
    i=int(input("Enter your age or Birth Year(YYYY): "))

    if(len(str(i))==4):
        if(1920<=i<=2021):
            print("Your age in 2090 will be ",(2090-i))

        elif(i>2022):
            print("You are not born yet !")

        else:
            print("You seem to be the oldest person alive")

    else:
        if(0<=i<=120):
            print("Your age in 2090 will be ",(2090-(2021-i)))
        elif(i<0):
            print("You are not born yet")
        else:
            print("You seem to be oldest person alive.")

    # print("Do you want to continue? 1 or 0")
    # ch=input()
    # if ch==1:
    #     continue
    # else:
    #     break

pr