"""
MIT 18.06 Linear Algebra — Lecture 1: The Geometry of Linear Equations
Following Gilbert Strang's lecture.

Scenes:
  1. Lecture1_RowPicture2D       — Two lines intersecting at (1,2)
  2. Lecture1_ColumnPicture2D    — Column vectors and their linear combination
  3. Lecture1_RowPicture3D       — Three planes intersecting in 3D
  4. Lecture1_ColumnPicture3D    — 3D column vectors combining to reach b
  5. Lecture1_SingularCase       — When columns are coplanar → can't reach all b
"""

from manim import *
import numpy as np


# ---------------------------------------------------------------------------
# Scene 1 — Row Picture (2×2)
# System:  2x -  y = 0
#         -x + 2y = 3
# Solution: (1, 2)
# ---------------------------------------------------------------------------
class Lecture1_RowPicture2D(Scene):
    def construct(self):
        # Title
        title = Text("Lecture 1 — Row Picture (2×2)", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Number plane
        plane = NumberPlane(
            x_range=[-2, 5, 1],
            y_range=[-1, 5, 1],
            x_length=7,
            y_length=6,
            background_line_style={"stroke_opacity": 0.4},
        ).shift(DOWN * 0.3)
        labels = plane.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(plane), Write(labels))

        # Line 1:  2x - y = 0  →  y = 2x
        line1 = plane.plot(lambda x: 2 * x, x_range=[-1, 2.5], color=BLUE)
        line1_label = MathTex("2x - y = 0", color=BLUE, font_size=30)
        line1_label.next_to(plane.c2p(2.2, 4.4), RIGHT, buff=0.15)

        # Line 2: -x + 2y = 3  →  y = (3 + x) / 2
        line2 = plane.plot(lambda x: (3 + x) / 2, x_range=[-2, 5], color=RED)
        line2_label = MathTex("-x + 2y = 3", color=RED, font_size=30)
        line2_label.next_to(plane.c2p(4, 3.5), RIGHT, buff=0.15)

        self.play(Create(line1), Write(line1_label))
        self.play(Create(line2), Write(line2_label))

        # Intersection point (1, 2)
        dot = Dot(plane.c2p(1, 2), color=YELLOW, radius=0.1)
        coord_label = MathTex("(1, 2)", color=YELLOW, font_size=30)
        coord_label.next_to(dot, UR, buff=0.15)
        self.play(FadeIn(dot, scale=1.5), Write(coord_label))

        # Equation summary
        solution = MathTex(
            r"x = 1, \; y = 2", font_size=36, color=YELLOW
        ).to_edge(DOWN)
        self.play(Write(solution))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 2 — Column Picture (2×2)
# x [2, -1] + y [-1, 2] = [0, 3]   with x=1, y=2
# ---------------------------------------------------------------------------
class Lecture1_ColumnPicture2D(Scene):
    def construct(self):
        title = Text("Lecture 1 — Column Picture (2×2)", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        plane = NumberPlane(
            x_range=[-3, 4, 1],
            y_range=[-3, 5, 1],
            x_length=7,
            y_length=7,
            background_line_style={"stroke_opacity": 0.4},
        ).shift(DOWN * 0.3)
        labels = plane.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(plane), Write(labels))

        # Column 1: [2, -1]
        col1 = Arrow(
            plane.c2p(0, 0), plane.c2p(2, -1),
            buff=0, color=BLUE, stroke_width=5
        )
        col1_label = MathTex(
            r"\begin{bmatrix} 2 \\ -1 \end{bmatrix}",
            color=BLUE, font_size=28
        ).next_to(col1, DOWN, buff=0.1)

        # Column 2: [-1, 2]
        col2 = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 2),
            buff=0, color=RED, stroke_width=5
        )
        col2_label = MathTex(
            r"\begin{bmatrix} -1 \\ 2 \end{bmatrix}",
            color=RED, font_size=28
        ).next_to(col2, LEFT, buff=0.1)

        self.play(GrowArrow(col1), Write(col1_label))
        self.play(GrowArrow(col2), Write(col2_label))

        # Show the combination equation
        combo_eq = MathTex(
            r"x", r"\begin{bmatrix} 2 \\ -1 \end{bmatrix}",
            r"+\; y", r"\begin{bmatrix} -1 \\ 2 \end{bmatrix}",
            r"=", r"\begin{bmatrix} 0 \\ 3 \end{bmatrix}",
            font_size=30,
        ).to_edge(DOWN, buff=0.6)
        combo_eq[0].set_color(BLUE)
        combo_eq[1].set_color(BLUE)
        combo_eq[2].set_color(RED)
        combo_eq[3].set_color(RED)
        combo_eq[5].set_color(YELLOW)
        self.play(Write(combo_eq))

        # x=1 copy of col1, then y=2 copies of col2 placed head-to-tail
        # 1 * [2,-1] = [2,-1]
        scaled_col1 = Arrow(
            plane.c2p(0, 0), plane.c2p(2, -1),
            buff=0, color=BLUE, stroke_width=4
        )
        # 2 * [-1, 2] = [-2, 4], placed at tip of col1 → (2,-1) to (0, 3)
        scaled_col2 = Arrow(
            plane.c2p(2, -1), plane.c2p(0, 3),
            buff=0, color=RED, stroke_width=4
        )
        self.play(GrowArrow(scaled_col1))
        self.play(GrowArrow(scaled_col2))

        # Result vector b = [0, 3]
        result = Arrow(
            plane.c2p(0, 0), plane.c2p(0, 3),
            buff=0, color=YELLOW, stroke_width=5
        )
        b_label = MathTex(
            r"\mathbf{b} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}",
            color=YELLOW, font_size=28,
        ).next_to(result, LEFT, buff=0.15)
        self.play(GrowArrow(result), Write(b_label))

        answer = MathTex(r"x=1,\; y=2", font_size=34, color=GREEN)
        answer.next_to(combo_eq, UP, buff=0.3)
        self.play(Write(answer))
        self.wait(2)


