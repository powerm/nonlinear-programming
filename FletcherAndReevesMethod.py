from Method import Method
from GradientNormStopCondition import GradientNormStopCondition
from PartialDerivative import PartialDerivative
from EuclideanSpace import EuclideanSpace

class FletcherAndReevesMethod( Method ):

    def __init__( self ):

        super().__init__()

        self.dimension = 2

        self.solution = None
        self.direction = [ 1, 1 ]
        self.gradient = [ 1, 1 ]
        self.previousGradient = None
        self.current = None
        self.previous = None
        self.linearOptimizationMethod = None

        self.partialDerivative = PartialDerivative()

        self.stopConditionMethod = GradientNormStopCondition()

    def iteration( self ):

        self.previous = self.current.copy()

        self.previousGradient = self.gradient

        self.gradient = [ self.partialDerivative.derivative( self.current[0], self.current[1], 1 ),
                          self.partialDerivative.derivative( self.current[0], self.current[1], 2 ) ]

        if self.iterationCounter == 0 :

            self.direction = [ -self.gradient[0], -self.gradient[1] ]
            
        else :
            
            alpha = ( EuclideanSpace.norm( self.gradient )**2 ) / ( EuclideanSpace.norm( self.previousGradient )**2 )

            newDirection = [ -self.gradient[0] + (alpha*self.direction[0]), -self.gradient[1] + (alpha*self.direction[1]) ]

            self.direction = newDirection

        self.linearOptimizationMethod.setCurrent( self.current )
        self.linearOptimizationMethod.setDirection( self.direction )

        optimumSolution = self.linearOptimizationMethod.optimize( 0 )    

        for i in range( self.dimension ) :

            self.current[ i ] = self.current[ i ] + optimumSolution * self.direction[ i ]
        
        self.solution = self.current

        self.iterationCounter = self.iterationCounter + 1
                
    def setObjectiveFunction( self, objectiveFunction ):
        
        self.objectiveFunction = objectiveFunction

        self.partialDerivative.setFunction( self.objectiveFunction )

    def getSolution( self ):
        
        return self.solution

    def setLinearOptimizationMethod( self, linearOptimizationMethod ):
        
        self.linearOptimizationMethod = linearOptimizationMethod
        self.linearOptimizationMethod.setCurrent( self.current )
        self.linearOptimizationMethod.setDirection( self.direction )
        self.linearOptimizationMethod.setFunction( self.objectiveFunction )

    def stopCondition( self ):

        return self.stopConditionMethod.stopCondition( self.gradient )

    def isLinearOptimizationRequired( self ):
        
        return True

        
        