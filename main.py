print("Welcome to the Chick-Fil-A job application")

hours = input("How many hours are you looking for? (10-20, 20-30, 30-40) ")

if hours == "10-20":
    work = input("Okay, so 10-20 hours. Do you have any previous work experience? (Yes/No) " )
    
if hours == "20-30":
    work = input("Alright, so 20-30 hours. Do you have any previous work experience? (Yes/No) " )
    
if hours == "30-40":
    work = input("Alright, so 30-40 hours. Do you have any previous work experience? (Yes/No) " )
    
permit = input("Do you have a Food Handlers Permit? (Yes/No) ")

if work == "Yes" and permit == "Yes":
    print("We here at Chick-Fil-A would love to hire you!")
    
elif work == "Yes" and permit == "No":
    print("When would you be able to meet in person for a interview?")
    
elif work == "No" and permit == "Yes":
    print("When would you be able to meet in person for a interview?")
    
elif work == "No" and permit == "No":
    print("Sorry but you don't have what we need at the moment.")
