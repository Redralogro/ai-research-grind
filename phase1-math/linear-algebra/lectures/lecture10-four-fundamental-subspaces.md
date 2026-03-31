# Lecture 10: The Four Fundamental Subspaces

> MIT 18.06 Linear Algebra — Gilbert Strang

## The Big Picture

For an $m \times n$ matrix $A$ of rank $r$, there are **four fundamental subspaces**. This is the heart of linear algebra.

| # | Subspace | Notation | Lives in | Dimension |
|---|---|---|---|---|
| 1 | Column space | $C(A)$ | $\mathbb{R}^m$ | $r$ |
| 2 | Nullspace | $N(A)$ | $\mathbb{R}^n$ | $n - r$ |
| 3 | Row space | $C(A^T)$ | $\mathbb{R}^n$ | $r$ |
| 4 | Left nullspace | $N(A^T)$ | $\mathbb{R}^m$ | $m - r$ |

### Dimension Check

The subspaces in $\mathbb{R}^n$: $\dim C(A^T) + \dim N(A) = r + (n - r) = n$. Good.

The subspaces in $\mathbb{R}^m$: $\dim C(A) + \dim N(A^T) = r + (m - r) = m$. Good.

## The Row Space $C(A^T)$

The **row space** is the column space of $A^T$ — equivalently, all linear combinations of the **rows** of $A$.

$$C(A^T) = \text{all combinations of rows of } A$$

It is a subspace of $\mathbb{R}^n$ (each row has $n$ components).

### Basis for the Row Space

> The **nonzero rows of $R$** (the reduced row echelon form) form a basis for $C(A^T)$.

Elimination changes the column space but **preserves the row space**: $C(A^T) = C(R^T)$. Each row operation is a combination of rows — so the row space doesn't change.

### Example

$$A = \begin{bmatrix} 1 & 2 & 3 & 1 \\ 1 & 1 & 2 & 1 \\ 1 & 2 & 3 & 1 \end{bmatrix} \longrightarrow R = \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

Rank $r = 2$.

**Basis for $C(A^T)$:** $(1, 0, 1, 1)$ and $(0, 1, 1, 0)$ — the nonzero rows of $R$.

Note how clean this basis is. The rref rows have the identity matrix sitting in the pivot columns, making them automatically independent.

## The Left Nullspace $N(A^T)$

The **left nullspace** is the nullspace of $A^T$ — all vectors $\mathbf{y}$ such that $A^T \mathbf{y} = \mathbf{0}$.

Equivalently: $\mathbf{y}^T A = \mathbf{0}^T$. The vector $\mathbf{y}$ acts on $A$ **from the left** — hence the name.

It is a subspace of $\mathbb{R}^m$ (the vectors $\mathbf{y}$ have $m$ components).

### Finding the Left Nullspace

Use the elimination record. If $EA = R$, then:

$$E = \begin{bmatrix} — & \text{rows that produce nonzero rows of } R & — \\ — & \text{rows that produce zero rows of } R & — \end{bmatrix}$$

The rows of $E$ corresponding to **zero rows of $R$** give vectors in the left nullspace.

Why? If the last row of $E$ is $\mathbf{e}^T$ and the last row of $R$ is $\mathbf{0}^T$, then $\mathbf{e}^T A = \mathbf{0}^T$, so $A^T \mathbf{e} = \mathbf{0}$.

### Example (continued)

With the $3 \times 4$ matrix above, the elimination matrix $E$ that takes $A$ to $R$ satisfies $EA = R$. The third row of $R$ is zero, so the third row of $E$ gives a vector in the left nullspace.

Tracking the row operations: $R_3 \leftarrow R_3 - R_1$ gives $E$'s third row as $(-1, 0, 1)$.

**Basis for $N(A^T)$:** $(-1, 0, 1)$. Dimension = $m - r = 3 - 2 = 1$.

