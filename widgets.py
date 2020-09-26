import networkx as nx

# Figure 1 in Garey et al
# Returns the outermost three vertices, so they can be connected to
# virtual edges
def add_required_edge_free( g ):
    next_id = g.graph['next_id']
    g.graph['next_id'] = next_id + 100
    a =  next_id + 1
    g.add_edge( next_id + 1, next_id + 2 )
    g.add_edge( next_id + 1, next_id + 4 )
    g.add_edge( next_id + 2, next_id + 3 )
    g.add_edge( next_id + 2, next_id + 5 )
    g.add_edge( next_id + 3, next_id + 4 )
    g.add_edge( next_id + 3, next_id + 7 )
    g.add_edge( next_id + 4, next_id + 9 )
    g.add_edge( next_id + 5, next_id + 6 )
    g.add_edge( next_id + 5, next_id + 13 )
    g.add_edge( next_id + 6, next_id + 7 )
    g.add_edge( next_id + 6, next_id + 10 )
    g.add_edge( next_id + 7, next_id + 8 )
    g.add_edge( next_id + 8, next_id + 9 )
    g.add_edge( next_id + 8, next_id + 11 )
    g.add_edge( next_id + 9, next_id + 12 )
    g.add_edge( next_id + 10, next_id + 11 )
    g.add_edge( next_id + 10, next_id + 14 )
    g.add_edge( next_id + 11, next_id + 12 )
    g.add_edge( next_id + 12, next_id + 15 )
    g.add_edge( next_id + 13, next_id + 14 )
    b = next_id + 13
    g.add_edge( next_id + 14, next_id + 15 )
    c = next_id + 15
    return (a,b,c)

def add_required_edge( g, a, b, c ):
    a_prime, b_prime, c_prime = add_required_edge_free( g )
    g.add_edge( a, a_prime )
    g.add_edge( b, b_prime )
    g.add_edge( c, c_prime )

# Figure 2 in Garey et al
def add_xor( g, v1, v2, u1, u2 ):
    next_id = g.graph['next_id']
    g.graph['next_id'] = next_id + 100
    g.add_edge( v1, next_id + 1 )
    g.add_edge( next_id + 1, next_id + 2 )
    g.add_edge( next_id + 2, next_id + 3 )
    g.add_edge( next_id + 2, next_id + 5 )
    g.add_edge( next_id + 3, next_id + 4 )
    g.add_edge( next_id + 3, next_id + 6 )
    g.add_edge( next_id + 4, v2 )
    add_required_edge( g, next_id + 1, u1, next_id + 5 )
    g.add_edge( next_id + 5, next_id + 6 )
    add_required_edge( g, next_id + 4, next_id + 6, u2 )

# As above, but exponse v1, v2, u1, u2 as vertices
# upon which virtual edges can be connected.
def add_xor_free( g ):
    next_id = g.graph['next_id']
    g.graph['next_id'] = next_id + 100
    v1 = next_id + 1
    g.add_edge( next_id + 1, next_id + 2 )
    g.add_edge( next_id + 2, next_id + 3 )
    g.add_edge( next_id + 3, next_id + 4 )
    v2 = next_id + 4
    g.add_edge( next_id + 2, next_id + 5 )
    g.add_edge( next_id + 3, next_id + 6 )
    a1,b1,c1 = add_required_edge_free( g )
    a2,b2,c2 = add_required_edge_free( g )
    u1 = b1
    u2 = c2
    g.add_edge( a1, next_id + 1 )
    g.add_edge( a2, next_id + 4 )
    g.add_edge( c1, next_id + 5 )
    g.add_edge( next_id + 5, next_id + 6 )
    g.add_edge( next_id + 6, b2 )
    return (v1,v2,u1,u2)
    
# Figure 5 in Garey et al
def add_or( g, v1, v2, u1, u2 ):
    next_id = g.graph['next_id']
    g.graph['next_id'] = next_id + 100
    # g.graph['next_id'] = next_id + 11
    g.add_edge( v1, next_id + 1 )
    g.add_edge( next_id + 1, next_id + 2 )
    g.add_edge( next_id + 2, next_id + 3 )
    g.add_edge( next_id + 3, next_id + 4 )
    g.add_edge( next_id + 4, v2 )
    
    g.add_edge( next_id + 5, next_id + 1 )
    g.add_edge( next_id + 5, next_id + 7 )
    add_required_edge( g, next_id + 5, next_id + 2, next_id + 8 )

    g.add_edge( next_id + 6, next_id + 4 )
    g.add_edge( next_id + 6, next_id + 10 )
    add_required_edge( g, next_id + 6, next_id + 3, next_id + 9 )
    
    g.add_edge( u1, next_id + 7 )
    g.add_edge( next_id + 7, next_id + 8 )
    g.add_edge( next_id + 8, next_id + 9 )
    g.add_edge( next_id + 9, next_id + 10 )
    g.add_edge( next_id + 10, u2 )

# Returns (v1,v2,u1,u2)
def add_or_free( g ):
    next_id = g.graph['next_id']
    g.graph['next_id'] = next_id + 100
    # g.graph['next_id'] = next_id + 11
    v1 = next_id + 1
    g.add_edge( next_id + 1, next_id + 2 )
    g.add_edge( next_id + 2, next_id + 3 )
    g.add_edge( next_id + 3, next_id + 4 )
    v2 = next_id + 4
    
    g.add_edge( next_id + 5, next_id + 1 )
    g.add_edge( next_id + 5, next_id + 7 )
    add_required_edge( g, next_id + 5, next_id + 2, next_id + 8 )

    g.add_edge( next_id + 6, next_id + 4 )
    g.add_edge( next_id + 6, next_id + 10 )
    add_required_edge( g, next_id + 6, next_id + 3, next_id + 9 )
    
    u1 = next_id + 7 
    g.add_edge( next_id + 7, next_id + 8 )
    g.add_edge( next_id + 8, next_id + 9 )
    g.add_edge( next_id + 9, next_id + 10 )
    u2 = next_id + 10
    return (v1,v2,u1,u2)
    
