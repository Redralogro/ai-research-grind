# Lecture 3: Multiplication and Inverse Matrices

**MIT 18.06 Linear Algebra, Prof. Gilbert Strang**

## The Big Ideas

1. There are **5 different ways** to think about matrix multiplication — each gives different insight
2. Some matrices have an **inverse** A⁻¹ that undoes the transformation
3. **Gauss-Jordan elimination** finds A⁻¹ by augmenting [A | I] → [I | A⁻¹]

---

## Part 1: 5 Ways to Multiply AB = C

### Way 1: Standard (Row · Column)
Each entry of C is the dot product of a row of A with a column of B:
```
C_ij = Σ_k  A_ik · B_kj
```
Think: row i of A  ·  column j of B = one number

### Way 2: Columns of C
Each **column** of C is A times that column of B:
```
col_j(C) = A · col_j(B)
```
Think: C's columns are **linear combinations** of A's columns

### Way 3: Rows of C
Each **row** of C is that row of A times B:
```
row_i(C) = row_i(A) · B
```
Think: C's rows are **linear combinations** of B's rows

### Way 4: Sum of Outer Products (Columns × Rows)
```
AB = Σ_k  col_k(A) · row_k(B)
```
Each term produces a full **rank-1 matrix**. AB is the sum of these.
This view is critical for understanding SVD and low-rank approximations.

### Way 5: Block Multiplication
Partition A and B into sub-matrices and multiply as if entries were numbers:
```
┌ A₁  A₂ ┐ ┌ B₁  B₂ ┐   ┌ A₁B₁+A₂B₃   A₁B₂+A₂B₄ ┐
│         │·│         │ = │                          │
└ A₃  A₄ ┘ └ B₃  B₄ ┘   └ A₃B₁+A₄B₃   A₃B₂+A₄B₄ ┘
```

---

## Part 2: Inverse Matrices

### Definition
```
A⁻¹A = I    and    AA⁻¹ = I
```
The inverse undoes the transformation. If A stretches space, A⁻¹ shrinks it back.

### Why It Matters
If A is invertible, solving Ax = b is easy:
```
Ax = b  →  A⁻¹(Ax) = A⁻¹b  →  x = A⁻¹b
```

### When Does A⁻¹ Exist?
A is **invertible** (non-singular) when:
- ✓ All n pivots are non-zero
- ✓ det(A) ≠ 0
- ✓ Rows are linearly independent
- ✓ Columns span all of Rⁿ

A is **singular** (no inverse) when:
- ✗ At least one zero pivot (after row exchanges)
- ✗ det(A) = 0
- ✗ Rows/columns are linearly dependent

---

## Part 3: Gauss-Jordan Elimination

### Method: [A | I] → [I | A⁻¹]
Augment A with the identity matrix. Apply elimination to both sides simultaneously.
When the left side becomes I, the right side is A⁻¹.

### Example: Find A⁻¹ where A = [[2,1],[5,3]]

**Setup:**
```
[ 2  1 | 1  0 ]
[ 5  3 | 0  1 ]
```

**Step 1:** R₂ → R₂ - (5/2)R₁
```
[ 2    1   |  1    0  ]
[ 0   1/2  | -5/2  1  ]
```

**Step 2:** R₂ → 2·R₂
```
[ 2  1 |  1  0 ]
[ 0  1 | -5  2 ]
```

**Step 3:** R₁ → R₁ - R₂
```
[ 2  0 |  6  -2 ]
[ 0  1 | -5   2 ]
```

**Step 4:** R₁ → (1/2)·R₁
```
[ 1  0 |  3  -1 ]
[ 0  1 | -5   2 ]
```

**Result:**
```
A⁻¹ = [ 3  -1 ]
      [-5   2 ]
```

**Verify:** A · A⁻¹ = [[2,1],[5,3]] · [[3,-1],[-5,2]] = [[1,0],[0,1]] = I ✓

---

## Key Properties of Inverses

| Property | Formula | Intuition |
|----------|---------|-----------|
| Reverse order | (AB)⁻¹ = B⁻¹A⁻¹ | Undo B first, then A |
| Transpose | (Aᵀ)⁻¹ = (A⁻¹)ᵀ | Transpose and inverse commute |
| Double inverse | (A⁻¹)⁻¹ = A | Undo the undo = original |
| Scalar | (cA)⁻¹ = (1/c)A⁻¹ | Scale factors invert |

---

## Key Takeaways

| Concept | Meaning |
|---------|---------|
| **5 ways to multiply** | Each perspective reveals different structure |
| **Outer product view** | Key for SVD, low-rank approximations in ML |
| **Invertible** | All pivots non-zero, det ≠ 0 |
| **Gauss-Jordan** | [A\|I] → [I\|A⁻¹] by elimination |
| **AB ≠ BA** | Matrix multiplication is NOT commutative! |
| **(AB)⁻¹ = B⁻¹A⁻¹** | Reverse order for products |

---

## Connection to ML

- **A⁻¹** used in: closed-form linear regression `(XᵀX)⁻¹Xᵀy`
- **Outer product view** (Way 4) → foundation for **SVD** and **PCA**
- **Block multiplication** → efficient computation in neural networks (batching)

---

## Coming Up

**Lecture 4**: A = LU Factorization — storing elimination steps efficiently  
**Lecture 5**: Transposes, Permutations, Spaces Rⁿ

---

**Videos**: Render with:
```bash
manim -qh phase1-math/linear-algebra/scripts/lecture3_multiplication_inverse.py Lecture3_MatrixMultiplication
manim -qh phase1-math/linear-algebra/scripts/lecture3_multiplication_inverse.py Lecture3_InverseMatrix
manim -qh phase1-math/linear-algebra/scripts/lecture3_multiplication_inverse.py Lecture3_InverseProperties
```
