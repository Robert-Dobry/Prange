# Prange
Implementation of Information-set decoding with 


## Define x
x <- phi(r) * (phi(G))^-1

## Main condition
- if hwt(r + xG) <= w:
    RETURN X


## gilbert_varshamov_distance:
    r = n-k
    d0(n,r) = SUM(n above i) from i=0 -> d0 - 1 <= 2*r


## hints:

- t = [5,1,2,4]
- n = 32
- ni = 8
- initially choose Xi = ni - ti --> x=(3,7,6,4)


## Pprange with particaular X = (ni - xi choose ti) * (ni choose ti)^-1
