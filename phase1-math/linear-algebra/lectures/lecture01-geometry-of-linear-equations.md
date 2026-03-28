# Lecture 1: The Geometry of Linear Equations

**Source:** MIT 18.06 — Gilbert Strang
**Video:** https://www.youtube.com/watch?v=J7DzL2_Na80
**Date:** 2026-03-28

## Key Concepts

### Row Picture
- Each equation = a line (2D) or plane (3D)
- Solution = intersection point
- System: 2x - y = 0, -x + 2y = 3 → intersection at (1, 2)

### Column Picture (THE important one)
- Rewrite as: x * col1 + y * col2 = b
- x[2,-1] + y[-1,2] = [0,3]
- Find the right **linear combination** of column vectors
- This is the core idea that carries through all of linear algebra and ML

### When It Fails
- If columns point in same direction (linearly dependent)
- Combinations can only reach points on a line, not all of 2D
- → Ax = b has no solution for some b

## Connection to ML
- Neural networks find linear combinations of features
- Columns dependent = redundant features (multicollinearity)
- Rank = how much "real information" is in the data

## Manim Videos
- `Lecture1_RowPicture.mp4` — Two lines crossing at (1,2)
- `Lecture1_ColumnPicture.mp4` — Vector addition tip-to-tail
- `Lecture1_WhenItFails.mp4` — Dependent columns can't span 2D

## Quiz (self-test)
1. What's the difference between row picture and column picture?
2. Write 2x-y=0, -x+2y=3 in column form (Ax=b)
3. When does Ax=b have no solution? (think column picture)
