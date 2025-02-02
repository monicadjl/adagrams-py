import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

POINTS_DICT = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10 }

def draw_letters():
    used_letters = {}
    letters_hand = []
    possible_letters = []

    #creates possible_letters list
    for key, value in LETTER_POOL.items():
        for i in range(value):
            possible_letters.append(key)

    #pull 10 letters
    while len(letters_hand) <= 9:
        random_int = random.randint(0,len(possible_letters)- 1)
        chosen_letter = possible_letters[random_int]
        letters_hand.append(chosen_letter)
        possible_letters.remove(chosen_letter)
    return letters_hand


def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    letter_bank_copy = letter_bank.copy()

    for character in upper_word:
        if character not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(character)
    return True


def score_word(word):
    upper_word = word.upper()
    total_points = 0
    

    for character in upper_word:
        total_points += POINTS_DICT[character]

    if len(upper_word) >= 7:
        total_points += 8 
    else:
        total_points += 0
    return total_points



def get_highest_word_score(word_list):
    highest_score = 0  
    score_dict = {}
    winning_word = ""
    tie_breaker = {}
    
    #calculates word & score & adds to score_dict
    for word in word_list:
        scorez = score_word(word)
        score_dict[word] = scorez
    
    # assigns highest_score & winning_word
    for word, scorez in score_dict.items():
        if scorez > highest_score:
            highest_score = scorez
            winning_word = word
        
        elif scorez == highest_score:
            if len(winning_word) == 10:
                pass
            elif len(word) == 10:
                winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word
            elif len(word) == len(winning_word):
                pass
    return (winning_word, highest_score)
        
    
    


        
    
    #indexing into a tuple

    # if 2 scorez are the same:
        # len of shortest word wins
    # elif len(word) == 10
        # that word wins 
    # elif if len(word) == len(word) and score ==score:
        # pick the first occuring