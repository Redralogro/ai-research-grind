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
