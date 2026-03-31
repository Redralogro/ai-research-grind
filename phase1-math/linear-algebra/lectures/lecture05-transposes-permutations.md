# Lecture 5: Transposes, Permutations, Spaces $\mathbb{R}^n$

> MIT 18.06 Linear Algebra — Gilbert Strang

## Permutation Matrices

A **permutation matrix** $P$ is obtained by rearranging the rows of the identity matrix $I$.

**Example:** The $3 \times 3$ permutation matrices include:

$$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad P_{12} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad P_{13} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}, \quad \ldots$$

### Key Facts

- For $n \times n$ matrices, there are **$n!$ permutation matrices**.
- $PA$ rearranges the **rows** of $A$; $AP$ rearranges the **columns** of $A$.
- Permutation matrices are **orthogonal**: $P^{-1} = P^T$.

**Why $P^{-1} = P^T$?** Each row and each column of $P$ has exactly one 1 and the rest 0s. So $P^T P = I$: the dot product of any row with itself is 1, and with any other row is 0.

### The Complete Factorization

With row exchanges included, elimination always works (for invertible matrices):

$$PA = LU$$

$P$ records whatever row exchanges were needed. $L$ is lower triangular (with 1s on the diagonal), and $U$ is upper triangular.

## Transposes

The **transpose** of $A$ is denoted $A^T$ and defined by:

$$(A^T)_{ij} = A_{ji}$$

Rows become columns, columns become rows.

### Properties of Transposes

- $(A + B)^T = A^T + B^T$
- $(cA)^T = cA^T$
- $(AB)^T = B^T A^T$ — the order reverses, just like inverses
- $(A^{-1})^T = (A^T)^{-1}$ — transpose and inverse commute
- $(A^T)^T = A$

### Why $(AB)^T = B^T A^T$?

Think about it entry by entry, or note that this is the same "reversal" pattern as $(AB)^{-1} = B^{-1}A^{-1}$. To "undo" a product, reverse the order.

## Symmetric Matrices

A matrix is **symmetric** if $A^T = A$, meaning $a_{ij} = a_{ji}$ for all $i, j$.

**Examples:**
- $\begin{bmatrix} 1 & 3 \\ 3 & 7 \end{bmatrix}$ is symmetric.
- Any diagonal matrix is symmetric.

### $A^T A$ Is Always Symmetric

**Claim:** For any matrix $A$ (not necessarily square), the product $A^T A$ is symmetric.

**Proof:** We need to show $(A^T A)^T = A^T A$.

$$(A^T A)^T = A^T (A^T)^T = A^T A \quad \checkmark$$

The transpose of $A^T A$ is itself. This product $A^T A$ appears throughout statistics, least squares, and the rest of this course.

## Vector Spaces

A **vector space** is a collection of vectors that is closed under addition and scalar multiplication.

**$\mathbb{R}^n$** = the space of all column vectors with $n$ real components. This is the primary vector space in this course.

### Rules (axioms)

If $v$ and $w$ are in the space, then:
- $v + w$ is in the space (closed under addition)
- $cv$ is in the space for any real scalar $c$ (closed under scalar multiplication)

These two rules together imply $c_1 v + c_2 w$ is in the space — closure under all linear combinations.

A consequence: the **zero vector** must be in every vector space (take $c = 0$).

## Subspaces

A **subspace** of $\mathbb{R}^n$ is a subset that is itself a vector space — closed under addition and scalar multiplication.

### Subspaces of $\mathbb{R}^2$

There are exactly three kinds:

1. **$\{0\}$** — the zero vector alone (the trivial subspace)
2. **Any line through the origin** — all multiples of some nonzero vector $v$
3. **All of $\mathbb{R}^2$** — the whole plane

**What is NOT a subspace of $\mathbb{R}^2$?**
- A line that does not pass through the origin (fails: does not contain $0$)
- The first quadrant (fails: not closed under scalar multiplication by $-1$)

### Subspaces of $\mathbb{R}^3$

1. $\{0\}$
2. Any line through the origin
3. Any plane through the origin
4. All of $\mathbb{R}^3$

The pattern: subspaces always pass through the origin and extend infinitely in every direction they span.

## Column Space (Preview)

Given a matrix $A$, the **column space** $C(A)$ is the set of all linear combinations of the columns of $A$. This is a subspace of $\mathbb{R}^m$ (where $A$ is $m \times n$).

The equation $Ax = b$ has a solution if and only if $b$ is in the column space of $A$. This connects back to the key question from Lecture 1.

## Key Takeaways

1. There are $n!$ permutation matrices of size $n$. They satisfy $P^{-1} = P^T$.
2. The complete factorization with row exchanges is $PA = LU$.
3. $(AB)^T = B^T A^T$ — the transpose of a product reverses the order.
4. $A^T A$ is **always symmetric**, for any matrix $A$.
5. A **vector space** must be closed under addition and scalar multiplication (and therefore contains $0$).
6. **Subspaces** of $\mathbb{R}^2$: just $\{0\}$, lines through the origin, or all of $\mathbb{R}^2$.
7. The **column space** of $A$ is the subspace of all $b$ for which $Ax = b$ is solvable.
