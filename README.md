# AI Research Grind 🧠

Learning path to AI Researcher — from fundamentals to frontier research.

Every concept visualized with [Manim](https://www.manim.community/) (the engine behind [3Blue1Brown](https://www.youtube.com/c/3blue1brown)).

## Why This Exists

Most ML courses teach you to call `model.fit()`. This repo goes deeper — building visual intuition for every concept from linear algebra to transformers, with animated proofs and explanations you can run yourself.

## Structure

```
ai-research-grind/
├── phase1-math/
│   ├── linear-algebra/    ← MIT 18.06 (Gilbert Strang)
│   │   ├── lectures/      ← Notes & key insights per lecture
│   │   └── scripts/       ← Manim scripts (render to get videos)
│   ├── probability-stats/
│   ├── optimization/
│   └── calculus/
├── phase2-ml-fundamentals/
├── phase3-transformers-llms/
├── phase4-research-skills/
├── phase5-coding-systems/
└── phase6-portfolio/
```

## Rendering Videos

Videos are not committed (too large for git). Generate them from scripts:

```bash
# Install manim
pip install manim

# Render a specific scene (1080p 60fps)
manim -qh phase1-math/linear-algebra/scripts/lecture01_geometry_linear_eq.py Lecture1_RowPicture2D

# Render all scenes in a file
manim -qh phase1-math/linear-algebra/scripts/lecture01_geometry_linear_eq.py

# Quick preview (480p)
manim -ql phase1-math/linear-algebra/scripts/lecture01_geometry_linear_eq.py Lecture1_ColumnPicture2D
```

Output goes to `media/videos/` (gitignored).

**Requirements:** Python 3.9+, LaTeX (`brew install --cask basictex` on macOS)

## Progress

### Phase 1: Math Foundations
**Linear Algebra — MIT 18.06 (Gilbert Strang, 34 lectures)**

Each lecture has a Manim script (`scripts/`) and study notes (`lectures/`) strictly following Strang's MIT 18.06 content.

- [x] Lecture 1: The Geometry of Linear Equations
- [x] Lecture 2: Elimination with Matrices
- [x] Lecture 3: Multiplication and Inverse Matrices
- [x] Lecture 4: Factorization into A = LU
- [x] Lecture 5: Transposes, Permutations, Spaces R^n
- [x] Lecture 6: Column Space and Nullspace
- [x] Lecture 7: Solving Ax = 0: Pivot Variables, Special Solutions
- [x] Lecture 8: Solving Ax = b: Row Reduced Form R
- [x] Lecture 9: Independence, Basis, and Dimension
- [x] Lecture 10: The Four Fundamental Subspaces
- [ ] Lecture 11: Matrix Spaces; Rank 1; Small World Graphs
- [ ] Lecture 12: Graphs, Networks, Incidence Matrices
- [ ] Lecture 13: Quiz 1 Review
- [ ] Lecture 14: Orthogonal Vectors and Subspaces
- [ ] Lecture 15: Projections onto Subspaces
- [ ] Lecture 16: Projection Matrices and Least Squares
- [ ] Lecture 17: Orthogonal Matrices and Gram-Schmidt
- [ ] Lecture 18: Properties of Determinants
- [ ] Lecture 19: Determinant Formulas and Cofactors
- [ ] Lecture 20: Cramer's Rule, Inverse Matrix, and Volume
- [ ] Lecture 21: Eigenvalues and Eigenvectors
- [ ] Lecture 22: Diagonalization and Powers of A
- [ ] Lecture 23: Differential Equations and exp(At)
- [ ] Lecture 24: Markov Matrices; Fourier Series
- [ ] Lecture 25: Symmetric Matrices and Positive Definiteness
- [ ] Lecture 26: Complex Matrices; Fast Fourier Transform
- [ ] Lecture 27: Positive Definite Matrices and Minima
- [ ] Lecture 28: Similar Matrices and Jordan Form
- [ ] Lecture 29: Singular Value Decomposition
- [ ] Lecture 30: Linear Transformations and Their Matrices
- [ ] Lecture 31: Change of Basis; Image Compression
- [ ] Lecture 32: Quiz 3 Review
- [ ] Lecture 33: Left and Right Inverses; Pseudoinverse
- [ ] Lecture 34: Final Course Review

### Phase 2-6: Coming soon

## Resources

| Resource | What | Link |
|----------|------|------|
| MIT 18.06 | Linear Algebra lectures | [YouTube](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) |
| 3Blue1Brown | Visual intuition | [Essence of LA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) |
| Manim | Animation engine | [docs](https://docs.manim.community/) |

## License

MIT
