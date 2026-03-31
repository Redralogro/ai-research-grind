# Lecture 6: Column Space and Nullspace

> MIT 18.06 Linear Algebra — Gilbert Strang

## Subspaces of a Vector Space

A **subspace** of a vector space must satisfy three requirements:

1. Contains the zero vector $\mathbf{0}$
2. Closed under addition: if $\mathbf{u}, \mathbf{v}$ are in the subspace, so is $\mathbf{u} + \mathbf{v}$
3. Closed under scalar multiplication: if $\mathbf{v}$ is in the subspace and $c$ is a scalar, so is $c\mathbf{v}$

Equivalently, a subspace must be **closed under all linear combinations**: if $\mathbf{u}$ and $\mathbf{v}$ are in the subspace, then $c\mathbf{u} + d\mathbf{v}$ is in the subspace for all scalars $c, d$.

### Examples and Non-Examples in $\mathbb{R}^2$

- The zero vector alone $\{\mathbf{0}\}$: subspace
- Any line through the origin: subspace
- All of $\mathbb{R}^2$: subspace
- A line **not** through the origin: **not** a subspace (fails to contain $\mathbf{0}$)
- The first quadrant ($x \geq 0, y \geq 0$): **not** a subspace (not closed under scalar multiplication — multiply by $-1$)

## Column Space $C(A)$

The **column space** of a matrix $A$ is the set of all linear combinations of the columns of $A$.

$$C(A) = \{ A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n \}$$

If $A$ is $m \times n$ with columns $\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n$, then:

$$C(A) = \text{all } x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n$$

The column space $C(A)$ is a **subspace of $\mathbb{R}^m$** (the columns have $m$ components).

### Why Is $C(A)$ a Subspace?

If $A\mathbf{x} = \mathbf{u}$ and $A\mathbf{y} = \mathbf{v}$, then $A(\mathbf{x} + \mathbf{y}) = \mathbf{u} + \mathbf{v}$ and $A(c\mathbf{x}) = c\mathbf{u}$. So the set of all outputs $A\mathbf{x}$ is closed under addition and scalar multiplication.

### Connection to $Ax = b$

> **$A\mathbf{x} = \mathbf{b}$ is solvable if and only if $\mathbf{b}$ is in the column space $C(A)$.**

This is the fundamental connection. Solving $A\mathbf{x} = \mathbf{b}$ is the same as asking: is $\mathbf{b}$ a linear combination of the columns of $A$?

### Example

$$A = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \\ 3 & 1 & 4 \\ 4 & 1 & 5 \end{bmatrix}$$

This is a $4 \times 3$ matrix, so $C(A)$ is a subspace of $\mathbb{R}^4$.

Can $C(A)$ be all of $\mathbb{R}^4$? **No.** Three columns in $\mathbb{R}^4$ cannot span all of $\mathbb{R}^4$ — we need at least 4 independent vectors for that.

Notice that column 3 = column 1 + column 2. So $C(A)$ is really spanned by just two independent columns. The column space is a **2-dimensional subspace** (a plane through the origin) in $\mathbb{R}^4$.

For which $\mathbf{b}$ can we solve $A\mathbf{x} = \mathbf{b}$? Exactly those $\mathbf{b}$ of the form $b_1 \mathbf{a}_1 + b_2 \mathbf{a}_2$ — the vectors in that 2D plane.

## Nullspace $N(A)$

The **nullspace** of a matrix $A$ is the set of all solutions to $A\mathbf{x} = \mathbf{0}$.

$$N(A) = \{ \mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0} \}$$

If $A$ is $m \times n$, then the nullspace $N(A)$ is a **subspace of $\mathbb{R}^n$** (the vectors $\mathbf{x}$ have $n$ components).

### Proof That $N(A)$ Is a Subspace

We verify closure under addition and scalar multiplication:

1. If $A\mathbf{x} = \mathbf{0}$ and $A\mathbf{y} = \mathbf{0}$, then $A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}$. So $\mathbf{x} + \mathbf{y} \in N(A)$.
2. If $A\mathbf{x} = \mathbf{0}$, then $A(c\mathbf{x}) = cA\mathbf{x} = c\mathbf{0} = \mathbf{0}$. So $c\mathbf{x} \in N(A)$.
3. $A\mathbf{0} = \mathbf{0}$, so $\mathbf{0} \in N(A)$.

### Important Contrast

The solutions to $A\mathbf{x} = \mathbf{b}$ (with $\mathbf{b} \neq \mathbf{0}$) do **not** form a subspace. The zero vector is not a solution when $\mathbf{b} \neq \mathbf{0}$.

### Example

Using the same matrix:

$$A = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \\ 3 & 1 & 4 \\ 4 & 1 & 5 \end{bmatrix}$$

Solve $A\mathbf{x} = \mathbf{0}$:

$$x_1 + x_2 + 2x_3 = 0$$
$$2x_1 + x_2 + 3x_3 = 0$$
$$3x_1 + x_2 + 4x_3 = 0$$
$$4x_1 + x_2 + 5x_3 = 0$$

Since column 3 = column 1 + column 2, one solution is $\mathbf{x} = (1, 1, -1)$. All scalar multiples $c(1, 1, -1)$ are also in the nullspace.

The nullspace is a **line through the origin** in $\mathbb{R}^3$.

## Column Space vs. Nullspace: Summary

| Property | Column Space $C(A)$ | Nullspace $N(A)$ |
|---|---|---|
| Definition | All $A\mathbf{x}$ | All $\mathbf{x}$ with $A\mathbf{x} = \mathbf{0}$ |
| Lives in | $\mathbb{R}^m$ | $\mathbb{R}^n$ |
| Subspace of | The output space | The input space |

For an $m \times n$ matrix: $C(A) \subseteq \mathbb{R}^m$ and $N(A) \subseteq \mathbb{R}^n$. These are subspaces of **different** spaces (unless $m = n$).

## Key Takeaways

1. A **subspace** must contain $\mathbf{0}$ and be closed under addition and scalar multiplication.
2. The **column space** $C(A)$ is all linear combinations of the columns of $A$. It is a subspace of $\mathbb{R}^m$.
3. $A\mathbf{x} = \mathbf{b}$ is solvable if and only if $\mathbf{b} \in C(A)$.
4. The **nullspace** $N(A)$ is all solutions to $A\mathbf{x} = \mathbf{0}$. It is a subspace of $\mathbb{R}^n$.
5. The proof that $N(A)$ is a subspace is a direct consequence of linearity: $A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y}$ and $A(c\mathbf{x}) = cA\mathbf{x}$.
6. Solutions to $A\mathbf{x} = \mathbf{b}$ with $\mathbf{b} \neq \mathbf{0}$ do **not** form a subspace.
