import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.
        #with open(Path.StopwordDir, "r", encoding="utf8") as f:
        #    self.sws_english = f.read().splitlines()
        self.sws_english = set(line.strip() for line in open(Path.StopwordDir, "r", encoding="utf8"))
        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        return word in self.sws_english