# Figure 5 in Garey et al
# This version extends v1 and u1 but
# returns v2 and u2 instead of accepting them as arguments
def extend_or_edge( g, v1, u1 ):
    next_id = g.graph['next_id']
    g.graph['next_id'] = next_id + 100
    # g.graph['next_id'] = next_id + 11
    g.add_edge( v1, next_id + 1 )
    g.add_edge( next_id + 1, next_id + 2 )
    g.add_edge( next_id + 2, next_id + 3 )
    g.add_edge( next_id + 3, next_id + 4 )
    v2 = next_id + 4
    
    g.add_edge( next_id + 5, next_id + 1 )
    g.add_edge( next_id + 5, next_id + 7 )
    add_required_edge( g, next_id + 5, next_id + 2, next_id + 8 )

    g.add_edge( next_id + 6, next_id + 4 )
    g.add_edge( next_id + 6, next_id + 10 )
    add_required_edge( g, next_id + 6, next_id + 3, next_id + 9 )
    
    g.add_edge( u1, next_id + 7 )
    g.add_edge( next_id + 7, next_id + 8 )
    g.add_edge( next_id + 8, next_id + 9 )
    g.add_edge( next_id + 9, next_id + 10 )
    u2 = next_id + 10
    return (v2, u2)

# Figure 6 in Garey et al
def add_triple_or( g, v1, v2, w1, w2, u1, u2 ):
    n = g.graph['next_id']
    # g.graph['next_id'] = n + 28
    g.graph['next_id'] = n + 100

    # u-u'
    g.add_edge( u1, n+1 )
    g.add_edge( n+1, n+2 )
    g.add_edge( n+2, n+3 )
    add_xor( g, n+1, n+6, n+2, n+4 )
    g.add_edge( n+3, n+5 )
    g.add_edge( n+4, n+5 )    
    g.add_edge( n+4, n+7 )
    # edges 5-"8", 12-"11"
    ua, wa = extend_or_edge( g, n+5, n+12 )
    # edge "8"-"25", 18-"19"
    ub, va = extend_or_edge( g, ua, n+18 )
    g.add_edge( n+6, n+7 )
    add_required_edge( g, n+17, n+7, ub )  
    g.add_edge( u2, n+6 )
    
    # w-w'
    g.add_edge( w1, n+10 )
    g.add_edge( n+9, n+10 )
    # edge "11"-"26", and "19"-"27"
    wb, vb = extend_or_edge( g, wa, va )    
    add_required_edge( g, n+3, wb, n+9 )
    g.add_edge( n+9, n+13 )
    g.add_edge( n+12, n+13 )
    g.add_edge( n+12, n+14 )
    add_xor( g, n+13, n+15, n+10, n+16 )    
    g.add_edge( n+14, n+15 )
    g.add_edge( n+15, n+16 )
    g.add_edge( n+16, w2 )

    # v-v'
    g.add_edge( n+17, n+18 )
    add_required_edge( g, n+14, vb, n+22 )
    g.add_edge( n+17, n+20 )
    g.add_edge( n+18, n+21 )
    add_xor( g, n+23, n+24, n+20, n+21 )
    g.add_edge( n+21, n+22 )
    g.add_edge( n+20, n+23 )
    g.add_edge( n+22, n+24 )
    g.add_edge( v1, n+23 )
    g.add_edge( n+24, v2 )
            

def count_degree( g ):
    for n in g.nodes():
        if g.degree( n ) != 3:
            print( n, g.degree( n ) )
    
def testR():
    g = nx.Graph()
    g.graph['next_id'] = 1
    add_required_edge( g, "a", "b", "c" )

    g.nodes["a"]["color"] = "red"
    g.nodes["b"]["color"] = "green"
    g.nodes["c"]["color"] = "blue"

    ag = nx.drawing.nx_agraph.to_agraph( g )
    ag.write( "required.dot" )
    
    count_degree( g )
    return g

def testXOR():
    g = nx.Graph()
    g.graph['next_id'] = 1
    add_xor( g, "a1", "a2", "b1", "b2")

    g.nodes["a1"]["color"] = "red"
    g.nodes["a2"]["color"] = "red"
    g.nodes["b1"]["color"] = "green"
    g.nodes["b2"]["color"] = "green"

    ag = nx.drawing.nx_agraph.to_agraph( g )
    ag.write( "xor.dot" )
    
    count_degree( g )
    return g

def testOR():
    g = nx.Graph()
    g.graph['next_id'] = 1
    add_or( g, "a1", "a2", "b1", "b2")

    g.nodes["a1"]["color"] = "red"
    g.nodes["a2"]["color"] = "red"
    g.nodes["b1"]["color"] = "green"
    g.nodes["b2"]["color"] = "green"

    ag = nx.drawing.nx_agraph.to_agraph( g )
    ag.write( "or.dot" )
    
    count_degree( g )
    return g

def test():
    g = nx.Graph()
    g.graph['next_id'] = 1
    add_triple_or( g, "a1", "a2", "b1", "b2", "c1", "c2" )
    g.nodes["a1"]["color"] = "red"
    g.nodes["a2"]["color"] = "red"
    g.nodes["b1"]["color"] = "green"
    g.nodes["b2"]["color"] = "green"
    g.nodes["c1"]["color"] = "blue"
    g.nodes["c2"]["color"] = "blue"
    ag = nx.drawing.nx_agraph.to_agraph( g )
    ag.write( "3or.dot" )

    count_degree( g )

    return g
