
from Hiram_sdk_the_one.functions import *
print("------------------------get all the informtaion for lord of the rings books ------------------------------------------")
print( get_book())
print("-------------------------------------get book information based on id -----------------------------")
string_number = "5cf5805fb53e011a64671582"
print( get_book_id(string_number))
print("------------------------------------get the chapter of a specific book ------------------------------")
print(get_book_chapter(string_number))
print("-------------------------------get lord of the rings movies -----------------------------------")
print(get_movies())
print("-----------------------------------get the movies based on id -------------------------------")
string_numbers = "5cd95395de30eff6ebccde5d"
print( get_movie_id(string_numbers))
print("----------------------------------get the selection of a movie quote --------------------------------")
print( get_movie_quote(string_numbers))
print("---------------------------------get the selection of a character ---------------------------------")
print( get_character())
print("-----------------------------------get character based on id -------------------------------")
string_numbersCh = "5cd99d4bde30eff6ebccfbda"
print( get_character_id(string_numbersCh))
print("---------------------------------get quotes---------------------------------")
print( get_quote())
print("------------------------------------get chapters------------------------------")
print( get_chapter())