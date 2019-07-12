from Method import Method
from Derivative import Derivative

class OneDimensionalNewtonMethod():

    def __init__( self , function = None ):

        self.epsilon = Method.epsilon
        
        self.maxIterations = 150
        
        self.function = function

        self.firstDerivative = Derivative( n = 1, dx = 0.00001 )
        
        self.secondDerivative = Derivative( n = 2, dx = 0.00001 )

        self.current = [ 0 , 3 ]

        self.direction = [ 0 , 3 ]

    def setCurrent( self, current ):
        
        self.current = current

    def setDirection( self, direction ):
        
        self.direction = direction

    def optimize( self, x ) :

        self.firstDerivative.setFunction( self.functionToOptimize() )
        self.secondDerivative.setFunction( self.functionToOptimize() )

        for k in range( self.maxIterations ) :
            
            p = x
            
            try:
                
                x = x - ( self.firstDerivative.derivative( x ) / self.secondDerivative.derivative( x ) )

            except ZeroDivisionError as error:
                
                return x

            e = x - p

            if e < 0 :

                e = e * - 1

            if e < self.epsilon :
                
                break

        return x

    def functionToOptimize( self ):

        def f( x ):

            return self.function( self.current[0] + ( self.direction[ 0 ] * x ), self.current[1] + ( self.direction[ 1 ] * x ) )

        return f
        
    def setFunction( self, function ):
        
        self.function = function

    def setFirstDerivative( self, firstDerivative ):

        self.firstDerivative = firstDerivative

    def setSecondDerivative( self, secondDerivative ):

        self.secondDerivative = secondDerivative
