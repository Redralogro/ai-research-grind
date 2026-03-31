"""
MIT 18.06 Lecture 6: Column Space and Null Space
Column space C(A), null space N(A), rank, nullity,
rank-nullity theorem, and solving Ax = b

Style: 3Blue1Brown inspired (Essence of Linear Algebra Ch.6)
"""

from manim import *
import numpy as np


# ──────────────────────────────────────────────────────────────
# Scene 1: Column Space Introduction
# ──────────────────────────────────────────────────────────────
class Lecture6_ColumnSpaceIntro(Scene):
    """Column space as the set of all possible outputs Ax."""

    def construct(self):
        # Title
        title = Text("Column Space of A", font_size=42, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Show matrix A (3x2)
        mat_label = MathTex(r"A =", font_size=34)
        mat = MathTex(
            r"\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}",
            font_size=34,
        )
        mat_group = VGroup(mat_label, mat).arrange(RIGHT, buff=0.2)
        mat_group.shift(UP * 1.5)
        self.play(Write(mat_group), run_time=1.0)
        self.wait(0.5)

        # Explanation line 1
        expl1 = Text(
            "The column space is the set of all possible outputs Ax",
            font_size=24, color=GREY,
        )
        expl1.next_to(mat_group, DOWN, buff=0.5)
        self.play(FadeIn(expl1), run_time=0.8)
        self.wait(0.8)

        # Explanation line 2
        expl2 = Text(
            "It's the span of the columns of A",
            font_size=24, color=GREY,
        )
        expl2.next_to(expl1, DOWN, buff=0.3)
        self.play(FadeIn(expl2), run_time=0.8)
        self.wait(0.5)

        # Extract columns as vectors
        self.play(FadeOut(expl1), FadeOut(expl2), run_time=0.4)

        col1_tex = MathTex(
            r"\mathbf{c}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}",
            font_size=30, color=GREEN,
        )
        col2_tex = MathTex(
            r"\mathbf{c}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}",
            font_size=30, color=RED,
        )
        cols = VGroup(col1_tex, col2_tex).arrange(RIGHT, buff=1.0)
        cols.shift(DOWN * 0.2)

        self.play(Write(col1_tex), Write(col2_tex), run_time=1.0)
        self.wait(0.5)

        span_text = MathTex(
            r"\text{C}(A) = \text{span}(\mathbf{c}_1, \mathbf{c}_2)",
            font_size=30,
        )
        span_text.next_to(cols, DOWN, buff=0.5)
        self.play(Write(span_text), run_time=0.8)
        self.wait(0.5)

        # Result
        result = Text(
            "= the xy-plane in R\u00b3",
            font_size=28, color=YELLOW,
        )
        result.next_to(span_text, DOWN, buff=0.4)
        self.play(FadeIn(result), run_time=0.6)
        self.wait(0.5)

        # 3D-ish diagram — show two arrows and a shaded rectangle for the plane
        self.play(
            FadeOut(mat_group), FadeOut(cols), FadeOut(span_text), FadeOut(result),
            run_time=0.5,
        )

        # Axes hints (pseudo-3D)
        axes_label = Text("R\u00b3", font_size=28, color=GREY).to_corner(DR, buff=0.4)
        arrow_c1 = Arrow(
            ORIGIN, RIGHT * 2.5, buff=0, color=GREEN, stroke_width=4,
        ).shift(DOWN * 0.5)
        arrow_c2 = Arrow(
            ORIGIN, UP * 2.5, buff=0, color=RED, stroke_width=4,
        ).shift(DOWN * 0.5)
        label_c1 = MathTex(r"\mathbf{c}_1", font_size=26, color=GREEN)
        label_c1.next_to(arrow_c1, DOWN, buff=0.15)
        label_c2 = MathTex(r"\mathbf{c}_2", font_size=26, color=RED)
        label_c2.next_to(arrow_c2, RIGHT, buff=0.15)

        # Shaded plane (rectangle at z=0)
        plane_rect = Rectangle(
            width=5, height=5, fill_color=BLUE, fill_opacity=0.15,
            stroke_color=BLUE, stroke_width=1, stroke_opacity=0.4,
        ).shift(DOWN * 0.5)

        plane_label = Text("Column Space (xy-plane)", font_size=24, color=BLUE)
        plane_label.next_to(plane_rect, DOWN, buff=0.2)

        self.play(
            FadeIn(plane_rect), Create(arrow_c1), Create(arrow_c2),
            Write(label_c1), Write(label_c2), FadeIn(axes_label),
            run_time=1.2,
        )
        self.play(Write(plane_label), run_time=0.6)
        self.wait(1.5)


# ──────────────────────────────────────────────────────────────
# Scene 2: Column Space via Grid Transformation (3B1B style)
# ──────────────────────────────────────────────────────────────
class Lecture6_ColumnSpaceGrid(Scene):
    """3B1B-style grid transformations showing full-rank vs rank-deficient."""

    def construct(self):
        title = Text("Column Space as Transformation Output", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # ─── Part A: Full rank 2×2 ───
        plane_a = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=4)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=4)
        i_label = MathTex(r"\hat{\imath}", font_size=24, color=GREEN).next_to(i_hat, DOWN, buff=0.1)
        j_label = MathTex(r"\hat{\jmath}", font_size=24, color=RED).next_to(j_hat, LEFT, buff=0.1)

        basis = VGroup(i_hat, j_hat, i_label, j_label)

        self.play(Create(plane_a), FadeIn(basis), run_time=1.0)
        self.wait(0.3)

        # Matrix A (full rank)
        mat_a_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}",
            font_size=30,
        )
        mat_a_bg = BackgroundRectangle(mat_a_tex, fill_opacity=0.85, buff=0.15)
        mat_a_group = VGroup(mat_a_bg, mat_a_tex).to_corner(UL, buff=0.6)
        mat_a_group.shift(DOWN * 0.5)
        self.play(FadeIn(mat_a_group), run_time=0.5)

        # Apply transformation
        matrix_a = [[1, 1], [1, 2]]
        self.play(
            ApplyMatrix(matrix_a, plane_a),
            ApplyMatrix(matrix_a, i_hat),
            ApplyMatrix(matrix_a, j_hat),
            run_time=3,
        )
        self.wait(0.3)

        # Update labels
        i_label.next_to(i_hat, DOWN, buff=0.1)
        j_label.next_to(j_hat, LEFT, buff=0.1)

        result_a = Text("Column space = all of R\u00b2 (full rank)", font_size=24, color=YELLOW)
        result_a_bg = BackgroundRectangle(result_a, fill_opacity=0.85, buff=0.12)
        result_a_group = VGroup(result_a_bg, result_a)
        result_a_group.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(result_a_group), run_time=0.6)
        self.wait(1.5)

        # ─── Transition: Reset ───
        self.play(
            FadeOut(plane_a), FadeOut(basis),
            FadeOut(mat_a_group), FadeOut(result_a_group),
            run_time=0.6,
        )

        # ─── Part B: Rank 1 (singular) ───
        plane_b = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )
        i_hat2 = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=4)
        j_hat2 = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=4)
        i_label2 = MathTex(r"\hat{\imath}", font_size=24, color=GREEN).next_to(i_hat2, DOWN, buff=0.1)
        j_label2 = MathTex(r"\hat{\jmath}", font_size=24, color=RED).next_to(j_hat2, LEFT, buff=0.1)

        basis2 = VGroup(i_hat2, j_hat2, i_label2, j_label2)

        # Gradient-colored vectors along null space direction [-2, 1]
        null_vectors = VGroup(*[
            Arrow(
                ORIGIN, a * np.array([-2, 1, 0]),
                buff=0, stroke_width=3,
            )
            for a in np.linspace(-2.5, 2.5, 13)
            if abs(a) > 0.2
        ])
        null_vectors.set_color_by_gradient(PINK, YELLOW)

        self.play(Create(plane_b), FadeIn(basis2), run_time=1.0)

        mat_b_tex = MathTex(
            r"B = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
            font_size=30,
        )
        mat_b_bg = BackgroundRectangle(mat_b_tex, fill_opacity=0.85, buff=0.15)
        mat_b_group = VGroup(mat_b_bg, mat_b_tex).to_corner(UL, buff=0.6)
        mat_b_group.shift(DOWN * 0.5)
        self.play(FadeIn(mat_b_group), run_time=0.5)
        self.wait(0.3)

        # Show null space vectors before transformation
        null_label = Text("Null space direction", font_size=20, color=PINK)
        null_label_bg = BackgroundRectangle(null_label, fill_opacity=0.85, buff=0.1)
        null_label_group = VGroup(null_label_bg, null_label).to_corner(UR, buff=0.6)
        null_label_group.shift(DOWN * 0.5)
        self.play(FadeIn(null_vectors), FadeIn(null_label_group), run_time=0.8)
        self.wait(0.5)

        # Apply singular transformation
        matrix_b = [[1, 2], [2, 4]]
        self.play(
            ApplyMatrix(matrix_b, plane_b),
            ApplyMatrix(matrix_b, i_hat2),
            ApplyMatrix(matrix_b, j_hat2),
            ApplyMatrix(matrix_b, null_vectors),
            run_time=3,
        )
        self.wait(0.3)

        result_b = Text("Column space = a line (rank 1)", font_size=24, color=YELLOW)
        result_b_bg = BackgroundRectangle(result_b, fill_opacity=0.85, buff=0.12)
        result_b_group = VGroup(result_b_bg, result_b)
        result_b_group.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(result_b_group), run_time=0.6)
        self.wait(1.0)

        # Key insight
        insight = Text("Rank = dimension of column space", font_size=28, color=TEAL)
        insight_bg = BackgroundRectangle(insight, fill_opacity=0.85, buff=0.12)
        insight_group = VGroup(insight_bg, insight)
        insight_group.next_to(result_b_group, UP, buff=0.3)
        self.play(FadeIn(insight_group), run_time=0.6)
        self.wait(2.0)


