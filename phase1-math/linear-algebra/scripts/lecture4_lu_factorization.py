"""
MIT 18.06 Lecture 4: A = LU Factorization
LU decomposition, why it matters, permutations, and cost of elimination

Example (same system as Lecture 2):
  A = [[1,2,1],[3,8,1],[0,4,1]]
  L = [[1,0,0],[3,1,0],[0,2,1]]
  U = [[1,2,1],[0,2,-2],[0,0,5]]

Style: 3Blue1Brown inspired
"""

from manim import *


class Lecture4_LUConcept(Scene):
    """Show A = LU factorization: elimination gives EA = U, so A = E⁻¹U = LU"""

    def construct(self):
        # Title
        title = Text("A = LU Factorization", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ─── Start from elimination: EA = U ───
        elim_label = Text("From elimination:", font_size=24, color=GREY)
        elim_label.shift(UP * 2.2 + LEFT * 4)

        ea_eq = MathTex(r"E", r"A", r"=", r"U", font_size=36)
        ea_eq.next_to(elim_label, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(FadeIn(elim_label), Write(ea_eq), run_time=1)
        self.wait(0.8)

        # Rearrange: A = E⁻¹ U = L U
        rearrange_label = Text("Rearrange:", font_size=24, color=GREY)
        rearrange_label.next_to(ea_eq, DOWN, buff=0.5, aligned_edge=LEFT)

        a_eq_einv = MathTex(r"A", r"=", r"E^{-1}", r"U", r"=", r"L", r"U", font_size=36)
        a_eq_einv.next_to(rearrange_label, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(FadeIn(rearrange_label), Write(a_eq_einv), run_time=1.2)
        self.wait(1)

        # Highlight L = E⁻¹
        box_einv = SurroundingRectangle(a_eq_einv[2], color=GREEN, buff=0.1)
        box_L = SurroundingRectangle(a_eq_einv[5], color=GREEN, buff=0.1)
        note_L = MathTex(r"L = E^{-1}", font_size=28, color=GREEN)
        note_L.next_to(a_eq_einv, DOWN, buff=0.4)

        self.play(Create(box_einv), Create(box_L), Write(note_L), run_time=1)
        self.wait(1)

        self.play(
            FadeOut(elim_label), FadeOut(ea_eq), FadeOut(rearrange_label),
            FadeOut(a_eq_einv), FadeOut(box_einv), FadeOut(box_L), FadeOut(note_L),
            run_time=0.6
        )

        # ─── 3×3 example ───
        example_label = Text("Example (Lecture 2 system):", font_size=26, color=GREY)
        example_label.shift(UP * 2.3)
        self.play(FadeIn(example_label), run_time=0.5)

        # A matrix
        mat_A = Matrix(
            [[1, 2, 1], [3, 8, 1], [0, 4, 1]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        label_A = MathTex("A", "=", font_size=34)

        # L matrix
        mat_L = Matrix(
            [[1, 0, 0], [3, 1, 0], [0, 2, 1]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        label_L = MathTex("L", font_size=34, color=BLUE)

        # U matrix
        mat_U = Matrix(
            [[1, 2, 1], [0, 2, -2], [0, 0, 5]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        label_U = MathTex("U", font_size=34, color=RED)

        # Arrange: A = L · U
        dot_sym = MathTex(r"\cdot", font_size=34)
        eq_sym = MathTex("=", font_size=34)

        factorization = VGroup(
            label_A, mat_A, eq_sym, label_L, mat_L, dot_sym, label_U, mat_U
        ).arrange(RIGHT, buff=0.15)
        factorization.shift(UP * 0.3)

        self.play(
            FadeIn(label_A), Create(mat_A),
            FadeIn(eq_sym),
            FadeIn(label_L), Create(mat_L),
            FadeIn(dot_sym),
            FadeIn(label_U), Create(mat_U),
            run_time=2
        )
        self.wait(1)

        # Highlight multipliers in L
        mult_label = Text("Multipliers go directly into L:", font_size=22, color=GREEN)
        mult_label.shift(DOWN * 1.5)
        self.play(FadeIn(mult_label), run_time=0.5)

        # L entries below diagonal: (1,0)=3, (2,1)=2
        # In a 3x3 Matrix, entries are indexed row-major: 0,1,2,3,4,5,6,7,8
        entry_3 = mat_L.get_entries()[3]  # row 1, col 0 = 3
        entry_7 = mat_L.get_entries()[7]  # row 2, col 1 = 2

        highlight_3 = SurroundingRectangle(entry_3, color=YELLOW, buff=0.08)
        highlight_2 = SurroundingRectangle(entry_7, color=YELLOW, buff=0.08)

        note_mult = VGroup(
            Text("3 = multiplier for Row₂ - 3·Row₁", font_size=18, color=YELLOW),
            Text("2 = multiplier for Row₃ - 2·Row₂", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        note_mult.shift(DOWN * 2.3)

        self.play(Create(highlight_3), FadeIn(note_mult[0]), run_time=0.8)
        self.wait(0.5)
        self.play(Create(highlight_2), FadeIn(note_mult[1]), run_time=0.8)
        self.wait(0.8)

        # Key insight
        insight = Text(
            "No sign flip! Multipliers go straight into L\n"
            "(when there are no row exchanges)",
            font_size=20, color=TEAL, line_spacing=1.3
        )
        insight.shift(DOWN * 3.2)
        self.play(FadeIn(insight), run_time=0.8)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)


class Lecture4_LUGridTransformation(Scene):
    """3B1B-style grid visualization of LU decomposition in 2D"""

    def construct(self):
        # Title
        title = Text("LU as Linear Transformations", font_size=38, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        bg_title = BackgroundRectangle(title, fill_opacity=0.8, buff=0.1)
        self.play(FadeIn(bg_title), Write(title), run_time=0.8)
        self.wait(0.3)

        # 2D example: A = LU
        # A = [[2,1],[6,4]], L = [[1,0],[3,1]], U = [[2,1],[0,1]]
        A = [[2, 1], [6, 4]]
        L = [[1, 0], [3, 1]]
        U = [[2, 1], [0, 1]]

        # ─── Part 1: Apply A directly ───
        plane1 = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4}
        )
        i_hat1 = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=4)
        j_hat1 = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=4)
        unit_sq1 = Square(side_length=1).move_to([0.5, 0.5, 0])
        unit_sq1.set_fill(YELLOW, opacity=0.3).set_stroke(YELLOW, width=2)

        grid1 = VGroup(plane1, i_hat1, j_hat1, unit_sq1)

        self.play(Create(plane1), run_time=1)
        self.play(
            GrowArrow(i_hat1), GrowArrow(j_hat1), FadeIn(unit_sq1),
            run_time=0.8
        )
        self.wait(0.3)

        step_label = Text("Applying A directly", font_size=26, color=WHITE)
        step_bg = BackgroundRectangle(step_label, fill_opacity=0.8, buff=0.1)
        step_label_group = VGroup(step_bg, step_label)
        step_label_group.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(step_label_group), run_time=0.5)

        mat_A_tex = MathTex(
            r"A = \begin{bmatrix} 2 & 1 \\ 6 & 4 \end{bmatrix}",
            font_size=28
        )
        mat_A_bg = BackgroundRectangle(mat_A_tex, fill_opacity=0.8, buff=0.1)
        mat_A_group = VGroup(mat_A_bg, mat_A_tex)
        mat_A_group.to_corner(UL, buff=0.5).shift(DOWN * 0.5)
        self.play(FadeIn(mat_A_group), run_time=0.5)

        self.play(
            ApplyMatrix(A, plane1),
            ApplyMatrix(A, i_hat1),
            ApplyMatrix(A, j_hat1),
            ApplyMatrix(A, unit_sq1),
            run_time=3
        )
        self.wait(1)

        # ─── Reset grid ───
        self.play(
            FadeOut(plane1), FadeOut(i_hat1), FadeOut(j_hat1), FadeOut(unit_sq1),
            FadeOut(step_label_group), FadeOut(mat_A_group),
            run_time=0.6
        )

        # ─── Part 2: Apply U then L ───
        plane2 = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4}
        )
        i_hat2 = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=4)
        j_hat2 = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=4)
        unit_sq2 = Square(side_length=1).move_to([0.5, 0.5, 0])
        unit_sq2.set_fill(YELLOW, opacity=0.3).set_stroke(YELLOW, width=2)

        grid2 = VGroup(plane2, i_hat2, j_hat2, unit_sq2)

        self.play(Create(plane2), run_time=1)
        self.play(
            GrowArrow(i_hat2), GrowArrow(j_hat2), FadeIn(unit_sq2),
            run_time=0.8
        )

        step2a_label = Text("Step 1: Apply U (upper triangular)", font_size=24, color=RED)
        step2a_bg = BackgroundRectangle(step2a_label, fill_opacity=0.8, buff=0.1)
        step2a_group = VGroup(step2a_bg, step2a_label)
        step2a_group.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(step2a_group), run_time=0.5)

        mat_U_tex = MathTex(
            r"U = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}",
            font_size=28, color=RED
        )
        u_label_sub = Text("Upper triangular (scale + shear)", font_size=18, color=RED)
        u_label_sub.next_to(mat_U_tex, DOWN, buff=0.1)
        mat_U_bg = BackgroundRectangle(
            VGroup(mat_U_tex, u_label_sub), fill_opacity=0.8, buff=0.1
        )
        mat_U_group = VGroup(mat_U_bg, mat_U_tex, u_label_sub)
        mat_U_group.to_corner(UL, buff=0.5).shift(DOWN * 0.5)
        self.play(FadeIn(mat_U_group), run_time=0.5)

        self.play(
            ApplyMatrix(U, plane2),
            ApplyMatrix(U, i_hat2),
            ApplyMatrix(U, j_hat2),
            ApplyMatrix(U, unit_sq2),
            run_time=3
        )
        self.wait(0.8)

        # Now apply L on top
        step2b_label = Text("Step 2: Apply L (lower triangular)", font_size=24, color=BLUE)
        step2b_bg = BackgroundRectangle(step2b_label, fill_opacity=0.8, buff=0.1)
        step2b_group = VGroup(step2b_bg, step2b_label)
        step2b_group.to_edge(DOWN, buff=0.5)

        mat_L_tex = MathTex(
            r"L = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}",
            font_size=28, color=BLUE
        )
        l_label_sub = Text("Lower triangular (shear)", font_size=18, color=BLUE)
        l_label_sub.next_to(mat_L_tex, DOWN, buff=0.1)
        mat_L_bg = BackgroundRectangle(
            VGroup(mat_L_tex, l_label_sub), fill_opacity=0.8, buff=0.1
        )
        mat_L_group = VGroup(mat_L_bg, mat_L_tex, l_label_sub)
        mat_L_group.to_corner(UL, buff=0.5).shift(DOWN * 0.5)

        self.play(
            FadeOut(step2a_group), FadeIn(step2b_group),
            FadeOut(mat_U_group), FadeIn(mat_L_group),
            run_time=0.6
        )

        self.play(
            ApplyMatrix(L, plane2),
            ApplyMatrix(L, i_hat2),
            ApplyMatrix(L, j_hat2),
            ApplyMatrix(L, unit_sq2),
            run_time=3
        )
        self.wait(1)

        # Key insight
        insight = Text(
            "LU decomposition breaks one transformation into two simpler ones",
            font_size=24, color=TEAL
        )
        insight_bg = BackgroundRectangle(insight, fill_opacity=0.85, buff=0.15)
        insight_group = VGroup(insight_bg, insight)
        insight_group.to_edge(DOWN, buff=0.5)

        eq_text = MathTex(
            r"A = L \cdot U", font_size=36, color=YELLOW
        )
        eq_bg = BackgroundRectangle(eq_text, fill_opacity=0.85, buff=0.15)
        eq_group = VGroup(eq_bg, eq_text)
        eq_group.next_to(insight_group, UP, buff=0.2)

        self.play(
            FadeOut(step2b_group), FadeOut(mat_L_group),
            FadeIn(insight_group), FadeIn(eq_group),
            run_time=0.8
        )
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)


