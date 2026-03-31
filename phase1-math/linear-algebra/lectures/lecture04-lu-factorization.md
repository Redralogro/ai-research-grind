# Lecture 4: Factorization into A = LU

**MIT 18.06 Linear Algebra, Prof. Gilbert Strang**

## The Big Idea

Elimination is not just a procedure — it produces a **factorization**. Every invertible matrix A can be written as:
```
A = L · U
```
where **L** is lower triangular (with 1s on the diagonal) and **U** is upper triangular (the pivots and above).

The key insight: **the multipliers from elimination go directly into L** (with no sign flip), as long as no row exchanges are needed.

---

## Review: From Elimination to Factorization

Elimination gives us:
```
E₃₂ · E₂₁ · A = U
```

Solving for A:
```
A = E₂₁⁻¹ · E₃₂⁻¹ · U = L · U
```

The product of inverse elimination matrices is **L**.

Why is this better than keeping track of E matrices?

| Approach | What happens to multipliers |
|----------|----------------------------|
| **E matrix** | Multipliers get a **minus sign** |
| **L = E⁻¹** | Multipliers go in **directly** (no sign flip) |
| **Product of Es** | Multipliers can **interact** and change |
| **L (no row exchanges)** | Multipliers just **sit in place** — beautiful! |

---

## Why L Is So Nice

When there are **no row exchanges**, the multipliers from elimination drop directly into L without interference.

If elimination uses multiplier `ℓᵢⱼ` to eliminate entry (i,j), then that same `ℓᵢⱼ` appears in position (i,j) of L.

This is a small miracle: the multipliers don't interact with each other when assembled into L.

---

## Full Example

### Start with A:
```
A = ┌         ┐
    │ 1  2  1 │
    │ 3  8  1 │
    │ 0  4  1 │
    └         ┘
```

### Step 1: Eliminate below pivot (1,1)

**Multiplier** ℓ₂₁ = 3 (because 3/1 = 3)

**Operation**: Row₂ → Row₂ - 3·Row₁
```
┌         ┐
│ 1  2  1 │
│ 0  2 -2 │  ← 3-3=0, 8-6=2, 1-3=-2
│ 0  4  1 │
└         ┘
```

### Step 2: Eliminate below pivot (2,2)

**Multiplier** ℓ₃₂ = 2 (because 4/2 = 2)

**Operation**: Row₃ → Row₃ - 2·Row₂
```
┌         ┐
│ 1  2  1 │
│ 0  2 -2 │
│ 0  0  5 │  ← 0-0=0, 4-4=0, 1-(-4)=5
└         ┘
```

This is **U**.

### Assemble L from multipliers:
```
L = ┌         ┐
    │ 1  0  0 │  ← 1s on diagonal
    │ 3  1  0 │  ← ℓ₂₁ = 3
    │ 0  2  1 │  ← ℓ₃₁ = 0, ℓ₃₂ = 2
    └         ┘
```

### Verify A = LU:
```
┌         ┐   ┌         ┐   ┌         ┐
│ 1  0  0 │   │ 1  2  1 │   │ 1  2  1 │
│ 3  1  0 │ · │ 0  2 -2 │ = │ 3  8  1 │ = A  ✓
│ 0  2  1 │   │ 0  0  5 │   │ 0  4  1 │
└         ┘   └         ┘   └         ┘
```

---

## Cost of Elimination

How many operations does elimination take for an n×n matrix?

| Step | Operations |
|------|-----------|
| Eliminate column 1 | ~n² |
| Eliminate column 2 | ~(n-1)² |
| Eliminate column 3 | ~(n-2)² |
| ... | ... |
| **Total** | **~n³/3** |

The sum 1² + 2² + ... + n² ≈ n³/3.

For a 100×100 matrix: ~333,000 operations (very fast).
For a 1000×1000 matrix: ~333,000,000 operations (still manageable).

---

## When Row Exchanges Are Needed: PA = LU

If a zero appears in a pivot position, we need a **row exchange** (permutation).

The general factorization becomes:
```
PA = LU
```
where **P** is a permutation matrix that reorders the rows of A so elimination can proceed without zero pivots.

Every invertible matrix has a PA = LU factorization.

---

## Solving Ax = b with LU

Once we have A = LU, solving Ax = b becomes two easy triangular solves:

### Step 1: Forward Substitution — Solve Ly = b
```
┌         ┐ ┌    ┐   ┌    ┐
│ 1  0  0 │ │ y₁ │   │ b₁ │
│ 3  1  0 │ │ y₂ │ = │ b₂ │
│ 0  2  1 │ │ y₃ │   │ b₃ │
└         ┘ └    ┘   └    ┘
```
Solve from **top to bottom** (forward substitution).

### Step 2: Back Substitution — Solve Ux = y
```
┌          ┐ ┌    ┐   ┌    ┐
│ 1  2   1 │ │ x₁ │   │ y₁ │
│ 0  2  -2 │ │ x₂ │ = │ y₂ │
│ 0  0   5 │ │ x₃ │   │ y₃ │
└          ┘ └    ┘   └    ┘
```
Solve from **bottom to top** (back substitution).

### Why is this useful?
If you need to solve Ax = b for **many different b vectors** (same A), you factor A = LU **once** and then do two cheap triangular solves for each b. This is much faster than re-doing elimination each time.

---

## Key Takeaways

| Concept | Meaning |
|---------|---------|
| **A = LU** | Elimination stored as a factorization |
| **L (lower triangular)** | Multipliers from elimination, 1s on diagonal |
| **U (upper triangular)** | Result of elimination (pivots on diagonal) |
| **Multipliers drop in** | No sign flip when building L (if no row exchanges) |
| **Cost: ~n³/3** | Elimination is O(n³), manageable for large matrices |
| **PA = LU** | General form when row exchanges are needed |
| **Two triangular solves** | Ly = b (forward), Ux = y (back) — fast for multiple b |

---

## Coming Up

**Lecture 5**: Transposes, Permutations, and Vector Spaces
**Lecture 6**: Column Space and Null Space

---

**Videos**: See `phase1-math/linear-algebra/videos/` for Manim animations of these concepts.
