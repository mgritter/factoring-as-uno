import networkx as nx
import widgets
import cnftools

with open( "factor19x37_3sat.dimacs", "r") as file:
    numLiterals, numClauses, clauses = cnftools.load( file )
    # Load into memory so we can exit this scope
    clauses = list( clauses )

variable_xor_edges = { x : [] for x in range( 1, numLiterals + 1 ) }
inverted_xor_edges = { x : [] for x in range( 1, numLiterals + 1 ) }

g = nx.Graph()
g.graph['next_id'] = 0

clause_string = []

for i, clause in enumerate( clauses ):
    if len( clause ) > 3:
        raise Exception( "3SAT only" )
    elif len( clause ) == 2:
        clause = clause + [ clause[0] ]
    elif len( clause ) == 1:
        clause = clause + [ clause[0], clause[0] ]

    
    # Two nodes for each term, "a" and "b"
    # They are connected by a triple-OR on one side,
    # and an XOR with the variable on the other
    base_name = "cl" + str(i) + "_"
    nodes = [ base_name + "1a", base_name + "1b",
              base_name + "2a", base_name + "2b",
              base_name + "3a", base_name + "3b" ]
    virtual_edges = [ ( nodes[0], nodes[1] ),
                      ( nodes[2], nodes[3] ),
                      ( nodes[4], nodes[5] ) ]
    
    widgets.add_triple_or( g, 
                           nodes[0], nodes[1],
                           nodes[2], nodes[3],
                           nodes[4], nodes[5] )

    if len( clause_string ) > 0:
        g.add_edge( clause_string[-1], nodes[0] )
    g.add_edge( nodes[1], nodes[2] )
    g.add_edge( nodes[3], nodes[4] )
    clause_string.extend( nodes )

    for literal, (a,b)  in zip( clause, virtual_edges ):
        (v1,v2,u1,u2) = widgets.add_xor_free( g )
        g.add_edge( a, v1 )
        g.add_edge( v2, b )
        
        if literal > 0:
            variable_xor_edges[literal].append( (u1, u2 ) )
        else:
            inverted_xor_edges[-literal].append( (u1, u2) )

variable_string = []

for literal in range( 1, numLiterals + 1 ):
    base_name = "x" + str(literal) + "_"

    # Two nodes for "x" and two for "not-x", connected
    # with an XOR on one side, and the XORs to the clause edges
    # on the other.
    nodes = [ base_name + "ta", base_name + "tb",
              base_name + "fa", base_name + "fb" ]
    if len( variable_string ) > 0:
        g.add_edge( variable_string[-1], nodes[0] )

    variable_string.extend( nodes )
    g.add_edge( nodes[1], nodes[2] )
    widgets.add_xor( g,
                     nodes[0], nodes[1],
                     nodes[2], nodes[3] )
    
    true_edges = variable_xor_edges[literal]
    if len( true_edges ) == 0:
        g.add_edge( nodes[0], nodes[1] )
    else:
        prev = nodes[0]
        for (a,b) in true_edges:
            g.add_edge( prev, a )
            prev = b
        g.add_edge( prev, nodes[1] )

    false_edges = inverted_xor_edges[literal]
    if len( false_edges ) == 0:
        g.add_edge( nodes[2], nodes[3] )
    else:
        prev = nodes[2]
        for (a,b) in false_edges:
            g.add_edge( prev, a )
            prev = b
        g.add_edge( prev, nodes[3] )

# Final connections, paper uses an OR but that is to preserve 3-connectivity
# which we don't care about.

g.add_edge( variable_string[0], clause_string[0] )
g.add_edge( variable_string[-1], clause_string[-1] )

for n in g.nodes():
    if g.degree( n ) != 3:
        print( "bad node:", n, g.degree( n ) )
        break

#print( len( g.nodes() ), "nodes")
#print( len( g.edges() ), "edges")

#ag = nx.drawing.nx_agraph.to_agraph( g )
#ag.write( "mult-undirected.dot" )

next_color = 0
next_number = 0

colors = {}
numbers = {}

print( "<html><head></head><body>" )
for n in g.nodes():
    for e in g.edges( nbunch=n ):
        #print( "node", n, "edge", e )
        if n in colors:
            color = colors[n]
        else:
            color = "#{:06X}".format( next_color )
            next_color = next_color + 1
            colors[n] = color
        (s,t) = e
        if (s,t) in numbers:
            number =  numbers[(s,t)]
        elif (t,s) in numbers:
            number =  numbers[(t,s)]            
        else:
            number = next_number
            next_number = next_number + 1
            numbers[e] = number
            
        print ('<span style="color: {0}">{1}</span>'.format( color, number) )

print( "</body></html>" )

