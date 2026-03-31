# Lecture 4: Factorization into A = LU

> MIT 18.06 Linear Algebra — Gilbert Strang

## From Elimination to Factorization

In Lecture 2, elimination gave us $EA = U$. Now we flip it around:

$$A = E^{-1}U = LU$$

The matrix $L$ (lower triangular) records **what elimination did**. The matrix $U$ (upper triangular) records **what elimination produced**. Together, $A = LU$ is the factorization form of elimination.

## Building $L$ from Elimination Matrices

Suppose elimination uses two steps (no row exchanges):

$$E_{32} E_{21} A = U$$

Then:

$$A = E_{21}^{-1} E_{32}^{-1} U = LU$$

where $L = E_{21}^{-1} E_{32}^{-1}$.

### Inverses of Elimination Matrices

If $E_{21}$ subtracts $\ell_{21}$ times row 1 from row 2, then $E_{21}^{-1}$ **adds** $\ell_{21}$ times row 1 back to row 2:

$$E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -\ell_{21} & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad E_{21}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ \ell_{21} & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

Just flip the sign of the multiplier.

### The Key Insight: Multipliers Drop Right In

When we multiply the inverses $E_{21}^{-1} E_{32}^{-1}$, the multipliers slot into $L$ with no interference:

$$L = E_{21}^{-1} E_{32}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ \ell_{21} & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & \ell_{32} & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ \ell_{21} & 1 & 0 \\ 0 & \ell_{32} & 1 \end{bmatrix}$$

This is why $L$ is better than $E$: the multipliers go directly below the diagonal with no interaction between them. If there were also $\ell_{31}$, it would sit in the $(3,1)$ position. Every multiplier lands in its natural spot.

**This does not work for $E$!** The product $E_{32}E_{21}$ mixes the multipliers together. $L$ is the clean factorization.

## The Structure of $A = LU$

$$A = LU = \begin{bmatrix} 1 & 0 & 0 \\ \ell_{21} & 1 & 0 \\ \ell_{31} & \ell_{32} & 1 \end{bmatrix} \begin{bmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{bmatrix}$$

- $L$: lower triangular, **1s on the diagonal**, multipliers below
- $U$: upper triangular, **pivots on the diagonal**

Some authors also write $A = LDU$ where $D$ is diagonal (containing the pivots) and $U$ has 1s on its diagonal.

## Computational Cost

How many operations does elimination require for an $n \times n$ matrix?

- Eliminating column 1: roughly $n^2$ operations (modify an $(n-1) \times (n-1)$ block)
- Eliminating column 2: roughly $(n-1)^2$ operations
- And so on...

Total: $n^2 + (n-1)^2 + \cdots + 1^2 \approx \frac{n^3}{3}$ multiplications.

**Not $n^3$, but $\frac{n^3}{3}$.** This is the cost of factoring $A$ into $LU$.

## Row Exchanges: $PA = LU$

When a zero (or dangerously small number) appears in a pivot position, we need a **row exchange**. This is recorded by a permutation matrix $P$.

The complete factorization with possible row exchanges is:

$$PA = LU$$

$P$ rearranges the rows of $A$ into the order that elimination actually processes them.

## Why Factor?

Suppose we need to solve $Ax = b$ for many different right-hand sides $b$, all with the same $A$.

**Without $LU$:** Each solve costs $\frac{n^3}{3}$ operations.

**With $LU$:** Factor once ($\frac{n^3}{3}$), then for each $b$:

1. **Forward substitution:** Solve $Lc = b$ for $c$ — cost $\frac{n^2}{2}$
2. **Back substitution:** Solve $Ux = c$ for $x$ — cost $\frac{n^2}{2}$

Each additional right-hand side costs only $n^2$, not $n^3$. This is a huge saving.

## Example

$$A = \begin{bmatrix} 1 & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & 1 \end{bmatrix}$$

From Lecture 2, elimination with multipliers $\ell_{21} = 3$, $\ell_{31} = 0$, $\ell_{32} = 2$ gives:

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 2 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 0 & 5 \end{bmatrix}$$

Verify: $LU = A$. The multipliers from elimination are sitting right there in $L$.

## Key Takeaways

1. Elimination is really a **factorization**: $A = LU$, where $L$ holds the multipliers and $U$ is the upper triangular result.
2. The inverses of elimination matrices combine cleanly: **multipliers drop into $L$ without interfering** with each other.
3. The cost of elimination is $\approx \frac{n^3}{3}$ operations, not $n^3$.
4. When row exchanges are needed, the factorization becomes $PA = LU$.
5. The payoff of $LU$: factor once, then solve for each new $b$ cheaply via forward and back substitution ($n^2$ per solve instead of $n^3$).
