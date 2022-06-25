# insert the text
text = ''' Li Luo entered the lowest level of the library, where he encountered a massive door made of an extraordinary spiritual metal. Utilising a drop of his blood allowed him to open it.
What lay behind the door was a brightly lit cultivation chamber.
This cultivation chamber was not as simple as it seemed. The purest of skygold was utilized as the main material for its construction. Skygold was a metal that was usually buried deep under the ground, created from the accumulation of worldly natural energy congealing into a physical form. This was the reason why it was such a special and highly sought-after metal.
Hence, skygold was not just a form of common currency, it could also naturally attract copious amounts of worldly natural energy to itself. A cultivation chamber built out of skygold would thus be a standard requirement for cultivators amongst mighty powers, greatly increasing the speed at which they could cultivate. 
"This truly is extravagant." Li Luo took slow steps as he entered the chamber, sighing in amazement at the sight around him. His parents had spent almost one hundred thousand pieces of skygold to construct this. Practicing his energy cultivation arts here would most definitely provide twice the results with half the effort. Till now, only Jiang Qing'e and him were allowed to cultivate here, and for that matter, this was his very first time stepping within.
This was truly a house made of gold. It has to be said that one got what they paid for. The skygold was truly not wasted, as merely standing within the room allowed Li Luo to sense the immense difference in density of worldly natural energy compared to just outside. 
Sighing again at how lucky he was, Li Luo moved towards the center of the chamber. Within which were two stone platforms, each with their own mats. Clearly, this was where his parents sat when they cultivated here.   
Li Luo picked one of the mats at random and sat cross-legged with both hands grasping a jade slip, his eyes closed. He began to chant the incantation recorded from the Azureflood Meditation Diagram in his heart. 
At the same time, his breathing followed the pattern prescribed by the art, gradually inhaling and exhaling.
Six exhales followed by three inhales. Nine shallow breaths followed by four deep ones... Li Luo began to adjust his breathing patterns, causing the effects to fluctuate. 
In the beginning, he would often make mistakes unknowingly, but his amazing perception and talent gradually revealed themselves. He quickly managed to grasp the underlying principles behind the Azureflood Meditation Diagram and truly entered the Ten Seals Stage.
As Li Luo sat on the mat, his eyes were closed tightly and his mind was fully '''

# add uninteresting words which we can update
uninteresting_words = ["the", "a", "an", "to", "if", "is", "it", "of", "and", "or", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

# function literate text and remove punctuation and uninteresting words
def Iterates_from_file(txt, unwords):
    text3 = []
    text1 = txt.lower()
    text2 = text1.split(' ')
    for word in text2:
        if word.isalpha():
            text3.append(word)
    for word in list(text3):
        if word in unwords:
            text3.remove(word)
    return text3

# function make dictionary where key - word, item - count word in text
def Make_Dict(text2):
    dictionary = {}
    for word in text2:
        dictionary[word] = text2.count(word)
    return dictionary
    
print(Make_Dict(Iterates_from_file(text, uninteresting_words)))