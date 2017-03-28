import re

class Dictionary(object):
    def __init__(self):
        self.dictionary = {}

    # increase the occurence word1->word2
    def increase_pair(self,primary,secondary):
        if primary in self.dictionary:
            if secondary in self.dictionary[primary]:
                self.dictionary[primary][secondary] = self.dictionary[primary][secondary] + 1
            else:
                self.dictionary[primary][secondary] = 1
        else:
            self.dictionary[primary] = { secondary : 1 }



    # update dictionary values with words from a file
    def update(self,filename):
        word_sequence = ['','']
        fl = open(filename,'r')
        line = fl.readline()
        while line:
            words = re.split(r'[ \-"\n\r]+',line.rstrip())
            for j in words:
                if word_sequence[0]  == '':
                    word_sequence[0] = j.lower()
                else:
                    word_sequence.pop(0)
                    word_sequence.append(j.lower())
                    self.increase_pair(word_sequence[0],word_sequence[1])
            line = fl.readline()
        fl.close()
        print "updated %s" % filename


    def normalize(self,hash):
        sum = 0.0
        # calculate the sum
        for key,value in hash.iteritems():
            sum = sum + value

        for key,value in hash.iteritems():
            hash[key] = value / sum


    def add_values(self,hash):
        sum = 0.0
        for key, value in sorted(hash.iteritems(), key=lambda (k,v): (v,k)):
            sum = sum + value
            hash[key] = sum

    def process(self):
        for key,value in self.dictionary.iteritems():
            self.normalize(value)
            self.add_values(value)

