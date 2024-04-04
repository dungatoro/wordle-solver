"""
0 Gray   
1 Yellow 
2 Green  
"""

import collections

def score(answer: str, guess: str) -> list:
    pool = collections.Counter(s for s, g in zip(answer, guess) if s != g)
    score = []
    for answer_char, guess_char in zip(answer, guess):
        if answer_char == guess_char:
            score.append(2)
        elif guess_char in answer and pool[guess_char] > 0:
            score.append(1)
            pool[guess_char] -= 1
        else:
            score.append(0)

    return score

def read_file_lines(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

# build lookup table
answers = read_file_lines('answers.txt')
guesses = read_file_lines('guesses.txt')

table = {}
for left, answer in enumerate(answers):
    print(1038-left)
    row = {}
    for guess in guesses:
        row[guess] = score(answer, guess)
    table[answer] = row

import pickle

with open('table.pickle','wb') as f:
    pickle.dump(table, f)








