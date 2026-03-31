"""
MIT 18.06 Linear Algebra — Lecture 6: Column Space and Nullspace
Following Gilbert Strang's lecture content.

Scenes:
  1. Lecture6_ColumnSpaceDefinition
  2. Lecture6_ColumnSpacePlane
  3. Lecture6_SolvabilityCondition
  4. Lecture6_NullspaceDefinition
  5. Lecture6_NullspaceIsSubspace

Manim Community Edition v0.20.1
Run:  manim -pql lecture06_column_space_nullspace.py <SceneName>
"""

from manim import *
import numpy as np


def title_slide(self, text, wait=1.5):
    title = Text(text, font_size=40, weight=BOLD)
    self.play(Write(title))
    self.wait(wait)
    self.play(title.animate.scale(0.55).to_edge(UP))
    return title


# ===================================================================
# Scene 1 — Column Space Definition
# ===================================================================

class Lecture6_ColumnSpaceDefinition(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 6: The Column Space C(A)")

        # Matrix A with columns highlighted
        A_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 3 \\ 2 & 1 \\ 4 & 5 \end{bmatrix}"
        ).scale(0.85).next_to(title, DOWN, buff=0.5)
        self.play(Write(A_tex))
        self.wait(0.8)

        # Pull out columns
        col1 = MathTex(
            r"\mathbf{a}_1 = \begin{bmatrix}1\\2\\4\end{bmatrix}", color=BLUE
        ).scale(0.7)
        col2 = MathTex(
            r"\mathbf{a}_2 = \begin{bmatrix}3\\1\\5\end{bmatrix}", color=GREEN
        ).scale(0.7)
        cols = VGroup(col1, col2).arrange(RIGHT, buff=1.0).next_to(A_tex, DOWN, buff=0.5)
        self.play(Write(col1), Write(col2))
        self.wait(0.8)

        # Column space definition
        defn = MathTex(
            r"C(A) = \{ x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 "
            r"\;:\; x_1, x_2 \in \mathbb{R} \}"
        ).scale(0.7).next_to(cols, DOWN, buff=0.5)
        self.play(Write(defn))
        self.wait(1)

        note1 = MathTex(
            r"\text{= all linear combinations of columns of } A"
        ).scale(0.6).next_to(defn, DOWN, buff=0.3)
        self.play(Write(note1))
        self.wait(0.8)

        note2 = MathTex(
            r"C(A) \text{ is a subspace of } \mathbb{R}^m \;(m = \text{number of rows})"
        ).scale(0.6).next_to(note1, DOWN, buff=0.3)
        box = SurroundingRectangle(note2, color=YELLOW, buff=0.1)
        self.play(Write(note2), Create(box))
        self.wait(0.5)

        note3 = MathTex(
            r"\text{Here } C(A) \subseteq \mathbb{R}^3 \text{ — a plane through the origin}"
        ).scale(0.6).next_to(box, DOWN, buff=0.3)
        self.play(Write(note3))
        self.wait(2)


# ===================================================================
# Scene 2 — Column space as a plane in R³  (3D)
# ===================================================================

