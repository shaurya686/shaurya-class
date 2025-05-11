class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

        def __str__(self):
            #we will return a string
            return self.word+' ( '+self.meaning+' )'
        
flash = []
print("welcome to flashcard application")        