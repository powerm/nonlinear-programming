from EuclideanSpace import EuclideanSpace
from SimplexMethod import SimplexMethod
from HookeAndJeevesMethod import HookeAndJeevesMethod
from SteepestDescentGradientMethod import SteepestDescentGradientMethod
from FletcherAndReevesMethod import FletcherAndReevesMethod
# from DavidonFletcherPowellMethod import DavidonFletcherPowellMethod
from OneDimensionalNewtonMethod import OneDimensionalNewtonMethod
from NewtonMethod import NewtonMethod
from Method import Method

class Solver():

    def __init__( self ):

        self.epsilon = Method.epsilon
        
        self.initialPoint = None

        self.previousPoint = None

        self.currentPoint = None

        self.dimension = 2
        
        self.methodName = None

        self.method = None

        self.objectiveFunction = None

        self.iterations = 0

        self.maxNumberOfIterations = Method.maxNumberOfIterations

    def setInitialPoint( self, initialPoint ):

        self.initialPoint = initialPoint

        self.previousPoint = initialPoint

        self.currentPoint = initialPoint

    def setEpsilon( self, epsilon ):

        self.epsilon = epsilon

    def setObjectiveFunction( self, objectiveFunction ):
        
        self.objectiveFunction = objectiveFunction        

    def setMaxNumberOfIterations( self, maxNumberOfIterations ):

        self.maxNumberOfIterations = maxNumberOfIterations

    def setMethod( self, methodName ):
        
        self.methodName = methodName

    def getSolution( self ):

        return self.method.getSolution();

    def getTotalOfIterations( self ):

        return self.method.getIterationCounter()

    def initialize(self):

        # Reset the total iterations performed

        self.iterations = 0
        
        if self.methodName == 'Simplex' :
            
            self.method = SimplexMethod()
        
        elif self.methodName == 'HookeAndJeeves' :
            
            self.method = HookeAndJeevesMethod()

        elif self.methodName == 'SteepestDescentGradient' :
            
            self.method = SteepestDescentGradientMethod()

        elif self.methodName == 'FletcherAndReeves' :
            
            self.method = FletcherAndReevesMethod()

        elif self.methodName == 'Newton' :
            
            self.method = NewtonMethod()

        # Define the initial point

        self.method.setCurrent( self.initialPoint )

        # Define the objective function

        self.method.setObjectiveFunction( self.objectiveFunction )

        if self.methodName == 'Simplex' :

            self.method.initializeSimplex()

        # Setup Line Search Method if the Method Requires

        if self.method.isLinearOptimizationRequired() == True :

            self.linearOptmizationMethod = OneDimensionalNewtonMethod()
            self.linearOptmizationMethod.setFunction( self.objectiveFunction )
            self.linearOptmizationMaxIterations = 20

            self.method.setLinearOptimizationMethod( self.linearOptmizationMethod )

    def solve( self ):

        self.initialize()

        if self.initialPoint == None :
            
            raise BaseException("Initial Point not defined.")

        if self.method.objectiveFunction == None :
            
            raise BaseException("Objective Function not defined.")

        while self.iterations < self.maxNumberOfIterations :

            self.method.iteration()
            
            self.iterations = self.iterations + 1

            if( self.method.stopCondition() < self.epsilon ):
                
                break

        return self.method.getSolution();