class Lecture6_ColumnSpacePlane(ThreeDScene):
    def construct(self):
        # Title (on screen before 3D)
        title = Text("Lecture 6: Column Space — a Plane in R³", font_size=36, weight=BOLD)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 5, 1], y_range=[-3, 5, 1], z_range=[-3, 8, 1],
            x_length=6, y_length=6, z_length=6,
        )
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), run_time=1)

        # Two column vectors
        col1 = np.array([1, 2, 4])
        col2 = np.array([3, 1, 5])

        arrow1 = Arrow3D(start=ORIGIN, end=axes.c2p(*col1), color=BLUE)
        arrow2 = Arrow3D(start=ORIGIN, end=axes.c2p(*col2), color=GREEN)

        label1 = MathTex(r"\mathbf{a}_1", color=BLUE, font_size=30)
        label2 = MathTex(r"\mathbf{a}_2", color=GREEN, font_size=30)
        self.add_fixed_orientation_mobjects(label1, label2)
        label1.next_to(axes.c2p(*col1), RIGHT, buff=0.1)
        label2.next_to(axes.c2p(*col2), RIGHT, buff=0.1)

        self.play(Create(arrow1), Write(label1))
        self.play(Create(arrow2), Write(label2))
        self.wait(0.5)

        # Draw the plane spanned by col1, col2
        # Parametric surface: s*col1 + t*col2
        plane_surface = Surface(
            lambda u, v: axes.c2p(
                *(u * col1 + v * col2)
            ),
            u_range=[-1, 1.5],
            v_range=[-1, 1.5],
            resolution=(8, 8),
            fill_opacity=0.3,
            fill_color=BLUE,
            stroke_width=0.5,
            stroke_color=BLUE_D,
        )
        self.play(Create(plane_surface), run_time=1.5)

        # Label
        cs_label = MathTex(r"C(A)", font_size=36, color=YELLOW)
        self.add_fixed_orientation_mobjects(cs_label)
        cs_label.move_to(axes.c2p(3, 2, 6))
        self.play(Write(cs_label))

        # Slowly rotate camera
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(1)


# ===================================================================
# Scene 3 — Solvability: Ax = b iff b in C(A)
# ===================================================================