# ──────────────────────────────────────────────────────────────
# Scene 3: Null Space Introduction
# ──────────────────────────────────────────────────────────────
class Lecture6_NullSpaceIntro(Scene):
    """Null space definition and example."""

    def construct(self):
        # Title
        title = Text("Null Space of A", font_size=42, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # Definition
        defn = MathTex(
            r"N(A) = \{ \mathbf{x} : A\mathbf{x} = \mathbf{0} \}",
            font_size=34,
        )
        defn.shift(UP * 1.5)
        self.play(Write(defn), run_time=1.0)
        self.wait(0.3)

        defn_words = Text(
            "All vectors that A sends to zero",
            font_size=24, color=GREY,
        )
        defn_words.next_to(defn, DOWN, buff=0.35)
        self.play(FadeIn(defn_words), run_time=0.6)
        self.wait(0.8)

        # Example matrix
        self.play(FadeOut(defn_words), run_time=0.3)

        mat_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
            font_size=32,
        )
        mat_tex.next_to(defn, DOWN, buff=0.5)
        self.play(Write(mat_tex), run_time=0.8)
        self.wait(0.3)

        # Null space vector
        null_vec = MathTex(
            r"A \begin{bmatrix} -2 \\ 1 \end{bmatrix}"
            r"= \begin{bmatrix} 1(-2)+2(1) \\ 2(-2)+4(1) \end{bmatrix}"
            r"= \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            font_size=28,
        )
        null_vec.next_to(mat_tex, DOWN, buff=0.5)
        self.play(Write(null_vec), run_time=1.5)
        self.wait(0.8)

        null_span = MathTex(
            r"N(A) = \text{span}\left( \begin{bmatrix} -2 \\ 1 \end{bmatrix} \right)",
            font_size=30, color=PINK,
        )
        null_span.next_to(null_vec, DOWN, buff=0.5)
        self.play(Write(null_span), run_time=0.8)
        self.wait(0.5)

        # Show several null space vectors mapping to origin
        self.play(
            FadeOut(defn), FadeOut(mat_tex), FadeOut(null_vec), FadeOut(null_span),
            run_time=0.5,
        )

        # Mini axes
        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False, "stroke_opacity": 0.5},
        ).shift(DOWN * 0.3)

        origin_dot = Dot(axes.c2p(0, 0), color=WHITE, radius=0.12)
        origin_label = MathTex(r"\mathbf{0}", font_size=22, color=WHITE)
        origin_label.next_to(origin_dot, DR, buff=0.1)

        self.play(Create(axes), FadeIn(origin_dot), FadeIn(origin_label), run_time=0.8)

        # Draw several vectors along null space direction
        scalars = [-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2]
        null_arrows = VGroup()
        for s in scalars:
            end = axes.c2p(-2 * s, 1 * s)
            arrow = Arrow(
                axes.c2p(0, 0), end,
                buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.15,
            )
            null_arrows.add(arrow)
        null_arrows.set_color_by_gradient(PINK, YELLOW)

        self.play(FadeIn(null_arrows, lag_ratio=0.1), run_time=1.5)
        self.wait(0.3)

        mapping_text = Text(
            "All these vectors map to the origin under A",
            font_size=22, color=YELLOW,
        )
        mapping_text.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(mapping_text), run_time=0.6)

        # Animate arrows shrinking to origin
        anims = [arrow.animate.put_start_and_end_on(axes.c2p(0, 0), axes.c2p(0, 0)) for arrow in null_arrows]
        collapse_dot = Dot(axes.c2p(0, 0), color=YELLOW, radius=0.2)
        self.play(*anims, FadeIn(collapse_dot, scale=2), run_time=2.0)
        self.wait(1.5)


