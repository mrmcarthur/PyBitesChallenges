dictionary = 'dictionary.txt'

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                              for letter in letters.split()
                              
### THESE PRECOMMENTS WERE NOTES AND PRACTICE

# ~ word = 'SCRABBLE'


# ~ print (scrabble_scores[0])
# ~ print(scrabble_scores[1])
# ~ print(scrabble_scores[0][0])

# ~ score = 0

# ~ for character in word:
    # ~ print(character)
    # ~ for letter, value in LETTER_SCORES.items():
        # ~ if character == letter:
            # ~ score += value

# ~ print(score)

### BEGINNING OF MAIN PROGRAM

dictionary_list = []
f = open(dictionary)
for line in f:
    dictionary_list.append(line.rstrip())

# Populate empty list to be filled and score initialized to 0
point_value = {}
score = 0

# Prints the length of the list of words
print(len(dictionary_list))

# Main loop to extract the information from list and place into dictionary
for word in dictionary_list:
    for character in word:
        for letter, value in LETTER_SCORES.items():
            if character.upper() == letter:
                score += value
            point_value[word] = score
    score = 0

# Creates a list from dictionary and sorts it with largest value first
results = sorted(point_value.items(), key=lambda x: x[1], reverse=True)

# Prints word that produces the most points on standard scrabble board
print(results[0][0] + " is the word that is worth the most.")

