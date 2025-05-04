# Lecture 5, PracticeSet 2: Hangman Game
# Hangman is an ancient game. Can retrieve relevant information online.

import random


def word_Letters(word):
    """
    ## input: An English word
    ## return letters: no duplicate and word length
    ## attention: sorting after converting the word into a list
    """
    list_1 = []
    str1 = ""
    for char in word:
        if char not in list_1:
            list_1.append(char)
    list_1.sort()
    for char in list_1:
        str1 += char
    return (str1, len(word))  # str1：letters of no duplicate， word length


def letters_Guess(word, guess):
    """
    # input word(is source) and guess
    # Judge and output results
    # if correct,output:"Wow, You Win!!!" and return True
    # otherwise output: give the same letter between word and guess,return False
    """
    if word == guess:
        print("  Wow, Congratulations,You Win!!!\n\nGame Over~")
        return True  # end of game
    else:  # Compare word and guess. get same letters are
        list_2 = []
        for char in guess:
            if char in word and char not in list_2:
                list_2.append(char)
        list_2.sort()
        print("Sorry,you guessed wrong! ^O^")
        print("You guessed the letter(s) in Ward:", list_2)
        return False  # need repeat


def repeat_times(word):
    """
    The repeat times of game is half the length of the word
    input: word (is source)
    return: repeat times of game
    """
    return len(word)//2


def guess_repeat(n, word):
    """
    # Guess repeat n times
    # input: n ( is times), word (is source word)
    # return: None
    """
    print(" 你可以尝试猜", n, "次")
    for i in range(n):
        guess = input("Please Enter your guess English word: ")
        if letters_Guess(word, guess):
            break
        elif i == n-1:
            print("\n\nYou Lost and Game Over!")
        else:
            print("You have tried", i+1, "times\n\nRepeat", i+1)


def choice_random(word_list):
    """
    # Randomly generate a value as the selected word index
    # input: words_list( is the list of English words)
    # return: the value between 0~ len(word_list)-1
    """
    return random.randint(0, len(word_list)-1)


# main/Test code
English_words = ['students', 'zhejiang', 'university', 'excellent', 'outstanding',
                 'good', 'mediocrity', 'inferior', 'dream', 'endurance', 'achieve']

words_index = choice_random(English_words)
word = English_words[words_index]  # Line 87& Line 88 从English_words中随机选择一个单词
word = word.lower()  # 将word中可能的大写字母变成小写

(x, y) = word_Letters(word)

print("Hangman Game\n 待猜英文单词包括的字母:", x, "\n 单词的长度是:", y)
print()
guess_repeat(repeat_times(word), word)  # 开始猜字游戏
