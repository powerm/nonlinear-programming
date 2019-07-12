import numpy as np

class Matrix:

    def __init__( self, matrix ):
        
        self.matrix = matrix
        self.totalOfRows = len( self.matrix )

        if self.totalOfRows > 0 :
            self.totalOfColumns = len( self.matrix[0] )

    def __add__( self, anotherMatrix ):

        if isinstance( anotherMatrix, Matrix ) :

            if ( self.totalOfRows == anotherMatrix.totalOfRows ) and ( self.totalOfColumns == anotherMatrix.totalOfColumns ) :

                result = [ [ None for i in range( self.totalOfColumns ) ] for i in range( self.totalOfRows ) ]
                
                result = Matrix( result )

                for i in range( self.totalOfRows ):
                    
                    for j in range( self.totalOfColumns ):
                        
                        result[ i ][ j ] = self.matrix[ i ][ j ] + anotherMatrix[ i ][ j ]

        elif isinstance( anotherMatrix, ( int, float ) ) :

            result = [ [ None for i in range( self.totalOfColumns ) ] for i in range( self.totalOfRows ) ]
            
            result = Matrix( result )

            for i in range( self.totalOfRows ):
                
                for j in range( self.totalOfColumns ):
                    
                    result[ i ][ j ] = self.matrix[ i ][ j ] + anotherMatrix


        return result

    def __radd__( self, anotherMatrix ):

        if isinstance( anotherMatrix, ( int, float ) ) :

            result = [ [ None for i in range( self.totalOfColumns ) ] for i in range( self.totalOfRows ) ]
            
            result = Matrix( result )

            for i in range( self.totalOfRows ):
                
                for j in range( self.totalOfColumns ):
                    
                    result[ i ][ j ] = self.matrix[ i ][ j ] + anotherMatrix

        return result

    def __mul__( self, anotherMatrix ):
        
        if isinstance( anotherMatrix, Matrix ) :
        
            if ( self.totalOfColumns == anotherMatrix.totalOfRows ) :

                result = [ [ 0 for n in range( anotherMatrix.totalOfColumns ) ] for m in range( self.totalOfRows ) ]
                
                result = Matrix( result )

                for mm in range( self.totalOfRows ):
                    
                    for nn in range( anotherMatrix.totalOfColumns ):
                            
                        for m in range( anotherMatrix.totalOfRows ):
                            
                            result[ mm ][ nn ] = result[ mm ][ nn ] + ( self.matrix[ mm ][ m ] * anotherMatrix[ m ][ nn ] )

                return result

            else:
                
                raise BaseException("Incompatible Dimensions")

        elif isinstance( anotherMatrix, ( int, float ) ) :

            return self.scalarByMatrix( anotherMatrix )

        else:

            raise BaseException("Incompatible Types")

    """
    Define right-side multiplication
    """
    def __rmul__( self, value ):

        if isinstance( value, ( int, float ) ) :

            return self.scalarByMatrix( value )

        else:

            raise BaseException("Incompatible Types")

    def scalarByMatrix( self, scalar ) :

        result = [ [ self.matrix[ m ][ n ] for n in range( self.totalOfColumns ) ] for m in range( self.totalOfRows ) ]

        result = Matrix( result )

        for mm in range( self.totalOfRows ):
                
            for nn in range( self.totalOfColumns ):
                        
                result[ mm ][ nn ] = scalar*result[ mm ][ nn ]

        return result

    def __getitem__( self, i ):
        
        return self.matrix[ i ]

    def asArray( self ):

        return self.matrix

    def transpose( self ):

        result = [ [ self.matrix[ n ][ m ] for n in range( self.totalOfRows ) ] for m in range( self.totalOfColumns ) ]

        result = Matrix( result )

        return result

    def inverse( self ):

        result = np.linalg.inv( self.matrix )

        result = [ [ result[ m ][ n ] for n in range( self.totalOfRows ) ] for m in range( self.totalOfColumns ) ]

        result = Matrix( result )

        return result
