# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:38:11 2021

@author: Jaroslav
"""
# -*- coding: utf-8 -*-
def f1(x):
    return x+1
x2=f1(1)

print("vvedite vo skolko uvelichet functziy:")
n=int(input())


def doublern (f):
    def g(n):
        return n*f
    return g


#print(x2)

g=doublern(x2)

print(g(n))

print("vvedite vo skolko uvelichet functziy:")
n=int(input())
def f1(x):
    return x+n
x2=f1(n)

def doublern (f):
    def g(n):
        return n*f
    return g


#print(x2)

g=doublern(x2)

print(g(n))


p='hello'

print(p)

#print(g(p))



text_file = open('C:/F#/exp2/file1.txt','r',encoding='utf8')
print(text_file)
line_list = text_file.readlines(); 

for line in line_list:
    print(line)
    
text_file.close()

import shutil 
shutil.copy('C:/F#/exp2/file1.txt', 'C:/F#/exp2/file3.txt')

import os
os.getcwd()

print(os.listdir('C:/F#/exp2/'))
#print(shutil.rmtree.avoids_symlink_attacks)

import shutil

for i in range(10):
    shutil.copy2('C:/F#/exp2/file1.txt',  'C:/F#/exp2/file1{}.txt'.format(i))