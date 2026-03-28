"""
MIT 18.06 Lecture 1: The Geometry of Linear Equations
Row Picture vs Column Picture

System:
  2x - y = 0
  -x + 2y = 3

Solution: x=1, y=2
"""

from manim import *


class Lecture1_RowPicture(Scene):
    """Row Picture: Two lines intersecting at (1,2)"""

    def construct(self):
        # Title
        title = Text("Row Picture", font_size=42, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # Create axes
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-2, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 24},
        ).shift(DOWN * 0.3)
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Equation 1: 2x - y = 0 => y = 2x
        line1 = axes.plot(lambda x: 2 * x, x_range=[-1, 2.5], color=BLUE)
        eq1 = MathTex("2x - y = 0", color=BLUE, font_size=32)
        eq1.next_to(line1, RIGHT, buff=0.3).shift(UP * 0.5)

        self.play(Create(line1), Write(eq1))
        self.wait(0.5)

        # Equation 2: -x + 2y = 3 => y = (3+x)/2
        line2 = axes.plot(lambda x: (3 + x) / 2, x_range=[-2, 4], color=RED)
        eq2 = MathTex("-x + 2y = 3", color=RED, font_size=32)
        eq2.next_to(line2, RIGHT, buff=0.3).shift(DOWN * 0.3)

        self.play(Create(line2), Write(eq2))
        self.wait(0.5)

        # Intersection point
        dot = Dot(axes.c2p(1, 2), color=GREEN, radius=0.12)
        label = MathTex("(1, 2)", color=GREEN, font_size=32)
        label.next_to(dot, UR, buff=0.2)

        self.play(FadeIn(dot, scale=2), Write(label))
        self.wait(0.5)

        # Explanation
        explanation = Text(
            "Each equation = a line\nSolution = intersection",
            font_size=24,
            color=WHITE,
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)


class Lecture1_ColumnPicture(Scene):
    """Column Picture: Linear combination of column vectors"""

    def construct(self):
        # Title
        title = Text("Column Picture", font_size=42, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # Show the equation Ax = b
        eq_matrix = MathTex(
            r"x \begin{bmatrix} 2 \\ -1 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}",
            font_size=36,
        )
        eq_matrix.to_edge(UP).shift(DOWN * 0.8)
        self.play(Write(eq_matrix))
        self.wait(1)

        # Create axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(DOWN * 0.5)
        self.play(Create(axes))

        # Column vector 1: [2, -1]
        col1 = Arrow(
            axes.c2p(0, 0), axes.c2p(2, -1), buff=0, color=BLUE, stroke_width=4
        )
        col1_label = MathTex(
            r"\vec{c_1} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}",
            color=BLUE,
            font_size=28,
        )
        col1_label.next_to(col1, DOWN, buff=0.2)

        self.play(GrowArrow(col1), Write(col1_label))
        self.wait(0.5)

        # Column vector 2: [-1, 2]
        col2 = Arrow(
            axes.c2p(0, 0), axes.c2p(-1, 2), buff=0, color=RED, stroke_width=4
        )
        col2_label = MathTex(
            r"\vec{c_2} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}",
            color=RED,
            font_size=28,
        )
        col2_label.next_to(col2, LEFT, buff=0.2)

        self.play(GrowArrow(col2), Write(col2_label))
        self.wait(1)

        # Now show x=1 times col1
        self.play(FadeOut(col1_label), FadeOut(col2_label))

        step1_text = MathTex(r"1 \times \vec{c_1}", color=BLUE, font_size=30)
        step1_text.to_corner(DL).shift(UP * 1.5)
        # x=1, so col1 stays the same: [2, -1]
        scaled_col1 = Arrow(
            axes.c2p(0, 0), axes.c2p(2, -1), buff=0, color=BLUE, stroke_width=5
        )
        self.play(Write(step1_text), Transform(col1, scaled_col1))
        self.wait(0.5)

        # y=2 times col2: 2 * [-1, 2] = [-2, 4]
        step2_text = MathTex(r"2 \times \vec{c_2}", color=RED, font_size=30)
        step2_text.next_to(step1_text, DOWN, buff=0.3)
        scaled_col2 = Arrow(
            axes.c2p(0, 0), axes.c2p(-2, 4), buff=0, color=RED, stroke_width=5
        )
        self.play(Write(step2_text), Transform(col2, scaled_col2))
        self.wait(0.5)

        # Show addition: move scaled_col2 to tip of scaled_col1
        # col1 tip is at (2, -1), col2 goes to (-2, 4), so from (2,-1) it goes to (0, 3)
        moved_col2 = Arrow(
            axes.c2p(2, -1), axes.c2p(0, 3), buff=0, color=RED, stroke_width=5
        )
        plus_text = MathTex("+", font_size=36)
        plus_text.next_to(step1_text, RIGHT, buff=0.5)

        self.play(Write(plus_text), Transform(col2, moved_col2))
        self.wait(0.5)

        # Result vector [0, 3]
        result = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 3), buff=0, color=GREEN, stroke_width=6
        )
        result_label = MathTex(
            r"\begin{bmatrix} 0 \\ 3 \end{bmatrix}", color=GREEN, font_size=32
        )
        result_label.next_to(result, LEFT, buff=0.2)
        result_dot = Dot(axes.c2p(0, 3), color=GREEN, radius=0.1)

        equals_text = MathTex(
            r"= \begin{bmatrix} 0 \\ 3 \end{bmatrix}", font_size=30, color=GREEN
        )
        equals_text.next_to(plus_text, RIGHT, buff=0.3)

        self.play(
            GrowArrow(result),
            Write(result_label),
            FadeIn(result_dot),
            Write(equals_text),
        )
        self.wait(1)

        # Key insight
        insight = Text(
            "Find the right combination of columns!",
            font_size=28,
            color=YELLOW,
        )
        insight.to_edge(DOWN)
        self.play(Write(insight))
        self.wait(2)


