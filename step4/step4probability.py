import json
ROCKYOU_MARKOV_FILEPATH = 'rockyou_markov_model.json'
ROCKABYE = 'rockyou_markov_model.json'

def run_on_input():
    filepath = 'step4-input.txt'
    outpath = 'step4-output.txt'

    # also open the markov file to access it's dictionary
    with open(ROCKYOU_MARKOV_FILEPATH,'r') as markovfile:
        markov = json.load(markovfile)

    with open(filepath, "r", encoding="utf8", errors="ignore") as infile:
        # also open the file to write results into
        with open(outpath,'w') as outfile:
                # read one line, aka password, at a time
                for password in infile:
                    # get rid of newline character from input
                    password = password.rstrip()
                    if not password:
                        # if the password is empty after
                        # getting rid of non-utf8, just keep going
                        continue

                    chance = get_probability_for_one_password(password,markov=markov)
                    # newline added manually
                    output_string = password + "\t" + str(chance) + "\n"

                    outfile.write(output_string)


def get_probability_for_one_password(password,markov):
    '''
    get's the probability for one password
    calculated as the product of the probability for each bigram
    as given by the dict from json
    '''
    pairs = [('SOP',password[0])] + list(zip(password,password[1:])) + [(password[-1],'EOP')]

    # starting at 1, multiplied by each bigram chance
    total_chance = 1

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
