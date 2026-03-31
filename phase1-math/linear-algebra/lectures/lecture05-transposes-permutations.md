# Lecture 5: Transposes, Permutations, Vector Spaces

**MIT 18.06 Linear Algebra, Prof. Gilbert Strang**

## The Big Ideas

1. **Permutation matrices** reorder rows — and have the beautiful property P⁻¹ = Pᵀ
2. **Transpose** flips a matrix across its diagonal — symmetric matrices are their own transpose
3. **Vector spaces** are the fundamental setting for linear algebra — closed under addition and scalar multiplication

---

## Part 1: Permutation Matrices

### What They Do

A permutation matrix **P** reorders the rows of a matrix. It's the identity matrix with its rows shuffled.

### Example: 3×3 Permutations
```
I = ┌       ┐     P₁₂ = ┌       ┐     P₁₃ = ┌       ┐
    │ 1 0 0 │           │ 0 1 0 │           │ 0 0 1 │
    │ 0 1 0 │           │ 1 0 0 │           │ 0 1 0 │
    │ 0 0 1 │           │ 0 0 1 │           │ 1 0 0 │
    └       ┘           └       ┘           └       ┘
    (no swap)         (swap rows 1,2)     (swap rows 1,3)
```

### Key Properties

| Property | Formula | Meaning |
|----------|---------|---------|
| Orthogonal | PᵀP = I | Columns are orthonormal |
| Inverse = Transpose | P⁻¹ = Pᵀ | Undo a permutation by transposing |
| Count | n! for n×n | 3×3 has 6, 4×4 has 24 permutation matrices |
| Closure | P₁·P₂ = P₃ | Product of permutations is a permutation |

### How Many?

For an n×n matrix, there are **n!** permutation matrices:
- 2×2: 2! = 2 permutations
- 3×3: 3! = 6 permutations
- 4×4: 4! = 24 permutations

---

## PA = LU: The General Factorization

With permutations, **every invertible matrix** can be factored:
```
PA = LU
```

The permutation matrix P reorders the rows of A so that:
- No zero pivots are encountered
- L is lower triangular (1s on diagonal, multipliers below)
- U is upper triangular (pivots on diagonal)

MATLAB/NumPy always use PA = LU (choosing the largest pivot for numerical stability).

---

## Part 2: Transpose

### Definition

The transpose **Aᵀ** flips a matrix across its diagonal:
```
(Aᵀ)ᵢⱼ = Aⱼᵢ
```

Rows become columns, columns become rows.

### Example
```
A = ┌      ┐        Aᵀ = ┌         ┐
    │ 1  3 │             │ 1  2  0 │
    │ 2  7 │             │ 3  7  4 │
    │ 0  4 │             └         ┘
    └      ┘
   (3×2)                    (2×3)
```

### Properties of Transpose

| Property | Formula |
|----------|---------|
| Double transpose | (Aᵀ)ᵀ = A |
| Sum | (A + B)ᵀ = Aᵀ + Bᵀ |
| Scalar | (cA)ᵀ = cAᵀ |
| Product | **(AB)ᵀ = BᵀAᵀ** (reverse order!) |
| Inverse | (A⁻¹)ᵀ = (Aᵀ)⁻¹ |

The reverse order rule for products is crucial — same pattern as inverses.

---

## Part 3: Symmetric Matrices

### Definition

A matrix is **symmetric** if:
```
A = Aᵀ
```

That is, Aᵢⱼ = Aⱼᵢ for all i, j. The matrix is mirrored across its diagonal.

### Example
```
S = ┌       ┐
    │ 3  1  7│
    │ 1  2  9│       S = Sᵀ  ✓
    │ 7  9  4│
    └       ┘
```

### AᵀA Is Always Symmetric

For **any** matrix A (even non-square), the product AᵀA is always symmetric.

**Proof:**
```
(AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA  ✓
```

This is why AᵀA appears everywhere in statistics and machine learning:
- **Linear regression**: normal equations use (XᵀX)
- **PCA**: covariance matrix is (1/n)XᵀX
- **Least squares**: minimizing ‖Ax - b‖² leads to AᵀAx = Aᵀb

---

## Part 4: Vector Spaces

### Definition

A **vector space** is a collection of vectors that is closed under:
1. **Addition**: if **v** and **w** are in the space, then **v + w** is in the space
2. **Scalar multiplication**: if **v** is in the space and c is a scalar, then c**v** is in the space

These two rules also imply closure under **linear combinations**: c₁v₁ + c₂v₂ + ... + cₙvₙ stays in the space.

### Important: The zero vector must be in every vector space
(Take c = 0: c·v = 0 must be in the space.)

### Examples of Vector Spaces

| Space | Description |
|-------|-------------|
| **R¹** | All real numbers (the number line) |
| **R²** | All 2-component vectors (the plane) |
| **R³** | All 3-component vectors (3D space) |
| **Rⁿ** | All n-component real vectors |

---

## Subspaces

### Definition

A **subspace** is a vector space that lives inside a larger vector space. It must:
1. Contain the **zero vector**
2. Be **closed under addition**
3. Be **closed under scalar multiplication**

### Subspaces of R²

| Subspace | Description |
|----------|-------------|
| **R² itself** | The whole plane |
| **Any line through the origin** | e.g., all multiples of [1, 2] |
| **The zero vector alone** | {**0**} — the trivial subspace |

That's it! **No other subspaces of R² exist.**

A line that does NOT pass through the origin is **not** a subspace (it doesn't contain the zero vector).

### Subspaces of R³

| Subspace | Description |
|----------|-------------|
| **R³ itself** | All of 3D space |
| **Any plane through the origin** | 2D subspace |
| **Any line through the origin** | 1D subspace |
| **The zero vector alone** | 0D subspace |

---

## Key Takeaways

| Concept | Meaning |
|---------|---------|
| **Permutation matrix** | Identity with rows shuffled; reorders rows |
| **P⁻¹ = Pᵀ** | Permutations are orthogonal matrices |
| **PA = LU** | General factorization for any invertible matrix |
| **Transpose** | (Aᵀ)ᵢⱼ = Aⱼᵢ; rows and columns swap |
| **(AB)ᵀ = BᵀAᵀ** | Reverse order rule for transpose |
| **Symmetric: A = Aᵀ** | Matrix equals its transpose |
| **AᵀA always symmetric** | Fundamental in statistics and ML |
| **Vector space** | Closed under addition and scalar multiplication |
| **Subspace** | A vector space inside a larger one; must contain **0** |

---

## Coming Up

**Lecture 6**: Column Space and Null Space — the key subspaces of a matrix
**Lecture 7**: Solving Ax = 0 — pivot variables and free variables

---

**Videos**: See `phase1-math/linear-algebra/videos/` for Manim animations of these concepts.
