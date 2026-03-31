"""
MIT 18.06 Linear Algebra — Lecture 5: Transposes, Permutations, Spaces Rⁿ
Following Gilbert Strang's lecture content.

Scenes:
  1. Lecture5_TransposeFlip
  2. Lecture5_SymmetricMatrices
  3. Lecture5_PermutationProperties
  4. Lecture5_VectorSpaceR2
  5. Lecture5_SubspaceTest

Manim Community Edition v0.20.1
Run:  manim -pql lecture05_transposes_permutations.py <SceneName>
"""

from manim import *


def title_slide(self, text, wait=1.5):
    title = Text(text, font_size=40, weight=BOLD)
    self.play(Write(title))
    self.wait(wait)
    self.play(title.animate.scale(0.55).to_edge(UP))
    return title


# ===================================================================
# Scene 1 — Transpose: flip across the diagonal
# ===================================================================

class Lecture5_TransposeFlip(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 5: The Transpose")

        # Definition
        defn = MathTex(r"(A^T)_{ij} = A_{ji}").scale(0.85).next_to(title, DOWN, buff=0.5)
        self.play(Write(defn))
        self.wait(1)

        # Concrete matrix
        A_entries = [["1", "2", "3"], ["4", "5", "6"]]
        AT_entries = [["1", "4"], ["2", "5"], ["3", "6"]]

        A_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}"
        ).scale(0.8)
        AT_tex = MathTex(
            r"A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}"
        ).scale(0.8)

        pair = VGroup(A_tex, AT_tex).arrange(RIGHT, buff=1.5).next_to(defn, DOWN, buff=0.6)
        self.play(Write(A_tex))
        self.wait(0.5)

        # Animate: transform A into A^T
        arrow = MathTex(r"\xrightarrow{\text{flip rows}\leftrightarrow\text{cols}}").scale(0.6)
        arrow.move_to((A_tex.get_right() + AT_tex.get_left()) / 2)
        self.play(Write(arrow))
        self.play(Write(AT_tex))
        self.wait(1)

        # Highlight diagonal preservation
        note = MathTex(
            r"\text{Diagonal entries stay: } a_{11},\, a_{22},\,\ldots"
        ).scale(0.6).next_to(pair, DOWN, buff=0.5)
        self.play(Write(note))

        # Shape changes
        shape_note = MathTex(
            r"A \text{ is } 2\times3 \;\;\Rightarrow\;\; A^T \text{ is } 3\times2"
        ).scale(0.6).next_to(note, DOWN, buff=0.3)
        self.play(Write(shape_note))
        self.wait(2)


# ===================================================================
# Scene 2 — A^T A is always symmetric
# ===================================================================

class Lecture5_SymmetricMatrices(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 5: AᵀA is Always Symmetric")

        # Proof
        proof_lines = VGroup(
            MathTex(r"\text{Claim: } (A^T A)^T = A^T A").scale(0.75),
            MathTex(r"\text{Proof: } (A^T A)^T = A^T (A^T)^T = A^T A \;\;\checkmark").scale(0.75),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=0.5)

        self.play(Write(proof_lines[0]))
        self.wait(1)
        self.play(Write(proof_lines[1]))
        self.wait(1.5)

        # Concrete example
        self.play(FadeOut(proof_lines))

        A_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \\ 0 & 1 \end{bmatrix}"
        ).scale(0.7)
        AT_tex = MathTex(
            r"A^T = \begin{bmatrix} 1 & 2 & 0 \\ 3 & 4 & 1 \end{bmatrix}"
        ).scale(0.7)
        prod = MathTex(
            r"A^T A = \begin{bmatrix} 5 & 11 \\ 11 & 26 \end{bmatrix}"
        ).scale(0.7)
        sym_note = MathTex(r"\text{Symmetric! } (A^T A)^T = A^T A").scale(0.65)

        steps = VGroup(A_tex, AT_tex, prod, sym_note).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.4)
        for s in steps:
            self.play(Write(s), run_time=0.8)
            self.wait(0.6)

        box = SurroundingRectangle(prod, color=GREEN, buff=0.1)
        self.play(Create(box))
        self.wait(2)


# ===================================================================
# Scene 3 — P⁻¹ = Pᵀ
# ===================================================================

