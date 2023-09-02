# Chapter 1: Tuples
This is the full language implementation in different languages I intend to 
complete. I started a Java one, but got lost in the build system mini-game
(I wanted to do mutation testing, unit test and, of course, Cucumber 
testing, and I could not figure out how to do all three in using 
gradle or maven).

Anyway, starting the Python implementation with tuples, leveraging
Python's namedtuple. I tried to minimize the implementation. Of course,
I got suckered in with the infix overrides for arithmetic. Still,
~55 lines for all the tuple functions does not seem over done. 

Biggest design decision was to make the tuples immutable. There is no in place
updates. And, by using Python tuples, this is not really negotiable.