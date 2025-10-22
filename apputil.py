from collections import defaultdict
import re
import random
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):

        self.corpus = re.findall(r"\b\w+\b", corpus)
        self.term_dict = defaultdict(list)

    def get_term_dict(self):
        """ This function creates dictionary of text """
        for i in range(len(self.corpus) - 1):
            current_word = self.corpus[i]
            next_word = self.corpus[i + 1]
            self.term_dict[current_word].append(next_word)
        return dict(self.term_dict)

   


    def generate(self, seed_term=None, term_count=15):
        """ This function generates text based on seed term provisioning """
        if seed_term is None:
            seed_term = random.choice(list(self.term_dict.keys()))
        elif seed_term not in self.term_dict:
            raise ValueError(f"'{seed_term}' is not present in corpus!")

        current_word = seed_term
        generated = [current_word]

        for _ in range(term_count - 1):
            next_words = self.term_dict.get(current_word)

            if not next_words:  # last word case
                current_word = random.choice(list(self.get_term_dict().keys()))
               
            else:
                current_word = np.random.choice(next_words)

            generated.append(current_word)

        return " ".join(generated)
