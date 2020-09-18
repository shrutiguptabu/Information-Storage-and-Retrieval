from nltk.tokenize import RegexpTokenizer

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordTokenizer:

    def __init__(self, content):
        # use the regular expression tokenizer
        tokenizer = RegexpTokenizer(r'\w+')
        # tokenize the content and save it to variable self.words 
        self.words = tokenizer.tokenize(content)
        self.currentIndex = 0
        # save the length of words to the variable self.length
        self.length = len(self.words)


    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        # check the condition if the current index is greater than length, then return None
        if (self.currentIndex >= self.length):
            return None
        word = self.words[self.currentIndex]
        self.currentIndex += 1
        return word