import json
from collections import defaultdict
import random
ROCKYOU_MARKOV_FILEPATH = 'rockyou_markov_model.json'


if __name__ == "__main__":
    with open(ROCKYOU_MARKOV_FILEPATH,'r') as markovfile:
        markov = json.load(markovfile)

    # dictionary mapping:
        # first bigram character: dict of:
            # second bigram character : probability
    two_layer_markov = defaultdict(dict)
    for bigram,probability in markov.items():
        if len(bigram) == 2:
            # dealing with two character bigrams
            first,second = bigram
            two_layer_markov[first][second] = probability
        elif "SOP" in bigram:
            # these are bigrams of format "SOP_"
            second = bigram[-1]
            two_layer_markov["SOP"][second] = probability
        elif "EOP" in bigram:
            # these are bigrams of format "_EOP"
            second = bigram[0]
            two_layer_markov["EOP"][second] = probability
        else:
            raise ValueError(f"somehow got bigram [{bigram}] which is of length {len(bigram)} without EOP or SOP")

    # to save the two_layer json for testing
    # with open('twolayer.json','w') as two:
    #     json.dump(two_layer_markov,two,indent=2)

    # pick 1000 SOP bigrams
    possible_first_chars = []
    possible_first_chars_weights = []

    for char,chance in two_layer_markov['SOP'].items():
        print(char,chance)
        possible_first_chars.append(char)
        possible_first_chars_weights.append(chance)

    print(random.choices(possible_first_chars[:5],weights=possible_first_chars[:5],k=100))
