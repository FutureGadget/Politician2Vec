from gensim import *

class Pol2Vec:
    def __init__(self, modelFileName):
        self.model = models.Word2Vec.load(modelFileName)
    
    def most_similar(self, pos, neg):
        self.model.wv.most_similar(positive=pos, negative=neg)