class Lecture5_PermutationProperties(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 5: Permutation Matrices — P⁻¹ = Pᵀ")

        # Example permutation
        P_tex = MathTex(
            r"P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}"
        ).scale(0.75)
        PT_tex = MathTex(
            r"P^T = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}"
        ).scale(0.75)
        row1 = VGroup(P_tex, PT_tex).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=0.5)
        self.play(Write(P_tex))
        self.wait(0.5)
        self.play(Write(PT_tex))
        self.wait(0.8)

        # Compute product
        prod = MathTex(
            r"P^T P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I"
        ).scale(0.75).next_to(row1, DOWN, buff=0.5)
        self.play(Write(prod))
        self.wait(0.8)

        conclusion = MathTex(
            r"P^T P = I \;\;\Longrightarrow\;\; P^{-1} = P^T"
        ).scale(0.85).next_to(prod, DOWN, buff=0.5)
        box = SurroundingRectangle(conclusion, color=YELLOW, buff=0.15)
        self.play(Write(conclusion), Create(box))
        self.wait(1)

        why = MathTex(
            r"\text{Each row and column of } P "
            r"\text{ has exactly one 1 — columns are orthonormal}"
        ).scale(0.55).next_to(box, DOWN, buff=0.4)
        self.play(Write(why))
        self.wait(2)


# ===================================================================
# Scene 4 — Subspaces of R²
# ===================================================================

