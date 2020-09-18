#import PorterStemmer
from nltk.stem import PorterStemmer

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordNormalizer:

    def __init__(self):
        # initialize Porter Stemmer
        self.stemmer = PorterStemmer()
        
        # initialize a empty dictionary
        self.stemmedDict = {}


    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        #return filter(self.letter_set.__contains__, word).lower()
        return word.lower()

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        
        # if the word is in Dictionary, return. 
        if (word in self.stemmedDict):
            return self.stemmedDict[word]
        else:
            # if the word not in Dictionary, add the word to Dictionary
            stemmedWord = self.stemmer.stem(word)
            self.stemmedDict[word] = stemmedWord
        
        #return stemmedWord
        return stemmedWord
