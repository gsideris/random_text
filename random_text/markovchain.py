from dictionary import Dictionary
import random
import StringIO

class MarkovChainWalker(object):
    def __init__(self):
        self.dictionary = Dictionary()


    def parse(self,filename):
        self.dictionary.update(filename)

    def process(self):
        self.dictionary.process()

    # pick a random word
    def pick(self,hash):
        random_pick = random.random()
        for key, value in sorted(hash.iteritems(), key=lambda (k,v): (v,k)):
            if random_pick < value:
                return key

                
    # generate 
    def generate(self,start_word,number_of_words):
        output = StringIO.StringIO()
        word = start_word
        for n in range(number_of_words):
            output.write('%s ' % word)
            secondary = self.dictionary.dictionary[word]
            word = self.pick(secondary)
        contents = output.getvalue()            
        output.close()
        return contents


