#!/usr/bin/env python3

from movie import Movie


class MovieBox(Movie):

    def __init__(self, title, movies):

        if len(movies) == 0 or not all(isinstance(child, Movie) for child in movies) or not title:
            raise Warning("Invalid input parameters")

        self.__title = title
        self.__movies = movies

    def __repr__(self):
        representation = f"MovieBox(\"{self.get_title()}\", {self.get_movies()})"
        return representation.replace("'", "\"")

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return self.get_title() == other.get_title() and self.get_movies() == other.get_movies()

    def __iter__(self):
        return list(self.__movies).__iter__()

    def get_title(self):
        return self.__title

    def get_actors(self):
        actor_list = []
        for movie in self.__movies:
            actor_list.extend(movie.get_actors())
        return list(set(actor_list))

    def get_duration(self):
        total_duration = 0
        for movie in self.__movies:
            total_duration += movie.get_duration()
        return total_duration

    def get_movies(self):
        all_movies = []
        for movie in self.__movies:
            all_movies.append(movie)
        return sorted(all_movies)

    # also implement the required special functions
