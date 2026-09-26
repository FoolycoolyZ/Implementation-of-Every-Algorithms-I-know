1 Introduction to CoinChangingSuppose
Suppose all you have are 1-cent, 5-cent and 10-cent coins but you have infinitely
many of each. For any given (cent) total n we wish to obtain n cents out of our
coins. Consider the following associated problems:

let 1-cent = p
    5-cent = m 
    10-cent = r 
    n = total number of the money that need to be changed.

(a) How can we do this if we don’t care how many coins we use?
answer: we can use all 1-cents, so it could be:
n*p = n
(b) How can we do this if we wish to use the minimum number of coins?
answer: we should do most with 10s, then goes 5s, then goes 1.
described in the algorithms
number of r(cr) = floor(n/10)
number of m(cm) = floor((n - cp)/5)
number of r(cr) = (n-cp-cm) or (n-cp-cm) mod 5 
n = cr + cm + cp

(c) How many ways can we do this if we don’t care about using the minimum
number of coins?
answer: I don't know

2 The Greedy Method (a Minimization Attempt)
An intuitive approach (which doesn’t always work, as we’ll see) to using the
minimum number of coins is to be greedy. Since we wish to use the minimum
number of coins it seems sensible to use as many of the large coins as possible,
followed by the next largest, and so on.
Example 2.1. Suppose C = $[1, 5, 10]$ and we wish to obtain n = 27 cents.
We first grab two 10-cent coins (the most we can have) followed by one 5-
cent coin (the most we can have) followed by two 1-cent coins. We have thus
used 5 coins.
This is in fact optimal - it is the minimal number of coins, but this may not
be obvious.
Example 2.2. Suppose C = $[1, 10, 25]$ and we wish to obtain n = 30 cents.
We first grab one 25-cent coins (the most we can have), we can’t grab any
10-cent coins, so we finish by grabbing five 1-cent coins. We have thus used
6 coins.
This solution is not optimal however since we could have grabbed three
10-cent coins instead.

3 An Algorithm for Minimization
1. Dynamic programming:
unlike greedy algorithms, this one always find the optimal way for doing it.
Define:
  A[x]=minimum number of coins needed to make x cents
For Example
| x | Minimum Coins | Explanation |
| - | ------------- | ----------- |
| 0 | 0             | No coins    |
| 1 | 1             | 1           |
| 2 | 2             | 1+1         |
| 3 | 3             | 1+1+1       |
| 4 | 4             | 1+1+1+1     |
| 5 | 1             | 5           |
| 6 | 2             | 5+1         |

so we keep continue to find the x = A$[x]$

1. We could first select a 1-cent coin, then obtain x − 1, then combine. We
can do this with A$[x − 1]$ + 1 coins.
2. We could first select a 5-cent coin, then obtain x − 5, then combine. We
can do this with A$[x − 5]$ + 1 coins. Note that this is only a possibility if
x ≥ 5 because if x < 5 then x − 5 < 0 which we can’t do.
3. We could first select a 10-cent coin, then obtain x−10, then combine. We
can do this with A$[x − 10]$ + 1 coins. Note that this is only a possibility if
x ≥ 10 because if x < 10 then x − 10 < 0 which we can’t do.

example:
we have 11 what can we do by using dynamic programming is that we could

using first method
note: We could first select a 1-cent coin, then obtain x − 1, then combine. We
can do this with A$[x − 1]$ + 1 coins.
note: A$[10]$ = 1 
A$[11 - 1]$ + 1 = 2 

using second method
A$[11-5]$ + 1 = 2 + 1 = 3 

using third method 
A$[11-10]$ + 1 = 1 + 1 = 2 
The minimal coin that need is 2

Proof: why does dynamic programming works at this point 
using contradiction
A$[x]$ < min {A$[x − 1]$ + 1, A$[x − 5]$ + 1, A$[x − 10]$ + 1}
Suppose the coin combination used to obtain the actual optimal solution for
x involves a c-cent coin where c ∈ {1, 5, 10} (it has to involve at least one of 
these). Then x − c cents may be obtained by removing a c-cent coin from this
optimal solution for x which implies that A$[x − c]$ ≤ A$[x]$ − 1.
However the assumption tells us that A$[x]$ < A$[x − c]$ + 1 and so we have:
A$[x]$ < A$[x − c]$ + 1 ≤ (A$[x]$ − 1) + 1 = A$[x]$
This is a contradiction. QED


