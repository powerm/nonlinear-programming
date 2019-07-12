from Method import Method
from GradientNormStopCondition import GradientNormStopCondition
from PartialDerivative import PartialDerivative
from Matrix import Matrix

class NewtonMethod( Method ):

    def __init__( self ):
        
        super().__init__()
        
        self.dimension = 2

        self.solution = None
        self.direction = Matrix( [ [ 1 ], [ 1 ] ] )
        self.gradient = Matrix([ [ 1 ], [ 1 ] ])

        self.hessian = Matrix( [ [ 1 , 1 ], 
                                 [ 1 , 1 ] ] )

        self.current = None
        self.previous = None
        self.linearOptimizationMethod = None

        self.partialDerivative = PartialDerivative()

        self.stopConditionMethod = GradientNormStopCondition()

    def iteration( self ):

        self.previous = self.current.copy()

        self.gradient = Matrix([ [ self.partialDerivative.derivative( self.current[0], self.current[ 1 ], 1, 1 ) ],
                                 [ self.partialDerivative.derivative( self.current[0], self.current[ 1 ], 2, 1 ) ] ] )
        
        self.hessian = Matrix( [ [ self.partialDerivative.derivative( self.current[0], self.current[ 1 ], 1, 2 ) , self.partialDerivative.derivative( self.current[ 0 ], self.current[ 1 ], 3, 2 ) ], 
                                 [ self.partialDerivative.derivative( self.current[0], self.current[ 1 ], 3, 2 ) , self.partialDerivative.derivative( self.current[ 0 ], self.current[ 1 ], 2, 2 ) ] ] )

        # print(self.hessian.asArray())

        self.direction = -1 * self.gradient 
                
        self.direction = self.hessian.inverse() * self.direction

        for i in range( self.dimension ) :

            self.current[ i ] = self.current[ i ] + self.direction.transpose().asArray()[ 0 ][ i ]
        
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
        
        return self.stopConditionMethod.stopCondition( self.gradient.transpose().asArray()[ 0 ] )

    def isLinearOptimizationRequired( self ):
        return False

        
        