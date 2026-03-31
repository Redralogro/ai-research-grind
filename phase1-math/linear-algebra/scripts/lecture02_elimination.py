"""
MIT 18.06 Linear Algebra — Lecture 2: Elimination with Matrices
Following Gilbert Strang's lecture.

System:  x + 2y +  z =  2
        3x + 8y +  z = 12
              4y +  z =  2

Scenes:
  1. Lecture2_ForwardElimination    — Augmented matrix, pivots, elimination steps
  2. Lecture2_EliminationMatrices   — E₂₁ and E₃₂ as matrices, E₂₁ A demo
  3. Lecture2_BackSubstitution      — Solve upper triangular system bottom-up
  4. Lecture2_WhenEliminationFails  — Zero pivot → row exchange or singular
"""

from manim import *
import numpy as np


# ── helpers ──────────────────────────────────────────────────────────────────
def matrix_mob(entries, color=WHITE, font_size=34, left="[", right="]"):
    """Shortcut to build an IntegerMatrix (or MathTex-based Matrix)."""
    return Matrix(
        entries,
        left_bracket=left,
        right_bracket=right,
        element_to_mobject_config={"font_size": font_size},
    ).set_color(color)


def highlight_entry(mat, row, col, color=YELLOW, buff=0.08):
    """Return a SurroundingRectangle around a matrix entry (0-indexed)."""
    n_cols = len(mat.get_columns())
    entry = mat.get_entries()[row * n_cols + col]
    return SurroundingRectangle(entry, color=color, buff=buff)


