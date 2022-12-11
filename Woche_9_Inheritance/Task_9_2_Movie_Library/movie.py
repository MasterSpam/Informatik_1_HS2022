#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):

        if not title or not actors or duration < 1:
            raise Warning("Invalid Input! Please Check again")

        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def __repr__(self):
        representation = f"Movie(\"{self.get_title()}\", {self.get_actors()}, {self.get_duration()})"
        return representation.replace("'", "\"")

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return self.__title == other.__title and self.__actors == other.__actors and self.__duration == other.__duration

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors[:]

    def get_duration(self):
        return self.__duration

    def __lt__(self, other):
        if isinstance(other, Movie):
            return self.__title < other.__title or self.__duration < other.__duration or self.__actors < other.__actors
        return False
    # also implement the required special functions
