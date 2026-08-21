import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'ball'
V -> 'kicked'
""")

parser = ChartParser(grammar)

sentence = "the boy kicked the ball".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
