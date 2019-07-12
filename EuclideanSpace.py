"""
This Class represents the Euclidean Space
"""

from math import sqrt
from Space import Space

class EuclideanSpace( Space ):

    @staticmethod
    def norm( vector ):

        sumOfSquares = 0

        for i in range( len(vector) ) :

            sumOfSquares = sumOfSquares + vector[ i ] ** 2

        return sqrt( sumOfSquares )