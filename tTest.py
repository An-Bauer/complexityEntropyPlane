#%%
import numpy as np
from scipy import stats
import networkx as nx
import matplotlib.pyplot as plt

import numerical as nm
import analytical as an

# %%

path = "sheep.txt"  
#path = "rhesus.txt"  

G = nx.read_edgelist(f"graphs/{path}")
A = nx.to_numpy_array(G)
n = G.number_of_nodes()
e = G.number_of_edges()

p = e*2/n/(n-1)
k = np.sum(A,axis=0) # degrees
d = np.sum(k[:, None] == np.arange(n),axis=0) # degree dist

s = np.dot(an.S(n),d)
q = np.dot(an.Q(n,p),d)

#%%
m = 1000
sample = [nm.Q(G)*s for _ in range(m)]

t_stat, p_value = stats.ttest_1samp(sample, popmean=q)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: the mean is statistically different")
else:
    print("Fail to reject the null hypothesis: no evidence that the mean differs")

# %%
plt.hist(sample,density=True,bins=30)
plt.plot([s*q,s*q],[0,10],"--")

# %%
np.dot(an.Q(n,p),d)*s,sum(sample)/m
# %%
n

# %%
