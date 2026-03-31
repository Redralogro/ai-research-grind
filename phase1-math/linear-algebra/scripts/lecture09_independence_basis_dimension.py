"""
Lecture 9: Independence, Basis, and Dimension
MIT 18.06 Linear Algebra (Gilbert Strang)

Scenes:
  1. Lecture9_Independence       — Independent vs dependent vectors
  2. Lecture9_Spanning           — Spanning sets
  3. Lecture9_BasisDefinition    — Basis = independent + spanning
  4. Lecture9_DimensionTheorem   — Dimension is well-defined
  5. Lecture9_ColumnSpaceBasis   — Pivot columns of A form basis for C(A)
"""

from manim import *

PIVOT_COLOR = YELLOW
FREE_COLOR = TEAL
HIGHLIGHT = RED
IND_COLOR = GREEN
DEP_COLOR = RED_C


class Lecture9_Independence(Scene):
    """Show independent vs dependent vectors in R² and R³."""

    def construct(self):
        title = Text("Lecture 9: Linear Independence", font_size=40).to_edge(UP)
        self.play(Write(title))

        # ── Definition ──
        defn = MathTex(
            r"c_1 v_1 + c_2 v_2 + \cdots + c_k v_k = 0"
            r"\;\;\text{only if all } c_i = 0",
            font_size=28,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(defn))
        self.wait()

        equiv = MathTex(
            r"\Longleftrightarrow\; A = [v_1 \cdots v_k]"
            r"\text{ has } N(A) = \{0\},\; \text{rank} = k",
            font_size=26,
            color=GRAY,
        ).next_to(defn, DOWN, buff=0.2)
        self.play(Write(equiv))
        self.wait()

        # ── R² example ──
        # Independent pair
        plane_left = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            background_line_style={"stroke_opacity": 0.2},
        ).shift(LEFT * 3 + DOWN * 1)
        left_label = Text(
            "Independent in R²", font_size=22, color=IND_COLOR
        ).next_to(plane_left, UP, buff=0.1)

        v1_l = Arrow(
            plane_left.c2p(0, 0), plane_left.c2p(1, 2),
            buff=0, color=IND_COLOR, stroke_width=3,
        )
        v2_l = Arrow(
            plane_left.c2p(0, 0), plane_left.c2p(2, 1),
            buff=0, color=IND_COLOR, stroke_width=3,
        )
        v1_lab = MathTex(r"v_1", font_size=22, color=IND_COLOR).next_to(
            plane_left.c2p(1, 2), RIGHT, buff=0.1
        )
        v2_lab = MathTex(r"v_2", font_size=22, color=IND_COLOR).next_to(
            plane_left.c2p(2, 1), RIGHT, buff=0.1
        )

        self.play(Create(plane_left), Write(left_label))
        self.play(GrowArrow(v1_l), Write(v1_lab))
        self.play(GrowArrow(v2_l), Write(v2_lab))
        self.wait()

        # Dependent pair
        plane_right = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            background_line_style={"stroke_opacity": 0.2},
        ).shift(RIGHT * 3 + DOWN * 1)
        right_label = Text(
            "Dependent in R²", font_size=22, color=DEP_COLOR
        ).next_to(plane_right, UP, buff=0.1)

        w1 = Arrow(
            plane_right.c2p(0, 0), plane_right.c2p(1, 2),
            buff=0, color=DEP_COLOR, stroke_width=3,
        )
        w2 = Arrow(
            plane_right.c2p(0, 0), plane_right.c2p(2, 4),
            buff=0, color=DEP_COLOR, stroke_width=3,
        )
        w1_lab = MathTex(r"v_1", font_size=22, color=DEP_COLOR).next_to(
            plane_right.c2p(1, 2), LEFT, buff=0.1
        )
        w2_lab = MathTex(r"v_2 = 2v_1", font_size=22, color=DEP_COLOR).next_to(
            plane_right.c2p(2, 4), RIGHT, buff=0.1
        )

        self.play(Create(plane_right), Write(right_label))
        self.play(GrowArrow(w1), Write(w1_lab))
        self.play(GrowArrow(w2), Write(w2_lab))
        self.wait()

        dep_note = Text(
            "Dependent: one vector is a multiple of the other — they lie on the same line",
            font_size=20,
            color=GRAY,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(dep_note))
        self.wait(2)


