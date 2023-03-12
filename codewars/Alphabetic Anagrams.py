from math import factorial as fact
def listPosition(word):
    if len(word) == 1:
        return 1
    upper_words = 0         #the number of words that come earlier in the dictionary
    for m in set(word[1:]):
        if m < word[0]:
            letters_dict = {l: word.count(l) for l in word} #dict of letters in subword
            if letters_dict[m] == 1:
                letters_dict.pop(m)
            else:
                letters_dict[m] -= 1
            subwords = fact(len(word)-1)
            for letter in letters_dict:
                subwords //= fact(letters_dict[letter])
            upper_words += subwords
    return (upper_words + listPosition(word[1:]))

word = 'QUESTION'
print(listPosition(word))


    