# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 09:41:06 2015

@author: heshenghuan
"""

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.kid = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def addstr(self, s):
        """Add a string to this trie"""
        p = self.root
        n = len(s)
        for i in range(n):
            if p.kid.has_key(s[i]):
                p = p.kid[s[i]]
                if i == n-1:
                    p.is_word = True
                    return
            else:
                new_node = TrieNode()
                if i == n-1:
                    new_node.is_word = True
                p.kid[s[i]] = new_node
                p = new_node
                
    def search(self, s):
        """Judge whether s is in this trie"""
        p = self.root
        for c in s:
            if p.kid.has_key(c):
                p = p.kid[c]
            else:
                return False
        if p.is_word:
            return True
        else:
            return False
            
if __name__ == '__main__':
    trie = Trie()
    trie.addstr(u"产科")
    trie.addstr(u"BBC")
    trie.addstr(u"专访")
    trie.addstr(u"非机动车")
    trie.addstr(u"非机动车道")
    print trie.search(u"BBC")
    print trie.search(u"非机动车道")
    print trie.search(u"非机动车")
    print trie.search(u"非机动")
    trie.addstr(u"非机动")
    print trie.search(u"非机动")