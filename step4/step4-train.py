import json
from collections import defaultdict
TEST_WORD = 'princess1'
MARKOV_DICT_OCCURENCE_COUNT_KEY = 'occurence_count'
def get_markov_dict(word):
    '''
    function to return a bigram dict for a single word
    '''
    # make list of bigrams, including start and end characters
    pairs = [('SOP',word[0])] + list(zip(word,word[1:])) + [(word[-1],'EOP')]

    markov = defaultdict(int)
    for first,second in pairs:
        key = first + second
        markov[key] += 1

    return markov

def update_markov_dict_with_word(markov,word):
    '''
    function to update a markov dict with the bigrams for
    a new word
    '''
    # make list of bigrams, including start and end characters
    pairs = [('SOP',word[0])] + list(zip(word,word[1:])) + [(word[-1],'EOP')]

    for first,second in pairs:
        key = first + second
        markov[MARKOV_DICT_OCCURENCE_COUNT_KEY] += 1
        markov[key] += 1

def markov_mode_from_file(filepath='rockyou.txt'):
    '''
    function to take in a file, and lie by line read passwords
    and create a markov model dictionary
    '''

    markov = defaultdict(int)
    markov[MARKOV_DICT_OCCURENCE_COUNT_KEY] = 0

    with open(filepath, "r", encoding="utf8", errors="ignore") as file:
        for line in file:
            line = line.rstrip()
            if not line:
                # if the line is empty after getting rid of non-utf8
                # just keep going
                continue

            update_markov_dict_with_word(markov=markov,word=line)

    return markov

def test_mini_markov():
    return get_markov_dict(word=TEST_WORD)

def write_bigrams_to_file(inputfilepath,outputfilepath):
    d = markov_mode_from_file(inputfilepath)
    with open(outputfilepath,'w') as outfile:
        json.dump(d,outfile,indent=2)

def transform_bigram_file_to_markov_model(bigramfile,markovmodelfile):
    '''
    take a bigram file and turn it into a markov model
    where each key:value in the json output is

        bigram : total probability (non log, so literally bigram count / total bigrams)
    '''
    # actual output dictionary mapping bigrab : probability
    markov = {}

    with open(bigramfile, 'r') as bigramfile:
        bigrams = json.load(bigramfile)
        total_bigram_count = bigrams[MARKOV_DICT_OCCURENCE_COUNT_KEY]

        try:
            # get rid of the occurence count k:v pair after reading
            del bigrams[MARKOV_DICT_OCCURENCE_COUNT_KEY]
        except KeyError as e:
            print(f"L + key error {e}")
            return

        for bigram,occurence_count in bigrams.items():
            bigram_probability = occurence_count / total_bigram_count
            markov[bigram] = bigram_probability

    with open(markovmodelfile, 'w') as markovfile:
        json.dump(markov,markovfile,indent=2)


def run_rockabye():
    '''
    baby test :)
    '''
    rockyou = 'rockabye.txt'
    rockbigram= 'rockabye_bigrams.json'
    rockmarkov= 'rockabye_markov_model.json'
    write_bigrams_to_file(inputfilepath=rockyou,outputfilepath=rockbigram)
    transform_bigram_file_to_markov_model(bigramfile=rockbigram,markovmodelfile=rockmarkov)

def run_rockyou():
    rockyou = 'rockyou.txt'
    rockbigram= 'rockyou_bigrams.json'
    rockmarkov= 'rockyou_markov_model.json'
    # write_bigrams_to_file(inputfilepath=rockyou,outputfilepath=rockbigram)
    transform_bigram_file_to_markov_model(bigramfile=rockbigram,markovmodelfile=rockmarkov)

if __name__ == "__main__":
    # run_rockabye()
    run_rockyou()
