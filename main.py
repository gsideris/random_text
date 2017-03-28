from random_text.markovchain import MarkovChainWalker

words = 1300

dickens = MarkovChainWalker()
dickens.parse('dickens/a_christmas_carol.txt')
dickens.parse('dickens/great_expectations.txt')  
dickens.parse('dickens/three_ghost_stories.txt')
dickens.parse('dickens/david_copperfield.txt')  
dickens.parse('dickens/oliver_twist.txt')
dickens.parse('dickens/dombey_and_son.txt')     
dickens.parse('dickens/tale_of_two_cities.txt')
dickens.process()
print dickens.generate('i', words)

