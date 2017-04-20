# random_text
Python module to create text based on existing text patterns


# example
<pre>
from random_text.markovchain import MarkovChainWalker

# number of words 1300
words = 1300

# create a new object
dickens = MarkovChainWalker()

# parse books in text
dickens.parse('dickens/a_christmas_carol.txt')
dickens.parse('dickens/great_expectations.txt')  

dickens.process()
# start with 'i' and generate 1300 words
print dickens.generate('i', words)
</pre>


# Live Demo
As this is done in a single web request, try not to put a lot of books; it will timout
[https://random-text-163109.appspot.com/](https://random-text-163109.appspot.com/)
