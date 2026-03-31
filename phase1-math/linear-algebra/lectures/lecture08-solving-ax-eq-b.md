# Lecture 8: Solving Ax = b — Row Reduced Form R

> MIT 18.06 Linear Algebra — Gilbert Strang

## Setup: From Ax = 0 to Ax = b

In Lecture 7 we found the nullspace (all solutions to $A\mathbf{x} = \mathbf{0}$). Now we solve $A\mathbf{x} = \mathbf{b}$ — and we need to know **when** it is solvable and **what** the complete solution looks like.

## Solvability of $A\mathbf{x} = \mathbf{b}$

### Using the Augmented Matrix

Work with the **augmented matrix** $[A \mid \mathbf{b}]$ and perform elimination.

### Worked Example

$$A = \begin{bmatrix} 1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$$

Form $[A \mid \mathbf{b}]$ and eliminate:

$$\begin{bmatrix} 1 & 2 & 2 & 2 & b_1 \\ 2 & 4 & 6 & 8 & b_2 \\ 3 & 6 & 8 & 10 & b_3 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 2 & 2 & b_1 \\ 0 & 0 & 2 & 4 & b_2 - 2b_1 \\ 0 & 0 & 2 & 4 & b_3 - 3b_1 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 2 & 2 & b_1 \\ 0 & 0 & 2 & 4 & b_2 - 2b_1 \\ 0 & 0 & 0 & 0 & b_3 - b_2 - b_1 \end{bmatrix}$$

The third equation becomes $0 = b_3 - b_2 - b_1$.

### The Solvability Condition

> $A\mathbf{x} = \mathbf{b}$ is solvable if and only if $\mathbf{b}$ is in the column space $C(A)$.

Equivalently in terms of rows:

> **If a combination of the rows of $A$ gives the zero row, then the same combination of the entries of $\mathbf{b}$ must give zero.**

In our example, row 3 - row 2 - row 1 = zero row, so we need $b_3 - b_2 - b_1 = 0$.

For concreteness, take $\mathbf{b} = (1, 5, 6)$: check $6 - 5 - 1 = 0$. Solvable.

## Finding the Complete Solution

The complete solution has two parts: a **particular solution** plus the **nullspace**.

### Step 1: Particular Solution $\mathbf{x}_p$

Set all **free variables to zero** and solve for the pivot variables.

With $\mathbf{b} = (1, 5, 6)$ and free variables $x_2 = 0$, $x_4 = 0$:

From row 2: $2x_3 = 5 - 2(1) = 3 \Rightarrow x_3 = 3/2$

From row 1: $x_1 + 2(3/2) = 1 \Rightarrow x_1 = -2$

$$\mathbf{x}_p = \begin{bmatrix} -2 \\ 0 \\ 3/2 \\ 0 \end{bmatrix}$$

Check: $A\mathbf{x}_p = \mathbf{b}$.

### Step 2: Add the Nullspace

From Lecture 7, the nullspace of this $A$ is spanned by:

$$\mathbf{s}_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{s}_2 = \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$$

### Step 3: The Complete Solution

$$\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n = \begin{bmatrix} -2 \\ 0 \\ 3/2 \\ 0 \end{bmatrix} + c_1 \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + c_2 \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$$

for all $c_1, c_2 \in \mathbb{R}$.

### Geometric Picture

The complete solution is a **plane** in $\mathbb{R}^4$, but it does **not** pass through the origin (unless $\mathbf{b} = \mathbf{0}$). It is a shifted copy of the nullspace. The solution set is **not a subspace** when $\mathbf{b} \neq \mathbf{0}$.

## The Four Cases: Full Picture by Rank

For an $m \times n$ matrix $A$ of rank $r$:

### Case 1: $r = m = n$ (Full rank, square matrix)

- $R = I$
- $A$ is **invertible**
- **Exactly 1 solution** for every $\mathbf{b}$
- $N(A) = \{\mathbf{0}\}$

### Case 2: $r = n < m$ (Full column rank, tall thin matrix)

- $R = \begin{bmatrix} I \\ 0 \end{bmatrix}$
- No free variables, $N(A) = \{\mathbf{0}\}$
- **0 or 1 solution** depending on $\mathbf{b}$
- If a solution exists, it is unique

### Case 3: $r = m < n$ (Full row rank, short wide matrix)

- $R = \begin{bmatrix} I & F \end{bmatrix}$
- $n - r = n - m$ free variables
- **Infinitely many solutions for every $\mathbf{b}$**
- Always solvable (every $\mathbf{b}$ is in $C(A)$)

### Case 4: $r < m$ and $r < n$ (Neither full row nor full column rank)

- $R = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix}$
- **0 or infinitely many solutions** depending on $\mathbf{b}$
- Solvable only for some $\mathbf{b}$; when solvable, infinitely many solutions

### Summary Table

| | $r = m$ | $r < m$ |
|---|---|---|
| $r = n$ | 1 solution | 0 or 1 solution |
| $r < n$ | $\infty$ solutions | 0 or $\infty$ solutions |

## The Structure of the Solution

$$\mathbf{x}_{\text{complete}} = \mathbf{x}_p + \mathbf{x}_n$$

- $\mathbf{x}_p$ is **one** particular solution (any solution to $A\mathbf{x} = \mathbf{b}$)
- $\mathbf{x}_n$ is the **general** element of $N(A)$

Why does this work? If $A\mathbf{x}_p = \mathbf{b}$ and $A\mathbf{x}_n = \mathbf{0}$, then:

$$A(\mathbf{x}_p + \mathbf{x}_n) = A\mathbf{x}_p + A\mathbf{x}_n = \mathbf{b} + \mathbf{0} = \mathbf{b}$$

And conversely, if $A\mathbf{x}_1 = \mathbf{b}$ and $A\mathbf{x}_2 = \mathbf{b}$, then $A(\mathbf{x}_1 - \mathbf{x}_2) = \mathbf{0}$, so $\mathbf{x}_1 - \mathbf{x}_2 \in N(A)$.

## Key Takeaways

1. $A\mathbf{x} = \mathbf{b}$ is solvable if and only if $\mathbf{b} \in C(A)$. Equivalently: if a combination of rows of $A$ produces the zero row, the same combination of entries of $\mathbf{b}$ must give zero.
2. The **particular solution** $\mathbf{x}_p$ is found by setting all free variables to zero.
3. The **complete solution** is $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n$, a shifted copy of the nullspace.
4. The solution set is **not a subspace** (unless $\mathbf{b} = \mathbf{0}$).
5. The rank $r$ relative to $m$ and $n$ determines whether solutions exist (0 vs. some) and whether they are unique (1 vs. $\infty$).
