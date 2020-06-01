import itertools
from typing import List, Tuple


def generate_upper_lower_pairs(input_string: str) -> List[Tuple[str, str]]:
    """
    Given an input string ("ab"), return a list of pairs of the form (c.lower(), c.upper()) for every c in input_string.
    """
    return [
        (c.lower(), c.upper()) if c.isalpha() else (c, ) for c in input_string
    ]


def letter_case_permutation(input_string) -> List[str]:
    """
    :type input_string: str
    :rtype: List[str]
    Example:
        input = 'ab'
        1. create a list of pairs of the form (c.lower(), c.upper()): [ ('a', 'A'), ('b', 'B') ]
        2. create a product(list of all possible combinations):
             [ ('a', 'b'), ('a', 'B'), ('A', 'b'), ('A', 'B' ]
        3. finally, apply ''.join to all the elements of this list to create strings
            [ 'ab', 'aB', 'Ab', 'AB' ]
    """
    upper_lower_pairs = generate_upper_lower_pairs(input_string)
    all_combinations = itertools.product(*upper_lower_pairs)
    return list("".join(comb) for comb in all_combinations)


def letter_case_permutation_dfs(input_string):
    """
    A "Depth-first search" approach to the problem. Here we explore different "branches"(each alphabetic character
    produces a new branch). We basically traverse the "tree" and stop at each "leaf" to add it to the solution.
    (should
    """
    res = []
    def dfs(S, sol, i):

        if len(sol) == len(S):
            print(f'adding {sol}')
            res.append(sol)
            return

        if S[i].isalpha():
            dfs(S, sol + S[i].upper(), i+1)
            dfs(S, sol + S[i].lower(), i+1)
        else:
            dfs(S, sol + S[i], i+1)

    dfs(input_string, '', 0)
    return res
