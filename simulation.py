import numpy as np
from tqdm import tqdm
import sys


def calculate_precision_percentage(data):
    """
    Per each R in the dictionary, calculates the average number of cases
    where best candidate was choosen.
    """
    for i in data.keys():
        p = (sum(data[i])/len(data[i])) * 100
        data[i] = p
    return data


def get_number_of_simulations():
    """
    Getting number of simulations from user.
    """
    need_input = True
    while(need_input):
        user_input = input(
            """Please enter number of simulations (recommended min 100000):""")
        try:
            value = int(user_input)
            need_input = False
            print("Requested number of simulations: "+str(value))
        except ValueError:
            print("That's not an integer, please input an integer number!")
    return value


def print_results_other_R():
    """
    Asking user for decision on printing results for all R values.
    """
    need_input = True
    while(need_input):
        user_input = input("""Do you want score for every R? (y/n)""")
        if user_input.lower() == "y":
            need_input = False
            return True
        if user_input.lower() == "n":
            need_input = False
            return False
        print("Please answer with y or n.")


def simulate(R):
    """
    Simulation of selecting candidate using the algorithm of optimal
    stopping. Expects parameter R and returns 1 if best candidate was choosen,
    otherwise 0 is returned.
    """
    candidates = np.random.uniform(0, 10, NUMBER_OF_CANDIDATES)
    absolute_best_candidate = max(candidates)
    best_candidate = 0
    # first R rejected, best among them is stored for benchmarking
    best_benchmark = max(candidates[:R], default=0)
    for i in range(R, NUMBER_OF_CANDIDATES):  # iterate over the rest
        if candidates[i] > best_benchmark:
            best_candidate = candidates[i]
            if best_candidate == absolute_best_candidate:  # is best candidate
                return 1
            return 0

        if i == NUMBER_OF_CANDIDATES-1:  # if it is last candidate, take it
            best_candidate = candidates[i]
            if best_candidate == absolute_best_candidate:  # is best candidate
                return 1
            return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            NUMBER_OF_CANDIDATES = int(sys.argv[1])
        except ValueError:
            print(
                "Argument passed is not an integer. Taking 100 as a default!")
            NUMBER_OF_CANDIDATES = 100
    else:
        NUMBER_OF_CANDIDATES = 100

    number_of_simulations = get_number_of_simulations()
    data = {}
    for iteration in tqdm(range(number_of_simulations)):
        # 0-NUMBER_OF_CANDIDATES
        # max number maskes no sesne since non of candidates will be choosen
        example_R = iteration % NUMBER_OF_CANDIDATES
        result = simulate(example_R)
        if example_R in data:
            data[example_R].append(result)
        else:
            data[example_R] = [result]
    data = calculate_precision_percentage(data)
    best_R = max(data, key=data.get)

    print("Best result is :{:.2f}% for R={} ".format(data[best_R], best_R))

    if print_results_other_R():
        for i in data.keys():
            print("R={} selected best in {:.2f}% of cases.".format(i, data[i]))
