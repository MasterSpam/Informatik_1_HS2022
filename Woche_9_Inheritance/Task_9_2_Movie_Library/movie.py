#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def __repr__(self):
        return f"Movie({self.get_title()}, {self.get_actors()}, {self.get_duration()})"

    def get_title(self):
        pass

    def get_actors(self):
        pass

    def get_duration(self):
        pass

    # also implement the required special functions
