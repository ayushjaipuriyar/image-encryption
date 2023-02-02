
> [!summary] Main points
> - N-traversal of a Latin square
>  - Permutate an image data group by group for the first time
>-  Use 2 latin square dfor auxilary diffusion on the basis of choatic sequence
> - Final pair of orthogonal latin square to do the second scrambling
> - **Hence "scrambling diffusion scrambling"**
 
> [!check] Achievements
> - Secure and fast encryption effect
> - The final information entropy is very close to 8
> - The correlation coefficient is approximate to 0
>

# Latin Square
A Latin square of order n (defined on an n-set S ) is an n × n array in which each cell contains a single symbol, such that each symbol occurs exactly once in each row and column[34]. For consistency, we set $S = {0, 1, . . . , n − 1}$ . Two Latin squares of order n $A = (a_{i j})$ and $B = (b_{i j})$
are orthogonal if every ordered pair $(a_{i j}, b_{i j})$ in $S × S$occurs exactly once.

Fig. 1 lists a pair of orthogonal Latin squares of order 4 $A = (a_{i j})$ and $B = (b_{i j})$. Denote $C = (c_{i j})$ as the juxta-position array, where $c_{i j} = ( a_{i j}, b_{i j})$. Each ordered pairing $S × S$ occurs exactly once. Notation: Using a pair of orthogonal Latin squares $A = (a_{i j})$ and $B = (b_{i j})$ can directly generate a two-dimensional map $φ : (i, j) → (a_{i j}, b_{i j}), i, j = 0, 1, ..., n−1$.

Suppose M is a Latin square defined on S .A transversal in M is a set of n positions, no two in the same row or column, including each of the n symbols exactly once. Two transversal are disjoint if there are no same positions in them. Any k disjoint transversal are called a k-transversal. If k = n there exists an n-traversal in M.