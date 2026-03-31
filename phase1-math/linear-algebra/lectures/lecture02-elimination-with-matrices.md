# Lecture 2: Elimination with Matrices

> MIT 18.06 Linear Algebra — Gilbert Strang

## Elimination: The Algorithm

Elimination is the systematic method for solving $Ax = b$. The goal is to transform $A$ into an **upper triangular** matrix $U$ using row operations, then solve by back substitution.

The strategy: use entries in earlier rows to eliminate entries below them, column by column, left to right.

## Worked Example: 3x3 System

Start with the system:

$$A = \begin{bmatrix} 1 & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & 1 \end{bmatrix}, \quad b = \begin{bmatrix} 2 \\ 12 \\ 2 \end{bmatrix}$$

### Step 1: Eliminate below the first pivot

The **first pivot** is $a_{11} = 1$.

The **multiplier** for row 2 is $\ell_{21} = 3/1 = 3$. Subtract $3 \times$ row 1 from row 2:

$$\begin{bmatrix} 1 & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 4 & 1 \end{bmatrix}$$

Row 3 already has a zero in the first column, so no operation is needed ($\ell_{31} = 0$).

### Step 2: Eliminate below the second pivot

The **second pivot** is $a_{22} = 2$ (after the first elimination step).

The multiplier for row 3 is $\ell_{32} = 4/2 = 2$. Subtract $2 \times$ row 2 from row 3:

$$U = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 0 & 5 \end{bmatrix}$$

The **pivots** are $1, 2, 5$ (on the diagonal of $U$). Pivots must be nonzero.

### The Augmented Matrix

We track $b$ alongside $A$ by forming $[A \mid b]$ and applying the same row operations. After elimination:

$$[U \mid c] = \left[\begin{array}{ccc|c} 1 & 2 & 1 & 2 \\ 0 & 2 & -2 & 6 \\ 0 & 0 & 5 & -10 \end{array}\right]$$

## Back Substitution

Starting from the bottom row of $Ux = c$:

- $5x_3 = -10 \implies x_3 = -2$
- $2x_2 - 2(-2) = 6 \implies x_2 = 1$
- $x_1 + 2(1) + 1(-2) = 2 \implies x_1 = 2$

Solution: $x = (2, 1, -2)$.

## Elimination Matrices

Each elimination step can be described by an **elementary matrix** (elimination matrix).

### $E_{21}$: Subtract $\ell_{21}$ times row 1 from row 2

$$E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

Multiplying $E_{21}A$ performs the row operation: (row 2) $\leftarrow$ (row 2) $- 3 \times$ (row 1).

### $E_{32}$: Subtract $\ell_{32}$ times row 2 from row 3

$$E_{32} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix}$$

### The Product

The full elimination is:

$$E_{32}(E_{21}A) = U$$

or equivalently:

$$EA = U, \quad \text{where } E = E_{32}E_{21}$$

## When Elimination Fails

**Temporary failure — fixable by row exchange:** A zero appears in the pivot position, but there is a nonzero entry below it. Swap rows and continue.

**Permanent failure — the matrix is singular:** A zero appears in the pivot position and every entry below it is also zero. There is no pivot available. The matrix does not have $n$ pivots and is not invertible.

## Multipliers Below the Diagonal

The multipliers $\ell_{ij}$ used during elimination are stored for later use. They sit naturally below the diagonal, exactly where the zeros were created:

$$\text{Multipliers: } \ell_{21} = 3, \quad \ell_{31} = 0, \quad \ell_{32} = 2$$

These multipliers will become the entries of $L$ in the $A = LU$ factorization (Lecture 4).

## Key Takeaways

1. **Elimination** transforms $A$ into upper triangular $U$ by subtracting multiples of earlier rows from later rows.
2. **Pivots** are the diagonal entries of $U$. They must all be nonzero for the system to have a unique solution.
3. Each elimination step is a left-multiplication by an **elimination matrix** $E_{ij}$.
4. **Back substitution** solves $Ux = c$ from the bottom up, one variable at a time.
5. A zero pivot that cannot be fixed by a row exchange signals a **singular** matrix.
6. The **multipliers** $\ell_{ij}$ are stored below the diagonal and will form the matrix $L$ in the $LU$ factorization.
