# Display the menu
# Ask the user to enter their choice [1 or 2]
# Using a switch-case statement
# If choice is 1 call function get_cm(). 
# If choice is 2 call function get_meter(). 
# Else print “Invalid choice” 
# In get_cm(): 
# Get the value of centimetre from the user. 
# Call function cm_to_meter(…) and pass centimeter to calculate meter. 
# Display the centimeter and meter.

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Enter centimeter: "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeters equals to {:.2f} meters".format(cm,m))

get_cm()

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

def get_meter():
    m = float(input("Enter meter: "))
    cm = meter_to_cm(m)
    print("{:.2f} meters equals to {:.2f} centimeters".format(m,cm))

get_meter()

print("======================================")
print("                MENU                  ")
print("======================================")
print("1.    Convert centimeter to meter     ")
print("2.    Convert meter to centimeter     ")
print("======================================")

choice = int(input("Enter your choice: "))

if(choice == 1):
    get_cm()

elif(choice == 2):
    get_meter()
    
else:
    print("Invalid choice.")