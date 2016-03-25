"""
Implementation of a Trie:
operations: ADD/FIND
"""


class Trie:
    def __init__(self):
        self.root = {}

    """
    Main operations: add/find
    """


    def add(self,word):
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

        if word[0] in self.root:
            letters_in_trie = self.union_trie_and_user_word(self.root, word) #"at"
            letters_not_in_trie = word.replace(letters_in_trie, "")

            add_to_tree = self.word_in_trie(self.root, letters_in_trie) #t --> 
            new_tree = self.build_tree(letters_not_in_trie) #t --> + o --> m
            add_to_tree[letters_not_in_trie[0]] = new_tree[letters_not_in_trie[0]]

            # self.root[word[0]][1] = new_tree
            return self.root
        else:
            new_tree = self.build_tree(word)
            self.root[word[0]] = new_tree[word[0]]
            return self.root



    def find(self,word, root):
        """
        number of contacts who have a name starting with that partial name.
        """
        pass


    """
    Helper functions
    """
    def build_tree(self,word):
        """
        Given string builds a tree
        example "ate"
        a --> t --> e
        """
        
        root = {}
        root[word[0] ] = [False, {}]
        
        child = root[word[0]][1]
        word = word.replace(word[0] , "")

        for i, letter in enumerate(word):
            is_word = i == (len(word) - 1)
            if not is_word:
                child[letter] = [is_word, {}]
            
                child = child[letter][1]
            else:
                child[letter] = [is_word, {None}]
            
        return root

    def word_in_trie(self,root, user_word):
        """
        Given root of a trie and a word gets the letters that exist in the trie
        example:
        input: word="atom" and root: a-->t-->e 
        out: what t points to

        """
        
        if len(user_word) <= 0:
            return "must have letters"
        dummy_root = root
        same_letters = ""
        for l in user_word:
            if l in dummy_root:
                same_letters += l
                dummy_root = dummy_root[l][1]
            else:
                break
        
        return dummy_root


    def union_trie_and_user_word(self,root, user_word):
        """
        Given root of a trie and a word gets the letters that exist in the trie
        example:
        input: word="atom" and root: a-->t-->e 
        out: "at"

        """
        same_letters = ""
        dummy_root = root
        for l in user_word:
            if l in dummy_root:
                same_letters += l
                dummy_root = dummy_root[l][1]
            else:
                break

        empty_string = len(same_letters) == 0
        to_return = None if empty_string else same_letters
        return to_return












