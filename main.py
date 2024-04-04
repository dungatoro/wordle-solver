import pickle

def read_file_lines(file_path):
    # reads a file into a list of words
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def num_answers_left(table, guess, score):
    """
    Finds how many possible answers there would be left if 'guess' was played
    and 'score' was the result.
    """
    num = 0
    for ans, row in table.items():
        if score == table[ans][guess]:
            num += 1
    return num

def rate_guess(table, guess):
    """
    A guess is given a rating based on how much it reduces the number of 
    possible answers. A lower rating is better, as that means that the guess, on
    average, results in the largest reduction in possible answers.
    """
    total = 0
    for answer in table:
        score = table[answer][guess]
        total += num_answers_left(table, guess, score)
    return total

def best_word(table, guesses):
    """
    The rating for each guess is calculated and the guess with the lowest 
    rating is chosen as the best guess (it reduces the number of possible 
    answers the most on average).
    """
    best, best_rating = guesses[0], rate_guess(table, guesses[0])
    for guess in guesses:
        rating = rate_guess(table, guess)
        if rating < best_rating:
            best, best_rating = guess, rating
    return best

if __name__ == "__main__":
    guesses = read_file_lines('guesses.txt')

    # load the score lookup table
    with open('table.pickle', 'rb') as f:
        table = pickle.load(f)

    guess = 'roate' # pre-calculated best guess
    while len(table) > 1:
        print(f"You should guess '{guess}'")

        # convert '01200' to [0,1,2,0,0]
        score = [int(c) for c in list(input("Enter score: "))]

        # get rid of impossible answers
        table = {ans: row for ans, row in table.items() if score == row[guess]}

        # choose the new guess
        guess = best_word(table, guesses)

    print(f"The answer is '{list(table)[0]}'.")
