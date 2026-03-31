# Lecture 9: Independence, Basis, and Dimension

> MIT 18.06 Linear Algebra — Gilbert Strang

## Linear Independence

Vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ are **linearly independent** if:

$$c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k = \mathbf{0} \quad \text{only when all } c_i = 0$$

Equivalently: **no vector is a linear combination of the others.**

If the vectors are **dependent**, there exist coefficients (not all zero) such that $c_1 \mathbf{v}_1 + \cdots + c_k \mathbf{v}_k = \mathbf{0}$. We can then solve for one vector in terms of the rest.

### Matrix Interpretation

Put $\mathbf{v}_1, \ldots, \mathbf{v}_k$ as columns of a matrix $A$. Then:

> The columns of $A$ are **independent** if and only if $N(A) = \{\mathbf{0}\}$ — the only solution to $A\mathbf{x} = \mathbf{0}$ is $\mathbf{x} = \mathbf{0}$.

This happens when $A$ has **rank $r = n$** (no free variables).

The columns are **dependent** if and only if $N(A) \neq \{\mathbf{0}\}$ — there is a nonzero solution to $A\mathbf{x} = \mathbf{0}$. This happens when there are free variables ($r < n$).

### Key Fact About Dependence

> If $m < n$ (more columns than rows), then the columns are **always dependent**.

Why? The system $A\mathbf{x} = \mathbf{0}$ has $n$ unknowns and $m < n$ equations, so there must be free variables ($n - r \geq n - m > 0$), giving nonzero solutions.

### Examples

**Independent:** $\mathbf{v}_1 = (1, 0), \mathbf{v}_2 = (0, 1)$ in $\mathbb{R}^2$. The matrix $A = I$ has $N(A) = \{\mathbf{0}\}$.

**Dependent:** $\mathbf{v}_1 = (1, 2), \mathbf{v}_2 = (2, 4)$ in $\mathbb{R}^2$. We have $\mathbf{v}_2 = 2\mathbf{v}_1$.

**Dependent (three vectors in $\mathbb{R}^2$):** Any three vectors in $\mathbb{R}^2$ must be dependent, regardless of what they are.

## Spanning

Vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$ **span** a space $S$ if every vector in $S$ is a linear combination of $\mathbf{v}_1, \ldots, \mathbf{v}_k$.

$$S = \text{all } c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k$$

The columns of $A$ span the column space $C(A)$ — by definition.

## Basis

A **basis** for a subspace $S$ is a set of vectors that is:

1. **Linearly independent**, AND
2. **Spans** the space $S$

A basis is the **right number** of vectors: not too many (dependent), not too few (don't span).

### Examples

**Standard basis for $\mathbb{R}^n$:** The columns of the $n \times n$ identity matrix:

$$\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}, \quad \ldots, \quad \mathbf{e}_n = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}$$

They are independent ($N(I) = \{\mathbf{0}\}$) and span $\mathbb{R}^n$ (every vector is a combination).

**Another basis for $\mathbb{R}^3$:** $(1,1,2), (2,2,5), (0,0,1)$ — provided they are independent (check by elimination).

**Not a basis:** $(1,2,3), (4,5,6), (7,8,9)$ — these are dependent (the third is the average of the first two in a certain sense; row reduction reveals rank 2).

### Basis for the Column Space

Given $A$, which columns form a basis for $C(A)$?

> The **pivot columns of the original matrix $A$** are a basis for $C(A)$.

**Not the pivot columns of $U$ or $R$!** Elimination changes the column space. But the **dependence relations** between columns are preserved. If column 3 of $A$ equals column 1 + column 2, then column 3 of $U$ equals column 1 + column 2 of $U$ as well. The pivot columns of $A$ are independent and span $C(A)$.

### Basis for the Nullspace

The **special solutions** (from Lecture 7) form a basis for $N(A)$. There are $n - r$ of them.

## Dimension

The **dimension** of a subspace is the number of vectors in any basis.

> **Every basis for a given subspace has the same number of vectors.**

This is a theorem, not obvious. It means dimension is well-defined.

### Dimensions of Key Subspaces

For an $m \times n$ matrix $A$ of rank $r$:

| Subspace | Dimension |
|---|---|
| Column space $C(A)$ | $r$ |
| Nullspace $N(A)$ | $n - r$ |

The rank tells you the dimension of the column space. The "nullity" $n - r$ tells you the dimension of the nullspace.

### The Rank + Nullity Theorem

$$\dim C(A) + \dim N(A) = r + (n - r) = n$$

The number of pivot variables plus the number of free variables equals the total number of variables.

## Example: Putting It All Together

$$A = \begin{bmatrix} 1 & 2 & 3 & 1 \\ 1 & 1 & 2 & 1 \\ 1 & 2 & 3 & 1 \end{bmatrix}$$

Row reduce:

$$U = \begin{bmatrix} 1 & 2 & 3 & 1 \\ 0 & -1 & -1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

- Rank $r = 2$. Pivot columns: 1 and 2. Free columns: 3 and 4.
- **Basis for $C(A)$:** Columns 1 and 2 of $A$: $\begin{bmatrix}1\\1\\1\end{bmatrix}$ and $\begin{bmatrix}2\\1\\2\end{bmatrix}$. Dimension = 2.
- **Basis for $N(A)$:** Two special solutions (set each free variable to 1, others to 0). Dimension = $4 - 2 = 2$.

## Key Takeaways

1. Vectors are **independent** if no nontrivial linear combination gives $\mathbf{0}$. For columns of $A$, this means $N(A) = \{\mathbf{0}\}$.
2. If there are more vectors than the dimension of the space ($n > m$), they must be **dependent**.
3. A **basis** is a set of vectors that is independent and spanning — the minimal spanning set, the maximal independent set.
4. **Dimension** is the number of vectors in any basis. It is always the same for a given subspace.
5. The **pivot columns of $A$** (not $U$!) form a basis for $C(A)$, with $\dim C(A) = r$.
6. The **special solutions** form a basis for $N(A)$, with $\dim N(A) = n - r$.
7. The rank + nullity theorem: $r + (n - r) = n$.
