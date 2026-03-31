"""
Lecture 10: The Four Fundamental Subspaces
MIT 18.06 Linear Algebra (Gilbert Strang)

Scenes:
  1. Lecture10_FourSubspaces   — Title scene: all four with dimensions
  2. Lecture10_DimensionCount  — r + (n-r) = n and r + (m-r) = m
  3. Lecture10_FindingBases    — Concrete bases for each subspace
  4. Lecture10_BigPicture      — The big picture diagram
"""

from manim import *

PIVOT_COLOR = YELLOW
FREE_COLOR = TEAL
COL_COLOR = BLUE
NULL_COLOR = GREEN
ROW_COLOR = RED_B
LNULL_COLOR = ORANGE


class Lecture10_FourSubspaces(Scene):
    """Title scene showing all four subspaces with their dimensions."""

    def construct(self):
        title = Text(
            "Lecture 10: The Four Fundamental Subspaces", font_size=38
        ).to_edge(UP)
        self.play(Write(title))

        setup = MathTex(
            r"A \text{ is } m \times n \text{ with rank } r",
            font_size=30,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(setup))
        self.wait()

        # ── Four subspaces ──
        subspaces = VGroup(
            VGroup(
                MathTex(r"1.\;\; C(A)", font_size=30, color=COL_COLOR),
                MathTex(
                    r"\text{Column space, in } \mathbb{R}^m,\; \dim = r",
                    font_size=26,
                ),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"2.\;\; N(A)", font_size=30, color=NULL_COLOR),
                MathTex(
                    r"\text{Nullspace, in } \mathbb{R}^n,\; \dim = n - r",
                    font_size=26,
                ),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"3.\;\; C(A^T)", font_size=30, color=ROW_COLOR),
                MathTex(
                    r"\text{Row space, in } \mathbb{R}^n,\; \dim = r",
                    font_size=26,
                ),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"4.\;\; N(A^T)", font_size=30, color=LNULL_COLOR),
                MathTex(
                    r"\text{Left nullspace, in } \mathbb{R}^m,\; \dim = m - r",
                    font_size=26,
                ),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(setup, DOWN, buff=0.5)

        for ss in subspaces:
            self.play(Write(ss))
            self.wait(0.3)

        self.wait()

        # ── Orthogonality preview ──
        orth = VGroup(
            MathTex(
                r"C(A^T) \perp N(A) \;\;\text{in } \mathbb{R}^n",
                font_size=26,
                color=PIVOT_COLOR,
            ),
            MathTex(
                r"C(A) \perp N(A^T) \;\;\text{in } \mathbb{R}^m",
                font_size=26,
                color=PIVOT_COLOR,
            ),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(orth, color=PIVOT_COLOR, buff=0.15)
        self.play(Write(orth), Create(box))
        self.wait(2)


class Lecture10_DimensionCount(Scene):
    """Show r + (n-r) = n and r + (m-r) = m with a concrete example."""

    def construct(self):
        title = Text("Dimension Counting", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Concrete example ──
        example = MathTex(
            r"A = \begin{pmatrix}1&2&2&2\\2&4&6&8\\3&6&8&10\end{pmatrix}"
            r"\quad m=3,\; n=4,\; r=2",
            font_size=28,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait()

        # ── Rⁿ split ──
        rn_title = MathTex(
            r"\mathbb{R}^n = \mathbb{R}^4:", font_size=28
        ).next_to(example, DOWN, buff=0.6).shift(LEFT * 2)
        rn_eq = MathTex(
            r"\underbrace{\dim C(A^T)}_{r=2}"
            r"+ \underbrace{\dim N(A)}_{n-r=2}"
            r"= n = 4",
            font_size=28,
        ).next_to(rn_title, RIGHT, buff=0.3)

        self.play(Write(rn_title), Write(rn_eq))
        self.wait()

        # ── Rᵐ split ──
        rm_title = MathTex(
            r"\mathbb{R}^m = \mathbb{R}^3:", font_size=28
        ).next_to(rn_title, DOWN, buff=0.6)
        rm_eq = MathTex(
            r"\underbrace{\dim C(A)}_{r=2}"
            r"+ \underbrace{\dim N(A^T)}_{m-r=1}"
            r"= m = 3",
            font_size=28,
        ).next_to(rm_title, RIGHT, buff=0.3)

        self.play(Write(rm_title), Write(rm_eq))
        self.wait()

        # ── Visual: two bars ──
        bar_rn = Rectangle(width=5, height=0.6, color=WHITE).shift(DOWN * 1.8)
        bar_rn_row = Rectangle(width=2.5, height=0.6, color=ROW_COLOR, fill_opacity=0.4)
        bar_rn_null = Rectangle(
            width=2.5, height=0.6, color=NULL_COLOR, fill_opacity=0.4
        )
        bar_rn_row.next_to(bar_rn.get_left(), RIGHT, buff=0)
        bar_rn_null.next_to(bar_rn_row, RIGHT, buff=0)
        rn_lab = MathTex(r"\mathbb{R}^4", font_size=22).next_to(bar_rn, LEFT, buff=0.2)
        row_lab = MathTex(r"C(A^T)\;r=2", font_size=18, color=ROW_COLOR).move_to(
            bar_rn_row
        )
        null_lab = MathTex(r"N(A)\;n{-}r=2", font_size=18, color=NULL_COLOR).move_to(
            bar_rn_null
        )

        bar_rm = Rectangle(width=5, height=0.6, color=WHITE).shift(DOWN * 2.8)
        bar_rm_col = Rectangle(
            width=5 * 2 / 3, height=0.6, color=COL_COLOR, fill_opacity=0.4
        )
        bar_rm_lnull = Rectangle(
            width=5 * 1 / 3, height=0.6, color=LNULL_COLOR, fill_opacity=0.4
        )
        bar_rm_col.next_to(bar_rm.get_left(), RIGHT, buff=0)
        bar_rm_lnull.next_to(bar_rm_col, RIGHT, buff=0)
        rm_lab = MathTex(r"\mathbb{R}^3", font_size=22).next_to(bar_rm, LEFT, buff=0.2)
        col_lab = MathTex(r"C(A)\;r=2", font_size=18, color=COL_COLOR).move_to(
            bar_rm_col
        )
        lnull_lab = MathTex(
            r"N(A^T)\;m{-}r=1", font_size=18, color=LNULL_COLOR
        ).move_to(bar_rm_lnull)

        self.play(
            Create(bar_rn),
            FadeIn(bar_rn_row),
            FadeIn(bar_rn_null),
            Write(rn_lab),
            Write(row_lab),
            Write(null_lab),
        )
        self.play(
            Create(bar_rm),
            FadeIn(bar_rm_col),
            FadeIn(bar_rm_lnull),
            Write(rm_lab),
            Write(col_lab),
            Write(lnull_lab),
        )
        self.wait(2)


class Lecture10_FindingBases(Scene):
    """Find basis for each of the four subspaces for Strang's 3x4 example."""

    def construct(self):
        title = Text("Bases for the Four Subspaces", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Matrix and rref ──
        mats = MathTex(
            r"A = \begin{pmatrix}1&2&2&2\\2&4&6&8\\3&6&8&10\end{pmatrix}"
            r"\;\;\xrightarrow{\text{rref}}\;\;"
            r"R = \begin{pmatrix}1&2&0&-2\\0&0&1&2\\0&0&0&0\end{pmatrix}",
            font_size=26,
        ).next_to(title, DOWN, buff=0.35)
        self.play(Write(mats))
        self.wait()

        # ── Four bases ──
        bases = VGroup(
            VGroup(
                MathTex(r"C(A):", font_size=26, color=COL_COLOR),
                MathTex(
                    r"\text{Pivot cols of } A:\;"
                    r"\begin{pmatrix}1\\2\\3\end{pmatrix},\;"
                    r"\begin{pmatrix}2\\6\\8\end{pmatrix}",
                    font_size=24,
                ),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"N(A):", font_size=26, color=NULL_COLOR),
                MathTex(
                    r"\text{Special solutions: }\;"
                    r"\begin{pmatrix}-2\\1\\0\\0\end{pmatrix},\;"
                    r"\begin{pmatrix}2\\0\\-2\\1\end{pmatrix}",
                    font_size=24,
                ),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"C(A^T):", font_size=26, color=ROW_COLOR),
                MathTex(
                    r"\text{Nonzero rows of } R:\;"
                    r"\begin{pmatrix}1\\2\\0\\-2\end{pmatrix},\;"
                    r"\begin{pmatrix}0\\0\\1\\2\end{pmatrix}",
                    font_size=24,
                ),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"N(A^T):", font_size=26, color=LNULL_COLOR),
                MathTex(
                    r"\text{From } EA = R:\;"
                    r"\begin{pmatrix}-1\\1\\-1\end{pmatrix}",
                    font_size=24,
                ),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).next_to(mats, DOWN, buff=0.4)

        for b in bases:
            self.play(Write(b))
            self.wait(0.5)

        # ── Verification of left nullspace ──
        check = MathTex(
            r"A^T y = 0 \;\;\text{check: } "
            r"\begin{pmatrix}1&2&3\\2&4&6\\2&6&8\\2&8&10\end{pmatrix}"
            r"\begin{pmatrix}-1\\1\\-1\end{pmatrix}"
            r"= \begin{pmatrix}0\\0\\0\\0\end{pmatrix}\;\checkmark",
            font_size=22,
            color=GRAY,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(check))
        self.wait(2)


class Lecture10_BigPicture(Scene):
    """The big picture: Rⁿ = row space + nullspace, Rᵐ = col space + left nullspace,
    A maps between them."""

    def construct(self):
        title = Text("The Big Picture of Linear Algebra", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Left: Rⁿ ──
        rn_box = RoundedRectangle(
            width=4.5, height=5, corner_radius=0.2, color=WHITE
        ).shift(LEFT * 3 + DOWN * 0.5)
        rn_label = MathTex(r"\mathbb{R}^n", font_size=30).next_to(
            rn_box, UP, buff=0.1
        )

        # Row space (top half)
        row_region = RoundedRectangle(
            width=3.8, height=2, corner_radius=0.15, color=ROW_COLOR, fill_opacity=0.15
        ).move_to(rn_box.get_center() + UP * 1.1)
        row_label = MathTex(
            r"C(A^T)", font_size=26, color=ROW_COLOR
        ).move_to(row_region.get_center() + UP * 0.5)
        row_dim = MathTex(
            r"\dim = r", font_size=22, color=ROW_COLOR
        ).next_to(row_label, DOWN, buff=0.1)

        # Nullspace (bottom half)
        null_region = RoundedRectangle(
            width=3.8, height=2, corner_radius=0.15, color=NULL_COLOR, fill_opacity=0.15
        ).move_to(rn_box.get_center() + DOWN * 1.1)
        null_label = MathTex(
            r"N(A)", font_size=26, color=NULL_COLOR
        ).move_to(null_region.get_center() + UP * 0.5)
        null_dim = MathTex(
            r"\dim = n - r", font_size=22, color=NULL_COLOR
        ).next_to(null_label, DOWN, buff=0.1)

        # Orthogonal symbol
        perp_left = MathTex(r"\perp", font_size=28).move_to(rn_box.get_center())

        # ── Right: Rᵐ ──
        rm_box = RoundedRectangle(
            width=4.5, height=5, corner_radius=0.2, color=WHITE
        ).shift(RIGHT * 3 + DOWN * 0.5)
        rm_label = MathTex(r"\mathbb{R}^m", font_size=30).next_to(
            rm_box, UP, buff=0.1
        )

        # Column space (top half)
        col_region = RoundedRectangle(
            width=3.8, height=2, corner_radius=0.15, color=COL_COLOR, fill_opacity=0.15
        ).move_to(rm_box.get_center() + UP * 1.1)
        col_label = MathTex(
            r"C(A)", font_size=26, color=COL_COLOR
        ).move_to(col_region.get_center() + UP * 0.5)
        col_dim = MathTex(
            r"\dim = r", font_size=22, color=COL_COLOR
        ).next_to(col_label, DOWN, buff=0.1)

        # Left nullspace (bottom half)
        lnull_region = RoundedRectangle(
            width=3.8, height=2, corner_radius=0.15, color=LNULL_COLOR, fill_opacity=0.15
        ).move_to(rm_box.get_center() + DOWN * 1.1)
        lnull_label = MathTex(
            r"N(A^T)", font_size=26, color=LNULL_COLOR
        ).move_to(lnull_region.get_center() + UP * 0.5)
        lnull_dim = MathTex(
            r"\dim = m - r", font_size=22, color=LNULL_COLOR
        ).next_to(lnull_label, DOWN, buff=0.1)

        # Orthogonal symbol
        perp_right = MathTex(r"\perp", font_size=28).move_to(rm_box.get_center())

        # ── Draw left side ──
        self.play(Create(rn_box), Write(rn_label))
        self.play(
            FadeIn(row_region), Write(row_label), Write(row_dim),
            FadeIn(null_region), Write(null_label), Write(null_dim),
            Write(perp_left),
        )
        self.wait()

        # ── Draw right side ──
        self.play(Create(rm_box), Write(rm_label))
        self.play(
            FadeIn(col_region), Write(col_label), Write(col_dim),
            FadeIn(lnull_region), Write(lnull_label), Write(lnull_dim),
            Write(perp_right),
        )
        self.wait()

        # ── Arrow: A maps row space → column space ──
        arrow_top = Arrow(
            row_region.get_right() + RIGHT * 0.1,
            col_region.get_left() + LEFT * 0.1,
            color=PIVOT_COLOR,
            stroke_width=3,
            buff=0.1,
        )
        a_label_top = MathTex(r"A", font_size=26, color=PIVOT_COLOR).next_to(
            arrow_top, UP, buff=0.1
        )
        self.play(GrowArrow(arrow_top), Write(a_label_top))
        self.wait(0.5)

        # ── Arrow: A maps nullspace → {0} ──
        zero_dot = Dot(
            rm_box.get_center() + DOWN * 1.1, color=PIVOT_COLOR, radius=0.06
        )
        arrow_bot = Arrow(
            null_region.get_right() + RIGHT * 0.1,
            zero_dot.get_center() + LEFT * 0.3,
            color=PIVOT_COLOR,
            stroke_width=3,
            buff=0.1,
        )
        a_label_bot = MathTex(r"A", font_size=26, color=PIVOT_COLOR).next_to(
            arrow_bot, DOWN, buff=0.1
        )
        zero_label = MathTex(r"\{0\}", font_size=22, color=PIVOT_COLOR).next_to(
            zero_dot, DOWN, buff=0.1
        )
        self.play(GrowArrow(arrow_bot), Write(a_label_bot))
        self.play(Create(zero_dot), Write(zero_label))
        self.wait()

        # ── Summary line ──
        summary = MathTex(
            r"\text{Row space } \xrightarrow{A} \text{ Column space}"
            r"\qquad\text{Nullspace } \xrightarrow{A} \{0\}",
            font_size=24,
        ).to_edge(DOWN, buff=0.3)
        box = SurroundingRectangle(summary, color=PIVOT_COLOR, buff=0.15)
        self.play(Write(summary), Create(box))
        self.wait(2)