class Lecture6_SolvabilityCondition(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 6: Ax = b Solvable iff b ∈ C(A)")

        # Key statement
        statement = MathTex(
            r"A\mathbf{x} = \mathbf{b} \text{ has a solution}"
            r"\;\;\Longleftrightarrow\;\;"
            r"\mathbf{b} \in C(A)"
        ).scale(0.75).next_to(title, DOWN, buff=0.5)
        box = SurroundingRectangle(statement, color=YELLOW, buff=0.15)
        self.play(Write(statement), Create(box))
        self.wait(1.5)

        # Why?
        why = VGroup(
            MathTex(
                r"A\mathbf{x} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n"
            ).scale(0.65),
            MathTex(
                r"\text{This is a linear combination of columns of } A"
            ).scale(0.6),
            MathTex(
                r"\text{So } A\mathbf{x} = \mathbf{b} \text{ asks: is } \mathbf{b} "
                r"\text{ a combination of the columns?}"
            ).scale(0.6),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(box, DOWN, buff=0.5)
        for w in why:
            self.play(Write(w), run_time=0.8)
            self.wait(0.5)

        # Example
        self.play(FadeOut(why))

        A_tex = MathTex(
            r"A = \begin{bmatrix}1 & 3\\2 & 1\\4 & 5\end{bmatrix}"
        ).scale(0.7)

        b_good = MathTex(
            r"\mathbf{b} = \begin{bmatrix}4\\3\\9\end{bmatrix}"
            r"= 1\!\cdot\!\begin{bmatrix}1\\2\\4\end{bmatrix}"
            r"+ 1\!\cdot\!\begin{bmatrix}3\\1\\5\end{bmatrix}"
            r"\;\;\checkmark"
        ).scale(0.6)

        b_bad = MathTex(
            r"\mathbf{b} = \begin{bmatrix}1\\1\\1\end{bmatrix}"
            r"\;\;\text{not in } C(A) \;\;\times"
        ).scale(0.6)

        examples = VGroup(A_tex, b_good, b_bad).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        examples.next_to(box, DOWN, buff=0.4)
        self.play(Write(A_tex))
        self.wait(0.5)
        self.play(Write(b_good))
        self.wait(1)
        self.play(Write(b_bad))
        self.wait(2)


# ===================================================================
# Scene 4 — Nullspace Definition
# ===================================================================

class Lecture6_NullspaceDefinition(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 6: The Nullspace N(A)")

        defn = MathTex(
            r"N(A) = \{ \mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0} \}"
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(Write(defn))
        self.wait(1)

        note = MathTex(
            r"N(A) \text{ is a subspace of } \mathbb{R}^n \;(n = \text{number of columns})"
        ).scale(0.6).next_to(defn, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(1)

        # Concrete example
        self.play(FadeOut(note))

        A_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \\ 3 & 1 & 4 \end{bmatrix}"
        ).scale(0.75).next_to(defn, DOWN, buff=0.5)
        self.play(Write(A_tex))
        self.wait(0.5)

        solve = MathTex(
            r"A\mathbf{x} = \mathbf{0} \;\;\Rightarrow\;\;"
            r"\text{eliminate to find solutions}"
        ).scale(0.6).next_to(A_tex, DOWN, buff=0.4)
        self.play(Write(solve))
        self.wait(0.8)

        # After elimination: x3 is free, x1 = -x3, x2 = -x3
        sol = MathTex(
            r"\mathbf{x} = x_3 \begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix}"
            r",\;\; x_3 \in \mathbb{R}"
        ).scale(0.7).next_to(solve, DOWN, buff=0.4)
        self.play(Write(sol))
        self.wait(0.8)

        interp = MathTex(
            r"N(A) = \text{a line through } \mathbf{0} \text{ in } \mathbb{R}^3"
        ).scale(0.65).next_to(sol, DOWN, buff=0.4)
        box = SurroundingRectangle(interp, color=GREEN, buff=0.1)
        self.play(Write(interp), Create(box))
        self.wait(0.5)

        check = MathTex(
            r"\text{Check: } A\begin{bmatrix}-1\\-1\\1\end{bmatrix}"
            r"= \begin{bmatrix}0\\0\\0\end{bmatrix} \;\checkmark"
        ).scale(0.6).next_to(box, DOWN, buff=0.3)
        self.play(Write(check))
        self.wait(2)


# ===================================================================
# Scene 5 — Nullspace is a subspace (closure proof)
# ===================================================================

class Lecture6_NullspaceIsSubspace(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 6: The Nullspace is a Subspace")

        header = MathTex(
            r"\text{Prove: } N(A) = \{\mathbf{x}: A\mathbf{x}=\mathbf{0}\} "
            r"\text{ is a subspace of } \mathbb{R}^n"
        ).scale(0.6).next_to(title, DOWN, buff=0.4)
        self.play(Write(header))
        self.wait(1)

        # Closure under addition
        add_title = MathTex(
            r"\textbf{Closure under addition:}", color=BLUE
        ).scale(0.65)
        add_lines = VGroup(
            MathTex(r"\text{Suppose } A\mathbf{x} = \mathbf{0} \text{ and } A\mathbf{y} = \mathbf{0}").scale(0.6),
            MathTex(r"A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}").scale(0.6),
            MathTex(r"\Rightarrow \mathbf{x}+\mathbf{y} \in N(A) \;\;\checkmark", color=GREEN).scale(0.6),
        )
        add_block = VGroup(add_title, *add_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        add_block.next_to(header, DOWN, buff=0.4)

        self.play(Write(add_title))
        for line in add_lines:
            self.play(Write(line), run_time=0.8)
            self.wait(0.5)

        # Closure under scalar multiplication
        sc_title = MathTex(
            r"\textbf{Closure under scalar multiplication:}", color=BLUE
        ).scale(0.65)
        sc_lines = VGroup(
            MathTex(r"\text{Suppose } A\mathbf{x} = \mathbf{0},\; c \in \mathbb{R}").scale(0.6),
            MathTex(r"A(c\,\mathbf{x}) = c\,(A\mathbf{x}) = c\,\mathbf{0} = \mathbf{0}").scale(0.6),
            MathTex(r"\Rightarrow c\,\mathbf{x} \in N(A) \;\;\checkmark", color=GREEN).scale(0.6),
        )
        sc_block = VGroup(sc_title, *sc_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        sc_block.next_to(add_block, DOWN, buff=0.4)

        self.play(Write(sc_title))
        for line in sc_lines:
            self.play(Write(line), run_time=0.8)
            self.wait(0.5)

        # Final box
        conclusion = MathTex(
            r"\therefore\; N(A) \text{ is a subspace of } \mathbb{R}^n"
        ).scale(0.75).next_to(sc_block, DOWN, buff=0.4)
        box = SurroundingRectangle(conclusion, color=YELLOW, buff=0.15)
        self.play(Write(conclusion), Create(box))
        self.wait(2)
