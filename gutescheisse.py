#!/usr/bin/python
# -*- coding: utf-8 -*-
import emoji
import sys

reload(sys)
sys.setdefaultencoding('utf8')

emoji1_def = ":ok_hand:"
emoji2_def = ":eyes:"
emoji3_def = ":heavy_check_mark:"
emoji4_def = ":100:"

word1_def = "gute"
word2_def = "scheiße"
word3_def = "gUte"
word4_def = "scHeiße"

emoji1 = raw_input("Erstes emoji [:ok_hand:]: ")
emoji2 = raw_input("Zweites emoji [:eyes:]: ")
emoji3 = raw_input("Drittes emoji [:heavy_check_mark:]: ")
emoji4 = raw_input("Viertes emoji [:100:]: ")

word1 = raw_input("Erstes Adjektiv [gute]: ")
word2 = raw_input("Erstes Nomen [scheiße]: ")
word3 = raw_input("Zweites Adjektiv [gUte]: ")
word4 = raw_input("Zweites Nomen [scHeiße]: ")

if emoji1 == "":
  emoji1 = emoji1_def
if emoji2 == "":
  emoji2 = emoji2_def
if emoji3 == "":
  emoji3 = emoji3_def
if emoji4 == "":
  emoji4 = emoji4_def

if word1 == "":
  word1 = word1_def
if word2 == "":
  word2 = word2_def
if word3 == "":
  word3 = word3_def
if word4 == "":
  word4 = word4_def
print(emoji.emojize(emoji1 + emoji2 + emoji1 + emoji2 + emoji1 + emoji2 + emoji1 + emoji2 + emoji1 + emoji2 + " " + word1 + " " + word2 + " " + word3 + " " + word4 + emoji1 + " das ist " + emoji3 + " " + word3 + emoji1 + emoji1 + word4 + " genau" + emoji1 + emoji1 + "hier" + emoji1 + emoji1+ emoji1 + " genau" + emoji3 + "hier " + emoji3 + emoji3 + "wenn ich so ƽage so ƽage ich es " + emoji4 + " ich sage es so " + emoji4 + " über genau das rede ich genau hier genau hier(Refrain: genau hier) mMMMMᎷМ" + emoji4 + " " + emoji1 + emoji1 + " " + emoji1 + "НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ" + emoji3 + " " + emoji1 + emoji1 + " " + emoji1 + " " + emoji4 + " " + emoji3 + " " + emoji2 + " " + emoji2 + " " + emoji2 + " " + emoji1 + emoji1 + word1 + " " + word2, use_aliases=True))
