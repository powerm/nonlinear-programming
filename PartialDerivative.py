class PartialDerivative():

    def __init__( self, n = 1, dx = 0.001 ):
        
        self.n = n
        self.function = None
        self.dx = dx

    def derivative( self, x, y, direction = 1, n = 1 ) :

        if n == 1 :

            if direction == 1 :

                return ( self.function( x + self.dx, y ) - self.function( x - self.dx, y ) ) / ( 2 * self.dx )

            elif direction == 2 :

                return ( self.function( x, y + self.dx ) - self.function( x, y - self.dx ) ) / ( 2 * self.dx )

            elif direction == 3 :

                return ( self.function( x + self.dx, y + self.dx ) - self.function( x - self.dx, y - self.dx ) ) / ( 2 * self.dx )

        elif n == 2 :

            if direction == 1 :

                return ( self.function( x + self.dx, y ) - ( 2 * self.function( x, y ) ) + self.function( x - self.dx, y ) ) / ( self.dx ** 2 )

            elif direction == 2 :

                return ( self.function( x, y + self.dx ) - ( 2 * self.function( x, y ) ) + self.function( x, y - self.dx ) ) / ( self.dx ** 2 )

            elif direction == 3 :

                return ( self.function( x + self.dx, y + self.dx ) - self.function( x + self.dx, y - self.dx ) - self.function( x - self.dx, y + self.dx ) + self.function( x - self.dx, y - self.dx ) ) / ( 4 * (self.dx**2) )

    def setFunction( self, function ):

        self.function = function


    