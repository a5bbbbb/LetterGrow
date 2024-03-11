import time
import random

class LetterGrow:

    '''
    A class that makes characters grow into a phrase.

    The order in which characters grow is identical to the order of characters 
    in whatever is provided to vocab parameter of the constructor.

    The default value of the vocab parameter of the constructor is 
    just lowercase alphabet + uppercase alphabet.

    The whitespace character need not be included in the vocab.

    The vocab can be randomly shuffled using shuffle_vocab method.

    '''

    __default_vocab = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def __init__(self, phrase, vocab = __default_vocab):

        '''
        The constructor has the phrase and the vocab parameters. 
        The phrase parameter is the target phrase.
        The vocab parameter provides the order of change of characters.
        '''

        self._phrase = phrase

        self._vocab = vocab

        self._check_correctness()

    
    def _check_correctness(self):

        '''
        
        '''

        vocab_with_space = self._vocab + [' ']

        for i in self._phrase:

            if not i in vocab_with_space:

                raise Exception(f'''The provided phrase contains character(s) that are absent in the provided vocab.
                                {i} is absent in vocab''')


    def shuffle_vocab(self):

        random.shuffle(self._vocab)

    
    def __iter__(self):

        ''' Initialize the variables to start from empty string. '''

        self._cur_str = ' ' * len(self._phrase)

        self._cur_i = 0

        self._cur_ord = 0

        return self
    

    def __next__(self):

        if self._cur_str == self._phrase:

            raise StopIteration
        
        self._make_step()

        return self._cur_str

    
    def _make_step(self):

        '''
        If the current character is that same as in the phrase
        then move to the next character, otherwise change current
        character to the next one in the vocab.
        '''

        if self._phrase[self._cur_i] == self._cur_str[self._cur_i]:

            self._cur_i += 1

            self._cur_ord = 0

            return

        self._cur_str = self._cur_str[0 : self._cur_i ] + \
                        self._vocab[ self._cur_ord ] + \
                        self._cur_str[ self._cur_i + 1 : ]

        self._cur_ord += 1



            
p = "Zhannur is now free from a girlfriend"

# best from 0.001 to 0.09
comb_delay = 0.001

a = LetterGrow(p)


a.shuffle_vocab()

for i in a:

    print(i)

    time.sleep(comb_delay)
        