class Lecture1_WhenItFails(Scene):
    """When columns are dependent — no solution for some b"""

    def construct(self):
        title = Text("When does it fail?", font_size=42, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(DOWN * 0.3)
        self.play(Create(axes))

        # Two vectors pointing in the same direction
        col1 = Arrow(
            axes.c2p(0, 0), axes.c2p(2, 1), buff=0, color=BLUE, stroke_width=4
        )
        col1_label = MathTex(r"\vec{c_1}", color=BLUE, font_size=28)
        col1_label.next_to(col1.get_end(), UR, buff=0.1)

        col2 = Arrow(
            axes.c2p(0, 0), axes.c2p(-2, -1), buff=0, color=RED, stroke_width=4
        )
        col2_label = MathTex(r"\vec{c_2}", color=RED, font_size=28)
        col2_label.next_to(col2.get_end(), DL, buff=0.1)

        self.play(GrowArrow(col1), Write(col1_label))
        self.play(GrowArrow(col2), Write(col2_label))
        self.wait(0.5)

        # Show the line they span
        span_line = DashedLine(
            axes.c2p(-3, -1.5), axes.c2p(3, 1.5), color=GREY, stroke_width=2
        )
        span_text = Text("All combinations stay on this line!", font_size=24, color=GREY)
        span_text.next_to(span_line, UP, buff=0.5).shift(RIGHT)

        self.play(Create(span_line), Write(span_text))
        self.wait(1)

        # Target point NOT on the line
        target = Dot(axes.c2p(1, 3), color=GREEN, radius=0.12)
        target_label = MathTex(r"\vec{b}", color=GREEN, font_size=32)
        target_label.next_to(target, UR, buff=0.1)

        self.play(FadeIn(target, scale=2), Write(target_label))

        # X mark
        cross = Text("✗ Can't reach!", font_size=28, color=RED)
        cross.next_to(target, RIGHT, buff=0.3)
        self.play(Write(cross))
        self.wait(1)

        # Key insight
        insight = VGroup(
            Text("Columns point in SAME direction", font_size=26, color=RED),
            Text("= linearly dependent", font_size=26, color=RED),
            Text("= can't solve Ax = b for every b", font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        insight.to_edge(DOWN)
        self.play(Write(insight))
        self.wait(3)
