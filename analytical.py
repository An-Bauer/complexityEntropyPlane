#%%
import networkx as nx
import numpy as np
from scipy.special import comb

#%%

def S(n):
    v = np.zeros(n)
    v[1:] = np.log(np.arange(1,n))
    return v/n/np.log(n) # not n-1 ?

def Q(n,pp):
    i = np.arange(1,n) # indices

    p = pp**i*(1-pp)**(n-1-i)*comb(n-2,i-1) # ref entry prob
    p0 = (1-pp) 

    v1 = np.zeros(n) # S((P+R)/2)
    v1[1:] += -(n-1-i)*np.sum(p[:,None]/2/i[:,None]*np.log(1/2/i[:,None]),axis=0) 
    v1[1:] += -(i)*(p0/2/i*np.log(1/2/i)+np.sum(p[:,None]*(1/2/i+1/2/i[:,None])*np.log(1/2/i+1/2/i[:,None]),axis=0))
    v1[0] = -(n-1)*np.sum(p/2/i*np.log(1/2/i)) 

    v2 = np.zeros(n) # S(P)
    v2[1:] = np.log(i)

    v3 = np.ones(n)*-(n-1)*np.sum(p/i*np.log(1/i)) # S(R)

    return (v1-v2/2-v3/2)/n/np.log(2)


# %%

path = "sheep.txt"  
#path = "rhesus.txt"  

G = nx.read_edgelist(f"graphs/{path}")
A = nx.to_numpy_array(G)

n = G.number_of_nodes()
e = G.number_of_edges()

k = np.sum(A,axis=0) # degrees
d = np.sum(k[:, None] == np.arange(n),axis=0) # degree dist
p = e*2/n/(n-1)

print(f"n: {n}")
print(f"p: {p}")
print(f"S: {np.dot(S(n),d)}")
print(f"C: {np.dot(S(n),d)*np.dot(Q(n,p),d)}")

# %%
Q(28,1)

# %%
