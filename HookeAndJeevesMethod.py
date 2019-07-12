from Method import Method
from DifferenceNormStopCondition import DifferenceNormStopCondition

class HookeAndJeevesMethod( Method ):

    def __init__( self ):
        
        super().__init__()
        
        self.dimension = 2

        self.solution = None
        self.direction = [ [ 1 if i == j else 0 for i in range( self.dimension ) ] for j in range( self.dimension ) ]
        self.current = None
        self.previous = None
        self.linearOptimizationMethod = None

        self.stopConditionMethod = DifferenceNormStopCondition()

    def iteration( self ):
        
        for j in range( self.dimension ) :
    
            for i in range( self.dimension ) :
        
                self.previous = self.current.copy()

                self.linearOptimizationMethod.setCurrent( self.current )
                
                if j == 0 :

                    self.linearOptimizationMethod.setDirection( [1,0] )

                else:
                    self.linearOptimizationMethod.setDirection( [0,1] )

                optimumSolution = self.linearOptimizationMethod.optimize( self.current[ j ] )

                self.current[ i ] = self.current[ i ] + optimumSolution * self.direction[ j ][ i ]
        
        self.linearOptimizationMethod.setCurrent( self.current )

        self.solution = self.current

        self.iterationCounter = self.iterationCounter + 1
                
    def setObjectiveFunction( self, objectiveFunction ):
        
        self.objectiveFunction = objectiveFunction

    def getSolution( self ):
        
        return self.solution

    def setLinearOptimizationMethod( self, linearOptimizationMethod ):
        
        self.linearOptimizationMethod = linearOptimizationMethod
        self.linearOptimizationMethod.setCurrent( self.current )
        self.linearOptimizationMethod.setDirection( self.direction )
        self.linearOptimizationMethod.setFunction( self.objectiveFunction )

    def stopCondition( self ):

        return self.stopConditionMethod.stopCondition( self.current, self.previous )

    def isLinearOptimizationRequired( self ):
        return True

        
        