Check: $(-1, 0, 1) \begin{bmatrix} 1 & 2 & 3 & 1 \\ 1 & 1 & 2 & 1 \\ 1 & 2 & 3 & 1 \end{bmatrix} = (0, 0, 0, 0)$. Confirmed.

## Bases for All Four Subspaces: Summary

For $A$ ($m \times n$, rank $r$), after computing $R = \text{rref}(A)$ via $EA = R$:

| Subspace | Basis | How to find it |
|---|---|---|
| $C(A)$ | Pivot columns of $A$ | Identify pivot columns from $R$, take those columns from $A$ |
| $N(A)$ | Special solutions | Set each free variable to 1 (others to 0), back-substitute in $R$ |
| $C(A^T)$ | First $r$ rows of $R$ | The nonzero rows of the rref |
| $N(A^T)$ | Last $m - r$ rows of $E$ | From $EA = R$, take rows of $E$ corresponding to zero rows of $R$ |

## New Vector Space: Matrix Spaces

The ideas of subspace, basis, and dimension apply beyond $\mathbb{R}^n$.

**Example:** The space of all $3 \times 3$ matrices. Dimension = 9 (the nine entries are free).

**Subspaces of $3 \times 3$ matrices:**

- Symmetric matrices ($A = A^T$): dimension = 6
- Upper triangular matrices: dimension = 6
- Diagonal matrices: dimension = 3

Note: symmetric $\cap$ upper triangular = diagonal, and $\dim = 6 + 6 - 9 = 3$. This is a dimension formula: $\dim(S_1 + S_2) = \dim S_1 + \dim S_2 - \dim(S_1 \cap S_2)$.

## Orthogonality Preview

The four subspaces come in **orthogonal pairs**:

$$N(A) \perp C(A^T) \quad \text{in } \mathbb{R}^n$$

$$N(A^T) \perp C(A) \quad \text{in } \mathbb{R}^m$$

Why $N(A) \perp C(A^T)$? If $A\mathbf{x} = \mathbf{0}$, then every row of $A$ is orthogonal to $\mathbf{x}$. The row space is all combinations of rows — so every vector in the row space is orthogonal to $\mathbf{x}$.

These are not just orthogonal — they are **orthogonal complements**. Their dimensions add up: $r + (n-r) = n$ and $r + (m-r) = m$. Together they fill the whole space.

## The Fundamental Theorem of Linear Algebra (Preview)

$A$ maps $\mathbb{R}^n$ to $\mathbb{R}^m$. The mapping splits into two clean pieces:

- The **row space** $C(A^T)$ maps onto the **column space** $C(A)$ — this is the "action" part
- The **nullspace** $N(A)$ maps to $\mathbf{0}$ — this is the "lost" part

Every $\mathbf{x} \in \mathbb{R}^n$ decomposes as $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ where $\mathbf{x}_r \in C(A^T)$ and $\mathbf{x}_n \in N(A)$, and:

$$A\mathbf{x} = A\mathbf{x}_r + A\mathbf{x}_n = A\mathbf{x}_r + \mathbf{0} = A\mathbf{x}_r$$

The matrix $A$ is a perfect one-to-one mapping from the row space to the column space (both $r$-dimensional).

## Key Takeaways

1. Every $m \times n$ matrix of rank $r$ has **four fundamental subspaces** with dimensions $r$, $n-r$, $r$, $m-r$.
2. Two subspaces live in $\mathbb{R}^n$ (row space and nullspace), two in $\mathbb{R}^m$ (column space and left nullspace).
3. **Basis for $C(A)$:** pivot columns of the original $A$. **Basis for $C(A^T)$:** nonzero rows of $R$.
4. **Basis for $N(A)$:** special solutions. **Basis for $N(A^T)$:** from rows of $E$ in $EA = R$.
5. The nullspace and row space are **orthogonal complements** in $\mathbb{R}^n$. The left nullspace and column space are orthogonal complements in $\mathbb{R}^m$.
6. $A$ maps the row space one-to-one onto the column space, and sends the nullspace to zero. This is the fundamental theorem of linear algebra.
