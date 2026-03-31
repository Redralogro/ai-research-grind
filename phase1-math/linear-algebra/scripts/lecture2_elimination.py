"""
MIT 18.06 Lecture 2: Elimination with Matrices
Step-by-step elimination, elimination matrices, and when it fails

System:
   x + 2y +  z = 2
  3x + 8y +  z = 12
       4y +  z = 2

Solution: x=2, y=1, z=-2

Style: 3Blue1Brown inspired
"""

from manim import *


class Lecture2_EliminationProcess(Scene):
    """Show step-by-step elimination with augmented matrix"""

    def construct(self):
        # Title
        title = Text("Elimination Process", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Original system
        system_label = Text("System:", font_size=24, color=GREY)
        system_label.to_edge(LEFT, buff=0.8).shift(UP * 2.5)
        
        system_eqs = VGroup(
            MathTex(r"x + 2y + z = 2", font_size=30),
            MathTex(r"3x + 8y + z = 12", font_size=30),
            MathTex(r"4y + z = 2", font_size=30),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        system_eqs.next_to(system_label, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(
            FadeIn(system_label),
            *[Write(eq) for eq in system_eqs],
            run_time=1.5
        )
        self.wait(0.8)

        # Augmented matrix [A|b]
        aug_label = Text("Augmented Matrix [A|b]:", font_size=24, color=GREY)
        aug_label.next_to(system_eqs, DOWN, buff=0.6, aligned_edge=LEFT)
        
        # Original matrix
        matrix_0 = Matrix(
            [[1, 2, 1, "|", 2],
             [3, 8, 1, "|", 12],
             [0, 4, 1, "|", 2]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        matrix_0.next_to(aug_label, DOWN, buff=0.3)
        
        self.play(FadeIn(aug_label), Create(matrix_0), run_time=1)
        self.wait(0.8)

        # Highlight first pivot
        pivot_1_highlight = SurroundingRectangle(
            matrix_0.get_entries()[0],  # (0,0) = 1
            color=YELLOW,
            buff=0.1
        )
        pivot_label_1 = Text("Pivot 1", font_size=20, color=YELLOW)
        pivot_label_1.next_to(matrix_0, RIGHT, buff=0.5).shift(UP * 0.8)
        
        self.play(Create(pivot_1_highlight), FadeIn(pivot_label_1), run_time=0.8)
        self.wait(0.6)

        # Step 1: Eliminate (2,1) entry
        step1_label = Text("Step 1: Row₂ - 3·Row₁", font_size=22, color=RED)
        step1_label.to_edge(RIGHT, buff=0.8).shift(UP * 1.5)
        
        multiplier_1 = Text("Multiplier = 3", font_size=20, color=GREEN)
        multiplier_1.next_to(step1_label, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(
            Write(step1_label),
            FadeIn(multiplier_1),
            run_time=1
        )
        self.wait(0.5)

        # New matrix after step 1
        matrix_1 = Matrix(
            [[1, 2, 1, "|", 2],
             [0, 2, -2, "|", 6],
             [0, 4, 1, "|", 2]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        matrix_1.move_to(matrix_0)
        
        self.play(
            Transform(matrix_0, matrix_1),
            FadeOut(pivot_1_highlight),
            run_time=1.2
        )
        self.wait(0.6)

        # Highlight second pivot
        pivot_2_highlight = SurroundingRectangle(
            matrix_1.get_entries()[6],  # (1,1) = 2
            color=YELLOW,
            buff=0.1
        )
        pivot_label_2 = Text("Pivot 2", font_size=20, color=YELLOW)
        pivot_label_2.move_to(pivot_label_1)
        
        self.play(
            FadeOut(step1_label),
            FadeOut(multiplier_1),
            FadeOut(pivot_label_1),
            Create(pivot_2_highlight),
            FadeIn(pivot_label_2),
            run_time=0.8
        )
        self.wait(0.5)

        # Step 2: Eliminate (3,2) entry
        step2_label = Text("Step 2: Row₃ - 2·Row₂", font_size=22, color=RED)
        step2_label.to_edge(RIGHT, buff=0.8).shift(UP * 1.5)
        
        multiplier_2 = Text("Multiplier = 2", font_size=20, color=GREEN)
        multiplier_2.next_to(step2_label, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(
            Write(step2_label),
            FadeIn(multiplier_2),
            run_time=1
        )
        self.wait(0.5)

        # Final matrix (upper triangular)
        matrix_2 = Matrix(
            [[1, 2, 1, "|", 2],
             [0, 2, -2, "|", 6],
             [0, 0, 5, "|", -10]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        matrix_2.move_to(matrix_1)
        
        self.play(
            Transform(matrix_0, matrix_2),
            FadeOut(pivot_2_highlight),
            run_time=1.2
        )
        self.wait(0.6)

        # Highlight all three pivots
        pivot_3_highlight = SurroundingRectangle(
            matrix_2.get_entries()[12],  # (2,2) = 5
            color=YELLOW,
            buff=0.1
        )
        
        pivot_summary = Text("3 Pivots: 1, 2, 5", font_size=24, color=YELLOW)
        pivot_summary.move_to(pivot_label_2)
        
        self.play(
            FadeOut(step2_label),
            FadeOut(multiplier_2),
            FadeOut(pivot_label_2),
            Create(pivot_3_highlight),
            Write(pivot_summary),
            run_time=1
        )
        self.wait(0.8)

        # Upper triangular label
        u_label = Text("Upper Triangular (U)", font_size=26, color=BLUE)
        u_label.next_to(matrix_2, DOWN, buff=0.5)
        
        self.play(Write(u_label), run_time=0.8)
        self.wait(0.8)

        # Clear for back substitution
        self.play(
            FadeOut(system_label),
            FadeOut(system_eqs),
            FadeOut(aug_label),
            FadeOut(pivot_3_highlight),
            FadeOut(pivot_summary),
            run_time=0.6
        )

        # Back substitution
        back_sub_title = Text("Back Substitution", font_size=32, color=ORANGE)
        back_sub_title.move_to(UP * 3)
        
        self.play(
            matrix_0.animate.shift(LEFT * 2.5),
            u_label.animate.shift(LEFT * 2.5),
            FadeOut(title),
            Write(back_sub_title),
            run_time=1
        )
        self.wait(0.5)

        # Solve from bottom to top
        solve_steps = VGroup(
            MathTex(r"5z = -10 \implies z = -2", font_size=28, color=WHITE),
            MathTex(r"2y - 2(-2) = 6 \implies y = 1", font_size=28, color=WHITE),
            MathTex(r"x + 2(1) + (-2) = 2 \implies x = 2", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        solve_steps.to_edge(RIGHT, buff=1).shift(UP * 0.5)
        
        for step in solve_steps:
            self.play(Write(step), run_time=1.2)
            self.wait(0.5)

        # Final answer
        answer = MathTex(
            r"\boxed{(x, y, z) = (2, 1, -2)}",
            font_size=36,
            color=GREEN
        )
        answer.next_to(solve_steps, DOWN, buff=0.7)
        
        self.play(Write(answer), run_time=1.2)
        self.wait(2)


class Lecture2_EliminationMatrices(Scene):
    """Show elimination matrices E₂₁ and E₃₂"""

    def construct(self):
        # Title
        title = Text("Elimination Matrices", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Concept
        concept = Text(
            "Each elimination step = matrix multiplication",
            font_size=24,
            color=GREY
        )
        concept.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(concept), run_time=0.8)
        self.wait(0.6)

        # Original matrix A
        a_label = MathTex("A =", font_size=32)
        a_matrix = Matrix(
            [[1, 2, 1],
             [3, 8, 1],
             [0, 4, 1]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        
        a_group = VGroup(a_label, a_matrix).arrange(RIGHT, buff=0.2)
        a_group.shift(UP * 1.8 + LEFT * 3)
        
        self.play(Write(a_label), Create(a_matrix), run_time=1)
        self.wait(0.6)

        # E₂₁ matrix (eliminate row 2, col 1)
        e21_label = MathTex("E_{21} =", font_size=32, color=BLUE)
        e21_matrix = Matrix(
            [[1, 0, 0],
             [-3, 1, 0],
             [0, 0, 1]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        
        e21_group = VGroup(e21_label, e21_matrix).arrange(RIGHT, buff=0.2)
        e21_group.next_to(a_group, DOWN, buff=0.8, aligned_edge=LEFT)
        
        e21_note = Text(
            "Subtracts 3× row 1 from row 2",
            font_size=18,
            color=GREY
        )
        e21_note.next_to(e21_group, RIGHT, buff=0.5)
        
        self.play(
            Write(e21_label),
            Create(e21_matrix),
            FadeIn(e21_note),
            run_time=1.2
        )
        self.wait(0.8)

        # Show E₂₁ · A
        mult_expr = MathTex(
            "E_{21} \\cdot A =",
            font_size=32,
            color=BLUE
        )
        result_1 = Matrix(
            [[1, 2, 1],
             [0, 2, -2],
             [0, 4, 1]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        
        mult_group = VGroup(mult_expr, result_1).arrange(RIGHT, buff=0.2)
        mult_group.to_edge(RIGHT, buff=1.2).shift(UP * 1.2)
        
        self.play(
            Write(mult_expr),
            Create(result_1),
            run_time=1.5
        )
        self.wait(0.8)

        # E₃₂ matrix (eliminate row 3, col 2)
        e32_label = MathTex("E_{32} =", font_size=32, color=RED)
        e32_matrix = Matrix(
            [[1, 0, 0],
             [0, 1, 0],
             [0, -2, 1]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85)
        
        e32_group = VGroup(e32_label, e32_matrix).arrange(RIGHT, buff=0.2)
        e32_group.next_to(e21_group, DOWN, buff=0.8, aligned_edge=LEFT)
        
        e32_note = Text(
            "Subtracts 2× row 2 from row 3",
            font_size=18,
            color=GREY
        )
        e32_note.next_to(e32_group, RIGHT, buff=0.5)
        
        self.play(
            Write(e32_label),
            Create(e32_matrix),
            FadeIn(e32_note),
            run_time=1.2
        )
        self.wait(0.8)

        # Show full elimination: U = E₃₂ · E₂₁ · A
        full_eq = MathTex(
            "U = E_{32} \\cdot E_{21} \\cdot A",
            font_size=36,
            color=YELLOW
        )
        full_eq.next_to(mult_group, DOWN, buff=0.8)
        
        self.play(Write(full_eq), run_time=1.2)
        self.wait(1)

        # Clear and show LU decomposition preview
        self.play(
            *[FadeOut(mob) for mob in [
                a_group, e21_group, e21_note, e32_group, e32_note,
                mult_group, full_eq, concept
            ]],
            run_time=0.8
        )

        # LU decomposition
        lu_title = Text("Preview: LU Decomposition", font_size=32, color=ORANGE)
        lu_title.move_to(UP * 2.5)
        
        lu_eq = MathTex(
            "A = L \\cdot U",
            font_size=40,
            color=WHITE
        )
        lu_eq.next_to(lu_title, DOWN, buff=0.8)
        
        l_label = MathTex("L =", font_size=32)
        l_matrix = Matrix(
            [[1, 0, 0],
             [3, 1, 0],
             [0, 2, 1]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.8)
        l_matrix.set_color(GREEN)
        
        l_group = VGroup(l_label, l_matrix).arrange(RIGHT, buff=0.2)
        l_group.next_to(lu_eq, DOWN, buff=0.8).shift(LEFT * 2.5)
        
        l_note = Text(
            "Lower triangular\n(stores multipliers)",
            font_size=18,
            color=GREY,
            line_spacing=1.2
        )
        l_note.next_to(l_group, DOWN, buff=0.3)
        
        u_label = MathTex("U =", font_size=32)
        u_matrix = Matrix(
            [[1, 2, 1],
             [0, 2, -2],
             [0, 0, 5]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.8)
        u_matrix.set_color(BLUE)
        
        u_group = VGroup(u_label, u_matrix).arrange(RIGHT, buff=0.2)
        u_group.next_to(lu_eq, DOWN, buff=0.8).shift(RIGHT * 2.5)
        
        u_note = Text(
            "Upper triangular\n(from elimination)",
            font_size=18,
            color=GREY,
            line_spacing=1.2
        )
        u_note.next_to(u_group, DOWN, buff=0.3)
        
        self.play(
            FadeOut(title),
            Write(lu_title),
            run_time=0.8
        )
        self.play(Write(lu_eq), run_time=1)
        self.wait(0.5)
        
        self.play(
            Write(l_label),
            Create(l_matrix),
            FadeIn(l_note),
            run_time=1.2
        )
        self.wait(0.5)
        
        self.play(
            Write(u_label),
            Create(u_matrix),
            FadeIn(u_note),
            run_time=1.2
        )
        self.wait(2)


class Lecture2_WhenItFails(Scene):
    """Demonstrate when elimination fails"""

    def construct(self):
        # Title
        title = Text("When Elimination Fails", font_size=40, color=RED)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Case 1: Temporary failure (row exchange)
        case1_label = Text(
            "Case 1: Temporary Failure (Zero Pivot)",
            font_size=28,
            color=YELLOW
        )
        case1_label.shift(UP * 2.2)
        
        self.play(Write(case1_label), run_time=0.8)
        self.wait(0.5)

        # Bad matrix
        bad_matrix = Matrix(
            [[0, 2, 1],
             [1, 3, 2],
             [0, 4, 5]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        bad_matrix.shift(UP * 0.5 + LEFT * 3)
        
        pivot_highlight = SurroundingRectangle(
            bad_matrix.get_entries()[0],  # (0,0) = 0
            color=RED,
            buff=0.1,
            stroke_width=3
        )
        
        problem_note = Text(
            "Pivot is 0!\nCan't divide",
            font_size=20,
            color=RED,
            line_spacing=1.2
        )
        problem_note.next_to(bad_matrix, RIGHT, buff=0.8)
        
        self.play(
            Create(bad_matrix),
            Create(pivot_highlight),
            FadeIn(problem_note),
            run_time=1.2
        )
        self.wait(0.8)

        # Solution: row exchange
        arrow = Arrow(
            bad_matrix.get_right() + RIGHT * 1.5,
            bad_matrix.get_right() + RIGHT * 2.5,
            color=GREEN,
            buff=0
        )
        arrow_label = Text("Row Exchange", font_size=20, color=GREEN)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        fixed_matrix = Matrix(
            [[1, 3, 2],
             [0, 2, 1],
             [0, 4, 5]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        fixed_matrix.shift(UP * 0.5 + RIGHT * 2)
        
        success_note = Text(
            "✓ Fixed!\nSwap row 1 ↔ row 2",
            font_size=20,
            color=GREEN,
            line_spacing=1.2
        )
        success_note.next_to(fixed_matrix, RIGHT, buff=0.5)
        
        self.play(
            GrowArrow(arrow),
            Write(arrow_label),
            run_time=0.8
        )
        self.play(
            Create(fixed_matrix),
            FadeIn(success_note),
            run_time=1.2
        )
        self.wait(1.2)

        # Clear case 1
        self.play(
            *[FadeOut(mob) for mob in [
                case1_label, bad_matrix, pivot_highlight, problem_note,
                arrow, arrow_label, fixed_matrix, success_note
            ]],
            run_time=0.8
        )

        # Case 2: Permanent failure (singular matrix)
        case2_label = Text(
            "Case 2: Permanent Failure (Singular Matrix)",
            font_size=28,
            color=RED
        )
        case2_label.shift(UP * 2.2)
        
        self.play(Write(case2_label), run_time=0.8)
        self.wait(0.5)

        # Singular matrix
        singular_matrix = Matrix(
            [[1, 2, 3],
             [0, 0, 0],
             [0, 0, 5]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32}
        ).scale(0.9)
        singular_matrix.shift(DOWN * 0.2)
        
        zero_row_highlight = SurroundingRectangle(
            VGroup(
                singular_matrix.get_entries()[3],
                singular_matrix.get_entries()[4],
                singular_matrix.get_entries()[5]
            ),
            color=RED,
            buff=0.15,
            stroke_width=3
        )
        
        fail_note = Text(
            "✗ Can't fix this!\nAll entries below are 0\nNo unique solution exists",
            font_size=22,
            color=RED,
            line_spacing=1.3
        )
        fail_note.next_to(singular_matrix, DOWN, buff=0.6)
        
        self.play(
            Create(singular_matrix),
            Create(zero_row_highlight),
            run_time=1.2
        )
        self.wait(0.5)
        self.play(FadeIn(fail_note), run_time=0.8)
        self.wait(1.5)

        # Summary
        self.play(
            *[FadeOut(mob) for mob in [
                case2_label, singular_matrix, zero_row_highlight, fail_note
            ]],
            run_time=0.6
        )

        summary_title = Text("Summary: Pivot Rules", font_size=32, color=YELLOW)
        summary_title.shift(UP * 2.5)
        
        summary_points = VGroup(
            Text("• Pivot ≠ 0 → Continue elimination", font_size=24, color=WHITE),
            Text("• Pivot = 0, can swap rows → Row exchange", font_size=24, color=GREEN),
            Text("• Pivot = 0, all below are 0 → Singular (no solution)", font_size=24, color=RED),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_points.next_to(summary_title, DOWN, buff=0.8)
        
        self.play(
            FadeOut(title),
            Write(summary_title),
            run_time=0.8
        )
        for point in summary_points:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.4)

        self.wait(2)


class Lecture2_EliminationAsShear(Scene):
    """Show elimination as a geometric shear transformation on a 2D grid."""

    def construct(self):
        # Create the number plane (grid)
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )

        # Basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=5)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=5)

        # Unit square at origin
        unit_square = Square(side_length=1)
        unit_square.move_to([0.5, 0.5, 0])
        unit_square.set_fill(YELLOW, opacity=0.3)
        unit_square.set_stroke(YELLOW, width=2)

        # Basis vector labels
        i_label = MathTex(r"\hat{\imath}", font_size=30, color=GREEN)
        i_label.next_to(i_hat, DOWN, buff=0.15)
        j_label = MathTex(r"\hat{\jmath}", font_size=30, color=RED)
        j_label.next_to(j_hat, LEFT, buff=0.15)

        self.play(Create(plane), run_time=1.5)
        self.play(
            GrowArrow(i_hat),
            GrowArrow(j_hat),
            FadeIn(i_label),
            FadeIn(j_label),
            FadeIn(unit_square),
            run_time=1,
        )
        self.wait(0.5)

        # Title with background
        title_tex = Text("Elimination = Shear Transformation", font_size=36, color=WHITE)
        title_bg = BackgroundRectangle(title_tex, fill_opacity=0.85, buff=0.2)
        title_group = VGroup(title_bg, title_tex).to_edge(UP, buff=0.3)
        self.play(FadeIn(title_group), run_time=0.8)
        self.wait(0.8)

        # Show the elimination matrix E21
        matrix_label = MathTex(
            r"E_{21} = \begin{bmatrix} 1 & 0 \\ -3 & 1 \end{bmatrix}",
            font_size=32,
        )
        matrix_bg = BackgroundRectangle(matrix_label, fill_opacity=0.85, buff=0.2)
        matrix_group = VGroup(matrix_bg, matrix_label)
        matrix_group.to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.play(FadeIn(matrix_group), run_time=0.8)
        self.wait(0.5)

        # Apply the shear transformation E21 = [[1,0],[-3,1]]
        e21 = [[1, 0], [-3, 1]]
        self.play(
            ApplyMatrix(e21, plane),
            ApplyMatrix(e21, i_hat),
            ApplyMatrix(e21, j_hat),
            ApplyMatrix(e21, unit_square),
            FadeOut(i_label),
            FadeOut(j_label),
            run_time=3,
        )
        self.wait(0.5)

        # Annotate the operation
        annot_tex = Text("Row 2 - 3 x Row 1", font_size=28, color=ORANGE)
        annot_bg = BackgroundRectangle(annot_tex, fill_opacity=0.85, buff=0.15)
        annot_group = VGroup(annot_bg, annot_tex)
        annot_group.to_edge(DOWN, buff=0.5).shift(LEFT * 2)
        self.play(FadeIn(annot_group), run_time=0.8)
        self.wait(0.8)

        # Note that horizontal lines are preserved
        horiz_note = Text("Horizontal lines stay horizontal", font_size=24, color=BLUE)
        horiz_bg = BackgroundRectangle(horiz_note, fill_opacity=0.85, buff=0.15)
        horiz_group = VGroup(horiz_bg, horiz_note)
        horiz_group.next_to(annot_group, UP, buff=0.3)
        self.play(FadeIn(horiz_group), run_time=0.8)
        self.wait(1)

        # Show determinant = 1 (area unchanged)
        det_tex = MathTex(
            r"\det(E_{21}) = 1 \quad \Rightarrow \quad \text{Area unchanged}",
            font_size=30,
            color=GREEN,
        )
        det_bg = BackgroundRectangle(det_tex, fill_opacity=0.85, buff=0.2)
        det_group = VGroup(det_bg, det_tex)
        det_group.to_corner(DR, buff=0.5)
        self.play(FadeIn(det_group), run_time=0.8)
        self.wait(2)


class Lecture2_ComposedElimination(Scene):
    """Show composing two elimination steps as sequential shears on a grid."""

    def construct(self):
        # Create the number plane
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )

        # Basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=5)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=5)

        # Unit square
        unit_square = Square(side_length=1)
        unit_square.move_to([0.5, 0.5, 0])
        unit_square.set_fill(YELLOW, opacity=0.3)
        unit_square.set_stroke(YELLOW, width=2)

        self.play(Create(plane), run_time=1.5)
        self.play(
            GrowArrow(i_hat),
            GrowArrow(j_hat),
            FadeIn(unit_square),
            run_time=1,
        )
        self.wait(0.5)

        # Title
        title_tex = Text("Composing Elimination Steps", font_size=36, color=WHITE)
        title_bg = BackgroundRectangle(title_tex, fill_opacity=0.85, buff=0.2)
        title_group = VGroup(title_bg, title_tex).to_edge(UP, buff=0.3)
        self.play(FadeIn(title_group), run_time=0.8)
        self.wait(0.5)

        # --- Step 1: E21 = [[1,0],[-2,1]] ---
        step1_tex = MathTex(
            r"\text{Step 1: } E_{21} = \begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}",
            font_size=30,
        )
        step1_bg = BackgroundRectangle(step1_tex, fill_opacity=0.85, buff=0.15)
        step1_group = VGroup(step1_bg, step1_tex)
        step1_group.to_corner(UL, buff=0.5).shift(DOWN * 0.8)

        step1_note = Text("Row2 - 2 * Row1", font_size=24, color=ORANGE)
        step1_note_bg = BackgroundRectangle(step1_note, fill_opacity=0.85, buff=0.1)
        step1_note_group = VGroup(step1_note_bg, step1_note)
        step1_note_group.next_to(step1_group, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(step1_group), FadeIn(step1_note_group), run_time=0.8)
        self.wait(0.5)

        e21 = [[1, 0], [-2, 1]]
        self.play(
            ApplyMatrix(e21, plane),
            ApplyMatrix(e21, i_hat),
            ApplyMatrix(e21, j_hat),
            ApplyMatrix(e21, unit_square),
            run_time=3,
        )
        self.wait(1)

        # --- Step 2: E12 = [[1,-1],[0,1]] (back-substitution) ---
        step2_tex = MathTex(
            r"\text{Step 2: } E_{12} = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}",
            font_size=30,
        )
        step2_bg = BackgroundRectangle(step2_tex, fill_opacity=0.85, buff=0.15)
        step2_group = VGroup(step2_bg, step2_tex)
        step2_group.to_corner(UR, buff=0.5).shift(DOWN * 0.8)

        step2_note = Text("Row1 - 1 * Row2  (back-sub)", font_size=24, color=TEAL)
        step2_note_bg = BackgroundRectangle(step2_note, fill_opacity=0.85, buff=0.1)
        step2_note_group = VGroup(step2_note_bg, step2_note)
        step2_note_group.next_to(step2_group, DOWN, buff=0.2, aligned_edge=RIGHT)

        self.play(
            FadeOut(step1_group),
            FadeOut(step1_note_group),
            FadeIn(step2_group),
            FadeIn(step2_note_group),
            run_time=0.8,
        )
        self.wait(0.5)

        e12 = [[1, -1], [0, 1]]
        self.play(
            ApplyMatrix(e12, plane),
            ApplyMatrix(e12, i_hat),
            ApplyMatrix(e12, j_hat),
            ApplyMatrix(e12, unit_square),
            run_time=3,
        )
        self.wait(1)

        # Show composed result
        self.play(FadeOut(step2_group), FadeOut(step2_note_group), run_time=0.6)

        composed_tex = MathTex(
            r"E_{12} \cdot E_{21} = "
            r"\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}"
            r"\begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}"
            r"= \begin{bmatrix} 3 & -1 \\ -2 & 1 \end{bmatrix}",
            font_size=28,
        )
        composed_bg = BackgroundRectangle(composed_tex, fill_opacity=0.85, buff=0.2)
        composed_group = VGroup(composed_bg, composed_tex)
        composed_group.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(composed_group), run_time=1)
        self.wait(0.8)

        # Determinant still 1
        det_tex = MathTex(
            r"\det(E_{12} \cdot E_{21}) = 1 \times 1 = 1",
            font_size=28,
            color=GREEN,
        )
        det_bg = BackgroundRectangle(det_tex, fill_opacity=0.85, buff=0.15)
        det_group = VGroup(det_bg, det_tex)
        det_group.next_to(composed_group, UP, buff=0.3)

        self.play(FadeIn(det_group), run_time=0.8)
        self.wait(2)


class Lecture2_SingularElimination(Scene):
    """Show what happens geometrically when elimination fails (singular matrix)."""

    def construct(self):
        # Create the number plane
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )

        # Basis vectors
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=5)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=5)

        # Unit square
        unit_square = Square(side_length=1)
        unit_square.move_to([0.5, 0.5, 0])
        unit_square.set_fill(YELLOW, opacity=0.3)
        unit_square.set_stroke(YELLOW, width=2)

        self.play(Create(plane), run_time=1.5)
        self.play(
            GrowArrow(i_hat),
            GrowArrow(j_hat),
            FadeIn(unit_square),
            run_time=1,
        )
        self.wait(0.5)

        # Title
        title_tex = Text("Singular Matrix: Elimination Fails", font_size=36, color=RED)
        title_bg = BackgroundRectangle(title_tex, fill_opacity=0.85, buff=0.2)
        title_group = VGroup(title_bg, title_tex).to_edge(UP, buff=0.3)
        self.play(FadeIn(title_group), run_time=0.8)
        self.wait(0.5)

        # Show the singular matrix
        matrix_label = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
            font_size=32,
        )
        matrix_bg = BackgroundRectangle(matrix_label, fill_opacity=0.85, buff=0.2)
        matrix_group = VGroup(matrix_bg, matrix_label)
        matrix_group.to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.play(FadeIn(matrix_group), run_time=0.8)
        self.wait(0.5)

        # Apply the singular transformation [[1,2],[2,4]]
        singular = [[1, 2], [2, 4]]
        self.play(
            ApplyMatrix(singular, plane),
            ApplyMatrix(singular, i_hat),
            ApplyMatrix(singular, j_hat),
            ApplyMatrix(singular, unit_square),
            run_time=3,
        )
        self.wait(1)

        # "Space collapses to a line"
        collapse_tex = Text(
            "Singular: Space collapses to a line",
            font_size=28,
            color=ORANGE,
        )
        collapse_bg = BackgroundRectangle(collapse_tex, fill_opacity=0.85, buff=0.15)
        collapse_group = VGroup(collapse_bg, collapse_tex)
        collapse_group.to_edge(DOWN, buff=1.2)
        self.play(FadeIn(collapse_group), run_time=0.8)
        self.wait(1)

        # Show determinant = 0
        det_tex = MathTex(
            r"\det(A) = 1 \cdot 4 - 2 \cdot 2 = 0 \quad \Rightarrow \quad \text{Area} \to 0",
            font_size=28,
            color=RED,
        )
        det_bg = BackgroundRectangle(det_tex, fill_opacity=0.85, buff=0.15)
        det_group = VGroup(det_bg, det_tex)
        det_group.next_to(collapse_group, DOWN, buff=0.3)
        self.play(FadeIn(det_group), run_time=0.8)
        self.wait(1)

        # Contrast: no inverse
        no_inv_tex = Text(
            "No inverse exists -- can't un-squish a line back to a plane",
            font_size=24,
            color=GREY,
        )
        no_inv_bg = BackgroundRectangle(no_inv_tex, fill_opacity=0.85, buff=0.15)
        no_inv_group = VGroup(no_inv_bg, no_inv_tex)
        no_inv_group.next_to(det_group, DOWN, buff=0.3)
        self.play(FadeIn(no_inv_group), run_time=0.8)
        self.wait(2)
