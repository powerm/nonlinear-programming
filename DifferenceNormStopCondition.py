from EuclideanSpace import EuclideanSpace

class DifferenceNormStopCondition():

    def __init__( self ):
        pass

    def stopCondition( self, current, previous ):
        
        diff = [ current[ 0 ] - previous[ 0 ], current[ 1 ] - previous[ 1 ] ]

        return EuclideanSpace.norm( diff )