from pyscript import display, document


club_members = ['Zoey Ledres', 'Therese Reyes','Cheree Mendoza','Princess Schwab', 'Elise Ramos'] #list of members allowed

def names(e): 
    first_name = document.getElementById("fname").value #grabs the input for first name
    last_name = document.getElementById("lname").value #grabs the input for last name

    full_name = first_name + " " + last_name #combines both first and last name

    is_member = full_name in club_members #checks if the combined first and last name is part of the list/ club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the club.",
        False: f"Sorry {full_name}, get out of here."
    } #if member is part of the list, it shows true. if member is not part, it shows false.

    document.getElementById("output").innerHTML = messages[is_member] 

#non metal elements
#Dictionary w info about non metals 
# planet name: Symbol, name, number, mass

nonmetals = {"Xenon": ("Xe", 54, 131.29),
           "Hydrogen": ("H", 1, 1.00784),
           "Carbon": ("C", 6, 12.011),
           "Nitrogen": ("N", 7, 14.007),
           "Phosphorus": ("P", 15, 30.974),
           "Oxygen": ("O", 8, 15.999),
           "Sulfur": ("S", 16, 32.06),
           "Selenium": ("Se", 34, 78.971),
           "Fluorine": ("F", 9, 18.998),
           "Chlorine": ("Cl", 17, 35.4527),
           "Bromine": ("Br", 35, 79.904),
           "Iodine": ("I", 53, 126.904),
           "Helium": ("He", 2, 4.0026),
           "Neon": ("Ne", 10, 20.18),
           "Argon": ("Ar", 18, 39.948),
           "Krypton": ("Kr", 36, 83.798),
           "Radon": ("Rn", 86, 222)
           }


# Create a function to search a planet
def search_nonmetal(e):
    #get the input from HTML
    nonmetal1 = document.getElementById("nonmetal1").value
    #retrieve information from the dictionary
    result = nonmetals.get(nonmetal1, ("Nonmetal not found", "-", "-"))
    # for fallback ^
    # display of result 
    document.getElementById("name").innerText = nonmetal1
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]

#display

Grade_7 = {'Zoey Ledres', 'Therese Reyes'}
Grade_8 = {'Elise Ramos', 'Cheree Mendoza'}
Grade_9 = {'Princess Schwab','Jericho Magsalin'}
Grade_10 ={'Tyler Sales', 'Savanna Bautista'}
master_set = (Grade_7 | Grade_8 | Grade_9 | Grade_10 | )


def new(e): 
    first_name = document.getElementById("fname").value #grabs the input for first name
    last_name = document.getElementById("lname").value #grabs the input for last name

    full_name = first_name + " " + last_name #combines both first and last name

    messages = f"{full_name} is now added to the club. "

    document.getElementById("output")
    display(f"{messages} + {master_set}")