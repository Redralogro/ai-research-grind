"""
Lecture 8: Solving Ax = b — Row Reduced Form R
MIT 18.06 Linear Algebra (Gilbert Strang)

Scenes:
  1. Lecture8_AugmentedElimination  — Eliminate [A|b], solvability condition
  2. Lecture8_ParticularSolution    — Set free vars = 0, solve for pivots
  3. Lecture8_CompleteSolution      — x = xₚ + xₙ, geometric picture
  4. Lecture8_RankCases             — The four cases of rank vs m, n
"""

from manim import *

PIVOT_COLOR = YELLOW
FREE_COLOR = TEAL
HIGHLIGHT = RED


class Lecture8_AugmentedElimination(Scene):
    """Augmented matrix [A|b] elimination and solvability condition."""

    def construct(self):
        title = Text("Lecture 8: Solving Ax = b", font_size=40).to_edge(UP)
        subtitle = Text(
            "Augmented Elimination", font_size=28, color=GRAY
        ).next_to(title, DOWN, buff=0.2)
        self.play(Write(title), FadeIn(subtitle))
        self.wait()

        # ── [A | b] ──
        aug_label = MathTex(r"[A \mid b]", "=", font_size=36).shift(
            LEFT * 4.5 + UP * 0.3
        )
        Aug = Matrix(
            [
                [1, 2, 2, 2, "b_1"],
                [2, 4, 6, 8, "b_2"],
                [3, 6, 8, 10, "b_3"],
            ],
            h_buff=1.2,
            element_to_mobject=lambda e: MathTex(str(e), font_size=30),
        ).next_to(aug_label, RIGHT, buff=0.2)
        self.play(Write(aug_label), Write(Aug))
        self.wait()

        # ── Elimination steps (same as lecture 7, carrying b along) ──
        steps_text = [
            r"R_2 \leftarrow R_2 - 2R_1",
            r"R_3 \leftarrow R_3 - 3R_1",
            r"R_3 \leftarrow R_3 - R_2",
        ]
        matrices = [
            [[1, 2, 2, 2, "b_1"], [0, 0, 2, 4, "b_2-2b_1"], [3, 6, 8, 10, "b_3"]],
            [
                [1, 2, 2, 2, "b_1"],
                [0, 0, 2, 4, "b_2-2b_1"],
                [0, 0, 2, 4, "b_3-3b_1"],
            ],
            [
                [1, 2, 2, 2, "b_1"],
                [0, 0, 2, 4, "b_2-2b_1"],
                [0, 0, 0, 0, "b_3-b_2-b_1"],
            ],
        ]
        step_mob = MathTex(steps_text[0], font_size=28, color=HIGHLIGHT).to_edge(
            DOWN, buff=1.5
        )
        self.play(Write(step_mob))
        for i, (st, mat_data) in enumerate(zip(steps_text, matrices)):
            new_step = MathTex(st, font_size=28, color=HIGHLIGHT).to_edge(
                DOWN, buff=1.5
            )
            new_mat = Matrix(
                mat_data,
                h_buff=1.2,
                element_to_mobject=lambda e: MathTex(str(e), font_size=30),
            ).move_to(Aug)
            anims = [Transform(Aug, new_mat)]
            if i > 0:
                anims.append(Transform(step_mob, new_step))
            self.play(*anims)
            self.wait(0.8)

        self.play(FadeOut(step_mob))

        # ── Solvability condition ──
        cond = MathTex(
            r"\text{Solvable iff } b_3 - b_2 - b_1 = 0",
            font_size=32,
            color=PIVOT_COLOR,
        ).to_edge(DOWN, buff=1.5)
        box = SurroundingRectangle(cond, color=PIVOT_COLOR, buff=0.15)
        self.play(Write(cond), Create(box))
        self.wait()

        explain = Text(
            "Row 3 of [A|b] is all zeros only when this holds",
            font_size=22,
            color=GRAY,
        ).next_to(cond, DOWN, buff=0.25)
        self.play(Write(explain))
        self.wait()

        # ── Concrete example ──
        concrete = MathTex(
            r"b = \begin{pmatrix}1\\5\\6\end{pmatrix}"
            r"\;\Longrightarrow\; 6 - 5 - 1 = 0 \;\checkmark",
            font_size=30,
        ).next_to(explain, DOWN, buff=0.3)
        self.play(Write(concrete))
        self.wait(2)


