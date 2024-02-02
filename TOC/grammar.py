#1/2/24
from nltk import CFG
from nltk.parse.generate import generate

grammar = ''
with open('grammar1.txt','r') as mygrammar:
    res = mygrammar.readlines()
    for i in res:
        grammar+=i
    
given_gramma = CFG.fromstring(grammar)
