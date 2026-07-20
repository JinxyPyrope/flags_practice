# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yuki", color ="#FFFFFF")


# The game starts here.

label start:
    y "What's your favorite food?"
    
    menu:
        "Sushi":
            y "Same!"
        "Pizza":
            y "hmmm"

    y "What's your favorite color?"

    menu:
        "Red":
            y "Same!"
        "Blue":
            y "hmm"
    
    y "What's your favorite pet?"

    menu:
        "Cat":
            y "Same!"
        "Dog":
            y "hmmm"
