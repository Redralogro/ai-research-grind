# Lecture 1: The Geometry of Linear Equations

> MIT 18.06 Linear Algebra — Gilbert Strang

## The Central Problem of Linear Algebra

The fundamental problem is: **solve $Ax = b$**.

Given an $n \times n$ matrix $A$ and a vector $b$, find the vector $x$ such that $Ax = b$. There are two geometric ways to understand what this equation means.

## The Row Picture

Each equation in the system represents a geometric object:

- In $\mathbb{R}^2$: each equation is a **line**
- In $\mathbb{R}^3$: each equation is a **plane**
- In $\mathbb{R}^n$: each equation is a **hyperplane**

The **solution** is the point (or points) where all these objects intersect.

### 2x2 Example

$$2x - y = 0$$
$$-x + 2y = 3$$

In the row picture, these are two lines in the $xy$-plane. The first line passes through the origin with slope 2. The second has slope $1/2$ and $y$-intercept $3/2$. They intersect at the point $(1, 2)$.

## The Column Picture

Rewrite $Ax = b$ as a **linear combination of columns**:

$$x \begin{bmatrix} 2 \\ -1 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$$

The question becomes: what combination of the column vectors produces $b$?

The answer is $x = 1, y = 2$:

$$1 \begin{bmatrix} 2 \\ -1 \end{bmatrix} + 2 \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 - 2 \\ -1 + 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$$

## 3x3 Example

Consider a system $Ax = b$ with three equations and three unknowns.

**Row picture:** Each equation defines a plane in $\mathbb{R}^3$. Two planes (typically) intersect in a line. Three planes (typically) intersect at a single point. That point is the solution.

**Column picture:** We have three column vectors in $\mathbb{R}^3$, and we are looking for the linear combination $x_1 \mathbf{c}_1 + x_2 \mathbf{c}_2 + x_3 \mathbf{c}_3 = b$. The solution gives the coefficients of that combination.

### Which picture is better?

- The **row picture** is intuitive for 2 equations (intersecting lines), manageable for 3 (intersecting planes), but hopeless to visualize in higher dimensions.
- The **column picture** scales better conceptually: we are always asking "can I combine these column vectors to reach $b$?"

Strang's emphasis: **think in columns.**

## The Singular Case

A system is **singular** (has no unique solution) when:

- **Row picture:** the planes (or lines) do not intersect at a single point. They might be parallel, or all three might intersect along a line rather than a point.
- **Column picture:** the columns all lie in the same plane (in 3D). No combination of vectors that lie in a plane can produce a vector $b$ that points out of that plane.

In the column picture, singularity means the columns do not **span** all of $\mathbb{R}^n$.

## The Key Question

> **For which right-hand sides $b$ can we solve $Ax = b$?**

If the columns of $A$ span all of $\mathbb{R}^n$, then we can solve $Ax = b$ for every $b$. This is the non-singular case.

If the columns do not span $\mathbb{R}^n$ (they are linearly dependent), then we can only solve for $b$ that happen to lie in the span of the columns. This is the singular case.

## Key Takeaways

1. The fundamental problem of linear algebra is solving $Ax = b$.
2. The **row picture** interprets each equation as a line/plane/hyperplane; the solution is their intersection.
3. The **column picture** interprets $Ax = b$ as "find a linear combination of columns of $A$ that equals $b$." This is the more powerful viewpoint.
4. A matrix is **singular** when its columns fail to span $\mathbb{R}^n$ — some right-hand sides $b$ have no solution.
5. The column picture generalizes better to higher dimensions and is the perspective that drives the rest of the course.
