import json
ROCKYOU_MARKOV_FILEPATH = 'rockyou_markov_model.json'
ROCKABYE = 'rockyou_markov_model.json'

def run_on_input():
    filepath = 'step4-input.txt'
    outpath = 'step4-output.txt'

    ex = 'princess'
    pr = get_probability_for_one_password(password=ex,markov_file=ROCKYOU_MARKOV_FILEPATH)
    print(f'princess pr : {pr}')

def get_probability_for_one_password(password,markov_file):
    '''
    get's the probability for one password
    calculated as the product of the probability for each bigram
    as given by the json in the provided markov model file
    '''
    pairs = [('SOP',password[0])] + list(zip(password,password[1:])) + [(password[-1],'EOP')]

    # starting at 1, multiplied by each bigram chance
    total_chance = 1
    with open(markov_file,'r') as markov_file:
        markov = json.load(markov_file)

        for first,second in pairs:
            key = first + second
            chance = markov.get(key,0)

            if chance == 0:
                # if the chance is 0, then the bigram was simply not found in the
                # model, thus meaning that my model thinks it's impossible
                # for a password to have it, thus any successive probabilities
                # don't matter
                return 0
            else:
                # update probability :)
                total_chance *= chance

    return total_chance





if __name__ == "__main__":
    run_on_input()
