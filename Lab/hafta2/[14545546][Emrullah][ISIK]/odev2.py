# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:57:40 2019

@author: Emrullah
"""

import pandas as pd
import numpy as np


VeriOku= pd.read_csv('C:/Users/Emrullah/Desktop/Dersler/_4.Sınıf Dersleri/Yapay Zeka ve Uzman Sistemler/Lab/hafta2/Odev1/hafta2.csv',
                     header=0,encoding = 'unicode_escape')
print(VeriOku)

 
numpy_array = np.array([[0, 10, 20 ,30 ], [6, 60, 600 , 6000], [12, 54, 108 , 1080]])

print(numpy_array)

print(numpy_array.reshape(6,2))

HavaDurum = {
"Gün": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14"],
"Hava Durumu": ["Güneşli", "Güneşli", "Kapalı", "Yağmurlu", "Yağmurlu", "Yağmurlu", "Kapalı", "Güneşli", "Güneşli", "Yağmurlu", "Güneşli", "Kapalı", "Kapalı", "Yağmurlu"],
"Sıcaklık": ["Sıcak", "Sıcak", "Sıcak", "Ilıman", "Soğuk", "Soğuk", "Soğuk", "Ilıman", "Soğuk", "Ilıman", "Ilıman", "Ilıman", "Sıcak", "Ilıman"],
"Nem": ["Yüksek", "Yüksek", "Yüksek", "Yüksek", "Normal", "Normal", "Normal", "Yüksek", "Normal", "Normal", "Normal", "Yüksek", "Normal", "Yüksek"],
"Yağış": ["Seyrek", "Aşırı", "Seyrek", "Seyrek", "Seyrek", "Aşırı", "Aşırı", "Seyrek", "Seyrek", "Seyrek", "Aşırı", "Aşırı", "Seyrek", "Aşırı"],
"Oyun" : ["Yok", "Yok", "Var", "Var", "Var", "Yok", "Var", "Var", "Yok", "Var", "Var", "Yok", "Var", "Yok"]
}
 
OyunOynama = pd.DataFrame(HavaDurum)
 
print(OyunOynama)

OyunOynama= OyunOynama.drop( columns = "Sıcaklık", axis=1)
OyunOynama= OyunOynama.drop( columns = "Nem", axis=1)
print(OyunOynama.columns)
print(OyunOynama)