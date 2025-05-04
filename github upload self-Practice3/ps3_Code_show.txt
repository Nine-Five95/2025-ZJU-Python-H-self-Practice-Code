import math         ## 导入数学函数
import random
import string

VOWELS = 'aeiou'    # constant
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7       # 标记一个字典hand的长度

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "D:\python\write\pythonProject\spring2025python(H)\Practice3\words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    1.1进行了一些修改使之只能收藏从a到z的字母以及通配符号 过滤非法符号
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        if "a" <= x <= "z" or x == "*":
               freq[x] = freq.get(x,0) + 1
        else:
            continue
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_1 = word.lower()
    point_1 = 0
    point_2 = 0
    for keys,values in get_frequency_dict(word_1).items():
        point_1 += SCRABBLE_LETTER_VALUES.get(keys,0)*values
    point_2 = max(7*len(word_1) - 3*(n - len(word_1)),1)
    return point_1 * point_2
   
# 注意测试文件之前需要保存

# Make sure you understand how this function works and what it does!

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand["*"] = 1
    for i in range(1,num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {}
    word_2 = get_frequency_dict(word.lower())
    for keys,values in hand.items():
        new_hand[keys] = max(hand[keys] - word_2.get(keys,0),0)
    return new_hand
    



# Problem #3: Test word validity

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_1 =word.lower()
    word_3 = get_frequency_dict(word_1)
    Flag = True
    k = word_1.find("*")
    if k < 0:
        if word.lower() not in word_list:
            return False
        else:
            for keys,values in word_3.items():
                if hand.get(keys,0) < values:
                    return False
            return True
    else:
        for i in VOWELS:
            word_2 = word_1[:k] + i + word_1 [k+1:] 
            for keys,values in get_frequency_dict(word_3).items():
                    if hand.get(keys,0) < values:
                        Flag = False
            if word_2 in word_list and Flag:
                return True
            Flag = True
        return False
                
        





def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    k = 0
    for i in hand.values():
        k += i
    return k

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0
    while sum(hand.values()) > 0:
        print("Current Hand:",end = " ")
        display_hand(hand)
        word = input("Please enter a word, or '!!' to indicate that you are finished:")
        if word == "!!":
            print(f"Total score for this hand: {total_score} points")
            return total_score
        elif not is_valid_word(word, hand, word_list):
            print("That is not a valid word. Please choose another word.")
            hand = update_hand(hand,word)
            print()
        else:
            total_score += get_word_score(word,sum(hand.values()))
            print(word,"earned",get_word_score(word,sum(hand.values())),"points.Total:",total_score,"points")
            hand = update_hand(hand,word)
            print()
    print("Run out of letters.Total score for this hand:",total_score)
    return total_score
  
            
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
         
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    It has been defaulted that letter is a character in hand
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = {}
    choice_from = ""
    for i in VOWELS+CONSONANTS:
        if i in hand.keys():
            continue
        else:
            choice_from += i
    for keys,values in hand.items():
        if keys == letter:
            new_hand[random.choice(choice_from)] = values 
        else:
            new_hand[keys] = values
    return new_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands
    注意，这里reply的实现是计分最后一次，而非取高
    word_list: list of lowercase strings
    """
    n = int(input("Enter total number of hands:"))
    i = 1
    Flag_1 = True
    Flag_2 = True
    total_score_final = 0
    answer_1 = ""
    answer_2 = ""
    while i <= n:
        hand = deal_hand(HAND_SIZE)
        if Flag_1:
            print("Current hand:",end = "")
            display_hand(hand)
            print()
            answer_1 = input("Would you like to substitute a letter?(yes/no)" )
        if answer_1 == "yes":
            letter = input("Which letter would you like to replace:")
            hand = substitute_hand(hand, letter)
            Flag_1 = False
        this_hand_score = play_hand(hand, word_list)
        print("---------")
        if Flag_2:
            answer_2 = input("Would you like to replay the hand? ")
        if answer_2 == "yes":
            Flag_2 = False
            this_hand_score = play_hand(hand,word_list) 
            print("---------")     
        total_score_final += this_hand_score
        i += 1
    print(f"Total score over all hands:{total_score_final}")
        
        
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    