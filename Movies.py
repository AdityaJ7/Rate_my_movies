import re
import os

movie_location = input("Enter the directory(Without the Quotes): ")


def movie_getter():

    movies_a = os.listdir(movie_location)

    movies = movies_a
    correct = []
    regex = [r"\([0-9]+\)", r"\[.+?\]", r"[0-9]+[P|p]( +.+)?", r"\.", r"Complete.*", r"\s( [ A-Z])?[0-9]+\S.\s.+", r"\s\b(Season|SEASON|season)\b.+",
             r"\s\b[0-9]{4}\b.+", r"NetFlix|HULU|Amazon Prime", r"S[0-9]{2}.+", r"(SD|HD|Remastered|Full|REMASTERED).+"]
    for movie in movies:
        for reg in regex:
            movie = re.sub(reg, " ", movie)

        correct.append(movie.strip())

    correct_set = set(correct)
    corrected = list(correct_set)
    corrected.sort()
    return corrected
