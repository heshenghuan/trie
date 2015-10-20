# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 09:41:06 2015

@author: heshenghuan
"""

import codecs

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
    
    def readDict(self, dictfile):
        """
        Reads a dictionary file to build a trie tree.
        """
        print "Loading dict data and building Trie Tree."
        input_data = codecs.open(dictfile, 'r', 'utf-8')
        entry_num = 0
        maxl = 0
        for line in input_data.readlines():
            rawText = line.strip()
            if rawText == '':
                continue
            else:
                entry_num += 1
            #if entry_num%1000 == 0 and entry_num !=0:
                #print '.',
            word = rawText.split()[0]      #remove the space
            length = len(word)
            maxl = max(maxl,length)
            self.addstr(word)
        print "Loading dictionary done."
        print "Total",entry_num, "entries."
        print "Maximum length of entry:",maxl
        return maxl
