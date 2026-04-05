import numpy

PASSWORD = "admin"
admin = False
rows = 5
columns = 8
seating = numpy.full((rows,columns),"x")
#-------------------- PRINT SEATING PLAN -------------------------
def seating_plan(columns):
    lists = ["A","B","C","D","E","F","G","H","I","J","K"]
    nums = []
   

    for i in range(columns):
        nums.append(i+1)
       
    print(*nums)
   
    def print_seat():
        i=0
        for row in seating:
           
            for element in row:
                print(element, end=" ")
            print(lists[i])
            i+= 1        
    print_seat()
    while True:
        seat = input("What seat would you like: ")
        print(ord(seat[0])-65)
        if seating[ord(seat[0])-65][int(seat[1])-1] == "-":
            print("This seat is already taken!")
            continue
        seating[ord(seat[0])-65][int(seat[1])-1] = "-"
        print_seat()                      
        choose_another = input("Do you want to choose another seat?(y/n) ")
        if choose_another == "y":
            continue
        else:
            break
#------------------------------------------------------------------------          
       

def main_system(mode,admin):
    film_lineup = ["Nemo", "Star Wars", "Minecraft Movie"]
    items_prices= {"popcorn": 2.80,
                   "slushy": 1.50,
                   "haribos": 2.00}
    #-------- Choose which mode to enter -------------
    if mode == "1":
        for i in range(3):
            enter_password = input("Enter the admin password: ")
            if enter_password != PASSWORD:
                print("Incorrect Password")
            else:
                print("Access Granted")
                admin = True
                break

    elif mode == "2":
        print("You have entered Customer Mode")
        seating_plan(columns)
    print(admin)
    #--------------- Admin Mode ----------------------    
    while admin == True:
        check_items = input("Do you want to change the film lineup(1) or update prices(2)? ")
        #----------- Updating Films -----------------------
        if check_items == "1":
            print("The current film lineup is:" , ", ".join(film_lineup))
            add_or_remove = input("Would you like to add(1) or remove(2) a film? ")
            if add_or_remove == "1":
                add_film = input("Which film would you like to add? ")
                film_lineup.append(add_film)
            if add_or_remove == "2":
                remove_film = input("Which film would you like to remove? ")
                for i in range(len(film_lineup)-1):
                    if film_lineup[i].lower() == remove_film.lower():
                        film_lineup.remove(film_lineup[i])
            print("The current film lineup is now:", ", ".join(film_lineup))
        #-------------- Updating Prices --------------------
        elif check_items == "2":
            print("The current items being sold are:")
            for i in range(len(items_prices)):
                print(items_prices.values())
while True:
    mode = input("Would you like to enter admin mode(1) or customer mode(2)? ")    
    main_system(mode,admin)
