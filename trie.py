# lets understand the concept of a Trie
# Trie is nothing but basically a tree data structure and is also known as 
# Prefix Tree

# lets define a class for TrieNode

class TrieNode:
    def __init__(self):
        # lets create a hash set of children where we will store and look for words
        self.children = {} 
        # and we will initialize the end of the word as False for now
        self.word = False

# define a class for the Trie or the Prefix Tree which will take the root node
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # now lets understand how we can insert a word in the Trie
    # lets define a function which takes in a word
    def insert(self, word):
        # we will set the current pointer to the root of the Trie
        curr = self.root
        # now we will iterate through each character in the word
        for c in word:
            # if the character is not in the hashset then we add it
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # here we can just set the current pointer 
            curr = curr.children[c]
        # now we will just set the end of the word as True
        curr.word = True

    # now lets see how we can search for a word
    def search(self, word):
        # we set the current pointer to the root node
        curr = self.root
        # now we iterate through every character in the word
        for c in word:
            # if the character does not exist we return False
            if c not in curr.children:
                return False
            # we set the current pointer if we find the character
            curr = curr.children[c]
        # and return the word
        return curr.word


    # now lets see how we can search for prefix
    def startsWith(self, prefix):
        # we set the current pointer to the root node
        curr = self.root
        # now we iterate through every character in the prefix
        for c in prefix:
            # if the character is not in the hashset we return False
            if c not in curr.children:
                return False
            # we set the current pointer if we find the character
            curr = curr.children[c]
        # now we return the true value if we find the prefix
        return True


