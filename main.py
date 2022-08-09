# function literate text and remove punctuation and uninteresting words
def iterates_from_file(txt, un_words):
    text3 = []
    text1 = txt.lower()
    text2 = text1.split(' ')
    for word in text2:
        if word.isalpha():
            text3.append(word)
    for word in list(text3):
        if word in un_words:
            text3.remove(word)
    return text3


# function make dictionary where key - word, item - count word in text
def make_dict(text2):
    dictionary = {}
    for word in text2:
        dictionary[word] = text2.count(word)
    return dictionary


# to open and close file
try:
    # open file which contains text 
    f = open('project_text.txt')
    cont = f.read()
    
    # open file which contains uninteresting words
    c = open('uninteresting_words.txt')
    words = c.read()
    
    # save a dictionary in the variable 
    result = make_dict(iterates_from_file(cont, words))
    
    # sorted dictionary from max to min
    print(dict(sorted(result.items(), key=lambda item: item[1], reverse=True)))
finally:
    f.close()
    c.close()
