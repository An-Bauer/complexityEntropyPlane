#%%
import networkx as nx
import numpy as np

from scipy.spatial.distance import jensenshannon
from scipy.stats import entropy

#%%
def grapToProbMatrix(G):
    r = np.vectorize(lambda x: 1/x if x != 0 else 0.) # inverse

    A = nx.to_numpy_array(G)
    k = np.sum(A,axis=0)
    return r(A*k)

def S(G):
    n = G.number_of_nodes()
    P = grapToProbMatrix(G)

    return (sum([entropy(P[:,i]) for i in range(n)])/n)/np.log(n)

def Q(G):
    n = G.number_of_nodes()
    e = G.number_of_edges()
    P = grapToProbMatrix(G)
    R = grapToProbMatrix(nx.erdos_renyi_graph(n,e*2/n/(n-1)))

    return (sum([(jensenshannon(R[:,i],P[:,i])**2) for i in range(n)])/n)/np.log(2)
#%%

path = "sheep.txt"  
#path = "rhesus.txt"  

G = nx.read_edgelist(f"graphs/{path}")
n = G.number_of_nodes()
e = G.number_of_edges()

m = 1000
print(f"n: {n}")
print(f"p: {e*2/n/(n-1)}")
print(f"S: {S(G)}")
print(f"C: {(sum([Q(G) for _ in range(m)])/m)*S(G)}")
# %%
