# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:20:36 2024

@author: sarah
"""

tab = [8,4.5,6,12,78,4,8000]


#algo tri par sélection: le tri par sélection est de complexité O(N²)
def tri_selection(tab):
    n =len(tab)
    for i in range (0,n-1):
        i_mini = i
        for j in range(i+1,n):
            if tab[j] < tab[i]:
                i_mini = j
                temp = tab[i]
                tab[i]=tab[i_mini]
                tab[i_mini] = temp
    return tab

#tri_selection(tab): le tri par bulles est de complexité O(N²)
print(tab)

# algo tri bulle : 
def tri_bulle(tab):
    n= len(tab)
    for i in range(n):
        for j in range(0,n-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]= tab[j+1],tab[j]
    return tab

#tri_bulle(tab)
print(tab)

# alog tri par insertion
def tri_insertion(tab):
    n=len(tab)
    for i in range(1,n):
        repere = tab[i]
        j = i-1
        while j>=0 and tab[j]> repere:
            tab[j+1] = tab[j]
            j = j-1
            tab[j+1] = repere
    return tab
tri_insertion(tab)
print(tab)

# tri fusion

        
        