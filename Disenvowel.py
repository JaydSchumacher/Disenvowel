''' OK, I need you to finish writing a function for me. The function disemvowel takes a single word as a parameter and then returns that word at the end.

I need you to make it so, inside of the function, all of the vowels ("a", "e", "i", "o", and "u") are removed from the word. Solve this however you want, it's totally up to you!

Oh, be sure to look for both uppercase and lowercase vowels! '''

def disemvowel(word):
    my_word = []
    new_word = ""
    my_word.extend(word)
    for letter in my_word:
        if(letter == "a" or letter == "A"):
            continue
        elif(letter == "e" or letter == "E"):
            continue
        elif(letter == "i" or letter == "I"):
            continue
        elif(letter == "o" or letter == "O"):
            continue
        elif(letter == "u" or letter == "U"):
            continue
        else:
            new_word += letter
    print(new_word)
    return new_word

disemvowel("Hello")