# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:47:37 2021

@author: Kasia
"""

class ksiazka:
    
    def __init__(self,tytul, ilosc_str, autor, data_wyd, wlasciciel):
        self.tytul = tytul
        self.ilosc_str = ilosc_str
        self.autor = autor
        self.data_wyd = data_wyd
        self.wlasciciel = wlasciciel
        
    def info_ksiazka(self):
        print ("Ksiazka: ", self.tytul, self.ilosc_str, self.autor,
               self.data_wyd, self.wlasciciel)
        
    def zmiana_wlasciciela(self, nowy_wlasciciel):
        self.wlasciciel = nowy_wlasciciel
        

ksiazka1 = ksiazka("Solaris", 500, "Lem", 1985, "Kasia")
ksiazka2 = ksiazka("Harry Potter", 600, "Rowling", 2000, "Julia")

lista_ksiazek = [ksiazka1, ksiazka2]

print(lista_ksiazek[0].wlasciciel)

ksiazka1.zmiana_wlasciciela("Dawid")
print(lista_ksiazek[0].wlasciciel)