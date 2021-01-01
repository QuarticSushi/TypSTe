import random
import time

characters_per_word = 5.8 # the average number of letters per english word is about 4.8, but 5.8 accounts for typing spaces

def calculate_wpm(string, time):
    character_count = len(string)
    cps = character_count / time
    cpm = cps * 60
    wpm = cpm / characters_per_word
    print(wpm)
    f = open("wpm.txt", "a")
    f.write(str(wpm) + "\n")
    f.close()


input("ready to start?")

play = True

while play:
    
    sentence = random.choice(list(open('sentences.txt')))
    print(sentence)

    start_time = time.time()

    input()

    end_time = time.time()
    total_time = end_time - start_time

    calculate_wpm(sentence, total_time)

    if input("continue (y/n)") == "n":
        play = False