class Lecture5_VectorSpaceR2(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 5: Subspaces of R²")

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=7, y_length=5,
            background_line_style={"stroke_opacity": 0.3},
        ).next_to(title, DOWN, buff=0.3)
        self.play(Create(plane), run_time=1)

        # Subspace 1: the origin
        origin_dot = Dot(plane.c2p(0, 0), color=RED, radius=0.12)
        label_origin = MathTex(r"\{0\}", color=RED, font_size=30).next_to(origin_dot, DR, buff=0.15)
        self.play(FadeIn(origin_dot), Write(label_origin))
        self.wait(1)

        # Subspace 2: a line through the origin
        line1 = plane.plot(lambda x: 0.7 * x, x_range=[-4, 4], color=GREEN, stroke_width=3)
        label_line = MathTex(
            r"\text{line through } \mathbf{0}", color=GREEN, font_size=28
        ).next_to(plane, RIGHT, buff=0.15).shift(UP * 0.5)
        self.play(Create(line1), Write(label_line))
        self.wait(1)

        line2 = plane.plot(lambda x: -1.5 * x, x_range=[-2.5, 2.5], color=TEAL, stroke_width=3)
        label_line2 = MathTex(
            r"\text{another line}", color=TEAL, font_size=28
        ).next_to(label_line, DOWN, buff=0.2)
        self.play(Create(line2), Write(label_line2))
        self.wait(1)

        # Subspace 3: all of R²
        r2_rect = Rectangle(
            width=plane.x_length, height=plane.y_length,
            fill_color=BLUE, fill_opacity=0.15, stroke_width=0,
        ).move_to(plane)
        label_r2 = MathTex(
            r"\text{all of } \mathbb{R}^2", color=BLUE, font_size=30
        ).next_to(label_line2, DOWN, buff=0.2)
        self.play(FadeIn(r2_rect), Write(label_r2))
        self.wait(1)

        summary = VGroup(
            MathTex(r"\text{Subspaces of } \mathbb{R}^2\!:", font_size=30),
            MathTex(r"1.\;\{\mathbf{0}\}", font_size=28),
            MathTex(r"2.\;\text{any line through the origin}", font_size=28),
            MathTex(r"3.\;\text{all of } \mathbb{R}^2", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.8)
        box = SurroundingRectangle(summary, color=WHITE, buff=0.15)
        self.play(Write(summary), Create(box))
        self.wait(2)


# ===================================================================
# Scene 5 — Subspace closure test
# ===================================================================

class Lecture5_SubspaceTest(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 5: Testing for a Subspace")

        # Rules
        rules = VGroup(
            MathTex(r"\text{A subset } S \subseteq \mathbb{R}^n \text{ is a subspace if:}").scale(0.7),
            MathTex(r"1.\; \mathbf{v},\mathbf{w}\in S \;\Rightarrow\; \mathbf{v}+\mathbf{w}\in S").scale(0.65),
            MathTex(r"2.\; \mathbf{v}\in S,\; c\in\mathbb{R} \;\Rightarrow\; c\,\mathbf{v}\in S").scale(0.65),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.4)
        self.play(Write(rules))
        self.wait(1.5)

        # Good example: line y = 2x
        self.play(rules.animate.shift(UP * 0.5).scale(0.85))

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=5, y_length=5,
            background_line_style={"stroke_opacity": 0.2},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)
        self.play(Create(plane), run_time=0.8)

        line = plane.plot(lambda x: 2 * x, x_range=[-2, 2], color=GREEN, stroke_width=3)
        line_label = MathTex(r"S: y=2x", color=GREEN, font_size=28).next_to(plane, UP, buff=0.1)
        self.play(Create(line), Write(line_label))

        # Show addition closure
        v = Arrow(plane.c2p(0, 0), plane.c2p(1, 2), buff=0, color=YELLOW, stroke_width=3)
        w = Arrow(plane.c2p(0, 0), plane.c2p(0.5, 1), buff=0, color=ORANGE, stroke_width=3)
        vpw = Arrow(plane.c2p(0, 0), plane.c2p(1.5, 3), buff=0, color=RED, stroke_width=3)
        v_label = MathTex(r"\mathbf{v}", color=YELLOW, font_size=26).next_to(v.get_end(), RIGHT, buff=0.1)
        w_label = MathTex(r"\mathbf{w}", color=ORANGE, font_size=26).next_to(w.get_end(), LEFT, buff=0.1)
        sum_label = MathTex(r"\mathbf{v+w}", color=RED, font_size=26).next_to(vpw.get_end(), RIGHT, buff=0.1)

        self.play(GrowArrow(v), Write(v_label))
        self.play(GrowArrow(w), Write(w_label))
        self.play(GrowArrow(vpw), Write(sum_label))

        check1 = MathTex(r"\mathbf{v+w} \in S \;\checkmark", color=GREEN, font_size=28)
        check1.next_to(plane, RIGHT, buff=0.3).shift(DOWN * 0.3)
        self.play(Write(check1))
        self.wait(1)

        # --- Bad example: y = 2x + 1 (not through origin) ---
        self.play(
            *[FadeOut(m) for m in [v, w, vpw, v_label, w_label, sum_label, check1, line, line_label]]
        )

        bad_line = plane.plot(lambda x: 2 * x + 1, x_range=[-2.5, 1.5], color=RED, stroke_width=3)
        bad_label = MathTex(r"S': y=2x+1", color=RED, font_size=28).next_to(plane, UP, buff=0.1)
        self.play(Create(bad_line), Write(bad_label))

        # 0 not in S'
        origin_dot = Dot(plane.c2p(0, 0), color=WHITE, radius=0.08)
        fail_note = MathTex(
            r"\mathbf{0} \notin S' \;\text{(fails!)}", color=RED, font_size=28
        ).next_to(plane, RIGHT, buff=0.3).shift(DOWN * 0.3)
        self.play(FadeIn(origin_dot), Write(fail_note))
        self.wait(0.5)

        # Also show addition failure
        a = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=YELLOW, stroke_width=3)
        b = Arrow(plane.c2p(0, 0), plane.c2p(1, 3), buff=0, color=ORANGE, stroke_width=3)
        apb = Arrow(plane.c2p(0, 0), plane.c2p(1, 4), buff=0, color=MAROON, stroke_width=3)
        a_l = MathTex(r"\mathbf{a}", color=YELLOW, font_size=26).next_to(a.get_end(), LEFT, buff=0.1)
        b_l = MathTex(r"\mathbf{b}", color=ORANGE, font_size=26).next_to(b.get_end(), RIGHT, buff=0.1)
        apb_l = MathTex(r"\mathbf{a+b}", color=MAROON, font_size=26).next_to(apb.get_end(), RIGHT, buff=0.1)

        self.play(GrowArrow(a), Write(a_l))
        self.play(GrowArrow(b), Write(b_l))
        self.play(GrowArrow(apb), Write(apb_l))

        fail2 = MathTex(
            r"\mathbf{a+b} \notin S' \;\text{— not a subspace!}", color=RED, font_size=28
        ).next_to(fail_note, DOWN, buff=0.25)
        self.play(Write(fail2))
        self.wait(2)
