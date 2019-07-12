from EuclideanSpace import EuclideanSpace

class GradientNormStopCondition():

    def __init__( self ):
        pass

    def stopCondition( self, gradient ):
        
        return EuclideanSpace.norm( gradient )