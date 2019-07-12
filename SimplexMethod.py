from Method import Method
from EuclideanSpace import EuclideanSpace
from DifferenceNormStopCondition import DifferenceNormStopCondition

class SimplexMethod( Method ):

    def __init__( self ):

        super().__init__()

        self.alpha = 1
        self.beta = 2
        self.gamma = 0.5
        self.theta = 0.5

        self.dimension = 2
        self.vertices = self.dimension + 1

        self.gList = [ 0 for i in range( self.vertices ) ]

        self.stopConditionMethod = DifferenceNormStopCondition()

    def initializeSimplex( self ):

        self.simplex = [ self.current, 
                        [ self.current[ 0 ] + 0.5, self.current[ 1 ] ], 
                        [ self.current[ 0 ], self.current[ 1 ] + 0.5 ] ]

    def iteration(self):

        shrink = False

        for i in range( self.vertices ):

            self.gList[ i ] = self.g( self.simplex[i] )

        # Sort

        for i in range( self.vertices ):

            for j in range( self.vertices ):

                if self.gList[ i ] < self.gList[ j ] :

                    gTemp = self.gList[ i ]

                    self.gList[ i ] = self.gList[ j ]
                    
                    self.gList[ j ] = gTemp

                    simplexTemp = self.simplex[ i ]

                    self.simplex[ i ] = self.simplex[ j ]
                    
                    self.simplex[ j ] = simplexTemp

        self.previous = self.simplex[ 0 ].copy()

        # The best point of simplex

        xB = self.simplex[ 0 ]

        # The point before of the worst

        xG = self.simplex[ self.dimension - 1 ]

        # The wrost point

        xW = self.simplex[ self.vertices - 1 ]

        centroid = [ 0, 0 ]

        for i in range( self.dimension ):

            centroid[ 0 ] = centroid[ 0 ] + self.simplex[ i ][ 0 ]
            centroid[ 1 ] = centroid[ 1 ] + self.simplex[ i ][ 1 ]

        centroid[ 0 ] = centroid [ 0 ] / self.dimension
        centroid[ 1 ] = centroid [ 1 ] / self.dimension

        xR = [ 0 for i in range( self.dimension ) ]
        xE = [ 0 for i in range( self.dimension ) ]
        xC = [ 0 for i in range( self.dimension ) ]
        xS = [ 0 for i in range( self.dimension ) ]

        fXr = self.g( xR )

        for i in range( self.dimension ):

            xR[ i ] = centroid[ i ] + self.alpha * ( centroid[ i ] - xW[ i ] )

        if self.g( xB ) <= self.g( xR ) and self.g( xR ) < self.g( xW ) :

            self.simplex[ self.vertices - 1 ] = xR

        elif self.g( xR ) < self.g( xB ) :

            for i in range( self.dimension ):

                xE[ i ] = centroid[ i ] + self.beta * ( xR[ i ] - centroid[ i ] )

            if self.g( xE ) < self.g( xR ) :

                self.simplex[ self.vertices - 1 ] = xE

            else :

                self.simplex[ self.vertices - 1 ] = xR

        else:

            for i in range( self.dimension ):

                xC[ i ] = centroid[ i ] + self.gamma * ( xW[ i ] - centroid[ i ] )

            if self.g( xC ) < self.g( xW ) :

                self.simplex[ self.vertices - 1 ] = xC

            else:

                shrink = True
                
                # Do a Shrink

                for j in range( 1 , self.vertices ):
                    
                    for j in range( self.dimension ):
                        
                        xS[ i ] = xB[ i ] + self.theta * ( self.simplex[ j ][ i ] - xB[ i ] )

        if shrink == False :

            self.current = self.simplex[ 1 ]

        else :

            self.current = xB

        self.iterationCounter = self.iterationCounter + 1

    def stopCondition( self ):

        return self.stopConditionMethod.stopCondition( self.current, self.previous )

    def g( self, point ):

        return self.objectiveFunction( point[0], point[1] )

    def getSolution( self ):
        
        return self.current

    def isLinearOptimizationRequired( self ):

        return False