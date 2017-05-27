# Nim
A Python3 program to find the period, preperiod, and P-positions for a given Nim ruleset 
(expressed as a quartenary code) in a given number of dimensions.

This program was written by [Leland Williams](https://lelandwilliams.github.io/)
, as part of his Senior Project in Mathematics at the University of Minnesota.
It implements the algorithm by [Mike Weimerskich](http://www-users.math.umn.edu/~weim0024/),
as described in [his paper](http://library.msri.org/books/Book63/files/131106-Weimerskirch.pdf)

## Example Session
To use the program interactively, open a terminal, enter the directory where the code is and type `./Nim, then simply follow the prompts. Here's an example:
```
$ ./Nim 
Do you wish to run this program interactively (y = yes) y
Number of Dimensions: 4
Quartenary Move Code (or just push enter for regular (1/3) Nim) 
(M)isere or (N)ormal Play N
Play:           Standard Play
Period:         (None, 2, 2, 2, 2)
Preperiod:      (None, 0, 0, 0, 0)
Moves:          (None, -1, 0, 0, 0), (None, 1, -1, 0, 0), 
                (None, 0, 1, -1, 0), (None, 0, 0, 1, -1), 
                (None, 0, -1, 0, 0), (None, 1, 0, -1, 0), 
                (None, 0, 1, 0, -1), (None, 0, 0, -1, 0), 
                (None, 1, 0, 0, -1), (None, 0, 0, 0, -1)
Rectangle:      (None, 2, 2, 2, 2)

               x_4 = 0                
x3 = 0  x1 = 0 1   x3 = 1  x1 = 0 1   
x2 = 0       P N                N N 
x2 = 1       N N                N P 

               x_4 = 1                
x3 = 0  x1 = 0 1   x3 = 1  x1 = 0 1   
x2 = 0       N N                N N 
x2 = 1       N N                N N 


```
