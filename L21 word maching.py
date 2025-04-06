def match_words(words):
    ctr = 0
    lst = []

    for w in words:
        if len(w) > 1 and w[0] == w[ -1]:
            ctr = ctr + 1
            lst.append(w) # adding the element in the lst

    print("list of words with first and last character same ")
    print(lst)
    return ctr

word_list = ['abc', 'cfc', 'xyz', '1221']
count = match_words(word_list)
print("Number of word having first and last charcter same:", count)