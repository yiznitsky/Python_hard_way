# -*- coding: utf-8 -*-
# python the hard way, exercise 6: Strings and Text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
# %s when using a sting, %r for representation: array
hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# çççƒ©