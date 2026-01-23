def check_hemoglobin():
    biological = input("Enter your gender (male/female): ").lower()
    if biological not in ["male", "female"]:
        print("Make sure you enter your gender correctly (male or female).")
        return

    try:
        hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
        if biological == "male":
            if hemoglobin_value < 134:
                print("Your hemoglobin value is low.")
            elif 134 <= hemoglobin_value <= 167:
                print("Your hemoglobin value is normal.")
            else:
                print("Your hemoglobin value is high.")
        
        elif biological == "female":
            if hemoglobin_value < 117:
                print("Your hemoglobin value is low.")
            elif 117 <= hemoglobin_value <= 155:
                print("Your hemoglobin value is normal.")
            else:
                print("Your hemoglobin value is high.")

    except ValueError:
        print("Invalid hemoglobin value. Please enter a number.")

check_hemoglobin()