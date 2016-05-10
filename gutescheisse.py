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

pasta_template = (
  "{e1}{e2}{e1}{e2}{e1}{e2}{e1}{e2}{e1}{e2} {w1} {w2} {w3} {w4}{e1} das"
  " ist {e3} {w3}{e1}{e1}{w4} genau{e1}{e1}hier{e1}{e1}{e1} genau{e3}"
  "hier {e3}{e3}wenn ich so ƽage so ƽage ich es {e4} ich sage es so "
  "{e4} über genau das rede ich genau hier genau hier(Refrain: genau "
  "hier) mMMMMᎷМ{e4} {e1}{e1} {e1}НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ{e3} {e1}"
  "{e1} {e1} {e4} {e3} {e2} {e2} {e2} {e1}{e1}{w1} {w2}")

emoji1 = raw_input("Erstes emoji [:ok_hand:]: ")
emoji2 = raw_input("Zweites emoji [:eyes:]: ")
emoji3 = raw_input("Drittes emoji [:heavy_check_mark:]: ")
emoji4 = raw_input("Viertes emoji [:100:]: ")

word1 = raw_input("Erstes Adjektiv [gute]: ")
word2 = raw_input("Erstes Nomen [scheiße]: ")
word3 = raw_input("Zweites Adjektiv [gUte]: ")
word4 = raw_input("Zweites Nomen [scHeiße]: ")

emoji1 = emoji1 if emoji1 else emoji1_def
emoji2 = emoji2 if emoji2 else emoji2_def
emoji3 = emoji3 if emoji3 else emoji3_def
emoji4 = emoji4 if emoji4 else emoji4_def

word1 = word1 if word1 else word1_def
word2 = word2 if word2 else word2_def
word3 = word3 if word3 else word3_def
word4 = word4 if word4 else word4_def

text_vars = {
  "e1": emoji1, "e2": emoji2, "e3": emoji3, "e4": emoji4,
  "w1": word1, "w2": word2, "w3": word3, "w4": word4}

print(emoji.emojize(pasta_template.format(**text_vars), use_aliases=True))
