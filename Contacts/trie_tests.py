import Trie

def tests():
    #test trie
    trie = Trie.Trie()
    assert trie.root == {}

    #test add: "ate"
    
    assert trie.add("ate") == {'a': [False, {'t': [False, {'e': [True, {None}]}]}]}
    assert trie.add("atom") == {'a': [False, {'t': [False, {'e': [True, {None}], 'o': [False, {'m': [True, {None}]}]}]}]}
    print ("tests passed")


tests()


