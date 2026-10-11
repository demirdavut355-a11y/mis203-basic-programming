import random
import webbrowser

print("ASSISTANT FOR YOUR MOOD ")
name = input("What is your name? ")
print(f"\nHello {name}! ")

print("\nHow do you feel today?")
print("1 - Very energetic / My mood is high")
print("2 - Tired / I need to relax")
print("3 - Very stressed / My head is full")

select = input("\nSelect (1/2/3): ")

energitic_songs = [
     "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
     "https://www.youtube.com/watch?v=l482T0yNkeo"
]

relax_songs = [
    "https://www.youtube.com/watch?v=RP0_8J7uxhs",
    "https://www.youtube.com/watch?v=S-Xm7s9eGxU"
]

stress_songs = [
    "https://www.youtube.com/watch?v=LhhLcbr9Jqg",
    "https://www.youtube.com/watch?v=DnGdoEa1tPg"
]

if select == "1":
    selected_songs = random.choice(energitic_songs)
    print("\nExcellent. Let's get your energy up with some music!")
elif select == "2":
    selected_songs = random.choice(relax_songs)
    print("\nGreat. Let's help you relax with some soothing tunes.")
elif select == "3":
    selected_songs = random.choice(stress_songs)
    print("\nI understand. Let's ease your stress with some great Türkish folk music.")
else:
    print("\nInvalid selection, but I'm still opening a nice song for you!")
    selected_songs = "https://yandex.com.tr/video/preview/15892366563661223737"  

webbrowser.open(selected_songs)  
