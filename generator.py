import os
import sys
import itertools
from random import shuffle

import genanki
from pick import pick

from rich.traceback import install
install()

from questions import *

title = "Please choose (space) question types desired and confirm (enter):"

# Parse CSV file and return a list of lists
def parse_csv(text, sep=","):
    lines = list(map(lambda t: t.strip(), text.split("\n")))
    lines = list(filter(lambda l: l != "" and l[0] != "#", lines))
    ret = list(map(lambda l: l.split(sep), lines))
    return ret


def get_label(option): return option[0]
selected = pick(questions, title, multiselect=True, min_selection_count=1, options_map_func=get_label)

# Ask for shuffle
shuffle_deck = 1 == pick(['No', 'Yes'], 'Would you like the deck to be shuffled?')[1]


print("Generating deck...\n")

deck = genanki.Deck(1863022921, "Kyōiku Kanji Full Deck")
deck_model = genanki.Model(
  8142243119,
  'Simple Model',
  fields=[
    {'name': 'id'},
    {'name': 'kanji'},
    {'name': 'strokes'},
    {'name': 'translation'},
    {'name': 'onread'},
    {'name': 'kunread'},
  ],
  templates=[]
)

for selection in selected:
    func = selection[0][1] # Generator function
    deck_model.templates.append(selection[0][1])

deck.add_model(deck_model)

# Input files
grade_min = 1
grade_max = 6

spinner = itertools.cycle(['-', '/', '|', '\\'])
for grade in range(grade_min, grade_max + 1):
    with open("data/grade" + str(grade) + ".csv", encoding="utf8") as c_file:
        print("Processing grade " + str(grade), end=" ")

        # Process grade file
        for line in parse_csv(c_file.read()):
            print(next(spinner), end="")
            sys.stdout.flush()

            # Note format is id, kanji, strokes, translation, on, kun
            deck.add_note(
                genanki.Note(
                    model=deck_model,
                    fields=[str(field) for field in line],
                )
            )

            print("\b", end="")
    print("[DONE]")

if shuffle_deck:
    print("Shuffling deck...")
    shuffle(deck.notes)

# Output file
if os.path.exists('output.apkg'):
    if not os.path.isfile('output.apkg'):
        print("\nError 'output.apkg' exists and is not a file!")
        exit(1)
    
    input("\nWarning 'output.apkg' exists!\nPress Enter to continue, Ctrl+C to cancel.")

genanki.Package(deck).write_to_file('output.apkg')