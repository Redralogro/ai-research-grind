"""
MIT 18.06 Lecture 1: The Geometry of Linear Equations
Row Picture vs Column Picture

System:
  2x - y = 0
  -x + 2y = 3

Solution: x=1, y=2

Layout: Split-screen — info panel (left) + graph (right)
Style: 3Blue1Brown inspired
"""

from manim import *


class Lecture1_RowPicture(Scene):
    """Row Picture: Two lines intersecting at (1,2)"""

    def construct(self):
        # === LAYOUT: Left panel (equations) | Right panel (graph) ===
        divider = Line(UP * 4, DOWN * 4, color=GREY, stroke_width=1, stroke_opacity=0.3)
        divider.shift(LEFT * 2.5)

        # Title
        title = Text("Row Picture", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # Left panel: equations
        eq_group = VGroup(
            Text("System:", font_size=22, color=GREY),
            MathTex(r"2x - y = 0", color=BLUE, font_size=34),
            MathTex(r"-x + 2y = 3", color=RED, font_size=34),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        eq_group.move_to(LEFT * 5 + UP * 0.5)

        # Right panel: axes (shifted right)
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 22},
        ).shift(RIGHT * 1.5 + DOWN * 0.3)
        labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=28),
            y_label=MathTex("y", font_size=28),
        )

        self.play(Create(divider), Create(axes), Write(labels))

        # Equation 1: y = 2x
        line1 = axes.plot(lambda x: 2 * x, x_range=[-0.5, 2.3], color=BLUE, stroke_width=3)
        self.play(Write(eq_group[0]), Write(eq_group[1]), Create(line1))
        self.wait(0.5)

        # Equation 2: y = (3+x)/2
        line2 = axes.plot(lambda x: (3 + x) / 2, x_range=[-1, 4], color=RED, stroke_width=3)
        self.play(Write(eq_group[2]), Create(line2))
        self.wait(0.5)

        # Intersection
        dot = Dot(axes.c2p(1, 2), color=GREEN, radius=0.1)
        sol_label = MathTex("(1, 2)", color=GREEN, font_size=30)
        sol_label.next_to(dot, UR, buff=0.15)

        self.play(FadeIn(dot, scale=2), Write(sol_label))
        self.wait(0.5)

        # Solution in left panel
        sol_panel = VGroup(
            Text("Solution:", font_size=22, color=GREY),
            MathTex(r"x = 1, \quad y = 2", color=GREEN, font_size=32),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        sol_panel.move_to(LEFT * 5 + DOWN * 1.5)

        insight = Text(
            "Each equation = a line\nSolution = intersection",
            font_size=20,
            color=YELLOW,
            line_spacing=1.3,
        )
        insight.move_to(LEFT * 5 + DOWN * 3)

        self.play(Write(sol_panel))
        self.wait(0.5)
        self.play(Write(insight))
        self.wait(2)


class Lecture1_ColumnPicture(Scene):
    """Column Picture: Linear combination of column vectors"""

    def construct(self):
        # Title
        title = Text("Column Picture", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # === LAYOUT ===
        divider = Line(UP * 4, DOWN * 4, color=GREY, stroke_width=1, stroke_opacity=0.3)
        divider.shift(LEFT * 2.5)
        self.play(Create(divider))

        # Left panel: matrix equation
        eq_matrix = MathTex(
            r"x", r"\begin{bmatrix} 2 \\ -1 \end{bmatrix}",
            r"+", r"y", r"\begin{bmatrix} -1 \\ 2 \end{bmatrix}",
            r"=", r"\begin{bmatrix} 0 \\ 3 \end{bmatrix}",
            font_size=30,
        )
        eq_matrix[0].set_color(BLUE)
        eq_matrix[1].set_color(BLUE)
        eq_matrix[3].set_color(RED)
        eq_matrix[4].set_color(RED)
        eq_matrix[6].set_color(GREEN)
        eq_matrix.move_to(LEFT * 5 + UP * 1.5)

        self.play(Write(eq_matrix))
        self.wait(1)

        # Right panel: axes
        axes = Axes(
            x_range=[-3, 4, 1],
            y_range=[-2, 5, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(RIGHT * 1.5 + DOWN * 0.3)
        self.play(Create(axes))

        # Column vector 1: [2, -1]
        col1 = Arrow(
            axes.c2p(0, 0), axes.c2p(2, -1), buff=0, color=BLUE, stroke_width=4
        )
        col1_label = MathTex(r"\vec{c_1}", color=BLUE, font_size=26)
        col1_label.next_to(axes.c2p(2, -1), DR, buff=0.1)

        self.play(GrowArrow(col1), Write(col1_label))
        self.wait(0.3)

        # Column vector 2: [-1, 2]
        col2 = Arrow(
            axes.c2p(0, 0), axes.c2p(-1, 2), buff=0, color=RED, stroke_width=4
        )
        col2_label = MathTex(r"\vec{c_2}", color=RED, font_size=26)
        col2_label.next_to(axes.c2p(-1, 2), UL, buff=0.1)

        self.play(GrowArrow(col2), Write(col2_label))
        self.wait(0.5)

        # Step 1: x=1, keep col1 as is
        step1 = MathTex(r"1 \times \vec{c_1} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}", 
                        color=BLUE, font_size=26)
        step1.move_to(LEFT * 5 + DOWN * 0.2)

        self.play(FadeOut(col1_label), FadeOut(col2_label))
        self.play(Write(step1), col1.animate.set_stroke(width=5))
        self.wait(0.3)

        # Step 2: y=2, scale col2 to [-2, 4]
        step2 = MathTex(r"2 \times \vec{c_2} = \begin{bmatrix} -2 \\ 4 \end{bmatrix}",
                        color=RED, font_size=26)
        step2.move_to(LEFT * 5 + DOWN * 1.2)

        scaled_col2 = Arrow(
            axes.c2p(0, 0), axes.c2p(-2, 4), buff=0, color=RED, stroke_width=5
        )
        self.play(Write(step2), Transform(col2, scaled_col2))
        self.wait(0.5)

        # Move col2 to tip of col1 (tip-to-tail addition)
        moved_col2 = Arrow(
            axes.c2p(2, -1), axes.c2p(0, 3), buff=0, color=RED, stroke_width=4,
            stroke_opacity=0.8,
        )
        # Dashed guide from origin to col1 tip
        guide = DashedLine(
            axes.c2p(0, 0), axes.c2p(2, -1), color=BLUE, stroke_width=1, stroke_opacity=0.4
        )

        add_label = Text("tip-to-tail", font_size=18, color=GREY)
        add_label.next_to(moved_col2, RIGHT, buff=0.15)

        self.play(Transform(col2, moved_col2), FadeIn(guide), FadeIn(add_label))
        self.wait(0.5)

        # Result: [0, 3]
        result = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 3), buff=0, color=GREEN, stroke_width=6
        )
        result_dot = Dot(axes.c2p(0, 3), color=GREEN, radius=0.08)
        result_label = MathTex(r"\begin{bmatrix} 0 \\ 3 \end{bmatrix}",
                              color=GREEN, font_size=26)
        result_label.next_to(axes.c2p(0, 3), LEFT, buff=0.3)

        # Result in left panel
        step3 = MathTex(r"= \begin{bmatrix} 0 \\ 3 \end{bmatrix} \checkmark",
                        color=GREEN, font_size=28)
        step3.move_to(LEFT * 5 + DOWN * 2.2)

        self.play(
            GrowArrow(result), FadeIn(result_dot),
            Write(result_label), Write(step3),
        )
        self.wait(0.5)

        # Insight
        insight = Text(
            "Find the right\ncombination of columns!",
            font_size=22, color=YELLOW, line_spacing=1.3,
        )
        insight.move_to(LEFT * 5 + DOWN * 3.2)
        self.play(Write(insight))
        self.wait(2)


class Lecture1_WhenItFails(Scene):
    """When columns are dependent — can't reach every b"""

    def construct(self):
        title = Text("When does it fail?", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # Layout
        divider = Line(UP * 4, DOWN * 4, color=GREY, stroke_width=1, stroke_opacity=0.3)
        divider.shift(LEFT * 2.5)
        self.play(Create(divider))

        # Left panel — compact, no overlap
        info = VGroup(
            Text("Problem:", font_size=20, color=GREY),
            Text("Columns are collinear", font_size=18, color=RED),
            Text("(one is a scalar multiple)", font_size=14, color=GREY),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        info.move_to(LEFT * 5 + UP * 1.5)

        self.play(Write(info))

        # Right panel: axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 4, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(RIGHT * 1.5 + DOWN * 0.3)
        self.play(Create(axes))

        # Two vectors in the same direction
        col1 = Arrow(
            axes.c2p(0, 0), axes.c2p(2, 1), buff=0, color=BLUE, stroke_width=4
        )
        col1_label = MathTex(r"\vec{c_1}", color=BLUE, font_size=24)
        col1_label.next_to(axes.c2p(2, 1), UR, buff=0.1)

        col2 = Arrow(
            axes.c2p(0, 0), axes.c2p(-2, -1), buff=0, color=RED, stroke_width=4
        )
        col2_label = MathTex(r"\vec{c_2}", color=RED, font_size=24)
        col2_label.next_to(axes.c2p(-2, -1), DL, buff=0.1)

        self.play(GrowArrow(col1), Write(col1_label))
        self.play(GrowArrow(col2), Write(col2_label))
        self.wait(0.3)

        # Show the line they span
        span_line = DashedLine(
            axes.c2p(-3.5, -1.75), axes.c2p(3.5, 1.75),
            color=YELLOW, stroke_width=2, stroke_opacity=0.5,
        )
        span_text = Text("all combinations\nland here", font_size=16, color=YELLOW)
        span_text.next_to(axes.c2p(3, 1.5), UP, buff=0.15)

        self.play(Create(span_line), Write(span_text))
        self.wait(0.5)

        # Target NOT on the line
        target = Dot(axes.c2p(1, 3), color=GREEN, radius=0.12)
        target_label = MathTex(r"\vec{b}", color=GREEN, font_size=28)
        target_label.next_to(target, RIGHT, buff=0.15)

        self.play(FadeIn(target, scale=2), Write(target_label))

        # Cross mark
        cross = MathTex(r"\times", color=RED, font_size=40)
        cross.next_to(target, LEFT, buff=0.15)
        self.play(Write(cross))
        self.wait(0.5)

        # Left panel: explanation — use smaller font, more spacing control
        eq_dep = MathTex(r"\vec{c_2} = -\vec{c_1}", font_size=24, color=GREY)
        eq_dep.move_to(LEFT * 5 + DOWN * 0)

        text_dep = Text("Linearly dependent!", font_size=18, color=RED)
        text_dep.move_to(LEFT * 5 + DOWN * 0.6)

        text_cover = Text("Can only reach a line,", font_size=16, color=WHITE)
        text_cover.move_to(LEFT * 5 + DOWN * 1.2)

        text_cover2 = Text("not all of 2D", font_size=16, color=WHITE)
        text_cover2.move_to(LEFT * 5 + DOWN * 1.6)

        text_result = MathTex(r"\Rightarrow \text{No solution for some } \vec{b}",
                             font_size=22, color=YELLOW)
        text_result.move_to(LEFT * 4.5 + DOWN * 2.3)

        self.play(Write(eq_dep))
        self.play(Write(text_dep))
        self.play(Write(text_cover), Write(text_cover2))
        self.play(Write(text_result))
        self.wait(3)
