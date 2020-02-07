# hotelreservation.py
# The hotel reservation system maintains
# a list of room and guests allocated to
# each room
# G Williams


## Constants
ROOMS = {} # Create an empty map
GUESTS = [] # Create an empty list


## The main function
def main():
    selfPopulate()
    print "Welcome to Hotel LMU"
    print
    print "Please select a menu option."
    menu()
    

# Menu function
def menu():
    print
    print
    print "1. Add a reservation"
    print "2. Remove a reservation"
    print "3. Look up a reservation"
    print "4. Display guests"
    print "5. Display available rooms"
    print "6. Exit"
    userInput = input()

    if userInput == 1:
        addReservation()
    elif userInput == 2:
        removeReservation()
    elif userInput == 3:
        lookUpReservation()
    elif userInput == 4:
        displayGuests()
        menu()
    elif userInput == 5:
        availableRooms()
        menu()
    elif userInput == 6:
        quit
    else:
        print "Please choose a valid option"
        menu()

        
# Create rooms
def createRooms():
    for i in range(101, 112):
        ROOMS[i] = ''

# Add guests
def addGuests():
    GUESTS.append("Jonathon")
    GUESTS.append("Samantha")
    GUESTS.append("Margaret")
    GUESTS.append("Dominic")
    GUESTS.append("Owen")
    GUESTS.append("Melissa")

    for guest in GUESTS:
        addToRoom(guest, 'n')

# Populates rooms and guests
def selfPopulate():
    createRooms()
    addGuests()

# Adds a guest to a room, takes an optional arguement to print out the allocated room
def addToRoom(guest, pout = 'y'):
    
    #loop until we find the first available room
    for rm in ROOMS:
        if ROOMS[rm] == '':
            # assigns guest to room
            ROOMS[rm] = guest
            
            # defaulted(y) will print the room number the guest was allocated to
            if pout == 'y':
                print "Guest:", guest, "has been allocated room number", rm

            # breaks the loop
            break



# Adds a reservation
def addReservation():
    # checks the number of available empty rooms
    cnt = 0
    for i in ROOMS:
        if ROOMS[i] == '':
            cnt += 1

    if cnt == 0:
        print "There are no free rooms available"
    else:
        name = raw_input("Please enter the name of the guest... ")
        print
        addToRoom(name)
        GUESTS.append(name)
        
    menu()

    
# Remove guest from room
def removeReservation():
    # Confirm if we want to remove a guest reservation
    response = raw_input("Are you sure you want to remove a guest reservation? (y/n) ")


    # If we do, ask for the room number and check its a valid room number
    # before removing the reservation
    if response == "y":
        room = input("Please enter the room number you would like to vacate... ")

        # check valid room number
        if room >= 101 and room <= 112:

            # remove guest from guest list and reset room
            GUESTS.remove(ROOMS[room])
            
            ROOMS[room] = ''
            print "Reservation removed"
            menu()
        else:
            # room number was invalid. Ask to try again or go back to menu
            try_again = raw_input("Invalid room number... Would you like to try again? (y/n)")
            if try_again == 'y':
                removeReservation()
            else:
                menu()
    else:
        menu()

# Look up a reservation by name.
def lookUpReservation():
    # Counter
    cnt = 0;
    name = raw_input("Please enter the name of the guest... ")
    print

    if name!='': # We at least have a string
        # loop through rooms to check if this user is in a room
        for rm in ROOMS:
            if ROOMS[rm] == name:
                print "Guest: ", name, "is in room",rm
                cnt += 1
        if cnt == 0:
            print "There are no guests matching that name"
    else:
        print "Invalid input"
    menu()
        
# displays the number of guests staying in the hotel and their allocated room
def displayGuests():
    # Output how many guests are currently staying
    print "There are currently", len(GUESTS),"guests staying with us"
    print

    # Loop through the rooms and print those that contain a name
    for room in ROOMS:
        if ROOMS[room]!='':
            print room,"-->", ROOMS[room]

# Displays the number of available (empty) rooms
def availableRooms():
    #set cnt (count var) to 0
    cnt = 0
    
    #loop for empty rooms
    for i in ROOMS:
        if ROOMS[i] == '':
            cnt += 1

    #print the count of rooms available
    print "There are", cnt, "available rooms left"

main()
