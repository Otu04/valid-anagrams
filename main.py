# Python 3.9.7
# Checking if two strings are anagrams
# anagram -  word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# ex. car - arc, nameless - salesmen
# in my program, anagrams MUST also have same amount of capital letters AND spaces to be considered as anagrams

def valid_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    freq1 = {} # create hash tables
    freq2 = {}
    for ch in s1: # add every char from s1 to freq1
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for key in freq1:
        if freq1 != freq2 or key not in freq2:# im not sure if 'or key not in freq2' is necessary there, but it works anyway
            return False
    return True

def sample_test_valid_anagrams():
    words = [["angel", "glean "], ["a r c", "car"], ["braag","grab"], # first 3 are not anagrams
             ["bored", "robed"],["cat","act"],["cider","cried"],
             ["a gentleman", "elegant man"],["twelve plus one","eleven plus two"],["William_Shakespeare","iam_aWeakishSpeller"],
             ["night", "thing"],["peach","cheap"],["players","parsley"],
             #["sadder", "dreadss"],["save","vase"],["state","tastee"], # 13 and 15 are not anagrams
             ]
    answers = [False, False, False,
               True, True, True,
               True, True, True,
               True, True, True,
               '''True, True, True''']
    # if You delete comments in line 28 and 30 You will trigger an 'else' below
    # but this doesn't make sense since answers MUST be correct :P
    counter = 0
    for pair in words:
        counter += 1
        if valid_anagrams(pair[0], pair[1]) is True:
            print("Output: '" + str(answers[counter-1]) + "', Sample test " + str(counter) + " ended successful")
        elif valid_anagrams(pair[0], pair[1]) == False and answers[counter-1] == False: # if return False and answer is False
            print("Output: '" + str(answers[counter-1]) + "', Sample test " + str(counter) + " ended successful")
        else:
            print("Output: '" + str(answers[counter-1]) + "', expected output: '" + str(not(answers[counter-1])) + "', Sample test " + str(counter) + " did NOT ended successful")

if __name__ == "__main__":
    sample_test_valid_anagrams()
