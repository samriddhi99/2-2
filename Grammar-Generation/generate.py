from nltk import CFG 
from nltk.parse.generate import generate

with open("g2.txt","r") as mygrammar: 
    grrammar = ""
    res = mygrammar.readlines()
    for i in res: 
        grrammar = grrammar+i
    print(grrammar)    
given_grammar = CFG.fromstring(grrammar)
print(given_grammar)    

for sentance in generate(given_grammar, depth = 10, n = 1000):
    print("".join(sentance))