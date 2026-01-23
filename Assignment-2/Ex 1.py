def check_zander():    
    try:
        length = int(input("Enter the zander's length(cm): "))
        if length < 42 :
            missinglength = 42 - length
            print("The length is not long enough, the fish is being release back")
            print("The zander need more", missinglength, "cm to meet the size to catch the fish")
        else:
            print("The fish has been successfully caught")
    except:
        print("Invalid length given")
check_zander()  