class Lecture8_ParticularSolution(Scene):
    """Find xₚ: set free variables = 0, solve for pivot variables."""

    def construct(self):
        title = Text("Particular Solution xₚ", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Take b = (1,5,6) ──
        setup = MathTex(
            r"A = \begin{pmatrix}1&2&2&2\\2&4&6&8\\3&6&8&10\end{pmatrix},\quad"
            r"b = \begin{pmatrix}1\\5\\6\end{pmatrix}",
            font_size=30,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(setup))
        self.wait()

        # ── After elimination ──
        elim = MathTex(
            r"U = \begin{pmatrix}1&2&2&2\\0&0&2&4\\0&0&0&0\end{pmatrix},\quad"
            r"c = \begin{pmatrix}1\\3\\0\end{pmatrix}",
            font_size=30,
        ).next_to(setup, DOWN, buff=0.4)
        self.play(Write(elim))
        self.wait()

        # ── Set free variables to 0 ──
        free = MathTex(
            r"\text{Set free variables } x_2 = 0,\; x_4 = 0",
            font_size=28,
            color=FREE_COLOR,
        ).next_to(elim, DOWN, buff=0.5)
        self.play(Write(free))
        self.wait()

        # ── Back-substitution ──
        back_sub = VGroup(
            MathTex(r"2x_3 = 3 \;\Rightarrow\; x_3 = \tfrac{3}{2}", font_size=28),
            MathTex(
                r"x_1 + 2(0) + 2\!\left(\tfrac{3}{2}\right) + 2(0) = 1"
                r"\;\Rightarrow\; x_1 = -2",
                font_size=28,
            ),
        ).arrange(DOWN, buff=0.2).next_to(free, DOWN, buff=0.4)
        self.play(Write(back_sub[0]))
        self.wait(0.5)
        self.play(Write(back_sub[1]))
        self.wait()

        xp = MathTex(
            r"x_p = \begin{pmatrix}-2\\0\\\frac{3}{2}\\0\end{pmatrix}",
            font_size=36,
            color=PIVOT_COLOR,
        ).next_to(back_sub, DOWN, buff=0.4)
        box = SurroundingRectangle(xp, color=PIVOT_COLOR, buff=0.15)
        self.play(Write(xp), Create(box))
        self.wait(2)


class Lecture8_CompleteSolution(Scene):
    """x = xₚ + xₙ shown algebraically and geometrically."""

    def construct(self):
        title = Text("Complete Solution: x = xₚ + xₙ", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Formula ──
        formula = MathTex(
            r"x = ",
            r"\underbrace{\begin{pmatrix}-2\\0\\\frac{3}{2}\\0\end{pmatrix}}_{x_p}",
            r"+ c_1",
            r"\begin{pmatrix}-2\\1\\0\\0\end{pmatrix}",
            r"+ c_2",
            r"\begin{pmatrix}2\\0\\-2\\1\end{pmatrix}",
            font_size=30,
        ).next_to(title, DOWN, buff=0.5)
        formula[1].set_color(PIVOT_COLOR)
        formula[3].set_color(FREE_COLOR)
        formula[5].set_color(FREE_COLOR)
        self.play(Write(formula))
        self.wait()

        note = Text(
            "xₚ: one particular solution    xₙ: any vector in N(A)",
            font_size=24,
            color=GRAY,
        ).next_to(formula, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait()

        # ── Geometric picture (2-D analogy) ──
        geo_title = Text(
            "Geometric picture (analogy in R²)", font_size=26
        ).next_to(note, DOWN, buff=0.5)
        self.play(Write(geo_title))

        plane = NumberPlane(
            x_range=[-3, 5, 1],
            y_range=[-2, 4, 1],
            x_length=5,
            y_length=3.5,
            background_line_style={"stroke_opacity": 0.3},
        ).next_to(geo_title, DOWN, buff=0.3)
        self.play(Create(plane))

        # Nullspace line through origin (slope 1)
        ns_line = plane.plot(lambda x: x, x_range=[-2, 4], color=FREE_COLOR)
        ns_label = MathTex(r"N(A)", font_size=24, color=FREE_COLOR).next_to(
            plane.c2p(3.5, 3.5), RIGHT, buff=0.1
        )
        self.play(Create(ns_line), Write(ns_label))
        self.wait(0.5)

        # Shifted line (particular + nullspace) — shifted by (1,2)
        shift_line = plane.plot(
            lambda x: x + 1, x_range=[-2, 3], color=PIVOT_COLOR
        )
        shift_label = MathTex(
            r"x_p + N(A)", font_size=24, color=PIVOT_COLOR
        ).next_to(plane.c2p(2.5, 3.5), RIGHT, buff=0.1)
        xp_dot = Dot(plane.c2p(1, 2), color=PIVOT_COLOR, radius=0.08)
        xp_text = MathTex(r"x_p", font_size=22, color=PIVOT_COLOR).next_to(
            xp_dot, UP + LEFT, buff=0.1
        )
        self.play(Create(shift_line), Write(shift_label))
        self.play(Create(xp_dot), Write(xp_text))
        self.wait()

        coset_note = Text(
            "Solution set is a coset — shifted subspace, not through origin",
            font_size=22,
            color=GRAY,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(coset_note))
        self.wait(2)


class Lecture8_RankCases(Scene):
    """Four cases depending on rank r vs m and n."""

    def construct(self):
        title = Text("The Four Rank Cases", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Table ──
        headers = VGroup(
            MathTex(r"\text{Case}", font_size=28),
            MathTex(r"\text{R shape}", font_size=28),
            MathTex(r"\text{Solutions of } Ax = b", font_size=28),
        ).arrange(RIGHT, buff=1.5).next_to(title, DOWN, buff=0.6)
        line = Line(
            headers.get_left() + LEFT * 0.3 + DOWN * 0.2,
            headers.get_right() + RIGHT * 0.3 + DOWN * 0.2,
            color=GRAY,
        )
        self.play(Write(headers), Create(line))

        cases_data = [
            (
                r"r = m = n",
                r"R = I",
                r"\text{Unique solution (always)}",
                GREEN,
            ),
            (
                r"r = n < m",
                r"R = \begin{pmatrix}I\\0\end{pmatrix}",
                r"\text{0 or 1 solution}",
                BLUE,
            ),
            (
                r"r = m < n",
                r"R = \begin{pmatrix}I & F\end{pmatrix}",
                r"\infty \text{ solutions (always)}",
                TEAL,
            ),
            (
                r"r < m,\; r < n",
                r"R = \begin{pmatrix}I&F\\0&0\end{pmatrix}",
                r"\text{0 or } \infty \text{ solutions}",
                YELLOW,
            ),
        ]

        rows = VGroup()
        prev = line
        for case_tex, r_tex, sol_tex, color in cases_data:
            row = VGroup(
                MathTex(case_tex, font_size=26, color=color),
                MathTex(r_tex, font_size=26),
                MathTex(sol_tex, font_size=26),
            ).arrange(RIGHT, buff=1.5)
            # Align columns with headers
            for h, r in zip(headers, row):
                r.move_to([h.get_center()[0], 0, 0])
            row.next_to(prev, DOWN, buff=0.4)
            rows.add(row)
            prev = row

        for row in rows:
            self.play(Write(row))
            self.wait(0.5)

        self.wait()

        # ── Summary ──
        summary = VGroup(
            MathTex(
                r"\text{Full column rank } (r = n): \; N(A) = \{0\}",
                font_size=26,
            ),
            MathTex(
                r"\text{Full row rank } (r = m): \; \text{always solvable}",
                font_size=26,
            ),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(summary, color=PIVOT_COLOR, buff=0.15)
        self.play(Write(summary), Create(box))
        self.wait(2)
