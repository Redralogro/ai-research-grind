# Lecture 7: Solving Ax = 0 — Pivot Variables, Special Solutions

> MIT 18.06 Linear Algebra — Gilbert Strang

## The Algorithm: Elimination to Echelon Form

To find the nullspace of $A$, we perform **elimination** to get an echelon form $U$, then identify **pivot variables** and **free variables**.

The nullspace does not change during elimination: $N(A) = N(U) = N(R)$.

### Worked Example

$$A = \begin{bmatrix} 1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10 \end{bmatrix}$$

**Step 1:** Eliminate below the first pivot (row 1, column 1):

- $R_2 \leftarrow R_2 - 2R_1$
- $R_3 \leftarrow R_3 - 3R_1$

$$\begin{bmatrix} 1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 2 & 4 \end{bmatrix}$$

Column 2 has no pivot — $x_2$ is a **free variable**.

**Step 2:** Eliminate below the second pivot (row 2, column 3):

- $R_3 \leftarrow R_3 - R_2$

$$U = \begin{bmatrix} 1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

## Pivots and Free Variables

- **Pivot columns:** 1 and 3 (columns containing pivots)
- **Pivot variables:** $x_1$ and $x_3$
- **Free columns:** 2 and 4
- **Free variables:** $x_2$ and $x_4$
- **Rank** $r = 2$ (number of pivots)
- **Number of free variables** $= n - r = 4 - 2 = 2$

> The rank $r$ counts the number of pivots. The number of free variables is $n - r$.

## Special Solutions

For each free variable, set it to $1$ and all other free variables to $0$, then solve for the pivot variables by back substitution.

**Special solution 1:** Set $x_2 = 1$, $x_4 = 0$.

From row 2: $2x_3 + 4(0) = 0 \Rightarrow x_3 = 0$

From row 1: $x_1 + 2(1) + 2(0) + 2(0) = 0 \Rightarrow x_1 = -2$

$$\mathbf{s}_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}$$

**Special solution 2:** Set $x_2 = 0$, $x_4 = 1$.

From row 2: $2x_3 + 4(1) = 0 \Rightarrow x_3 = -2$

From row 1: $x_1 + 2(0) + 2(-2) + 2(1) = 0 \Rightarrow x_1 = 2$

$$\mathbf{s}_2 = \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$$

**The nullspace** is all combinations of the special solutions:

$$N(A) = \{ c_1 \mathbf{s}_1 + c_2 \mathbf{s}_2 : c_1, c_2 \in \mathbb{R} \}$$

This is a 2-dimensional subspace (a plane through the origin) in $\mathbb{R}^4$.

## Reduced Row Echelon Form (rref)

Continue elimination **upward** and **scale pivots to 1**:

Divide row 2 by 2:

$$\begin{bmatrix} 1 & 2 & 2 & 2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

Eliminate above pivot 2: $R_1 \leftarrow R_1 - 2R_2$:

$$R = \begin{bmatrix} 1 & 2 & 0 & -2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

This is $R = \text{rref}(A)$. The pivots are $1$ with zeros above and below.

## The Block Structure of R

If we rearrange columns to put pivot columns first (columns 1, 3) and free columns second (columns 2, 4):

$$R_{\text{permuted}} = \begin{bmatrix} 1 & 0 & 2 & -2 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix}$$

where $I$ is the $r \times r$ identity and $F$ is the $r \times (n-r)$ matrix that encodes relationships between pivot and free variables.

Here: $I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, $F = \begin{bmatrix} 2 & -2 \\ 0 & 2 \end{bmatrix}$.

## The Nullspace Matrix

The **nullspace matrix** $N$ has the special solutions as its columns. From the block form of $R$:

$$N = \begin{bmatrix} -F \\ I \end{bmatrix}$$

(with the same row permutation applied to match the column reordering).

Check: $RN = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix} \begin{bmatrix} -F \\ I \end{bmatrix} = \begin{bmatrix} -F + F \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. Confirmed.

For our example:

$$N = \begin{bmatrix} -2 & 2 \\ 0 & -2 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$$

(rows 1, 3 are pivot variables; rows 2, 4 are free variables with the identity block.)

## The Complete Picture

Given $A$ of size $m \times n$ with rank $r$:

| Quantity | Value |
|---|---|
| Number of pivots | $r$ |
| Number of free variables | $n - r$ |
| Dimension of $N(A)$ | $n - r$ |
| Number of special solutions | $n - r$ |
| Zero rows in $U$ | $m - r$ |

## Key Takeaways

1. **Elimination** converts $A$ to echelon form $U$ without changing the nullspace.
2. **Pivot columns** contain pivots; **free columns** do not. Free variables can take any value.
3. The **rank** $r$ = number of pivots. There are $n - r$ free variables and $n - r$ special solutions.
4. The **reduced row echelon form** $R$ has pivots equal to $1$ with zeros above and below.
5. In block form, $R = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix}$ and the nullspace matrix is $N = \begin{bmatrix} -F \\ I \end{bmatrix}$.
6. The nullspace is spanned by the $n - r$ special solutions. Every vector in $N(A)$ is a linear combination of these special solutions.
