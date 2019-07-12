from Solver import Solver

solver = Solver()

def objectiveFunction( x,y ):
    
    return ( x - 2 )**4 + ( x - 2 * y )**2

solver.setObjectiveFunction( objectiveFunction )

solver.setInitialPoint( [ 0, 3 ] )

# solver.setMethod( 'Simplex' )
# solver.setMethod( 'SteepestDescentGradient' )
# solver.setMethod( 'HookeAndJeeves' )
# solver.setMethod( 'FletcherAndReeves' )
solver.setMethod( 'Newton' )

solver.setMaxNumberOfIterations( 100 )

solver.setEpsilon( 10e-10 )

solver.solve()

solution = solver.getSolution()

print( "\nTotal of Iterations: {}\n".format( solver.getTotalOfIterations() ) )

print( "Solution: ( {} ; {} )\n".format( solution[0], solution[1] ) )

print( "Objective Function at ( {} ; {} ): {}\n".format( round( solution[0], 2 ) , round( solution[1], 2 ), objectiveFunction( solution[0], solution[1] ) )  )
