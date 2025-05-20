## Ideas for complexity

>[!NOTE]
>Das sind  meine Notizen, damit ich weiß, was ich Ihnen erzählen kann, wenn wir uns treffen.

### Paper Summary
- probability distribution for every node  (randome walker)
- $S$ <- average per node shanon entropy
- $Q$ <- average per node JSD with Erdös-Renyi as reference
- $C := E[SQ]$ <- graph complexity

### Paper Definitions
- adjacency matrix : $A_{ij}$ with $i,j \in \{1...N\}$

- probability matrix : $P_{ij} := A_{ij}/k_i$ with $k_i :=\sum_j A_{ij}$

- entrop : $S(P) := c_S \sum_{ij}P_{ij}\ln P_{ij}$ with $c_S := \frac{-1}{N \ln(N-1)}$

- probability matrix of reference graph : $R_k$ from Erdös-Renyi-Model

- Jensen-Shanon-Divergence can be shown to be equal to : $Q(P,R_k) := \frac{c_Q}{c_S} (S(\frac{P+R_k}{2})+\frac{S(P)}{2} + \frac{S(R_k)}{2})$ with $c_Q := \frac{1}{N \ln2}$

  - not obviously only degree dependent, beacuse $S(P+R_k)$ is dependent on mixing

- "complexity" : $C(P):= E[Q(P,R_k)S(P)]$ <- only dependent on degree dist

### Some Calculations
- degree distribution: $d_a $

- probability of entry $1/x$ in $R_k$ : $a_x$ ($x=0$ means entry is 0)
    - idependence, nonezero if edge exists, p * bernoulli dist
    - $a_0 = 1-p$
    - $a_x =p^x (1-p)^{N-1-x} {N-2\choose x-1}$

- $E[Q(P,R_k)]$ is big sum over $i,j$ and prob-weighted reference graphs...
- $E[S(\frac{P+R_k}{2})]$ is most interesting
  - contribution of n-1-x zeros in row
    - $(n-1-x) (p_0 0 + \sum_y p_y (\frac{1}{2y}\ln\frac{1}{2y}))$
      
  - contribution of x (1/x) entries
    - $(x)(p_0 (\frac{1}{2x}\ln\frac{1}{2x}) +  \sum_y p_y(\frac{1}{2x}+\frac{1}{2y})\ln(\frac{1}{2x}+\frac{1}{2y}))$
  - contribution of row with rank x
    - $v^1_x := (x)(p_0 (\frac{1}{2x}\ln\frac{1}{2x}) +  \sum_y p_y(\frac{1}{2x}+\frac{1}{2y}))+(n-1-x) (p_0 0 + \sum_y p_y (\frac{1}{2y}\ln\frac{1}{2y}))$

  - $S(\frac{P+R_k}{2})/c_Q = \sum_x d_x v^1_x = v^1d$

- $E[S(P)] = S(P)$ is easy, also dot prod
  - $S(P)/c_Q = \sum_x d_x (x (\frac{1}{x}\ln \frac{1}{x})+(n-1-x)0) =\sum_x d_x v^2_x = v^2d$

- $E[S(R_k)]$ can also be written as dot prod
  - $S(R_k)/c_Q =n(n-1) (p_0 0 + \sum_x p_x (\frac{1}{x}\ln\frac{1}{x})) = u$
  - $S(R_k) = \sum_x (u/n) d_x  = v^3d =  (u/n)\sum d_x = (u/n)n= u$  

- construction of special vector $v$ such that $E[Q(P,R_k)] = vd$



### Dicuss ideas
- $Q$ can be represented as scalar product of special vector $v$ and degree dist -> only dependent on degree dist, not who connects to who
- checked with sheeps and rhesus (dist and E) (they messed up n-1), why only n=100?
- counter examples same degree dist different intuitive complexity
- can allways be done if all nodes are treated the same in reference
- quote"mesures based on degree dist have little power"
- quote"so far no analytical expression found"
