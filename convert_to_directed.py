import cnftools
import networkx as nx

with open( "factor19x37.dimacs", "r") as file:
    numLiterals, numClauses, clauses = cnftools.load( file )
    # Load into memory so we can exit this scope
    clauses = list( clauses )

variables_to_clauses = { x : set() for x in range( 1, numLiterals + 1 ) }

for i, clause in enumerate( clauses ):
    for l in clause:
        var = abs( l )
        variables_to_clauses[var].add( i )

#print( variables_to_clauses )

g = nx.DiGraph()

# A row of nodes for each variable, with one edge for
# each clause it appears in.
# "right" is true, "left" is false
for v in range( 1, numLiterals + 1 ):
    start = "x_" + str(v) + "_true"
    end = "x_" + str(v) + "_false"
    inClauses = variables_to_clauses[v]
    intermediate = [ "x_" + str(v) + "_" + str(i)
                     for i in range( 1, len( inClauses ) ) ]
    row = [start] + intermediate + [end]
    for a,b in zip( row, row[1:] ):
        g.add_edge( a, b )
        g.add_edge( b, a )
        
    for i, c_i in enumerate( inClauses ):
        node = "clause_" + str(c_i)
        if v in clauses[c_i]:
            g.add_edge( row[i], node )
            g.add_edge( node, row[i+1] )
        elif -v in clauses[c_i]:
            g.add_edge( row[i+1], node )
            g.add_edge( node, row[i] )
        else:
            raise Exception("variable absent in clause")

g.add_edge( "s", "x_1_true")
g.add_edge( "s", "x_1_false")

for v in range( 1, numLiterals ):
    t1 = "x_" + str(v) + "_true"
    f1 = "x_" + str(v) + "_false"
    t2 = "x_" + str(v+1) + "_true"
    f2 = "x_" + str(v+1) + "_false"
    g.add_edge( t1, t2 )
    g.add_edge( t1, f2 )
    g.add_edge( f1, t2 )
    g.add_edge( f1, f2 )

tLast = "x_" + str(numLiterals) + "_true"
fLast = "x_" + str(numLiterals) + "_false"
g.add_edge( tLast, "t" )
g.add_edge( fLast, "t" )
g.add_edge( "t", "s" )
        
ag = nx.drawing.nx_agraph.to_agraph( g )
ag.write( "mult.dot" )
