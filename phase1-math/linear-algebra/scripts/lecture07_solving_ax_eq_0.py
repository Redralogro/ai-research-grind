"""
Lecture 7: Solving Ax = 0 — Pivot Variables, Special Solutions
MIT 18.06 Linear Algebra (Gilbert Strang)

Scenes:
  1. Lecture7_EliminationToEchelon  — A → U via elimination
  2. Lecture7_ReducedRowEchelon     — U → R (rref)
  3. Lecture7_SpecialSolutions      — Special solutions from free variables
  4. Lecture7_NullspaceStructure    — Nullspace = span of special solutions
"""

from manim import *


# ── Shared colours ──────────────────────────────────────────────────
PIVOT_COLOR = YELLOW
FREE_COLOR = TEAL
HIGHLIGHT = RED
LABEL_COLOR = BLUE


class Lecture7_EliminationToEchelon(Scene):
    """Show A → U via elimination, identify pivots and free columns."""

    def construct(self):
        # ── Title ──
        title = Text("Lecture 7: Solving Ax = 0", font_size=40).to_edge(UP)
        subtitle = Text(
            "Elimination → Echelon Form", font_size=28, color=GRAY
        ).next_to(title, DOWN, buff=0.2)
        self.play(Write(title), FadeIn(subtitle))
        self.wait()

        # ── Matrix A ──
        a_label = MathTex("A", "=", font_size=42).shift(LEFT * 4.5 + UP * 0.5)
        A = Matrix(
            [[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).next_to(a_label, RIGHT, buff=0.2)
        self.play(Write(a_label), Write(A))
        self.wait()

        # ── Step 1: R2 ← R2 − 2R1 ──
        step1 = MathTex(
            r"R_2 \leftarrow R_2 - 2R_1", font_size=30, color=HIGHLIGHT
        ).to_edge(DOWN, buff=1.5)
        self.play(Write(step1))
        self.wait(0.5)

        A1 = Matrix(
            [[1, 2, 2, 2], [0, 0, 2, 4], [3, 6, 8, 10]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).move_to(A)
        self.play(Transform(A, A1))
        self.wait()

        # ── Step 2: R3 ← R3 − 3R1 ──
        step2 = MathTex(
            r"R_3 \leftarrow R_3 - 3R_1", font_size=30, color=HIGHLIGHT
        ).move_to(step1)
        self.play(Transform(step1, step2))
        self.wait(0.5)

        A2 = Matrix(
            [[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 2, 4]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).move_to(A)
        self.play(Transform(A, A2))
        self.wait()

        # ── Step 3: R3 ← R3 − R2 ──
        step3 = MathTex(
            r"R_3 \leftarrow R_3 - R_2", font_size=30, color=HIGHLIGHT
        ).move_to(step1)
        self.play(Transform(step1, step3))
        self.wait(0.5)

        U_mat = Matrix(
            [[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).move_to(A)
        self.play(Transform(A, U_mat))
        self.wait()
        self.play(FadeOut(step1))

        # ── Label U ──
        u_label = MathTex("U", "=", font_size=42, color=PIVOT_COLOR).move_to(a_label)
        self.play(Transform(a_label, u_label))
        self.wait()

        # ── Highlight pivots ──
        pivot_note = Text(
            "Pivots in columns 1 & 3", font_size=26, color=PIVOT_COLOR
        ).to_edge(DOWN, buff=1.5)
        # Pivot (0,0) → entry index 0, pivot (1,2) → entry index 6
        pivot_entries = VGroup(
            U_mat.get_entries()[0],   # row0 col0: 1
            U_mat.get_entries()[6],   # row1 col2: 2
        )
        boxes = VGroup(*[
            SurroundingRectangle(e, color=PIVOT_COLOR, buff=0.1)
            for e in pivot_entries
        ])
        self.play(Create(boxes), Write(pivot_note))
        self.wait()

        # ── Highlight free columns ──
        free_note = Text(
            "Free variables: x₂, x₄ (columns 2 & 4)",
            font_size=26,
            color=FREE_COLOR,
        ).next_to(pivot_note, DOWN, buff=0.3)
        free_cols = VGroup(
            # Column 2: entries 1,5,9  |  Column 4: entries 3,7,11
            *[U_mat.get_entries()[i] for i in [1, 5, 9]],
            *[U_mat.get_entries()[i] for i in [3, 7, 11]],
        )
        free_boxes = VGroup(*[
            SurroundingRectangle(e, color=FREE_COLOR, buff=0.1)
            for e in free_cols
        ])
        self.play(Create(free_boxes), Write(free_note))
        self.wait(2)


class Lecture7_ReducedRowEchelon(Scene):
    """U → R (rref): make pivots 1, clear above pivots."""

    def construct(self):
        title = Text("Reduced Row Echelon Form (rref)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait()

        # ── U ──
        u_label = MathTex("U", "=", font_size=42).shift(LEFT * 4.5 + UP * 0.5)
        U = Matrix(
            [[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).next_to(u_label, RIGHT, buff=0.2)
        self.play(Write(u_label), Write(U))
        self.wait()

        # ── Step 1: divide R2 by 2 ──
        step = MathTex(
            r"R_2 \leftarrow \tfrac{1}{2}\,R_2", font_size=30, color=HIGHLIGHT
        ).to_edge(DOWN, buff=1.8)
        self.play(Write(step))
        U1 = Matrix(
            [[1, 2, 2, 2], [0, 0, 1, 2], [0, 0, 0, 0]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).move_to(U)
        self.play(Transform(U, U1))
        self.wait()

        # ── Step 2: R1 ← R1 − 2R2 ──
        step2 = MathTex(
            r"R_1 \leftarrow R_1 - 2R_2", font_size=30, color=HIGHLIGHT
        ).move_to(step)
        self.play(Transform(step, step2))
        R_mat = Matrix(
            [[1, 2, 0, -2], [0, 0, 1, 2], [0, 0, 0, 0]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e)),
        ).move_to(U)
        self.play(Transform(U, R_mat))
        self.wait()
        self.play(FadeOut(step))

        # ── Label R ──
        r_label = MathTex("R", "=", font_size=42, color=PIVOT_COLOR).move_to(u_label)
        self.play(Transform(u_label, r_label))
        self.wait()

        # ── Show block structure  R = [I  F] with zero row ──
        block_text = MathTex(
            r"R = \begin{pmatrix} I & F \\ 0 & 0 \end{pmatrix}",
            font_size=36,
        ).shift(DOWN * 2)
        detail = MathTex(
            r"I = \begin{pmatrix}1&0\\0&1\end{pmatrix},\quad"
            r"F = \begin{pmatrix}2&-2\\0&2\end{pmatrix}",
            font_size=32,
            color=FREE_COLOR,
        ).next_to(block_text, DOWN, buff=0.3)
        note = Text(
            "Pivot columns ↔ I block, Free columns ↔ F block",
            font_size=24,
            color=GRAY,
        ).next_to(detail, DOWN, buff=0.3)
        self.play(Write(block_text))
        self.wait()
        self.play(Write(detail), Write(note))
        self.wait(2)


class Lecture7_SpecialSolutions(Scene):
    """Find special solutions by setting free variables to 0/1."""

    def construct(self):
        title = Text("Special Solutions", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Rx = 0 system ──
        system = MathTex(
            r"Rx = 0 \;\Longrightarrow\;"
            r"\begin{cases}"
            r"x_1 + 2x_2 - 2x_4 = 0 \\"
            r"x_3 + 2x_4 = 0"
            r"\end{cases}",
            font_size=30,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(system))
        self.wait()

        free_label = Text(
            "Free variables: x₂, x₄", font_size=26, color=FREE_COLOR
        ).next_to(system, DOWN, buff=0.4)
        self.play(Write(free_label))
        self.wait()

        # ── Special solution 1 ──
        s1_title = Text("Special solution 1:", font_size=26).shift(
            LEFT * 3 + DOWN * 0.8
        )
        s1_set = MathTex(
            r"x_2 = 1,\; x_4 = 0", font_size=28, color=FREE_COLOR
        ).next_to(s1_title, DOWN, buff=0.2)
        s1_solve = MathTex(
            r"\Rightarrow x_3 = 0,\; x_1 = -2", font_size=28
        ).next_to(s1_set, DOWN, buff=0.15)
        s1_vec = MathTex(
            r"s_1 = \begin{pmatrix}-2\\1\\0\\0\end{pmatrix}",
            font_size=34,
            color=PIVOT_COLOR,
        ).next_to(s1_solve, DOWN, buff=0.25)

        self.play(Write(s1_title))
        self.play(Write(s1_set))
        self.play(Write(s1_solve))
        self.play(Write(s1_vec))
        self.wait()

        # ── Special solution 2 ──
        s2_title = Text("Special solution 2:", font_size=26).shift(
            RIGHT * 3 + DOWN * 0.8
        )
        s2_set = MathTex(
            r"x_2 = 0,\; x_4 = 1", font_size=28, color=FREE_COLOR
        ).next_to(s2_title, DOWN, buff=0.2)
        s2_solve = MathTex(
            r"\Rightarrow x_3 = -2,\; x_1 = 2", font_size=28
        ).next_to(s2_set, DOWN, buff=0.15)
        s2_vec = MathTex(
            r"s_2 = \begin{pmatrix}2\\0\\-2\\1\end{pmatrix}",
            font_size=34,
            color=PIVOT_COLOR,
        ).next_to(s2_solve, DOWN, buff=0.25)

        self.play(Write(s2_title))
        self.play(Write(s2_set))
        self.play(Write(s2_solve))
        self.play(Write(s2_vec))
        self.wait(2)


class Lecture7_NullspaceStructure(Scene):
    """Nullspace = span of special solutions; rank + nullity = n."""

    def construct(self):
        title = Text("Nullspace Structure", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Nullspace formula ──
        ns_formula = MathTex(
            r"N(A) = c_1",
            r"\begin{pmatrix}-2\\1\\0\\0\end{pmatrix}",
            r"+ \; c_2",
            r"\begin{pmatrix}2\\0\\-2\\1\end{pmatrix}",
            font_size=34,
        ).next_to(title, DOWN, buff=0.6)
        ns_formula[1].set_color(PIVOT_COLOR)
        ns_formula[3].set_color(PIVOT_COLOR)
        self.play(Write(ns_formula))
        self.wait()

        # ── Nullspace matrix ──
        null_mat = MathTex(
            r"N = \begin{pmatrix}-F \\ I\end{pmatrix}"
            r"= \begin{pmatrix}-2 & 2 \\ 1 & 0 \\ 0 & -2 \\ 0 & 1\end{pmatrix}",
            font_size=32,
        ).next_to(ns_formula, DOWN, buff=0.5)
        note = Text(
            "Columns of N are the special solutions  (RN = 0)",
            font_size=24,
            color=GRAY,
        ).next_to(null_mat, DOWN, buff=0.3)
        self.play(Write(null_mat))
        self.play(Write(note))
        self.wait()

        # ── Rank–nullity theorem ──
        rank_box = VGroup(
            MathTex(r"\text{rank}(A) = r = 2", font_size=30),
            MathTex(r"\text{nullity} = n - r = 4 - 2 = 2", font_size=30),
            MathTex(
                r"\text{rank} + \text{nullity} = n", font_size=30, color=PIVOT_COLOR
            ),
        ).arrange(DOWN, buff=0.25).next_to(note, DOWN, buff=0.5)
        box = SurroundingRectangle(rank_box, color=PIVOT_COLOR, buff=0.25)
        self.play(Write(rank_box), Create(box))
        self.wait(2)
