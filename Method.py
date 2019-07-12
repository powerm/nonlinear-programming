from abc import ABC as AbstractClass
from abc import abstractclassmethod

class Method( AbstractClass ):

    epsilon = 10e-10
    maxNumberOfIterations = 100

    def __init__(self):

        self.dimension = 2
        
        self.objectiveFunction = None
        
        self.current = None

        self.solution = None

        self.stopConditionMethod = None

        self.iterationCounter = 0

    def setObjectiveFunction( self, objectiveFunction ):
        
        self.objectiveFunction = objectiveFunction

    def setCurrent( self, current ):
        
        self.current = current

    def getIterationCounter(self):
        
        return self.iterationCounter
        
    def getSolution( self ):
        
        return self.solution

    def setDimension( self, dimension ):
        
        self.dimension = dimension

    @abstractclassmethod
    def iteration():
        pass;

    @abstractclassmethod
    def stopCondition():
        pass

    @abstractclassmethod
    def isLinearOptimizationRequired():
        pass