# ──────────────────────────────────────────────────────────────
# Scene 4: Null Space Grid Visualization (3B1B style)
# ──────────────────────────────────────────────────────────────
class Lecture6_NullSpaceGrid(Scene):
    """3B1B-style visualization of the null space collapsing."""

    def construct(self):
        title = Text("Null Space: What Gets Lost", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # ─── Before transformation ───
        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=4)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=4)

        # Null space vectors (gradient pink-yellow, 3B1B style)
        null_vecs = VGroup(*[
            Arrow(
                ORIGIN, a * np.array([-2, 1, 0]),
                buff=0, stroke_width=3,
            )
            for a in np.linspace(-3, 3, 15)
            if abs(a) > 0.15
        ])
        null_vecs.set_color_by_gradient(PINK, YELLOW)

        null_line = Line(
            3.5 * np.array([2, -1, 0]), 3.5 * np.array([-2, 1, 0]),
            color=PINK, stroke_width=2, stroke_opacity=0.5,
        )

        self.play(Create(plane), FadeIn(i_hat), FadeIn(j_hat), run_time=1.0)

        mat_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
            font_size=28,
        )
        mat_bg = BackgroundRectangle(mat_tex, fill_opacity=0.85, buff=0.15)
        mat_group = VGroup(mat_bg, mat_tex).to_corner(UL, buff=0.6)
        mat_group.shift(DOWN * 0.5)
        self.play(FadeIn(mat_group), run_time=0.5)

        # Show null space direction
        ns_label = Text("Null space", font_size=20, color=PINK)
        ns_bg = BackgroundRectangle(ns_label, fill_opacity=0.85, buff=0.1)
        ns_group = VGroup(ns_bg, ns_label).to_corner(UR, buff=0.6)
        ns_group.shift(DOWN * 0.5)

        self.play(
            Create(null_line), FadeIn(null_vecs),
            FadeIn(ns_group),
            run_time=1.0,
        )
        self.wait(0.8)

        before_label = Text("BEFORE", font_size=22, color=WHITE)
        before_bg = BackgroundRectangle(before_label, fill_opacity=0.85, buff=0.1)
        before_group = VGroup(before_bg, before_label).to_corner(DL, buff=0.5)
        self.play(FadeIn(before_group), run_time=0.4)
        self.wait(0.5)

        # ─── Apply transformation ───
        self.play(FadeOut(before_group), run_time=0.3)

        matrix = [[1, 2], [2, 4]]
        collapse_dot = Dot(ORIGIN, color=WHITE, radius=0.15)

        self.play(
            ApplyMatrix(matrix, plane),
            ApplyMatrix(matrix, i_hat),
            ApplyMatrix(matrix, j_hat),
            ApplyMatrix(matrix, null_vecs),
            ApplyMatrix(matrix, null_line),
            run_time=3,
        )
        self.play(FadeIn(collapse_dot), run_time=0.3)
        self.wait(0.3)

        after_label = Text("AFTER", font_size=22, color=WHITE)
        after_bg = BackgroundRectangle(after_label, fill_opacity=0.85, buff=0.1)
        after_group = VGroup(after_bg, after_label).to_corner(DL, buff=0.5)
        self.play(FadeIn(after_group), run_time=0.4)

        # Column space line label
        cs_label = Text("Column space (line)", font_size=20, color=TEAL)
        cs_bg = BackgroundRectangle(cs_label, fill_opacity=0.85, buff=0.1)
        cs_group = VGroup(cs_bg, cs_label)
        cs_group.next_to(after_group, UP, buff=0.3)
        self.play(FadeIn(cs_group), run_time=0.5)
        self.wait(0.5)

        # Key insight
        insight = Text(
            "Null space vectors are 'lost' by the transformation",
            font_size=24, color=YELLOW,
        )
        insight_bg = BackgroundRectangle(insight, fill_opacity=0.85, buff=0.12)
        insight_group = VGroup(insight_bg, insight)
        insight_group.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(insight_group), run_time=0.6)
        self.wait(2.0)


