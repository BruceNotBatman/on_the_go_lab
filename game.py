from scene import Scene
import reader

def gm(scene1):
    read_page(scene1.speaker[1], scene1.dialogue[0])
    response = int(input("Press 1 to Greet and 2 to Diss"))
    if response == 1:
        read_page(scene1.speaker[0], scene1.dialogue[1])
    if response == 2:
        read_page(scene1.speaker[0], scene1.dialogue[3])
    read_page(scene1.speaker[2], scene1.dialogue[4])

speaker=["Boy1", "Boy2", "Narrator"]
dialogue=["Hi there!",
        "Greetings fellow Human!",
        "I think we can be friends",
        "Fuck off!",
        "The End"]

scene1 = Scene(speaker, dialogue)

gm(scene1)
