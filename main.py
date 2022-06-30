# add uninteresting words which we can update
uninteresting_words = ["the", "a", "an", "to", "if", "is", "it", "of", "and", "or", "as", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                       "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                       "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                       "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


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
    f = open('Project_text.txt')
    cont = f.read()
    result = make_dict(iterates_from_file(cont, uninteresting_words))
    # sorted dictionary from max to min
    print(dict(sorted(result.items(), key=lambda item: item[1], reverse=True)))
finally:
    f.close()


