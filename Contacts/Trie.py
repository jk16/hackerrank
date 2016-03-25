"""
Implementation of a Trie:
operations: ADD/FIND


"""


def root():
    return {}


"""
Main operations: add/find
"""


def add(word, root):
    """
    ******************************************************************
    Given a word and a root of a Trie returns a new root with the word
    ******************************************************************

    example 1: word="ate" and root = {}
                output: {'a': [False, {'t': [False, {'e': [True, {None}]}]}]}

    example 2: word="atom" and root = {'a': [False, {'t': [False, {'e': [True, {None}]}]}]}

                    step 1: word and root --> "at" ie the union
                    step 2: decompose word into: part in Trie and part not in Trie ie "at" + "om"
                    step 3: build a tree using "om" ie o --> m
                    step 4: connect a --> t with o --> m
    """

    #is first letter of the word in the root?
    is_word_in_trie = is_in_trie(word, root)

    # if word is in Trie then just add it to the Trie
    # else create a new tree and add it to the trie
    #
def find(word, root):
    """
    number of contacts who have a name starting with that partial name.
    """

"""
Helper functions
"""


def tests():
    print (root())

if __name__ == "__main__":
    """
    Purpose: If you use as a module code wont get executed
             If you use it as an executable it will get called 
    """
    tests()