# ──────────────────────────────────────────────────────────────
# Scene 5: Rank-Nullity Theorem
# ──────────────────────────────────────────────────────────────
class Lecture6_RankNullityTheorem(Scene):
    """Rank-nullity theorem with visual partitioning."""

    def construct(self):
        # Title
        title = Text("Rank-Nullity Theorem", font_size=42, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # Theorem statement
        theorem = MathTex(
            r"\text{rank}(A)", r"+",
            r"\dim(\text{null space})", r"=",
            r"n", r"\text{ (number of columns)}",
            font_size=30,
        )
        theorem[0].set_color(TEAL)
        theorem[2].set_color(PINK)
        theorem[4].set_color(WHITE)
        theorem.shift(UP * 1.5)
        self.play(Write(theorem), run_time=1.2)
        self.wait(0.8)

        # Example verification
        example_title = Text("Example check:", font_size=24, color=GREY)
        example_title.next_to(theorem, DOWN, buff=0.6)

        mat_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
            font_size=28,
        )
        mat_tex.next_to(example_title, DOWN, buff=0.3)

        check = MathTex(
            r"\underbrace{\text{rank } 1}_{\text{rank}(A)}"
            r"+ \underbrace{1}_{\text{nullity}}"
            r"= \underbrace{2}_{n} \quad \checkmark",
            font_size=28,
        )
        check.next_to(mat_tex, DOWN, buff=0.5)

        self.play(Write(example_title), run_time=0.5)
        self.play(Write(mat_tex), run_time=0.6)
        self.play(Write(check), run_time=1.0)
        self.wait(1.0)

        # Visual: partitioning input space
        self.play(
            FadeOut(example_title), FadeOut(mat_tex), FadeOut(check),
            run_time=0.5,
        )

        # Full rank case
        full_title = Text("Full Rank", font_size=26, color=GREEN)
        full_title.shift(LEFT * 3.5 + DOWN * 0.2)

        full_box = Rectangle(width=3, height=2, color=TEAL, fill_opacity=0.3)
        full_box.next_to(full_title, DOWN, buff=0.3)
        full_label = Text("rank = n", font_size=20, color=TEAL)
        full_label.move_to(full_box)

        null_zero = MathTex(
            r"N(A) = \{\mathbf{0}\}", font_size=22, color=GREY,
        )
        null_zero.next_to(full_box, DOWN, buff=0.2)

        # Rank-deficient case
        def_title = Text("Rank Deficient", font_size=26, color=RED)
        def_title.shift(RIGHT * 3.5 + DOWN * 0.2)

        rank_box = Rectangle(width=1.5, height=2, color=TEAL, fill_opacity=0.3)
        null_box = Rectangle(width=1.5, height=2, color=PINK, fill_opacity=0.3)
        boxes = VGroup(rank_box, null_box).arrange(RIGHT, buff=0)
        boxes.next_to(def_title, DOWN, buff=0.3)

        rank_label = Text("rank", font_size=18, color=TEAL)
        rank_label.move_to(rank_box)
        null_label = Text("nullity", font_size=18, color=PINK)
        null_label.move_to(null_box)

        dim_note = MathTex(
            r"\dim(N(A)) > 0", font_size=22, color=PINK,
        )
        dim_note.next_to(boxes, DOWN, buff=0.2)

        self.play(
            Write(full_title), FadeIn(full_box), Write(full_label), Write(null_zero),
            run_time=1.0,
        )
        self.wait(0.5)
        self.play(
            Write(def_title), FadeIn(rank_box), FadeIn(null_box),
            Write(rank_label), Write(null_label), Write(dim_note),
            run_time=1.0,
        )
        self.wait(2.0)


