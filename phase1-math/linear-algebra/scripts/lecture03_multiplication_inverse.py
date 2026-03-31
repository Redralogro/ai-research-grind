"""
MIT 18.06 Linear Algebra — Lecture 3: Multiplication and Inverse Matrices
Following Gilbert Strang's lecture.

Scenes:
  1. Lecture3_DotProductView     — Row of A · Column of B = one entry cᵢⱼ
  2. Lecture3_ColumnView         — A × (columns of B) = columns of C
  3. Lecture3_RowView            — (Rows of A) × B = rows of C
  4. Lecture3_OuterProductView   — (Col of A)(Row of B) = rank-1 matrix, sum
  5. Lecture3_GaussJordan        — [A|I] → [I|A⁻¹] step by step
  6. Lecture3_SingularNoInverse  — Ax=0 with nonzero x → no inverse
"""

from manim import *
import numpy as np


# ── helpers ──────────────────────────────────────────────────────────────────
def hl_entry(mat, r, c, color=YELLOW, buff=0.08):
    """SurroundingRectangle around entry (r,c) in a Matrix mobject."""
    n_cols = len(mat.get_columns())
    entry = mat.get_entries()[r * n_cols + c]
    return SurroundingRectangle(entry, color=color, buff=buff)


def hl_row(mat, r, color=YELLOW, buff=0.08):
    """SurroundingRectangle around row r."""
    row_entries = mat.get_rows()[r]
    return SurroundingRectangle(row_entries, color=color, buff=buff)


def hl_col(mat, c, color=YELLOW, buff=0.08):
    """SurroundingRectangle around column c."""
    col_entries = mat.get_columns()[c]
    return SurroundingRectangle(col_entries, color=color, buff=buff)