# ---------------------------------------------------------------------------
# Scene 1 — Forward Elimination
# ---------------------------------------------------------------------------
class Lecture2_ForwardElimination(Scene):
    def construct(self):
        title = Text("Lecture 2 — Forward Elimination", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # ── Step 0: show the system ──────────────────────────────
        system = MathTex(
            r"x + 2y + z &= 2 \\",
            r"3x + 8y + z &= 12 \\",
            r"4y + z &= 2",
            font_size=32,
        ).shift(UP * 1.5)
        self.play(Write(system))
        self.wait()
        self.play(FadeOut(system))

        # ── Step 1: augmented matrix ─────────────────────────────
        aug0 = Matrix(
            [["1", "2", "1", "2"],
             ["3", "8", "1", "12"],
             ["0", "4", "1", "2"]],
            left_bracket="[",
            right_bracket="]",
            h_buff=1.2,
            element_to_mobject_config={"font_size": 34},
        )
        # Dividing line for augmented part
        aug0_line = Line(
            aug0.get_columns()[2].get_right() + RIGHT * 0.15 + UP * 0.8,
            aug0.get_columns()[2].get_right() + RIGHT * 0.15 + DOWN * 0.8,
            color=GREY,
            stroke_width=2,
        )
        aug_group0 = VGroup(aug0, aug0_line)
        aug_label = MathTex(r"[A \mid \mathbf{b}]", font_size=30).next_to(aug0, UP, buff=0.3)
        self.play(Write(aug0), Create(aug0_line), Write(aug_label))

        # Highlight pivot (1,1)
        piv1 = highlight_entry(aug0, 0, 0, YELLOW)
        piv_text1 = Text("pivot 1", font_size=22, color=YELLOW).next_to(piv1, LEFT, buff=0.4)
        self.play(Create(piv1), Write(piv_text1))
        self.wait(0.5)

        # ── Step 2: eliminate (2,1) — multiplier ℓ₂₁ = 3 ────────
        mult1 = MathTex(r"\ell_{21} = 3", font_size=28, color=ORANGE)
        mult1.to_edge(RIGHT, buff=1).shift(UP)
        step1_text = MathTex(
            r"R_2 \leftarrow R_2 - 3\,R_1", font_size=28, color=ORANGE
        ).next_to(mult1, DOWN, buff=0.3)
        self.play(Write(mult1), Write(step1_text))
        self.wait(0.5)

        # New matrix after step 1
        aug1 = Matrix(
            [["1", "2", "1", "2"],
             ["0", "2", "-2", "6"],
             ["0", "4", "1", "2"]],
            left_bracket="[",
            right_bracket="]",
            h_buff=1.2,
            element_to_mobject_config={"font_size": 34},
        )
        aug1_line = Line(
            aug1.get_columns()[2].get_right() + RIGHT * 0.15 + UP * 0.8,
            aug1.get_columns()[2].get_right() + RIGHT * 0.15 + DOWN * 0.8,
            color=GREY,
            stroke_width=2,
        )
        self.play(
            FadeOut(piv1), FadeOut(piv_text1), FadeOut(aug_label),
            ReplacementTransform(aug0, aug1),
            ReplacementTransform(aug0_line, aug1_line),
        )

        # Highlight pivot (2,2)
        piv2 = highlight_entry(aug1, 1, 1, YELLOW)
        piv_text2 = Text("pivot 2", font_size=22, color=YELLOW).next_to(piv2, LEFT, buff=0.4)
        self.play(Create(piv2), Write(piv_text2))

        # ── Step 3: eliminate (3,2) — multiplier ℓ₃₂ = 2 ────────
        mult2 = MathTex(r"\ell_{32} = 2", font_size=28, color=ORANGE)
        mult2.next_to(step1_text, DOWN, buff=0.5)
        step2_text = MathTex(
            r"R_3 \leftarrow R_3 - 2\,R_2", font_size=28, color=ORANGE
        ).next_to(mult2, DOWN, buff=0.3)
        self.play(Write(mult2), Write(step2_text))
        self.wait(0.5)

        # Final upper-triangular augmented matrix
        aug2 = Matrix(
            [["1", "2", "1", "2"],
             ["0", "2", "-2", "6"],
             ["0", "0", "5", "-10"]],
            left_bracket="[",
            right_bracket="]",
            h_buff=1.2,
            element_to_mobject_config={"font_size": 34},
        )
        aug2_line = Line(
            aug2.get_columns()[2].get_right() + RIGHT * 0.15 + UP * 0.8,
            aug2.get_columns()[2].get_right() + RIGHT * 0.15 + DOWN * 0.8,
            color=GREY,
            stroke_width=2,
        )
        self.play(
            FadeOut(piv2), FadeOut(piv_text2),
            ReplacementTransform(aug1, aug2),
            ReplacementTransform(aug1_line, aug2_line),
        )

        # Highlight pivot (3,3)
        piv3 = highlight_entry(aug2, 2, 2, YELLOW)
        piv_text3 = Text("pivot 3", font_size=22, color=YELLOW).next_to(piv3, LEFT, buff=0.4)
        self.play(Create(piv3), Write(piv_text3))

        # Label [U|c]
        uc_label = MathTex(r"[U \mid \mathbf{c}]", font_size=30, color=GREEN)
        uc_label.next_to(aug2, UP, buff=0.3)
        self.play(Write(uc_label))

        # Pivots summary
        pivots_text = MathTex(
            r"\text{Pivots: } 1, \; 2, \; 5", font_size=28, color=YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(pivots_text))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 2 — Elimination Matrices  E₂₁  and  E₃₂
# ---------------------------------------------------------------------------
class Lecture2_EliminationMatrices(Scene):
    def construct(self):
        title = Text("Lecture 2 — Elimination Matrices", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # E₂₁: subtract 3× row1 from row2
        e21_label = MathTex(r"E_{21}", font_size=32, color=BLUE)
        e21 = Matrix(
            [["1", "0", "0"],
             ["-3", "1", "0"],
             ["0", "0", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).set_color(BLUE)
        e21_group = VGroup(e21_label, e21).arrange(RIGHT, buff=0.3)
        e21_group.shift(UP * 1.5 + LEFT * 3)
        self.play(Write(e21_label), Write(e21))

        # Highlight the multiplier -3
        mult_entry = highlight_entry(e21, 1, 0, ORANGE)
        mult_note = MathTex(r"-\ell_{21} = -3", font_size=26, color=ORANGE)
        mult_note.next_to(mult_entry, DOWN, buff=0.3)
        self.play(Create(mult_entry), Write(mult_note))
        self.wait(0.5)

        # Show E₂₁ × A
        times = MathTex(r"\times", font_size=32)
        a_mat = Matrix(
            [["1", "2", "1"],
             ["3", "8", "1"],
             ["0", "4", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        )
        equals = MathTex(r"=", font_size=32)
        result_mat = Matrix(
            [["1", "2", "1"],
             ["0", "2", "-2"],
             ["0", "4", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).set_color(GREEN)

        product_group = VGroup(times, a_mat, equals, result_mat).arrange(RIGHT, buff=0.3)
        product_group.next_to(e21_group, RIGHT, buff=0.3)
        # Shift the whole thing to fit
        full_row = VGroup(e21_group, product_group)
        full_row.move_to(ORIGIN + UP * 1.0).scale(0.85)

        self.play(Write(times), Write(a_mat))
        self.play(Write(equals), Write(result_mat))
        self.wait()

        # E₃₂
        e32_label = MathTex(r"E_{32}", font_size=32, color=RED)
        e32 = Matrix(
            [["1", "0", "0"],
             ["0", "1", "0"],
             ["0", "-2", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
        ).set_color(RED)
        e32_group = VGroup(e32_label, e32).arrange(RIGHT, buff=0.3)
        e32_group.shift(DOWN * 1.8)
        self.play(Write(e32_label), Write(e32))

        mult2_entry = highlight_entry(e32, 2, 1, ORANGE)
        mult2_note = MathTex(r"-\ell_{32} = -2", font_size=26, color=ORANGE)
        mult2_note.next_to(mult2_entry, DOWN, buff=0.3)
        self.play(Create(mult2_entry), Write(mult2_note))

        # Combined
        combined = MathTex(
            r"E_{32}\, E_{21}\, A = U",
            font_size=32, color=YELLOW,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(combined))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 3 — Back Substitution
# ---------------------------------------------------------------------------
class Lecture2_BackSubstitution(Scene):
    def construct(self):
        title = Text("Lecture 2 — Back Substitution", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Upper triangular system Ux = c
        system = MathTex(
            r"x + 2y + z &= 2 \\",
            r"2y - 2z &= 6 \\",
            r"5z &= -10",
            font_size=32,
        ).shift(UP * 0.5)
        self.play(Write(system))

        # Step 1: solve for z
        box3 = SurroundingRectangle(system[2], color=GREEN, buff=0.1)
        sol_z = MathTex(r"z = -2", font_size=32, color=GREEN)
        sol_z.next_to(system, RIGHT, buff=1.2).align_to(system[2], UP)
        self.play(Create(box3))
        self.play(Write(sol_z))
        self.wait(0.5)

        # Step 2: solve for y
        box2 = SurroundingRectangle(system[1], color=BLUE, buff=0.1)
        sub_y = MathTex(
            r"2y - 2(-2) = 6 \;\Rightarrow\; 2y = 2 \;\Rightarrow\; y = 1",
            font_size=28, color=BLUE,
        ).next_to(sol_z, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(ReplacementTransform(box3, box2))
        self.play(Write(sub_y))
        self.wait(0.5)

        # Step 3: solve for x
        box1 = SurroundingRectangle(system[0], color=YELLOW, buff=0.1)
        sub_x = MathTex(
            r"x + 2(1) + (-2) = 2 \;\Rightarrow\; x = 2",
            font_size=28, color=YELLOW,
        ).next_to(sub_y, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(ReplacementTransform(box2, box1))
        self.play(Write(sub_x))
        self.wait(0.5)
        self.play(FadeOut(box1))

        # Final answer
        answer = MathTex(
            r"\mathbf{x} = \begin{bmatrix} 2 \\ 1 \\ -2 \end{bmatrix}",
            font_size=36, color=YELLOW,
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(answer))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 4 — When Elimination Fails
# ---------------------------------------------------------------------------
class Lecture2_WhenEliminationFails(Scene):
    def construct(self):
        title = Text("Lecture 2 — When Elimination Fails", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Case 1: fixable — zero pivot but row exchange saves us
        case1_title = Text(
            "Case 1: Zero pivot — row exchange fixes it",
            font_size=26, color=GREEN,
        ).shift(UP * 2.2)
        self.play(Write(case1_title))

        mat_before = Matrix(
            [["1", "2", "1"],
             ["3", "6", "1"],
             ["0", "4", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).shift(LEFT * 3 + UP * 0.3)
        self.play(Write(mat_before))

        arrow1 = MathTex(r"\xrightarrow{R_2 - 3R_1}", font_size=26)
        arrow1.next_to(mat_before, RIGHT, buff=0.3)

        mat_mid = Matrix(
            [["1", "2", "1"],
             ["0", "0", "-2"],
             ["0", "4", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).next_to(arrow1, RIGHT, buff=0.3)
        self.play(Write(arrow1), Write(mat_mid))

        # Highlight zero pivot
        zero_piv = highlight_entry(mat_mid, 1, 1, RED)
        zero_label = Text("zero pivot!", font_size=22, color=RED)
        zero_label.next_to(zero_piv, DOWN, buff=0.2)
        self.play(Create(zero_piv), Write(zero_label))
        self.wait(0.5)

        # Row exchange
        arrow2 = MathTex(r"\xrightarrow{P_{23}}", font_size=26)
        mat_after = Matrix(
            [["1", "2", "1"],
             ["0", "4", "1"],
             ["0", "0", "-2"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        )
        exchange_group = VGroup(arrow2, mat_after).arrange(RIGHT, buff=0.3)
        exchange_group.next_to(mat_mid, DOWN, buff=0.7, aligned_edge=LEFT)
        swap_note = Text("swap rows 2 & 3", font_size=22, color=GREEN)
        swap_note.next_to(arrow2, UP, buff=0.15)
        self.play(
            FadeOut(zero_piv), FadeOut(zero_label),
            Write(arrow2), Write(mat_after), Write(swap_note),
        )
        self.wait()

        # Clear and show Case 2
        self.play(*[FadeOut(m) for m in self.mobjects if m is not title])

        case2_title = Text(
            "Case 2: No nonzero pivot available — SINGULAR",
            font_size=26, color=RED,
        ).shift(UP * 2.2)
        self.play(Write(case2_title))

        sing_mat = Matrix(
            [["1", "2", "1"],
             ["3", "6", "1"],
             ["2", "4", "1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).shift(LEFT * 3 + UP * 0.3)
        self.play(Write(sing_mat))

        sarrow1 = MathTex(r"\xrightarrow{R_2-3R_1,\; R_3-2R_1}", font_size=24)
        sarrow1.next_to(sing_mat, RIGHT, buff=0.3)

        sing_mid = Matrix(
            [["1", "2", "1"],
             ["0", "0", "-2"],
             ["0", "0", "-1"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30},
        ).next_to(sarrow1, RIGHT, buff=0.3)
        self.play(Write(sarrow1), Write(sing_mid))

        # Highlight: column 2 is all zeros below pivot
        zero_col_box = SurroundingRectangle(
            VGroup(
                sing_mid.get_entries()[4],  # (1,1)
                sing_mid.get_entries()[7],  # (2,1)
            ),
            color=RED, buff=0.1,
        )
        no_pivot = Text(
            "No pivot available in column 2\nMatrix is SINGULAR",
            font_size=24, color=RED,
        ).next_to(sing_mid, DOWN, buff=0.5)
        self.play(Create(zero_col_box), Write(no_pivot))
        self.wait(2)