class Lecture9_Spanning(Scene):
    """Show vectors that span R² vs don't span."""

    def construct(self):
        title = Text("Spanning a Space", font_size=36).to_edge(UP)
        self.play(Write(title))

        defn = MathTex(
            r"\text{Vectors } v_1, \ldots, v_k \text{ span } V"
            r"\;\text{if every } v \in V \text{ is a combination } "
            r"c_1 v_1 + \cdots + c_k v_k",
            font_size=26,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(defn))
        self.wait()

        # ── Spans R² ──
        plane_left = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            background_line_style={"stroke_opacity": 0.2},
        ).shift(LEFT * 3 + DOWN * 1)
        lab_l = Text("Spans R²", font_size=22, color=GREEN).next_to(
            plane_left, UP, buff=0.1
        )

        v1 = Arrow(
            plane_left.c2p(0, 0), plane_left.c2p(1, 0),
            buff=0, color=GREEN, stroke_width=3,
        )
        v2 = Arrow(
            plane_left.c2p(0, 0), plane_left.c2p(0, 1),
            buff=0, color=GREEN, stroke_width=3,
        )
        self.play(Create(plane_left), Write(lab_l))
        self.play(GrowArrow(v1), GrowArrow(v2))

        # Show that any point can be reached
        target = Dot(plane_left.c2p(2, 1.5), color=YELLOW, radius=0.06)
        dashed_h = DashedLine(
            plane_left.c2p(0, 0), plane_left.c2p(2, 0), color=YELLOW
        )
        dashed_v = DashedLine(
            plane_left.c2p(2, 0), plane_left.c2p(2, 1.5), color=YELLOW
        )
        self.play(Create(target), Create(dashed_h), Create(dashed_v))
        self.wait()

        # ── Does NOT span R² ──
        plane_right = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            background_line_style={"stroke_opacity": 0.2},
        ).shift(RIGHT * 3 + DOWN * 1)
        lab_r = Text("Does NOT span R²", font_size=22, color=RED).next_to(
            plane_right, UP, buff=0.1
        )

        w1 = Arrow(
            plane_right.c2p(0, 0), plane_right.c2p(1, 2),
            buff=0, color=RED, stroke_width=3,
        )
        w2 = Arrow(
            plane_right.c2p(0, 0), plane_right.c2p(2, 4),
            buff=0, color=RED, stroke_width=3,
        )
        span_line = Line(
            plane_right.c2p(-1.5, -3), plane_right.c2p(1.5, 3),
            color=RED_B, stroke_width=2, stroke_opacity=0.6,
        )
        self.play(Create(plane_right), Write(lab_r))
        self.play(GrowArrow(w1), GrowArrow(w2), Create(span_line))

        unreachable = Dot(plane_right.c2p(2, 0), color=YELLOW, radius=0.06)
        cross = MathTex(r"\times", font_size=28, color=YELLOW).move_to(
            plane_right.c2p(2, 0)
        )
        self.play(Create(unreachable), Write(cross))
        self.wait()

        note = Text(
            "Collinear vectors only span a line, not all of R²",
            font_size=22,
            color=GRAY,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(2)


class Lecture9_BasisDefinition(Scene):
    """Basis = independent + spanning. Standard basis of R³."""

    def construct(self):
        title = Text("Basis: Independent + Spanning", font_size=36).to_edge(UP)
        self.play(Write(title))

        defn = MathTex(
            r"\text{A }\textbf{basis}\text{ for a space }V\text{ is a set of vectors that:}",
            font_size=28,
        ).next_to(title, DOWN, buff=0.4)
        cond1 = MathTex(
            r"\text{1. Are linearly independent}", font_size=28, color=GREEN
        ).next_to(defn, DOWN, buff=0.2, aligned_edge=LEFT)
        cond2 = MathTex(
            r"\text{2. Span the space } V", font_size=28, color=GREEN
        ).next_to(cond1, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(defn))
        self.play(Write(cond1))
        self.play(Write(cond2))
        self.wait()

        # ── Standard basis of R³ ──
        std_title = Text("Standard basis for R³", font_size=26).next_to(
            cond2, DOWN, buff=0.5
        )
        self.play(Write(std_title))

        axes = ThreeDAxes(
            x_range=[-1, 2, 1],
            y_range=[-1, 2, 1],
            z_range=[-1, 2, 1],
            x_length=3,
            y_length=3,
            z_length=3,
        ).shift(DOWN * 1.5)

        e1_vec = MathTex(
            r"e_1 = \begin{pmatrix}1\\0\\0\end{pmatrix}", font_size=26, color=RED
        ).shift(LEFT * 4 + DOWN * 1.5)
        e2_vec = MathTex(
            r"e_2 = \begin{pmatrix}0\\1\\0\end{pmatrix}", font_size=26, color=GREEN
        ).next_to(e1_vec, RIGHT, buff=0.6)
        e3_vec = MathTex(
            r"e_3 = \begin{pmatrix}0\\0\\1\end{pmatrix}", font_size=26, color=BLUE
        ).next_to(e2_vec, RIGHT, buff=0.6)

        self.play(Write(e1_vec), Write(e2_vec), Write(e3_vec))
        self.wait()

        basis_note = MathTex(
            r"\text{Any } n \text{ independent vectors in } \mathbb{R}^n "
            r"\text{ form a basis for } \mathbb{R}^n",
            font_size=26,
            color=PIVOT_COLOR,
        ).to_edge(DOWN, buff=0.4)
        box = SurroundingRectangle(basis_note, color=PIVOT_COLOR, buff=0.15)
        self.play(Write(basis_note), Create(box))
        self.wait(2)


class Lecture9_DimensionTheorem(Scene):
    """Any two bases have the same number of vectors → dimension is well-defined."""

    def construct(self):
        title = Text("Dimension", font_size=36).to_edge(UP)
        self.play(Write(title))

        theorem = VGroup(
            MathTex(
                r"\textbf{Theorem: }",
                r"\text{All bases for a space } V \text{ have the same number of vectors.}",
                font_size=28,
            ),
            MathTex(
                r"\text{This number is the }\textbf{dimension}\text{ of } V.",
                font_size=28,
                color=PIVOT_COLOR,
            ),
        ).arrange(DOWN, buff=0.15).next_to(title, DOWN, buff=0.5)
        self.play(Write(theorem))
        self.wait()

        # ── Examples ──
        examples = VGroup(
            MathTex(r"\dim(\mathbb{R}^n) = n", font_size=30),
            MathTex(
                r"\dim(C(A)) = r \;\;\text{(rank)}", font_size=30, color=PIVOT_COLOR
            ),
            MathTex(
                r"\dim(N(A)) = n - r \;\;\text{(nullity)}",
                font_size=30,
                color=FREE_COLOR,
            ),
        ).arrange(DOWN, buff=0.3).next_to(theorem, DOWN, buff=0.6)

        for ex in examples:
            self.play(Write(ex))
            self.wait(0.5)

        # ── Rank–nullity again ──
        rank_nullity = MathTex(
            r"\underbrace{\dim(C(A))}_{\text{rank } r}"
            r"+ \underbrace{\dim(N(A))}_{\text{nullity } n-r}"
            r"= n \;\;(\text{number of columns})",
            font_size=28,
        ).next_to(examples, DOWN, buff=0.6)
        box = SurroundingRectangle(rank_nullity, color=PIVOT_COLOR, buff=0.2)
        self.play(Write(rank_nullity), Create(box))
        self.wait(2)


class Lecture9_ColumnSpaceBasis(Scene):
    """Pivot columns of the ORIGINAL matrix A form a basis for C(A)."""

    def construct(self):
        title = Text("Basis for the Column Space", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Matrix A ──
        a_label = MathTex("A", "=", font_size=36).shift(LEFT * 5 + UP * 1)
        A = Matrix(
            [[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]],
            h_buff=1.0,
            element_to_mobject=lambda e: MathTex(str(e), font_size=28),
        ).next_to(a_label, RIGHT, buff=0.2)
        self.play(Write(a_label), Write(A))
        self.wait()

        pivot_info = MathTex(
            r"\text{Pivot columns: 1 and 3}", font_size=28, color=PIVOT_COLOR
        ).next_to(A, DOWN, buff=0.4)
        self.play(Write(pivot_info))

        # Highlight columns 1 and 3 in A
        col1_entries = VGroup(*[A.get_entries()[i] for i in [0, 4, 8]])
        col3_entries = VGroup(*[A.get_entries()[i] for i in [2, 6, 10]])
        box1 = SurroundingRectangle(col1_entries, color=PIVOT_COLOR, buff=0.1)
        box3 = SurroundingRectangle(col3_entries, color=PIVOT_COLOR, buff=0.1)
        self.play(Create(box1), Create(box3))
        self.wait()

        # ── Basis vectors ──
        basis = MathTex(
            r"\text{Basis for } C(A): \;\;"
            r"\begin{pmatrix}1\\2\\3\end{pmatrix},\;"
            r"\begin{pmatrix}2\\6\\8\end{pmatrix}",
            font_size=30,
            color=PIVOT_COLOR,
        ).next_to(pivot_info, DOWN, buff=0.5)
        self.play(Write(basis))
        self.wait()

        # ── Warning ──
        warning = VGroup(
            Text("Use pivot columns of A (original), not U!", font_size=24, color=RED),
            MathTex(
                r"\text{Columns of } U \text{ have different combinations than columns of } A",
                font_size=24,
            ),
        ).arrange(DOWN, buff=0.15).next_to(basis, DOWN, buff=0.5)
        warn_box = SurroundingRectangle(warning, color=RED, buff=0.15)
        self.play(Write(warning), Create(warn_box))
        self.wait()

        dim_note = MathTex(
            r"\dim(C(A)) = r = 2", font_size=28, color=PIVOT_COLOR
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(dim_note))
        self.wait(2)
