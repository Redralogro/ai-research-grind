# Lecture 3: Multiplication and Inverse Matrices

> MIT 18.06 Linear Algebra — Gilbert Strang

## Four Ways to Multiply $AB = C$

Let $A$ be $m \times n$ and $B$ be $n \times p$. Then $C = AB$ is $m \times p$.

### Way 1: Standard (dot product) — row of $A$ times column of $B$

$$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} = (\text{row } i \text{ of } A) \cdot (\text{col } j \text{ of } B)$$

This is the definition you already know. One dot product gives one entry of $C$.

### Way 2: Matrix times columns

Think of $B$ as a collection of columns $[b_1 \; b_2 \; \cdots \; b_p]$. Then:

$$AB = [Ab_1 \; Ab_2 \; \cdots \; Ab_p]$$

Each column of $C$ is $A$ times the corresponding column of $B$. This is the most fundamental perspective: matrix multiplication acts on columns.

### Way 3: Rows times matrix

Think of $A$ as a stack of rows. Each row of $C$ is the corresponding row of $A$ times $B$:

$$\text{row } i \text{ of } C = (\text{row } i \text{ of } A) \cdot B$$

Each row of $C$ is a linear combination of the rows of $B$.

### Way 4: Sum of outer products (columns of $A$ times rows of $B$)

$$AB = \sum_{k=1}^{n} (\text{col } k \text{ of } A)(\text{row } k \text{ of } B)$$

Each term $(\text{col } k)(\text{row } k)$ is an $m \times p$ matrix of **rank 1**. The product $AB$ is the sum of $n$ rank-1 matrices.

**Example:** If $A$ is $3 \times 2$ and $B$ is $2 \times 4$:

$$AB = \underbrace{\begin{bmatrix} a_{11} \\ a_{21} \\ a_{31}\end{bmatrix} \begin{bmatrix} b_{11} & b_{12} & b_{13} & b_{14} \end{bmatrix}}_{\text{rank-1}} + \underbrace{\begin{bmatrix} a_{12} \\ a_{22} \\ a_{32}\end{bmatrix} \begin{bmatrix} b_{21} & b_{22} & b_{23} & b_{24} \end{bmatrix}}_{\text{rank-1}}$$

## Block Multiplication

If $A$ and $B$ are partitioned into compatible blocks:

$$\begin{bmatrix} A_1 & A_2 \\ A_3 & A_4 \end{bmatrix} \begin{bmatrix} B_1 & B_2 \\ B_3 & B_4 \end{bmatrix} = \begin{bmatrix} A_1B_1 + A_2B_3 & A_1B_2 + A_2B_4 \\ A_3B_1 + A_4B_3 & A_3B_2 + A_4B_4 \end{bmatrix}$$

Block multiplication follows the same row-times-column rule, but with blocks instead of numbers. The blocks must be compatible sizes.

## Inverse Matrices

A square matrix $A$ is **invertible** (nonsingular) if there exists a matrix $A^{-1}$ such that:

$$A^{-1}A = I \quad \text{and} \quad AA^{-1} = I$$

For square matrices, a left inverse equals the right inverse (this is a theorem, not obvious).

### Properties of Inverses

- $(AB)^{-1} = B^{-1}A^{-1}$ — the order reverses ("socks and shoes")
- $(A^{-1})^{-1} = A$
- $(A^T)^{-1} = (A^{-1})^T$

### Why $(AB)^{-1} = B^{-1}A^{-1}$?

Check directly: $(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I$. Done.

## Gauss-Jordan Method for Finding $A^{-1}$

Solve $AA^{-1} = I$ by solving all $n$ columns of $A^{-1}$ simultaneously.

Form the augmented matrix $[A \mid I]$ and apply elimination to reach $[I \mid A^{-1}]$:

$$\left[\begin{array}{cc} A & I \end{array}\right] \xrightarrow{\text{row reduce}} \left[\begin{array}{cc} I & A^{-1} \end{array}\right]$$

**Example:** Find the inverse of $A = \begin{bmatrix} 1 & 3 \\ 2 & 7 \end{bmatrix}$.

$$\left[\begin{array}{cc|cc} 1 & 3 & 1 & 0 \\ 2 & 7 & 0 & 1 \end{array}\right] \xrightarrow{R_2 - 2R_1} \left[\begin{array}{cc|cc} 1 & 3 & 1 & 0 \\ 0 & 1 & -2 & 1 \end{array}\right] \xrightarrow{R_1 - 3R_2} \left[\begin{array}{cc|cc} 1 & 0 & 7 & -3 \\ 0 & 1 & -2 & 1 \end{array}\right]$$

So $A^{-1} = \begin{bmatrix} 7 & -3 \\ -2 & 1 \end{bmatrix}$.

## Singular Matrices (Non-invertible)

$A$ is **singular** (not invertible) if and only if there exists a nonzero vector $x$ such that $Ax = 0$.

**Why no inverse can exist:** Suppose $A^{-1}$ existed. Then from $Ax = 0$ we get $x = A^{-1}0 = 0$. But we said $x \neq 0$. Contradiction.

Another way to see it: if $Ax = 0$ for $x \neq 0$, then $A$ squashes something to zero — it loses information — and that cannot be undone.

## Key Takeaways

1. There are **four ways** to think about matrix multiplication. The column view (Way 2) and outer product view (Way 4) are especially powerful.
2. **Block multiplication** works just like regular multiplication with blocks replacing scalars, provided the block sizes are compatible.
3. $A^{-1}$ exists when $A$ is square and nonsingular (all pivots nonzero, no $x \neq 0$ with $Ax = 0$).
4. $(AB)^{-1} = B^{-1}A^{-1}$ — the inverse of a product reverses the order.
5. **Gauss-Jordan elimination** on $[A \mid I]$ produces $[I \mid A^{-1}]$ and is the practical method for computing inverses.
6. If $Ax = 0$ has a nonzero solution, then $A$ is **singular** and has no inverse.
