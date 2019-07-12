class Derivative():

    def __init__( self, n = 1, dx = 0.001 ):
        
        self.n = n
        self.function = None
        self.dx = dx

    def derivative( self, x ) :
        
        if self.n == 1 :

            return ( self.function( x + self.dx ) - self.function( x - self.dx ) ) / ( 2 * self.dx )

        elif self.n == 2 :

            return ( self.function( x + self.dx ) - ( 2 * self.function( x ) ) + self.function( x - self.dx ) ) / ( self.dx ** 2 )

    def setFunction( self, function ):

        self.function = function


    