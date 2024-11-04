def greet_english():
    print("Hello!")
def greet_spanish():
    print("Hola!")
    
def greet_french():
    print("Bonjour!")
    
def greet_german():
    print("Hallo!")
    
def greet_italian():
    print("Ciao!")

def language_choose(choice):
    switch = {
        1: greet_english,
        2: greet_spanish,
        3: greet_french,
        4: greet_german,
        5: greet_italian
    }
    
    print("1. English")
    print("2. Spanish")
    print("3. French")
    print("4. German")
    print("5. Italian")
    
    if choice in switch:
        switch[choice]()
    else:
        print("Invalid Choice")

choice = int(input("Enter a number between 1 and 5: "))
language_choose(choice)
    