class Lecture4_WhyLU(Scene):
    """Why factor A = LU? Solving multiple right-hand sides cheaply."""

    def construct(self):
        # Title
        title = Text("Why Factor A = LU?", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Ax = b becomes two triangular solves
        main_eq = MathTex(r"A", r"x", r"=", r"b", font_size=36)
        main_eq.shift(UP * 2.2)
        self.play(Write(main_eq), run_time=0.8)

        arrow_down = Arrow(
            main_eq.get_bottom(), main_eq.get_bottom() + DOWN * 0.8,
            buff=0.1, color=YELLOW
        )
        becomes = Text("becomes", font_size=20, color=GREY)
        becomes.next_to(arrow_down, RIGHT, buff=0.15)
        self.play(GrowArrow(arrow_down), FadeIn(becomes), run_time=0.6)

        # Two steps
        step1 = MathTex(
            r"1.\;", r"L", r"y", r"=", r"b",
            font_size=32
        )
        step1[1].set_color(BLUE)
        step1_note = Text("(forward substitution — easy!)", font_size=20, color=BLUE)

        step2 = MathTex(
            r"2.\;", r"U", r"x", r"=", r"y",
            font_size=32
        )
        step2[1].set_color(RED)
        step2_note = Text("(back substitution — easy!)", font_size=20, color=RED)

        steps_group = VGroup(
            VGroup(step1, step1_note).arrange(RIGHT, buff=0.3),
            VGroup(step2, step2_note).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        steps_group.shift(UP * 0.3)

        self.play(Write(step1), FadeIn(step1_note), run_time=1)
        self.wait(0.5)
        self.play(Write(step2), FadeIn(step2_note), run_time=1)
        self.wait(1)

        self.play(
            FadeOut(main_eq), FadeOut(arrow_down), FadeOut(becomes),
            FadeOut(steps_group),
            run_time=0.5
        )

        # ─── Cost comparison ───
        cost_title = Text("Cost Comparison", font_size=30, color=YELLOW)
        cost_title.shift(UP * 2.5)
        self.play(Write(cost_title), run_time=0.6)

        # Old way
        old_label = Text("Elimination from scratch:", font_size=24, color=RED)
        old_label.shift(UP * 1.6 + LEFT * 2)
        old_cost = MathTex(r"O(n^3)", font_size=30, color=RED)
        old_cost.next_to(old_label, RIGHT, buff=0.3)
        old_note = Text("each time for every new b", font_size=18, color=GREY)
        old_note.next_to(VGroup(old_label, old_cost), DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(FadeIn(old_label), Write(old_cost), FadeIn(old_note), run_time=1)
        self.wait(0.8)

        # New way
        new_label = Text("With LU factorization:", font_size=24, color=GREEN)
        new_label.shift(UP * 0.3 + LEFT * 2)
        new_line1 = MathTex(r"O(n^3)", font_size=30, color=GREEN)
        new_note1 = Text("once (factor A = LU)", font_size=18, color=GREY)
        new_line1_group = VGroup(new_line1, new_note1).arrange(RIGHT, buff=0.2)
        new_line1_group.next_to(new_label, DOWN, buff=0.15, aligned_edge=LEFT)

        new_line2 = MathTex(r"O(n^2)", font_size=30, color=GREEN)
        new_note2 = Text("per new b (just substitution)", font_size=18, color=GREY)
        new_line2_group = VGroup(new_line2, new_note2).arrange(RIGHT, buff=0.2)
        new_line2_group.next_to(new_line1_group, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(FadeIn(new_label), run_time=0.5)
        self.play(FadeIn(new_line1_group), run_time=0.8)
        self.play(FadeIn(new_line2_group), run_time=0.8)
        self.wait(1)

        # ─── Visual: multiple b's flowing through L and U ───
        self.play(
            FadeOut(cost_title), FadeOut(old_label), FadeOut(old_cost),
            FadeOut(old_note), FadeOut(new_label),
            FadeOut(new_line1_group), FadeOut(new_line2_group),
            run_time=0.5
        )

        pipeline_title = Text("Solving many right-hand sides", font_size=28, color=YELLOW)
        pipeline_title.shift(UP * 2.8)
        self.play(Write(pipeline_title), run_time=0.6)

        # b vectors on the left
        b_colors = [BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        b_labels = []
        for i, c in enumerate(b_colors):
            b_tex = MathTex(f"b_{i+1}", font_size=28, color=c)
            b_tex.move_to(LEFT * 5 + UP * (1 - i * 0.8))
            b_labels.append(b_tex)

        b_group = VGroup(*b_labels)
        self.play(*[FadeIn(b) for b in b_labels], run_time=0.8)

        # L and U boxes
        l_box = RoundedRectangle(
            corner_radius=0.15, width=1.8, height=2.8,
            color=BLUE, fill_opacity=0.15
        )
        l_box.move_to(LEFT * 1.5)
        l_text = MathTex("L", font_size=36, color=BLUE)
        l_text.move_to(l_box.get_center())
        l_sub = Text("forward\nsubst.", font_size=14, color=BLUE)
        l_sub.next_to(l_text, DOWN, buff=0.15)

        u_box = RoundedRectangle(
            corner_radius=0.15, width=1.8, height=2.8,
            color=RED, fill_opacity=0.15
        )
        u_box.move_to(RIGHT * 1.5)
        u_text = MathTex("U", font_size=36, color=RED)
        u_text.move_to(u_box.get_center())
        u_sub = Text("back\nsubst.", font_size=14, color=RED)
        u_sub.next_to(u_text, DOWN, buff=0.15)

        self.play(
            Create(l_box), FadeIn(l_text), FadeIn(l_sub),
            Create(u_box), FadeIn(u_text), FadeIn(u_sub),
            run_time=1
        )

        # Arrows between stages
        arr1 = Arrow(LEFT * 3.8, LEFT * 2.5, buff=0, color=WHITE, stroke_width=2)
        arr2 = Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0, color=WHITE, stroke_width=2)
        arr3 = Arrow(RIGHT * 2.5, RIGHT * 3.8, buff=0, color=WHITE, stroke_width=2)
        self.play(GrowArrow(arr1), GrowArrow(arr2), GrowArrow(arr3), run_time=0.6)

        # x vectors on the right
        x_labels = []
        for i, c in enumerate(b_colors):
            x_tex = MathTex(f"x_{i+1}", font_size=28, color=c)
            x_tex.move_to(RIGHT * 5 + UP * (1 - i * 0.8))
            x_labels.append(x_tex)

        # Animate b's flowing through
        for i in range(4):
            self.play(
                b_labels[i].animate.move_to(l_box.get_center()),
                run_time=0.4
            )
            self.play(
                b_labels[i].animate.move_to(u_box.get_center()),
                run_time=0.4
            )
            self.play(
                FadeOut(b_labels[i]),
                FadeIn(x_labels[i]),
                run_time=0.4
            )

        cheap_label = MathTex(r"O(n^2) \text{ each!}", font_size=28, color=GREEN)
        cheap_label.shift(DOWN * 2.5)
        self.play(FadeIn(cheap_label), run_time=0.6)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)


class Lecture4_PermutationLU(Scene):
    """PA = LU: when row exchanges are needed"""

    def construct(self):
        # Title
        title = Text(
            "When Row Exchanges Are Needed: PA = LU",
            font_size=34, color=YELLOW
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Problem matrix
        problem_label = Text(
            "This matrix has a zero pivot:", font_size=24, color=GREY
        )
        problem_label.shift(UP * 2)

        mat_A = Matrix(
            [[0, 1], [1, 0]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)

        a_label = MathTex("A =", font_size=32)
        a_group = VGroup(a_label, mat_A).arrange(RIGHT, buff=0.2)
        a_group.shift(UP * 1)

        self.play(FadeIn(problem_label), run_time=0.5)
        self.play(FadeIn(a_label), Create(mat_A), run_time=0.8)

        # Highlight the zero
        zero_entry = mat_A.get_entries()[0]
        zero_box = SurroundingRectangle(zero_entry, color=RED, buff=0.08)
        zero_note = Text("Zero pivot!", font_size=20, color=RED)
        zero_note.next_to(zero_box, RIGHT, buff=0.3)

        self.play(Create(zero_box), FadeIn(zero_note), run_time=0.6)
        self.wait(0.8)

        # Solution: permutation matrix
        self.play(FadeOut(zero_box), FadeOut(zero_note), run_time=0.4)

        solution_label = Text("Solution: permute rows first", font_size=24, color=GREEN)
        solution_label.shift(DOWN * 0.2)
        self.play(FadeIn(solution_label), run_time=0.5)

        # P matrix
        mat_P = Matrix(
            [[0, 1], [1, 0]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        p_label = MathTex("P =", font_size=32)

        p_group = VGroup(p_label, mat_P).arrange(RIGHT, buff=0.2)
        p_group.shift(DOWN * 1.3 + LEFT * 3.5)

        p_note = Text("(swaps rows 1 and 2)", font_size=18, color=GREY)
        p_note.next_to(p_group, DOWN, buff=0.15)

        self.play(FadeIn(p_label), Create(mat_P), FadeIn(p_note), run_time=0.8)
        self.wait(0.5)

        # PA = LU equation
        pa_eq = MathTex(
            r"PA", r"=", r"LU",
            font_size=34
        )
        pa_eq.shift(DOWN * 1.3 + RIGHT * 1)

        self.play(Write(pa_eq), run_time=0.8)

        # Show the result
        result_eq = MathTex(
            r"\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}",
            r"\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}",
            r"=",
            r"\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}",
            r"=",
            r"L \cdot U",
            font_size=26
        )
        result_eq.shift(DOWN * 2.5)

        result_note = Text(
            "PA = I, so L = I, U = I (trivial in this case)",
            font_size=18, color=GREY
        )
        result_note.next_to(result_eq, DOWN, buff=0.15)

        self.play(Write(result_eq), FadeIn(result_note), run_time=1.2)
        self.wait(1)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # ─── Grid visualization: permutation as reflection ───
        perm_title = Text("Permutation as a Transformation", font_size=32, color=YELLOW)
        perm_title.to_edge(UP, buff=0.3)
        bg_perm = BackgroundRectangle(perm_title, fill_opacity=0.8, buff=0.1)
        self.play(FadeIn(bg_perm), Write(perm_title), run_time=0.6)

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.4}
        )
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=4)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=4)
        unit_sq = Square(side_length=1).move_to([0.5, 0.5, 0])
        unit_sq.set_fill(YELLOW, opacity=0.3).set_stroke(YELLOW, width=2)

        self.play(Create(plane), run_time=0.8)
        self.play(
            GrowArrow(i_hat), GrowArrow(j_hat), FadeIn(unit_sq),
            run_time=0.6
        )

        perm_label = Text("P swaps x and y → reflection over y = x", font_size=22, color=WHITE)
        perm_bg = BackgroundRectangle(perm_label, fill_opacity=0.8, buff=0.1)
        perm_label_group = VGroup(perm_bg, perm_label)
        perm_label_group.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(perm_label_group), run_time=0.5)

        # Draw y = x line
        diag_line = DashedLine(
            LEFT * 3.5 + DOWN * 3.5, RIGHT * 3.5 + UP * 3.5,
            color=YELLOW, stroke_width=2
        )
        diag_label = MathTex("y = x", font_size=24, color=YELLOW)
        diag_label.move_to(RIGHT * 2.8 + UP * 3.2)
        diag_bg = BackgroundRectangle(diag_label, fill_opacity=0.8, buff=0.05)
        self.play(Create(diag_line), FadeIn(diag_bg), FadeIn(diag_label), run_time=0.6)

        P_matrix = [[0, 1], [1, 0]]
        self.play(
            ApplyMatrix(P_matrix, plane),
            ApplyMatrix(P_matrix, i_hat),
            ApplyMatrix(P_matrix, j_hat),
            ApplyMatrix(P_matrix, unit_sq),
            run_time=3
        )
        self.wait(1)

        general_note = MathTex(
            r"\text{In general: } PA = LU",
            font_size=30, color=TEAL
        )
        gen_bg = BackgroundRectangle(general_note, fill_opacity=0.85, buff=0.12)
        gen_group = VGroup(gen_bg, general_note)
        gen_group.to_edge(DOWN, buff=0.5)

        self.play(FadeOut(perm_label_group), FadeIn(gen_group), run_time=0.6)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)


class Lecture4_CostOfElimination(Scene):
    """Visualize the O(n³/3) cost of Gaussian elimination"""

    def construct(self):
        # Title
        title = Text("Cost of Elimination", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Show n×n matrix schematic
        n_label = Text("n × n matrix", font_size=26, color=GREY)
        n_label.shift(UP * 2.2)
        self.play(FadeIn(n_label), run_time=0.4)

        # Draw a grid representing the matrix
        n = 6  # visual size
        cell_size = 0.45
        grid_group = VGroup()
        offset = np.array([-n * cell_size / 2, -n * cell_size / 2 + 0.5, 0])

        # All cells
        cells = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cell = Square(side_length=cell_size)
                cell.move_to(
                    offset + np.array([
                        j * cell_size + cell_size / 2,
                        (n - 1 - i) * cell_size + cell_size / 2,
                        0
                    ])
                )
                cell.set_stroke(WHITE, width=1)
                cells[i][j] = cell
                grid_group.add(cell)

        self.play(Create(grid_group), run_time=1)
        self.wait(0.5)

        # Animate elimination: column by column, highlight operations
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

        step_label = Text("", font_size=22, color=WHITE)
        step_label.to_edge(RIGHT, buff=0.5).shift(UP * 1)

        for col in range(n - 1):
            # Highlight pivot
            pivot_cell = cells[col][col]
            pivot_cell.set_fill(WHITE, opacity=0.6)

            # Highlight cells being eliminated (below pivot in this column)
            ops_cells = []
            for row in range(col + 1, n):
                for c in range(col, n):
                    cells[row][c].set_fill(colors[col], opacity=0.35)
                    ops_cells.append(cells[row][c])

            new_label = Text(
                f"Step {col + 1}: ~{(n - col - 1) * (n - col)} ops",
                font_size=20, color=colors[col]
            )
            new_label.to_edge(RIGHT, buff=0.5).shift(UP * (1.5 - col * 0.45))

            self.play(
                *[cell.animate.set_fill(colors[col], opacity=0.35) for cell in ops_cells],
                pivot_cell.animate.set_fill(WHITE, opacity=0.6),
                FadeIn(new_label),
                run_time=0.6
            )
            self.wait(0.3)

        self.wait(0.8)

        # ─── Formula ───
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title], run_time=0.5)

        formula_label = Text("Total operations:", font_size=26, color=GREY)
        formula_label.shift(UP * 2)

        sum_eq = MathTex(
            r"\sum_{k=1}^{n} k^2 \;\approx\; \frac{n^3}{3}",
            font_size=36
        )
        sum_eq.next_to(formula_label, DOWN, buff=0.4)

        self.play(FadeIn(formula_label), Write(sum_eq), run_time=1)
        self.wait(1)

        # Concrete numbers
        examples_title = Text("Concrete examples:", font_size=24, color=GREY)
        examples_title.shift(DOWN * 0.2)

        ex1 = MathTex(
            r"n = 100 \;\rightarrow\; \approx 333{,}000 \text{ operations}",
            font_size=28
        )
        ex2 = MathTex(
            r"n = 1{,}000 \;\rightarrow\; \approx 333{,}000{,}000 \text{ operations}",
            font_size=28
        )
        ex3 = MathTex(
            r"n = 10{,}000 \;\rightarrow\; \approx 333 \text{ billion operations}",
            font_size=28
        )

        examples = VGroup(ex1, ex2, ex3).arrange(DOWN, buff=0.35)
        examples.next_to(examples_title, DOWN, buff=0.3)

        self.play(FadeIn(examples_title), run_time=0.4)

        for ex in [ex1, ex2, ex3]:
            self.play(Write(ex), run_time=0.8)
            self.wait(0.4)

        # Highlight the cubic growth
        growth_note = Text(
            "10× bigger matrix → 1000× more work!",
            font_size=24, color=RED
        )
        growth_note.shift(DOWN * 2.8)
        self.play(FadeIn(growth_note), run_time=0.6)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)
