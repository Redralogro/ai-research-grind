# Lecture 6: Column Space and Null Space

**MIT 18.06 Linear Algebra, Prof. Gilbert Strang**

## The Big Ideas

1. Every matrix A has two fundamental subspaces: its **column space** C(A) and its **null space** N(A)
2. **Ax = b** is solvable exactly when b is in the column space
3. The **rank-nullity theorem** connects the dimensions of these spaces: rank + nullity = n

---

## Column Space C(A)

### Definition

The **column space** of A is the set of all linear combinations of the columns of A:
```
C(A) = { Ax : x ∈ Rⁿ } = span of columns of A
```

It answers the question: **what outputs b can Ax produce?**

### Example
```
A = ┌      ┐
    │ 1  3 │
    │ 2  6 │       columns: [1,2] and [3,6]
    │ 3  9 │
    └      ┘
```

The columns [1,2,3] and [3,6,9] are **parallel** (second = 3 × first). So:
```
C(A) = all multiples of [1, 2, 3] = a line through the origin in R³
```

C(A) is a **1-dimensional** subspace of R³.

### Why It's a Subspace

C(A) is closed under addition and scalar multiplication:
- If b₁ = Ax₁ and b₂ = Ax₂, then b₁ + b₂ = A(x₁ + x₂) ∈ C(A)
- If b = Ax, then cb = A(cx) ∈ C(A)
- The zero vector is in C(A): A·**0** = **0**

---

## Null Space N(A)

### Definition

The **null space** of A is the set of all solutions to Ax = **0**:
```
N(A) = { x ∈ Rⁿ : Ax = 0 }
```

It answers the question: **what inputs x does A send to zero?**

### Example
```
A = ┌         ┐
    │ 1  2  3 │
    │ 2  4  6 │
    └         ┘
```

Solve Ax = 0. After elimination:
```
U = ┌         ┐
    │ 1  2  3 │
    │ 0  0  0 │
    └         ┘
```

One pivot (column 1), two free variables (columns 2 and 3).

Setting free variables: x₂ = 1, x₃ = 0 → x₁ = -2:
```
x₁ = [-2, 1, 0]
```

Setting free variables: x₂ = 0, x₃ = 1 → x₁ = -3:
```
x₂ = [-3, 0, 1]
```

**Null space** = all combinations c₁[-2,1,0] + c₂[-3,0,1] — a **2-dimensional** subspace of R³.

### Why It's a Subspace

N(A) is closed under addition and scalar multiplication:
- If Ax₁ = 0 and Ax₂ = 0, then A(x₁ + x₂) = Ax₁ + Ax₂ = 0 + 0 = 0
- If Ax = 0, then A(cx) = cAx = c·0 = 0
- A·**0** = **0**, so the zero vector is in N(A)

---

## Rank and Dimension

### Rank

The **rank** of a matrix is the dimension of its column space:
```
rank(A) = dim(C(A)) = number of pivots
```

### Nullity

The **nullity** of a matrix is the dimension of its null space:
```
nullity(A) = dim(N(A)) = number of free variables
```

---

## The Rank-Nullity Theorem

For an m×n matrix A:
```
rank(A) + nullity(A) = n
```

| Term | Equals | Meaning |
|------|--------|---------|
| rank | # pivots | Dimensions of output that A "uses" |
| nullity | # free variables | Dimensions of input that A "kills" |
| n | # columns | Total input dimensions |

### Example
```
A = ┌         ┐
    │ 1  2  3 │    2×3 matrix, so n = 3
    │ 2  4  6 │
    └         ┘
```
- rank = 1 (one pivot)
- nullity = 2 (two free variables)
- 1 + 2 = 3 = n ✓

---

## Solving Ax = b

### When Is Ax = b Solvable?

**Ax = b is solvable if and only if b is in the column space C(A).**

```
b ∈ C(A)  ⟺  Ax = b has a solution
```

### Example: Solvable
```
A = ┌      ┐       b = ┌   ┐
    │ 1  3 │           │ 4 │
    │ 2  6 │           │ 8 │    b = 4·[1,2,3] → b ∈ C(A) ✓
    │ 3  9 │           │12 │
    └      ┘           └   ┘
```

### Example: Not Solvable
```
A = ┌      ┐       b = ┌   ┐
    │ 1  3 │           │ 1 │
    │ 2  6 │           │ 1 │    b is NOT a multiple of [1,2,3] → b ∉ C(A) ✗
    │ 3  9 │           │ 1 │
    └      ┘           └   ┘
```

---

## Complete Solution

When Ax = b **is** solvable, the complete solution has the form:
```
x = x_particular + x_null
```

| Component | What It Is | How to Find It |
|-----------|-----------|----------------|
| **x_particular** | Any single solution to Ax = b | Set free variables to 0, solve for pivots |
| **x_null** | Any vector in N(A) | All solutions to Ax = 0 |

### Why This Works

If Ax_p = b and Ax_n = 0, then:
```
A(x_p + x_n) = Ax_p + Ax_n = b + 0 = b  ✓
```

### Geometric Picture

The complete solution is **a shifted copy of the null space**:
- The null space passes through the origin
- x_particular shifts it to pass through a solution of Ax = b
- If nullity = 0, there's exactly **one** solution (the particular solution)
- If nullity > 0, there are **infinitely many** solutions

---

## Key Takeaways

| Concept | Meaning |
|---------|---------|
| **Column space C(A)** | All possible outputs Ax; span of columns |
| **Null space N(A)** | All x where Ax = 0 |
| **Rank** | dim(C(A)) = number of pivots |
| **Nullity** | dim(N(A)) = number of free variables |
| **Rank-nullity theorem** | rank + nullity = n (number of columns) |
| **Solvability** | Ax = b solvable iff b ∈ C(A) |
| **Complete solution** | x = x_particular + x_null |

---

## Coming Up

**Lecture 7**: Solving Ax = 0 — pivot variables, free variables, and special solutions
**Lecture 8**: Solving Ax = b — row reduced form R

---

**Videos**: See `phase1-math/linear-algebra/videos/` for Manim animations of these concepts.
