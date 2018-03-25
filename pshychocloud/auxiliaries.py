from string import punctuation as punctuation_marks

def clean_line(line):
    ''' 
        This functinality aims to remove the puntuaction marks from the text
        and finally the spaces. 
    '''
    return filter(lambda char: char not in punctuation_marks, line ).strip()

def remove_space_as_word(wordlist):
    '''
        This function just removes the space from the words
    '''
    return filter(lambda word: word != '', wordlist)
