#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from movie import Movie
from moviebox import MovieBox
from library import Library


a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])

l = Library()
l.add_movie(a)
l.add_movie(d)
print(l.get_movies())
print(l.get_total_duration())

a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
a2 = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])
d2 = MovieBox("Top Movies", [b, c])
# e = Movie('a', ['a'], 0)
# f = MovieBox('a', [])

l = Library()
l.add_movie(a)
l.add_movie(d)
l.add_movie(c)
l.add_movie(d2)
a.get_actors().append('sven')
d.get_actors().append('sven')
print(a.get_actors())
print(d.get_actors())
print(l.get_movies())
print(l.get_total_duration())
#
#
print(a == a2)
print(a == b)
print(d == d2)

di = {}

di[a] = 'a'
di[a] = 'new a'
di[d] = 'd'
di[d2] = 'd2'

print(di)

f = MovieBox("a", [a, b, c])
x = MovieBox("Sven", [f, a, b])
l.add_movie(x)
print(l.get_movies())
print(l.get_total_duration())

di[x] = "sven"
