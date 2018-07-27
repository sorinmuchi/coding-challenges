'''
Tries: Contacts
Hard
https://www.hackerrank.com/challenges/ctci-contacts/problem
'''

#!/bin/python3

class TrieNode():
    def __init__(self, wordsBelow):
        self.completeWordsBelow = wordsBelow
        self.children = {}
        
    def addChild(self, letter):
        self.completeWordsBelow += 1
        if not self.children.get(letter, False):
            self.children[letter] = TrieNode(0)
        return self.children[letter]

def addContact(node, word):
    if not word:
        node.completeWordsBelow += 1
        return        
    return addContact(node.addChild(word[0]), word[1:])
    
def findContacts(node, word, count):
    if not word:
        return node.completeWordsBelow
    if node.children.get(word[0], False):
        return findContacts(node.children[word[0]], word[1:], count)
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    root = TrieNode(0)

    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]
        contact = opContact[1]
        
        if (op == 'add'):
            addContact(root, contact)
        else:
            print(findContacts(root, contact, 0))
