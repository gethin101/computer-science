import time
from dataclasses import dataclass

customer_LoggedIn = False
admin_LoggedIn = False
login_attempt = 0


admin_login = {
    "username": "admin",
    "password": "password"
}

user_login = {
    "username": "gethin",
    "password": "login"
}

@dataclass
class Film:
    movie: str
    price: float
    category: str
    tickets: int

spiderman = Film("Spiderman", 10.99, "Action", 120)
starwars = Film("Star Wars", 8.50, "Science Fiction", 95)
jurassic_park = Film("Jurassic Park", 7.25, "Adventure", 70)

films = [spiderman, starwars, jurassic_park]


def rejection():
    print("\nEdit movie confirmation rejected")
    time.sleep(1)
    quit()


def display_movies():
    print("\n     CURRENT MOVIES")
    print("--------------------------------------------------")
    for film in films:
        print(f"- {film.movie}")
        print(f"    Category : {film.category}")
        print(f"    Price    : £{film.price:.2f}")
        print(f"    Tickets  : {film.tickets}")
        print("--------------------------------------------------")


# ================== Login ==================

def login():
    global admin_LoggedIn, customer_LoggedIn, login_attempt

    login_name = input("Enter username ").lower()

    #admin login
    if login_name == admin_login["username"]:
        print("------------------------------------------------------------------")
        confirm_admin = input("Are you sure you want to access ADMIN PANEL? (y/n) ").lower()
        print("------------------------------------------------------------------")

        if confirm_admin == "y":
            password = input("Enter password ").lower()

            if password == admin_login["password"]:
                admin_LoggedIn = True
                print("\nLogged in as admin")

            else:
                while login_attempt < 3:
                    login_attempt += 1
                    print("\n------------------------------------------------")
                    print(f"Incorrect password. Attempt: {login_attempt}")
                    print("------------------------------------------------")
                    time.sleep(2)

                    if login_attempt < 3:
                        password = input("\nEnter password ").lower()

                    if password == admin_login["password"]:
                        print("\nLogged in as admin")
                        admin_LoggedIn = True
                        break

                if login_attempt == 3:
                    print("\nToo many login attempts")
                    time.sleep(1)
                    quit()

        elif confirm_admin == "n":
            print("Admin login rejected")
            time.sleep(1)
            quit()

    #customer login
    elif login_name == user_login["username"]:
        confirm_login = input(f"\nAre you sure you want to log in as {login_name}? (y/n) ").lower()

        if confirm_login == "y":
            password = input("Enter password: ")

            if password == user_login["password"]:
                customer_LoggedIn = True
                print(f"\nCustomer logged in as {login_name}")

            else:
                while login_attempt < 3:
                    login_attempt += 1
                    print("\n------------------------------------------------")
                    print(f"Incorrect password. Attempt: {login_attempt}")
                    print("------------------------------------------------")
                    time.sleep(2)

                    if login_attempt < 3:
                        password = input("\nEnter password ").lower()

                    if password == user_login["password"]:
                        print(f"\nLogged in as {login_name}")
                        customer_LoggedIn = True
                        break

                if login_attempt == 3:
                    print("\nToo many login attempts")
                    quit()

        elif confirm_login == "n":
            print("\nCustomer login rejected")
            time.sleep(1)
            quit()

    else:
        print("\nIncorrect username..")
        time.sleep(1)
        quit()

login()


#customer logged in
if customer_LoggedIn:
    print("----------------------------------------------------------------------------------")
    print("Welcome to Gethin-Plex, which movie would you like to see?")
    display_movies()

    book_film = input().lower()
    selected_film = None

    for film in films:
        if film.movie.lower() == book_film:
            selected_film = film
            break

    if selected_film is None:
        print("\nSorry, you can't book this movie right now")

    else:
        print(f"\nHow many tickets would you like to book for {selected_film.movie}?")

        try:
            amount = int(input("Number of tickets: "))
        except ValueError:
            print("\nError: This isn't a number of tickets")
            quit()

        if amount <= 0:
            print("\nYou have to buy at least 1 ticket")

        elif amount > selected_film.tickets:
            print(f"\nSorry, there are only {selected_film.tickets} tickets left")

        else:
            selected_film.tickets -= amount
            print("------------------------------------------------------------")
            print(f"You just booked {amount} tickets for {selected_film.movie}!")
            print("------------------------------------------------------------")
            print(f"Tickets left: {selected_film.tickets}")


#admin logged in
elif admin_LoggedIn:
    display_movies()

    confirm_edit = input("Would you like to edit a movie? (y/n) ").lower()

    if confirm_edit == "n":
        rejection()

    elif confirm_edit == "y":
        edit_movie = input("Which movie would you like to edit? ").lower()
        selected_movie = "none"

        for film in films:
            if film.movie.lower() == edit_movie:
                selected_movie = film
                break

        if selected_movie == "none":
            rejection()

        section_edit = input(f"Which data would you like to edit for {selected_movie.movie}?   Price | Tickets | Category  ").lower()

        if section_edit == "price":
            print("\n-----------------------------------------------------")
            selected_movie.price = float(input(f"Current price: £{selected_movie.price:.2f} | Enter new price: £"))
            print("-----------------------------------------------------")
            print(f"{selected_movie.movie} price updated to £{selected_movie.price:.2f}!")
            print()
            time.sleep(1)
            display_movies()

    else:
        print('\nYou need to type "Y" or "N"')
        quit()
