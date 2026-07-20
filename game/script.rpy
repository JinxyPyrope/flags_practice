# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yuki", color ="#FFFFFF")
default yuki_affection = 0

# The game starts here.

label start:
    y "What's your favorite food?"
    
    menu:
        "Sushi":
            $ yuki_affection += 1
            y "Same!"
        "Pizza":
            y "hmmm"

    y "What's your favorite color?"

    menu:
        "Red":
            $ yuki_affection += 1
            y "Same!"
        "Blue":
            y "hmm"
    
    y "What's your favorite pet?"

    menu:
        "Cat":
            $ yuki_affection += 1
            y "Same!"
        "Dog":
            y "hmmm"


label ending_evaluation:
    if yuki_affection >= 2:
        jump yuki_best_ending
    elif yuki_affection == 1:
        jump yuki_good_ending
    else:
        jump yuki_bad_ending

label yuki_marriage_ending:
    y "I do. I love you."
    jump ending_credits


label yuki_best_ending:
    y 'I love you'
    jump ending_credits

label yuki_good_ending:
    y "I like you."
    jump ending_credits

label yuki_bad_ending:
    y "Go away."
    jump ending_credits

label ending_credits:
    "The End"