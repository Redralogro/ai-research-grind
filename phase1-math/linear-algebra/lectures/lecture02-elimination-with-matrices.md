# Lecture 2: Elimination with Matrices

**MIT 18.06 Linear Algebra, Prof. Gilbert Strang**

## The Big Idea

Elimination is the algorithm computers use to solve **Ax = b**. It's systematic, mechanical, and reveals the structure of A.

The key insight: **each elimination step can be represented as a matrix multiplication**.

---

## The 3×3 Example

Solve this system:
```
 x + 2y +  z = 2
3x + 8y +  z = 12
    4y + z = 2
```

Write as augmented matrix **[A|b]**:
```
┌              ┐
│ 1  2  1 | 2 │
│ 3  8  1 | 12│
│ 0  4  1 | 2 │
└              ┘
```

---

## Elimination Steps

### Step 1: Eliminate below the first pivot

**Pivot** = 1 (top-left corner, the number we use to eliminate below)

**Multiplier** = 3 (because row2[0]/pivot = 3/1 = 3)

**Operation**: Row₂ → Row₂ - 3·Row₁
```
┌              ┐
│ 1  2  1 | 2 │
│ 0  2  -2| 6 │  ← 3-3=0, 8-6=2, 1-3=-2, 12-6=6
│ 0  4  1 | 2 │
└              ┘
```

### Step 2: Eliminate below the second pivot

**Pivot** = 2 (the 2 in row 2, column 2)

**Multiplier** = 2 (because row3[1]/pivot = 4/2 = 2)

**Operation**: Row₃ → Row₃ - 2·Row₂
```
┌              ┐
│ 1  2  1 | 2 │
│ 0  2  -2| 6 │
│ 0  0  5 | -10│  ← 0-0=0, 4-4=0, 1-(-4)=5, 2-12=-10
└              ┘
```

This is **upper triangular form** (U). All entries below the diagonal are zero.

The three pivots are: **1, 2, 5**

---

## Back Substitution

Now solve from bottom to top:

**Row 3**: `5z = -10` → **z = -2**

**Row 2**: `2y - 2z = 6` → `2y - 2(-2) = 6` → `2y + 4 = 6` → **y = 1**

**Row 1**: `x + 2y + z = 2` → `x + 2(1) + (-2) = 2` → `x + 0 = 2` → **x = 2**

**Solution**: `x = 2, y = 1, z = -2`

---

## When Elimination Fails

### Temporary Failure (Row Exchange)
If you encounter a **zero pivot**, try swapping rows:
```
┌          ┐
│ 0  2  1 │  ← pivot is 0!
│ 1  3  2 │
└          ┘
```
**Fix**: Swap row 1 ↔ row 2, then continue.

### Permanent Failure (Singular Matrix)
If **all** entries below a zero pivot are also zero, the matrix is **singular** (not invertible):
```
┌          ┐
│ 1  2  3 │
│ 0  0  0 │  ← can't fix this
│ 0  0  5 │
└          ┘
```
**No unique solution exists.**

---

## Elimination Matrices

Each elimination step can be written as **E · A**.

### E₂₁: Eliminate row 2, column 1
```
E₂₁ = ┌            ┐
      │  1  0  0  │
      │ -3  1  0  │  ← subtract 3× row 1 from row 2
      │  0  0  1  │
      └            ┘
```

### E₃₂: Eliminate row 3, column 2
```
E₃₂ = ┌           ┐
      │ 1  0  0  │
      │ 0  1  0  │
      │ 0 -2  1  │  ← subtract 2× row 2 from row 3
      └           ┘
```

### Full Elimination
```
U = E₃₂ · E₂₁ · A
```

The product of elimination matrices **E = E₃₂ · E₂₁** transforms A into U.

---

## Connection to LU Decomposition

Elimination gives us:
```
A = L · U
```
where:
- **U** = upper triangular (the result of elimination)
- **L** = lower triangular (the inverse of E, storing all the multipliers)

For our example:
```
L = ┌         ┐
    │ 1  0  0 │
    │ 3  1  0 │  ← multipliers from elimination
    │ 0  2  1 │
    └         ┘
```

This will be covered in detail in **Lecture 4**.

---

## Key Takeaways

| Concept | Meaning |
|---------|---------|
| **Elimination** | Systematic process to convert A to upper triangular U |
| **Pivot** | Diagonal entry used to eliminate below |
| **Multiplier** | The ratio `(entry to eliminate) / pivot` |
| **E matrix** | Each elimination step as a matrix multiplication |
| **Failure modes** | Zero pivot → row exchange or singular matrix |
| **U (upper triangular)** | Final form after elimination |
| **Back substitution** | Solve Ux = c from bottom to top |

---

## Coming Up

**Lecture 3**: Matrix multiplication and inverses  
**Lecture 4**: A = LU factorization (storing elimination steps)

---

**Videos**: See `phase1-math/linear-algebra/videos/` for Manim animations of these concepts.
