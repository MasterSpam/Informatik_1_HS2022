#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox


class Library():

    def __init__(self):

        self.__library = []

    def add_movie(self, movie):
        """
        adds movie or moviebox to library
        :param movie: Movie or MovieBox
        :return:
        """
        if movie not in self.__library:
            self.__library.append(movie)

    def get_movies(self):
        all_movies = []
        for movie in self.__library:
            if isinstance(movie, MovieBox):
                all_movies += self.__get_movies_unboxed(movie)
            else:
                all_movies.append(movie)
        return sorted(list(set(all_movies)), key=lambda x: x.get_title())

    def get_total_duration(self):
        total_duration = 0
        for item in self.__library:
            total_duration += item.get_duration()
        return total_duration

    def __get_movies_unboxed(self, movie_box: MovieBox):
        all_movies = []
        for movie in movie_box:
            if isinstance(movie, MovieBox):
                all_movies += self.__get_movies_unboxed(movie)
            else:
                all_movies.append(movie)
        return all_movies
