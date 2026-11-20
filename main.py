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