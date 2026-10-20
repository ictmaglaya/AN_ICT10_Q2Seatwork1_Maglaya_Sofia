from pyscript import document, display

my_list= ["Thomas Edison", "Minho Lee", "Newt Isaac", "Ben Frank"]

def check_runner():
    first = document.getElementById("first_user_input").value.strip()
    last = document.getElementById("last_user_input").value.strip()
    name = first + last
    message= document.getElementById("message")
    
    if name in my_list:
        message.innerHTML("Runner made it!")

    else:
        message.innerHTML("Doors closed.")