# ---------------------------------------------------------------------------
# Scene 1 — Dot-Product View  (Way 1)
# (row i of A) · (col j of B) = cᵢⱼ
# ---------------------------------------------------------------------------
class Lecture3_DotProductView(Scene):
    def construct(self):
        title = Text("Lecture 3 — Way 1: Dot Product", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = MathTex(
            r"c_{ij} = (\text{row } i \text{ of } A) \cdot (\text{col } j \text{ of } B)",
            font_size=30,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # A (2×3)  B (3×2)
        A = Matrix(
            [["1", "2", "3"],
             ["4", "5", "6"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).shift(LEFT * 3.5)
        B = Matrix(
            [["7", "8"],
             ["9", "10"],
             ["11", "12"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).next_to(A, RIGHT, buff=0.6)
        eq = MathTex("=", font_size=32).next_to(B, RIGHT, buff=0.4)
        C = Matrix(
            [["58", "64"],
             ["139", "154"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).next_to(eq, RIGHT, buff=0.4)

        a_label = MathTex("A", font_size=30).next_to(A, UP, buff=0.15)
        b_label = MathTex("B", font_size=30).next_to(B, UP, buff=0.15)
        c_label = MathTex("C", font_size=30).next_to(C, UP, buff=0.15)

        self.play(Write(A), Write(a_label))
        self.play(Write(B), Write(b_label))
        self.play(Write(eq), Write(C), Write(c_label))

        # Highlight row 0 of A, col 1 of B → c₀₁ = 64
        row_hl = hl_row(A, 0, BLUE)
        col_hl = hl_col(B, 1, RED)
        entry_hl = hl_entry(C, 0, 1, GREEN)

        self.play(Create(row_hl), Create(col_hl))
        dot_calc = MathTex(
            r"c_{12} = 1\!\cdot\!8 + 2\!\cdot\!10 + 3\!\cdot\!12 = 64",
            font_size=28, color=GREEN,
        ).to_edge(DOWN, buff=0.6)
        self.play(Create(entry_hl), Write(dot_calc))
        self.wait(1.5)

        # Highlight row 1, col 0 → c₁₀ = 139
        row_hl2 = hl_row(A, 1, BLUE)
        col_hl2 = hl_col(B, 0, RED)
        entry_hl2 = hl_entry(C, 1, 0, GREEN)
        dot_calc2 = MathTex(
            r"c_{21} = 4\!\cdot\!7 + 5\!\cdot\!9 + 6\!\cdot\!11 = 139",
            font_size=28, color=GREEN,
        ).to_edge(DOWN, buff=0.6)
        self.play(
            ReplacementTransform(row_hl, row_hl2),
            ReplacementTransform(col_hl, col_hl2),
            ReplacementTransform(entry_hl, entry_hl2),
            ReplacementTransform(dot_calc, dot_calc2),
        )
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 2 — Column View  (Way 2)
# A × (col j of B) = col j of C
# ---------------------------------------------------------------------------
class Lecture3_ColumnView(Scene):
    def construct(self):
        title = Text("Lecture 3 — Way 2: Matrix × Column", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = MathTex(
            r"A \times (\text{col } j \text{ of } B) = \text{col } j \text{ of } C",
            font_size=30,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        A = Matrix(
            [["1", "2", "3"],
             ["4", "5", "6"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).shift(LEFT * 3.5)
        B = Matrix(
            [["7", "8"],
             ["9", "10"],
             ["11", "12"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).next_to(A, RIGHT, buff=0.6)
        eq = MathTex("=", font_size=32).next_to(B, RIGHT, buff=0.4)
        C = Matrix(
            [["58", "64"],
             ["139", "154"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).next_to(eq, RIGHT, buff=0.4)

        self.play(Write(A), Write(B), Write(eq), Write(C))

        # Highlight column 0 of B and column 0 of C
        col_b_hl = hl_col(B, 0, RED)
        col_c_hl = hl_col(C, 0, GREEN)
        a_hl = SurroundingRectangle(A, color=BLUE, buff=0.1)
        self.play(Create(a_hl), Create(col_b_hl))

        explanation = MathTex(
            r"A \begin{bmatrix}7\\9\\11\end{bmatrix}"
            r"= 7\begin{bmatrix}1\\4\end{bmatrix}"
            r"+ 9\begin{bmatrix}2\\5\end{bmatrix}"
            r"+ 11\begin{bmatrix}3\\6\end{bmatrix}"
            r"= \begin{bmatrix}58\\139\end{bmatrix}",
            font_size=26,
        ).to_edge(DOWN, buff=0.5)
        self.play(Create(col_c_hl), Write(explanation))

        note = Text(
            "Each column of C is a combination of columns of A",
            font_size=24, color=YELLOW,
        ).next_to(explanation, UP, buff=0.3)
        self.play(Write(note))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 3 — Row View  (Way 3)
# (row i of A) × B = row i of C
# ---------------------------------------------------------------------------
class Lecture3_RowView(Scene):
    def construct(self):
        title = Text("Lecture 3 — Way 3: Row × Matrix", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = MathTex(
            r"(\text{row } i \text{ of } A) \times B = \text{row } i \text{ of } C",
            font_size=30,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        A = Matrix(
            [["1", "2", "3"],
             ["4", "5", "6"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).shift(LEFT * 3.5)
        B = Matrix(
            [["7", "8"],
             ["9", "10"],
             ["11", "12"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).next_to(A, RIGHT, buff=0.6)
        eq = MathTex("=", font_size=32).next_to(B, RIGHT, buff=0.4)
        C = Matrix(
            [["58", "64"],
             ["139", "154"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).next_to(eq, RIGHT, buff=0.4)

        self.play(Write(A), Write(B), Write(eq), Write(C))

        # Highlight row 0 of A → row 0 of C
        row_a_hl = hl_row(A, 0, BLUE)
        row_c_hl = hl_row(C, 0, GREEN)
        b_hl = SurroundingRectangle(B, color=RED, buff=0.1)

        self.play(Create(row_a_hl), Create(b_hl))

        explanation = MathTex(
            r"\begin{bmatrix}1 & 2 & 3\end{bmatrix} B"
            r"= 1\begin{bmatrix}7 & 8\end{bmatrix}"
            r"+ 2\begin{bmatrix}9 & 10\end{bmatrix}"
            r"+ 3\begin{bmatrix}11 & 12\end{bmatrix}"
            r"= \begin{bmatrix}58 & 64\end{bmatrix}",
            font_size=26,
        ).to_edge(DOWN, buff=0.5)
        self.play(Create(row_c_hl), Write(explanation))

        note = Text(
            "Each row of C is a combination of rows of B",
            font_size=24, color=YELLOW,
        ).next_to(explanation, UP, buff=0.3)
        self.play(Write(note))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 4 — Outer-Product View  (Way 4)
# AB = sum of (col k of A)(row k of B)  — each is rank-1
# ---------------------------------------------------------------------------
class Lecture3_OuterProductView(Scene):
    def construct(self):
        title = Text("Lecture 3 — Way 4: Outer Product (Rank-1 Sum)", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = MathTex(
            r"AB = \sum_{k} (\text{col } k \text{ of } A)"
            r"(\text{row } k \text{ of } B)",
            font_size=28,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Use simple 2×2 for clarity
        # A = [[1,2],[3,4]]   B = [[5,6],[7,8]]
        # AB = [1;3][5,6] + [2;4][7,8]
        #    = [[5,6],[15,18]] + [[14,16],[28,32]]
        #    = [[19,22],[43,50]]

        eq_parts = MathTex(
            r"\underbrace{"
            r"\begin{bmatrix}1\\3\end{bmatrix}"
            r"\begin{bmatrix}5 & 6\end{bmatrix}"
            r"}_{\text{rank 1}}"
            r"+\;"
            r"\underbrace{"
            r"\begin{bmatrix}2\\4\end{bmatrix}"
            r"\begin{bmatrix}7 & 8\end{bmatrix}"
            r"}_{\text{rank 1}}",
            font_size=30,
        ).shift(UP * 0.2)
        self.play(Write(eq_parts))

        equals_line = MathTex(r"=", font_size=30)

        outer1 = Matrix(
            [["5", "6"],
             ["15", "18"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).set_color(BLUE)
        plus = MathTex(r"+", font_size=30)
        outer2 = Matrix(
            [["14", "16"],
             ["28", "32"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).set_color(RED)
        eq2 = MathTex(r"=", font_size=30)
        result = Matrix(
            [["19", "22"],
             ["43", "50"]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).set_color(GREEN)

        bottom_row = VGroup(equals_line, outer1, plus, outer2, eq2, result).arrange(
            RIGHT, buff=0.25
        )
        bottom_row.shift(DOWN * 1.8)
        self.play(Write(equals_line), Write(outer1))
        self.play(Write(plus), Write(outer2))
        self.play(Write(eq2), Write(result))

        note = MathTex(
            r"AB = C", font_size=32, color=YELLOW,
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(note))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 5 — Gauss-Jordan:  [A | I] → [I | A⁻¹]
# A = [[1, 3], [2, 7]]   →   A⁻¹ = [[7, -3], [-2, 1]]
# ---------------------------------------------------------------------------
class Lecture3_GaussJordan(Scene):
    def construct(self):
        title = Text("Lecture 3 — Gauss-Jordan → A⁻¹", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        idea = MathTex(
            r"[A \mid I] \;\xrightarrow{\text{row reduce}}\; [I \mid A^{-1}]",
            font_size=30,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(idea))

        # Step 0: [A | I]
        def aug_mat(rows, color=WHITE):
            return Matrix(
                rows,
                left_bracket="[", right_bracket="]",
                h_buff=1.0,
                element_to_mobject_config={"font_size": 32},
            ).set_color(color)

        def aug_line(mat):
            """Vertical bar between column 1 and column 2 of a 2×4 matrix."""
            cols = mat.get_columns()
            mid = (cols[1].get_right() + cols[2].get_left()) / 2
            return Line(
                mid + UP * 0.6, mid + DOWN * 0.6,
                color=GREY, stroke_width=2,
            )

        m0 = aug_mat([
            ["1", "3", "1", "0"],
            ["2", "7", "0", "1"],
        ])
        l0 = aug_line(m0)
        label0 = MathTex(r"[A \mid I]", font_size=28).next_to(m0, UP, buff=0.2)
        g0 = VGroup(m0, l0, label0)
        self.play(Write(m0), Create(l0), Write(label0))

        # Step 1: R₂ ← R₂ - 2R₁
        step1_text = MathTex(
            r"R_2 \leftarrow R_2 - 2R_1", font_size=26, color=ORANGE
        ).to_edge(RIGHT, buff=0.8).shift(UP * 0.5)
        self.play(Write(step1_text))

        m1 = aug_mat([
            ["1", "3", "1", "0"],
            ["0", "1", "-2", "1"],
        ])
        l1 = aug_line(m1)
        self.play(
            ReplacementTransform(m0, m1),
            ReplacementTransform(l0, l1),
            FadeOut(label0),
        )
        self.wait(0.5)

        # Step 2: R₁ ← R₁ - 3R₂  (back-eliminate to get I on left)
        step2_text = MathTex(
            r"R_1 \leftarrow R_1 - 3R_2", font_size=26, color=ORANGE
        ).next_to(step1_text, DOWN, buff=0.4)
        self.play(Write(step2_text))

        m2 = aug_mat([
            ["1", "0", "7", "-3"],
            ["0", "1", "-2", "1"],
        ])
        l2 = aug_line(m2)
        label2 = MathTex(r"[I \mid A^{-1}]", font_size=28, color=GREEN)
        label2.next_to(m2, UP, buff=0.2)
        self.play(
            ReplacementTransform(m1, m2),
            ReplacementTransform(l1, l2),
            Write(label2),
        )

        # Highlight the inverse on the right
        inv_entries = VGroup(
            m2.get_columns()[2], m2.get_columns()[3],
        )
        inv_box = SurroundingRectangle(inv_entries, color=GREEN, buff=0.12)
        self.play(Create(inv_box))

        inv_result = MathTex(
            r"A^{-1} = \begin{bmatrix} 7 & -3 \\ -2 & 1 \end{bmatrix}",
            font_size=32, color=GREEN,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(inv_result))

        # Verify
        verify = MathTex(
            r"A^{-1}A = "
            r"\begin{bmatrix}7&-3\\-2&1\end{bmatrix}"
            r"\begin{bmatrix}1&3\\2&7\end{bmatrix}"
            r"= \begin{bmatrix}1&0\\0&1\end{bmatrix} = I",
            font_size=26, color=TEAL,
        ).next_to(inv_result, UP, buff=0.3)
        self.play(Write(verify))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 6 — Singular Matrix: No Inverse
# If Ax = 0 has a nonzero solution x, then A has no inverse.
# ---------------------------------------------------------------------------
class Lecture3_SingularNoInverse(Scene):
    def construct(self):
        title = Text("Lecture 3 — Singular: No Inverse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # The key argument
        argument = VGroup(
            MathTex(r"\text{Suppose } A\mathbf{x} = \mathbf{0}", font_size=30),
            MathTex(r"\text{with } \mathbf{x} \neq \mathbf{0}.", font_size=30),
        ).arrange(RIGHT, buff=0.2).next_to(title, DOWN, buff=0.4)
        self.play(Write(argument))

        # Proof by contradiction
        proof = VGroup(
            MathTex(
                r"\text{If } A^{-1} \text{ existed: }",
                font_size=28,
            ),
            MathTex(
                r"A^{-1}(A\mathbf{x}) = A^{-1}\mathbf{0}",
                font_size=28,
            ),
            MathTex(
                r"\Rightarrow\; \mathbf{x} = \mathbf{0}",
                font_size=28, color=RED,
            ),
            MathTex(
                r"\text{Contradiction! So } A^{-1} \text{ cannot exist.}",
                font_size=28, color=RED,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        for line in proof:
            self.play(Write(line))
            self.wait(0.4)

        self.wait(0.5)

        # Concrete example
        example_title = Text("Example:", font_size=26, color=YELLOW)
        example_title.shift(DOWN * 1.0 + LEFT * 4)
        self.play(Write(example_title))

        a_mat = MathTex(
            r"A = \begin{bmatrix} 1 & 3 \\ 2 & 6 \end{bmatrix}",
            font_size=30,
        ).next_to(example_title, RIGHT, buff=0.4)
        self.play(Write(a_mat))

        x_vec = MathTex(
            r"\mathbf{x} = \begin{bmatrix} 3 \\ -1 \end{bmatrix} \neq \mathbf{0}",
            font_size=30,
        ).next_to(a_mat, RIGHT, buff=0.6)
        self.play(Write(x_vec))

        check = MathTex(
            r"A\mathbf{x} = \begin{bmatrix}1\!\cdot\!3 + 3\!\cdot\!(-1)"
            r"\\ 2\!\cdot\!3 + 6\!\cdot\!(-1)\end{bmatrix}"
            r"= \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            font_size=28,
        ).next_to(VGroup(a_mat, x_vec), DOWN, buff=0.4)
        self.play(Write(check))

        conclusion = Text(
            "Column 2 = 3 × Column 1 → columns are dependent → singular",
            font_size=24, color=RED,
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(conclusion))
        self.wait(2)
