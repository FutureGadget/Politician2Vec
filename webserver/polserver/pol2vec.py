from gensim import *
import os
from settings import APP_DATA

class Pol2Vec:
    def __init__(self, modelFileName):
        self.model = models.Word2Vec.load(os.path.join(APP_DATA, modelFileName))
    
    def most_similar(self, pos, neg):
        return self.model.wv.most_similar(positive=pos, negative=neg)
    
    @staticmethod
    def process_query(query):
        d = {}
        p = []
        n = []
        st = []
        state = 0
        for ch in query:
            if ch == '+' or ch == '-':
                if len(st) > 0:
                    if state == 0:
                        p.append(''.join(st))
                    elif state == 1:
                        n.append(''.join(st))
                if ch == '+':
                    state = 0
                elif ch == '-':
                    state = 1
                st = []
            else:
                st.append(ch)

        if len(st) > 0:
            if state == 0:
                p.append(''.join(st))
            elif state == 1:
                n.append(''.join(st))

        d['positives'] = p
        d['negatives'] = n
        return d