# ──────────────────────────────────────────────────────────────
# Scene 6: Solving Ax = b
# ──────────────────────────────────────────────────────────────
class Lecture6_SolvingAxEqb(Scene):
    """Solving Ax = b: particular + null space solutions."""

    def construct(self):
        # Title
        title = Text("Solving Ax = b", font_size=42, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # Condition for solution
        cond = Text(
            "Ax = b has a solution  iff  b is in the column space C(A)",
            font_size=24, color=GREY,
        )
        cond.shift(UP * 1.8)
        self.play(FadeIn(cond), run_time=0.8)
        self.wait(0.8)

        # Solution structure
        sol_eq = MathTex(
            r"\mathbf{x}",
            r"=",
            r"\mathbf{x}_{\text{particular}}",
            r"+",
            r"\mathbf{x}_{\text{null}}",
            font_size=32,
        )
        sol_eq[2].set_color(GREEN)
        sol_eq[4].set_color(PINK)
        sol_eq.shift(UP * 0.8)
        self.play(Write(sol_eq), run_time=1.0)
        self.wait(0.5)

        note = Text(
            "x_null is any vector in the null space N(A)",
            font_size=22, color=GREY,
        )
        note.next_to(sol_eq, DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(0.5)

        # Visual: particular solution + null space offset
        self.play(FadeOut(cond), FadeOut(sol_eq), FadeOut(note), run_time=0.4)

        axes = Axes(
            x_range=[-4, 6, 1], y_range=[-3, 4, 1],
            x_length=8, y_length=5.5,
            axis_config={"include_numbers": False, "stroke_opacity": 0.4},
        ).shift(DOWN * 0.3)

        self.play(Create(axes), run_time=0.6)

        # Null space direction (through origin)
        null_dir = np.array([-2, 1, 0])
        null_dir_norm = null_dir / np.linalg.norm(null_dir)

        null_line_origin = Line(
            axes.c2p(*(4 * null_dir_norm[:2])),
            axes.c2p(*(-4 * null_dir_norm[:2])),
            color=GREY, stroke_width=1.5, stroke_opacity=0.4,
        )

        # Particular solution
        x_p = np.array([1, 1, 0])
        x_p_dot = Dot(axes.c2p(x_p[0], x_p[1]), color=GREEN, radius=0.1)
        x_p_label = MathTex(
            r"\mathbf{x}_p", font_size=24, color=GREEN,
        ).next_to(x_p_dot, UR, buff=0.1)
        x_p_arrow = Arrow(
            axes.c2p(0, 0), axes.c2p(x_p[0], x_p[1]),
            buff=0, color=GREEN, stroke_width=3,
        )

        self.play(
            Create(x_p_arrow), FadeIn(x_p_dot), Write(x_p_label),
            run_time=0.8,
        )
        self.wait(0.3)

        # Solution set = shifted null space
        shifted_line = Line(
            axes.c2p(x_p[0] + 4 * null_dir_norm[0], x_p[1] + 4 * null_dir_norm[1]),
            axes.c2p(x_p[0] - 4 * null_dir_norm[0], x_p[1] - 4 * null_dir_norm[1]),
            color=YELLOW, stroke_width=2.5,
        )

        # Solution dots along the shifted line
        sol_dots = VGroup()
        for t in np.linspace(-2, 2, 9):
            pt = x_p[:2] + t * null_dir_norm[:2]
            d = Dot(axes.c2p(pt[0], pt[1]), radius=0.06, color=YELLOW)
            sol_dots.add(d)

        sol_label = Text("Solution set", font_size=22, color=YELLOW)
        sol_bg = BackgroundRectangle(sol_label, fill_opacity=0.8, buff=0.1)
        sol_group = VGroup(sol_bg, sol_label)
        sol_group.next_to(shifted_line, RIGHT, buff=0.3)
        sol_group.shift(UP * 0.5)

        self.play(
            Create(null_line_origin),
            run_time=0.5,
        )
        null_text = Text("Null space N(A)", font_size=18, color=GREY)
        null_text_bg = BackgroundRectangle(null_text, fill_opacity=0.8, buff=0.08)
        null_text_group = VGroup(null_text_bg, null_text)
        null_text_group.next_to(null_line_origin, RIGHT, buff=0.2)
        null_text_group.shift(DOWN * 0.8)
        self.play(FadeIn(null_text_group), run_time=0.4)
        self.wait(0.3)

        self.play(
            Create(shifted_line), FadeIn(sol_dots, lag_ratio=0.05),
            FadeIn(sol_group),
            run_time=1.2,
        )
        self.wait(0.5)

        # Add null space vectors from x_p
        ns_arrows = VGroup()
        for t in [-1.5, -0.8, 0.8, 1.5]:
            end = x_p[:2] + t * null_dir_norm[:2]
            arr = Arrow(
                axes.c2p(x_p[0], x_p[1]),
                axes.c2p(end[0], end[1]),
                buff=0, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.15,
            )
            ns_arrows.add(arr)
        ns_arrows.set_color_by_gradient(PINK, YELLOW)

        self.play(FadeIn(ns_arrows, lag_ratio=0.15), run_time=1.0)
        self.wait(0.3)

        insight = Text(
            "The solution set is a shifted copy of the null space",
            font_size=24, color=YELLOW,
        )
        insight_bg = BackgroundRectangle(insight, fill_opacity=0.85, buff=0.12)
        insight_group = VGroup(insight_bg, insight)
        insight_group.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(insight_group), run_time=0.6)
        self.wait(2.0)


# ──────────────────────────────────────────────────────────────
# Scene 7: Summary
# ──────────────────────────────────────────────────────────────
class Lecture6_ColumnNullSpaceSummary(Scene):
    """Summary: column space vs null space, rank vs nullity."""

    def construct(self):
        title = Text("Column Space & Null Space", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        # Two-panel layout
        divider = Line(UP * 2.8, DOWN * 2.8, color=GREY, stroke_width=1, stroke_opacity=0.4)

        # ─── Left: Column Space ───
        left_title = Text("Column Space C(A)", font_size=26, color=TEAL)
        left_title.shift(LEFT * 3.5 + UP * 2.0)

        left_side = Text("(output side)", font_size=18, color=GREY)
        left_side.next_to(left_title, DOWN, buff=0.15)

        left_q = Text('"Where can Ax land?"', font_size=20, color=TEAL)
        left_q.next_to(left_side, DOWN, buff=0.4)

        # Column space icon: filled parallelogram
        cs_shape = Polygon(
            LEFT * 1.2 + DOWN * 0.6,
            RIGHT * 0.3 + DOWN * 0.6,
            RIGHT * 1.2 + UP * 0.6,
            LEFT * 0.3 + UP * 0.6,
            fill_color=TEAL, fill_opacity=0.25,
            stroke_color=TEAL, stroke_width=2,
        )
        cs_shape.scale(0.9).next_to(left_q, DOWN, buff=0.4)

        cs_icon_label = MathTex(r"C(A) \subseteq \mathbb{R}^m", font_size=22, color=TEAL)
        cs_icon_label.next_to(cs_shape, DOWN, buff=0.2)

        # ─── Right: Null Space ───
        right_title = Text("Null Space N(A)", font_size=26, color=PINK)
        right_title.shift(RIGHT * 3.5 + UP * 2.0)

        right_side = Text("(input side)", font_size=18, color=GREY)
        right_side.next_to(right_title, DOWN, buff=0.15)

        right_q = Text('"What does A kill?"', font_size=20, color=PINK)
        right_q.next_to(right_side, DOWN, buff=0.4)

        # Null space icon: line through origin
        ns_line = Line(
            LEFT * 1.2 + DOWN * 0.6,
            RIGHT * 1.2 + UP * 0.6,
            color=PINK, stroke_width=3,
        )
        ns_dot = Dot(ORIGIN, color=WHITE, radius=0.06)
        ns_icon = VGroup(ns_line, ns_dot).next_to(right_q, DOWN, buff=0.5)

        ns_icon_label = MathTex(r"N(A) \subseteq \mathbb{R}^n", font_size=22, color=PINK)
        ns_icon_label.next_to(ns_icon, DOWN, buff=0.25)

        self.play(
            Create(divider),
            Write(left_title), FadeIn(left_side),
            Write(right_title), FadeIn(right_side),
            run_time=1.0,
        )
        self.play(
            Write(left_q), Write(right_q),
            run_time=0.8,
        )
        self.play(
            FadeIn(cs_shape), Write(cs_icon_label),
            FadeIn(ns_icon), Write(ns_icon_label),
            run_time=1.0,
        )
        self.wait(0.8)

        # Bottom: key equations
        eq1 = MathTex(
            r"\text{Rank} = \dim C(A) = \dim C(A^T)",
            font_size=24, color=TEAL,
        )
        eq2 = MathTex(
            r"\text{Nullity} = \dim N(A) = n - \text{rank}",
            font_size=24, color=PINK,
        )
        eq3 = Text(
            "Together they account for all n dimensions",
            font_size=22, color=YELLOW,
        )

        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.25)
        eqs.to_edge(DOWN, buff=0.4)

        self.play(Write(eq1), run_time=0.8)
        self.play(Write(eq2), run_time=0.8)
        self.play(FadeIn(eq3), run_time=0.6)
        self.wait(2.5)