# ---------------------------------------------------------------------------
# Scene 3 — Row Picture (3×3)
# System:  2x -  y      = 0
#         -x + 2y -  z  = -1
#               -3y + 4z = 4
# Solution: (0, 0, 1)
# ---------------------------------------------------------------------------
class Lecture1_RowPicture3D(ThreeDScene):
    def construct(self):
        title = Text("Lecture 1 — Row Picture (3×3)", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.set_camera_orientation(phi=70 * DEGREES, theta=-40 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6, y_length=6, z_length=6,
        )
        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x"), y_label=MathTex("y"), z_label=MathTex("z")
        )
        self.play(Create(axes), Write(axis_labels))

        # Plane 1: 2x - y = 0  →  y = 2x  (any z)
        plane1 = Surface(
            lambda u, v: axes.c2p(u, 2 * u, v),
            u_range=[-2, 2], v_range=[-2, 2],
            resolution=(8, 8),
            fill_opacity=0.3,
            stroke_width=0.5,
        ).set_color(BLUE)

        # Plane 2: -x + 2y - z = -1  →  z = -x + 2y + 1
        plane2 = Surface(
            lambda u, v: axes.c2p(u, v, -u + 2 * v + 1),
            u_range=[-2, 2], v_range=[-2, 2],
            resolution=(8, 8),
            fill_opacity=0.3,
            stroke_width=0.5,
        ).set_color(RED)

        # Plane 3: -3y + 4z = 4  →  z = (4 + 3y) / 4
        plane3 = Surface(
            lambda u, v: axes.c2p(u, v, (4 + 3 * v) / 4),
            u_range=[-2, 2], v_range=[-2, 2],
            resolution=(8, 8),
            fill_opacity=0.3,
            stroke_width=0.5,
        ).set_color(GREEN)

        lbl1 = MathTex("2x - y = 0", font_size=26, color=BLUE)
        lbl2 = MathTex("-x + 2y - z = -1", font_size=26, color=RED)
        lbl3 = MathTex("-3y + 4z = 4", font_size=26, color=GREEN)
        legend = VGroup(lbl1, lbl2, lbl3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend.to_corner(UL, buff=0.5).shift(DOWN * 0.7)
        self.add_fixed_in_frame_mobjects(legend)

        self.play(Create(plane1), Write(lbl1))
        self.play(Create(plane2), Write(lbl2))
        self.play(Create(plane3), Write(lbl3))

        # Intersection point (0, 0, 1)
        dot = Dot3D(axes.c2p(0, 0, 1), color=YELLOW, radius=0.1)
        self.play(FadeIn(dot, scale=1.5))

        sol_label = MathTex(r"(0,\,0,\,1)", font_size=30, color=YELLOW)
        sol_label.next_to(legend, DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(sol_label)
        self.play(Write(sol_label))

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait()


# ---------------------------------------------------------------------------
# Scene 4 — Column Picture (3×3)
# Columns: [2,-1,0], [-1,2,-3], [0,-1,4]
# b = [0, -1, 4],  solution x=0, y=0, z=1
# ---------------------------------------------------------------------------
class Lecture1_ColumnPicture3D(ThreeDScene):
    def construct(self):
        title = Text("Lecture 1 — Column Picture (3×3)", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.set_camera_orientation(phi=70 * DEGREES, theta=-40 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 5, 1],
            x_length=6, y_length=6, z_length=6,
        )
        self.play(Create(axes))

        # Column vectors
        col_data = [
            ([2, -1, 0], BLUE, r"\mathbf{c}_1 = \begin{bmatrix}2\\-1\\0\end{bmatrix}"),
            ([-1, 2, -3], RED, r"\mathbf{c}_2 = \begin{bmatrix}-1\\2\\-3\end{bmatrix}"),
            ([0, -1, 4], GREEN, r"\mathbf{c}_3 = \begin{bmatrix}0\\-1\\4\end{bmatrix}"),
        ]

        arrows = []
        for vec, color, _ in col_data:
            arr = Arrow3D(
                start=axes.c2p(0, 0, 0),
                end=axes.c2p(*vec),
                color=color,
            )
            arrows.append(arr)

        legend_items = []
        for _, color, tex in col_data:
            legend_items.append(MathTex(tex, font_size=24, color=color))
        legend = VGroup(*legend_items).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend.to_corner(UL, buff=0.5).shift(DOWN * 0.7)
        self.add_fixed_in_frame_mobjects(legend)

        for arr, item in zip(arrows, legend_items):
            self.play(Create(arr), Write(item), run_time=0.8)

        # Show the equation
        eq = MathTex(
            r"x\,\mathbf{c}_1 + y\,\mathbf{c}_2 + z\,\mathbf{c}_3 = \mathbf{b}",
            font_size=30,
        )
        eq.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(eq)
        self.play(Write(eq))

        # Solution: x=0, y=0, z=1  →  result is column 3 = [0,-1,4]
        b_arrow = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(0, -1, 4),
            color=YELLOW,
        )
        self.play(Create(b_arrow))

        sol = MathTex(
            r"x=0,\; y=0,\; z=1", font_size=30, color=YELLOW
        )
        sol.next_to(eq, UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(sol)
        self.play(Write(sol))

        insight = MathTex(
            r"A\mathbf{x} = \mathbf{b}",
            r"\;\text{ asks: is } \mathbf{b} \text{ in the column space of } A\text{?}",
            font_size=28, color=TEAL,
        )
        insight.to_edge(DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(insight)
        self.play(FadeOut(eq), Write(insight))

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait()


# ---------------------------------------------------------------------------
# Scene 5 — Singular Case
# When columns lie in the same plane → can't reach every b
# ---------------------------------------------------------------------------
class Lecture1_SingularCase(ThreeDScene):
    def construct(self):
        title = Text("Lecture 1 — Singular Case", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.set_camera_orientation(phi=70 * DEGREES, theta=-40 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=6, y_length=6, z_length=6,
        )
        self.play(Create(axes))

        # Three coplanar column vectors (all in xy-plane, z=0)
        vecs = [
            ([2, 1, 0], BLUE, r"\mathbf{c}_1"),
            ([1, 2, 0], RED, r"\mathbf{c}_2"),
            ([3, 3, 0], GREEN, r"\mathbf{c}_3"),   # c1 + c2 → dependent
        ]

        arrows = []
        for v, c, _ in vecs:
            arr = Arrow3D(
                start=axes.c2p(0, 0, 0),
                end=axes.c2p(*v),
                color=c,
            )
            arrows.append(arr)
            self.play(Create(arr), run_time=0.6)

        # Show the plane they span (xy-plane patch)
        span_plane = Surface(
            lambda u, v: axes.c2p(u, v, 0),
            u_range=[-3, 3], v_range=[-3, 3],
            resolution=(6, 6),
            fill_opacity=0.25,
            stroke_width=0.5,
        ).set_color(PURPLE)
        self.play(Create(span_plane))

        # A b NOT in that plane
        b_arrow = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1, 1, 2),
            color=YELLOW,
        )
        b_label = MathTex(
            r"\mathbf{b} = \begin{bmatrix}1\\1\\2\end{bmatrix}",
            font_size=26, color=YELLOW,
        )
        b_label.to_corner(UR, buff=0.6).shift(DOWN)
        self.add_fixed_in_frame_mobjects(b_label)
        self.play(Create(b_arrow), Write(b_label))

        # Explanation
        fail_text = VGroup(
            Text("Columns are coplanar", font_size=26, color=RED),
            MathTex(
                r"\Rightarrow \text{can't reach } \mathbf{b} \text{ outside the plane}",
                font_size=26, color=RED,
            ),
            Text("Matrix is SINGULAR", font_size=28, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(fail_text)
        self.play(Write(fail_text), run_time=2)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait()
