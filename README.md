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
manim -qh phase1-math/linear-algebra/scripts/lecture1_geometry_linear_eq.py Lecture1_RowPicture

# Render all scenes in a file
manim -qh phase1-math/linear-algebra/scripts/lecture1_geometry_linear_eq.py

# Quick preview (480p)
manim -ql phase1-math/linear-algebra/scripts/lecture1_geometry_linear_eq.py Lecture1_ColumnPicture
```

Output goes to `media/videos/` (gitignored).

**Requirements:** Python 3.9+, LaTeX (`brew install --cask basictex` on macOS)

## Progress

### Phase 1: Math Foundations
**Linear Algebra — MIT 18.06 (34 lectures)**
- [x] Lecture 1: The Geometry of Linear Equations
- [ ] Lecture 2: Elimination with Matrices
- [ ] Lecture 3: Multiplication and Inverse Matrices
- [ ] Lecture 4: Factorization into A = LU
- [ ] Lecture 5: Transposes, Permutations, Spaces R^n
- [ ] Lecture 6: Column Space and Nullspace
- [ ] Lecture 7: Solving Ax = 0: Pivot Variables, Special Solutions
- [ ] Lecture 8: Solving Ax = b: Row Reduced Form R
- [ ] Lecture 9: Independence, Basis, and Dimension
- [ ] Lecture 10: The Four Fundamental Subspaces
- [ ] Lectures 11-34: _(in progress)_

### Phase 2-6: Coming soon

## Resources

| Resource | What | Link |
|----------|------|------|
| MIT 18.06 | Linear Algebra lectures | [YouTube](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) |
| 3Blue1Brown | Visual intuition | [Essence of LA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) |
| Manim | Animation engine | [docs](https://docs.manim.community/) |

## License

MIT
