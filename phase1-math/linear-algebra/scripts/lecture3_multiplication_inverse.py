"""
MIT 18.06 Lecture 3: Multiplication and Inverse Matrices
5 ways to multiply matrices, column/row/block methods,
and matrix inverses (Gauss-Jordan)

Style: 3Blue1Brown inspired
"""

from manim import *


class Lecture3_MatrixMultiplication(Scene):
    """5 ways to think about matrix multiplication AB = C"""

    def construct(self):
        title = Text("5 Ways to Multiply Matrices", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Show AB = C setup
        eq_label = MathTex("A \\cdot B = C", font_size=36, color=WHITE)
        eq_label.shift(UP * 2.8)
        self.play(Write(eq_label), run_time=0.8)
        self.wait(0.4)

        # ─── Way 1: Standard (dot product of rows × cols) ───
        way1_title = Text("Way 1: Row · Column (Standard)", font_size=28, color=BLUE)
        way1_title.shift(UP * 1.8)
        self.play(Write(way1_title), run_time=0.7)

        way1_formula = MathTex(
            r"C_{ij} = \sum_{k} A_{ik} \cdot B_{kj}",
            font_size=32
        )
        way1_formula.next_to(way1_title, DOWN, buff=0.3)

        way1_note = Text(
            "Each entry of C = dot product of a row of A with a column of B",
            font_size=20, color=GREY
        )
        way1_note.next_to(way1_formula, DOWN, buff=0.25)

        self.play(Write(way1_formula), FadeIn(way1_note), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(way1_title), FadeOut(way1_formula), FadeOut(way1_note), run_time=0.5)

        # ─── Way 2: Columns of C ───
        way2_title = Text("Way 2: Columns of C", font_size=28, color=GREEN)
        way2_title.shift(UP * 1.8)
        self.play(Write(way2_title), run_time=0.7)

        way2_formula = MathTex(
            r"\text{col}_j(C) = A \cdot \text{col}_j(B)",
            font_size=32
        )
        way2_formula.next_to(way2_title, DOWN, buff=0.3)

        way2_note = Text(
            "Each column of C = A times that column of B\n"
            "(C's columns are linear combinations of A's columns)",
            font_size=20, color=GREY, line_spacing=1.3
        )
        way2_note.next_to(way2_formula, DOWN, buff=0.25)

        self.play(Write(way2_formula), FadeIn(way2_note), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(way2_title), FadeOut(way2_formula), FadeOut(way2_note), run_time=0.5)

        # ─── Way 3: Rows of C ───
        way3_title = Text("Way 3: Rows of C", font_size=28, color=ORANGE)
        way3_title.shift(UP * 1.8)
        self.play(Write(way3_title), run_time=0.7)

        way3_formula = MathTex(
            r"\text{row}_i(C) = \text{row}_i(A) \cdot B",
            font_size=32
        )
        way3_formula.next_to(way3_title, DOWN, buff=0.3)

        way3_note = Text(
            "Each row of C = that row of A times B\n"
            "(C's rows are linear combinations of B's rows)",
            font_size=20, color=GREY, line_spacing=1.3
        )
        way3_note.next_to(way3_formula, DOWN, buff=0.25)

        self.play(Write(way3_formula), FadeIn(way3_note), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(way3_title), FadeOut(way3_formula), FadeOut(way3_note), run_time=0.5)

        # ─── Way 4: Columns × Rows (outer product sum) ───
        way4_title = Text("Way 4: Sum of Outer Products", font_size=28, color=RED)
        way4_title.shift(UP * 1.8)
        self.play(Write(way4_title), run_time=0.7)

        way4_formula = MathTex(
            r"AB = \sum_{k} \text{col}_k(A) \cdot \text{row}_k(B)",
            font_size=30
        )
        way4_formula.next_to(way4_title, DOWN, buff=0.3)

        way4_note = Text(
            "AB = sum of (rank-1 matrices)\n"
            "Each term: column of A × row of B → full matrix",
            font_size=20, color=GREY, line_spacing=1.3
        )
        way4_note.next_to(way4_formula, DOWN, buff=0.25)

        self.play(Write(way4_formula), FadeIn(way4_note), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(way4_title), FadeOut(way4_formula), FadeOut(way4_note), run_time=0.5)

        # ─── Way 5: Block multiplication ───
        way5_title = Text("Way 5: Block Multiplication", font_size=28, color=PURPLE)
        way5_title.shift(UP * 1.8)
        self.play(Write(way5_title), run_time=0.7)

        way5_formula = MathTex(
            r"\begin{bmatrix} A_1 & A_2 \\ A_3 & A_4 \end{bmatrix}"
            r"\begin{bmatrix} B_1 & B_2 \\ B_3 & B_4 \end{bmatrix}"
            r"= \begin{bmatrix} A_1B_1+A_2B_3 & A_1B_2+A_2B_4 \\ "
            r"A_3B_1+A_4B_3 & A_3B_2+A_4B_4 \end{bmatrix}",
            font_size=22
        )
        way5_formula.next_to(way5_title, DOWN, buff=0.3)

        way5_note = Text(
            "Treat sub-matrices as single elements — same multiplication rules apply",
            font_size=20, color=GREY
        )
        way5_note.next_to(way5_formula, DOWN, buff=0.25)

        self.play(Write(way5_formula), FadeIn(way5_note), run_time=1.5)
        self.wait(2)

        # Summary
        self.play(
            FadeOut(way5_title), FadeOut(way5_formula), FadeOut(way5_note),
            FadeOut(eq_label), run_time=0.5
        )

        summary = VGroup(
            Text("5 Ways to Multiply AB:", font_size=26, color=YELLOW),
            Text("1. Row · Col → C_ij  (standard)", font_size=22, color=BLUE),
            Text("2. Columns of C = A · col(B)", font_size=22, color=GREEN),
            Text("3. Rows of C = row(A) · B", font_size=22, color=ORANGE),
            Text("4. Sum of col(A) × row(B) outer products", font_size=22, color=RED),
            Text("5. Block multiplication", font_size=22, color=PURPLE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.center()

        self.play(FadeOut(title), run_time=0.3)
        for item in summary:
            self.play(FadeIn(item), run_time=0.5)
        self.wait(2)


class Lecture3_InverseMatrix(Scene):
    """Concept of inverse matrix and Gauss-Jordan method"""

    def construct(self):
        title = Text("Inverse Matrices", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Definition
        def_text = MathTex(
            r"A^{-1} A = I \quad \text{and} \quad A A^{-1} = I",
            font_size=34
        )
        def_text.shift(UP * 2.5)
        self.play(Write(def_text), run_time=1)
        self.wait(0.6)

        # Why it matters
        why = Text(
            "If A is invertible: Ax = b  →  x = A⁻¹b",
            font_size=26, color=GREY
        )
        why.next_to(def_text, DOWN, buff=0.4)
        self.play(FadeIn(why), run_time=0.8)
        self.wait(0.8)

        # Conditions for invertibility
        cond_title = Text("When does A⁻¹ exist?", font_size=28, color=ORANGE)
        cond_title.next_to(why, DOWN, buff=0.6)
        self.play(Write(cond_title), run_time=0.7)

        conditions = VGroup(
            Text("✓  All n pivots are non-zero", font_size=22, color=GREEN),
            Text("✓  det(A) ≠ 0", font_size=22, color=GREEN),
            Text("✗  If det(A) = 0 → A is singular (no inverse)", font_size=22, color=RED),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        conditions.next_to(cond_title, DOWN, buff=0.4)

        for c in conditions:
            self.play(FadeIn(c), run_time=0.6)
        self.wait(1)

        self.play(
            FadeOut(cond_title), FadeOut(conditions), FadeOut(why),
            def_text.animate.shift(UP * 0.5),
            run_time=0.7
        )

        # Gauss-Jordan Method
        gj_title = Text("Gauss-Jordan Elimination: [A | I] → [I | A⁻¹]", font_size=26, color=BLUE)
        gj_title.next_to(def_text, DOWN, buff=0.6)
        self.play(Write(gj_title), run_time=0.9)
        self.wait(0.5)

        # Example: find inverse of 2x2 matrix
        example_label = Text("Example: Find A⁻¹", font_size=24, color=WHITE)
        example_label.next_to(gj_title, DOWN, buff=0.5)
        self.play(FadeIn(example_label), run_time=0.6)

        a_label = MathTex("A = ", font_size=30)
        a_mat = Matrix(
            [[2, 1], [5, 3]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.9)
        a_group = VGroup(a_label, a_mat).arrange(RIGHT, buff=0.15)
        a_group.next_to(example_label, DOWN, buff=0.4).shift(LEFT * 3)
        self.play(Write(a_label), Create(a_mat), run_time=0.8)
        self.wait(0.4)

        # Augmented [A|I]
        aug_label = Text("Augmented [A | I]:", font_size=22, color=GREY)
        aug_label.next_to(a_group, DOWN, buff=0.5, aligned_edge=LEFT)
        aug_mat = Matrix(
            [[2, 1, "|", 1, 0], [5, 3, "|", 0, 1]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.85)
        aug_mat.next_to(aug_label, DOWN, buff=0.25, aligned_edge=LEFT)

        self.play(FadeIn(aug_label), Create(aug_mat), run_time=1)
        self.wait(0.6)

        # Step 1 annotation
        step1 = Text("R₂ → R₂ - (5/2)R₁", font_size=20, color=RED)
        step1.to_edge(RIGHT, buff=1).shift(UP * 0)
        self.play(Write(step1), run_time=0.6)

        mid_mat = Matrix(
            [[2, 1, "|", 1, 0], [0, "½", "|", "-5/2", 1]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.85)
        mid_mat.move_to(aug_mat)
        self.play(Transform(aug_mat, mid_mat), run_time=1)
        self.wait(0.5)

        # Step 2 annotation
        step2 = Text("Scale & eliminate upward", font_size=20, color=RED)
        step2.next_to(step1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(step2), run_time=0.6)

        final_aug = Matrix(
            [[1, 0, "|", 3, -1], [0, 1, "|", -5, 2]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.85)
        final_aug.move_to(aug_mat)
        self.play(Transform(aug_mat, final_aug), run_time=1)
        self.wait(0.6)

        # Result
        result_label = MathTex(r"A^{-1} = ", font_size=30)
        result_mat = Matrix(
            [[3, -1], [-5, 2]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).scale(0.9)
        result_mat.set_color(GREEN)
        result_group = VGroup(result_label, result_mat).arrange(RIGHT, buff=0.15)
        result_group.to_edge(RIGHT, buff=1.2).shift(DOWN * 1.5)

        self.play(Write(result_label), Create(result_mat), run_time=1)
        self.wait(2)


class Lecture3_InverseProperties(Scene):
    """Key properties of inverses and when they don't exist"""

    def construct(self):
        title = Text("Properties of Inverses", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Properties list
        props_title = Text("Key Properties:", font_size=28, color=ORANGE)
        props_title.shift(UP * 2.5)
        self.play(Write(props_title), run_time=0.6)

        props = VGroup(
            MathTex(r"(AB)^{-1} = B^{-1} A^{-1}", font_size=30),
            MathTex(r"(A^T)^{-1} = (A^{-1})^T", font_size=30),
            MathTex(r"(A^{-1})^{-1} = A", font_size=30),
            MathTex(r"(cA)^{-1} = \frac{1}{c} A^{-1}", font_size=30),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        props.next_to(props_title, DOWN, buff=0.5)

        notes = [
            "Reverse order! (undo B first, then A)",
            "Transpose and inverse commute",
            "Inverse of inverse = original",
            "Scalar scales the inverse",
        ]

        for prop, note in zip(props, notes):
            note_text = Text(f"← {note}", font_size=18, color=GREY)
            note_text.next_to(prop, RIGHT, buff=0.5)
            self.play(Write(prop), FadeIn(note_text), run_time=0.9)
            self.wait(0.4)

        self.wait(1)
        self.play(FadeOut(props_title), FadeOut(props), run_time=0.5)

        # When inverse doesn't exist
        no_inv_title = Text("When A⁻¹ Does NOT Exist", font_size=30, color=RED)
        no_inv_title.shift(UP * 2.5)
        self.play(Write(no_inv_title), run_time=0.7)

        cases = VGroup(
            Text("• Zero pivot → singular matrix", font_size=24, color=WHITE),
            Text("• Rows are linearly dependent", font_size=24, color=WHITE),
            Text("• Columns don't span the full space", font_size=24, color=WHITE),
            Text("• det(A) = 0", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        cases.next_to(no_inv_title, DOWN, buff=0.6)

        for case in cases:
            self.play(FadeIn(case), run_time=0.6)
        self.wait(0.8)

        # Connection to solving Ax = b
        self.play(FadeOut(no_inv_title), FadeOut(cases), run_time=0.5)

        connection_title = Text("Connection: Ax = b", font_size=30, color=BLUE)
        connection_title.shift(UP * 2.5)
        self.play(Write(connection_title), run_time=0.7)

        table = VGroup(
            Text("A invertible   →  x = A⁻¹b  (unique solution)", font_size=22, color=GREEN),
            Text("A singular     →  no solution or ∞ solutions", font_size=22, color=RED),
            Text("", font_size=10),
            MathTex(
                r"Ax = b \implies A^{-1}(Ax) = A^{-1}b \implies Ix = A^{-1}b \implies x = A^{-1}b",
                font_size=22
            )
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        table.next_to(connection_title, DOWN, buff=0.6)

        for row in table:
            self.play(FadeIn(row), run_time=0.8)
        self.wait(2)

        # Takeaway
        self.play(
            *[FadeOut(mob) for mob in [connection_title, table]],
            run_time=0.5
        )

        takeaway = VGroup(
            Text("Key Takeaway", font_size=32, color=YELLOW),
            Text("Elimination → finds pivots → tells us if A is invertible", font_size=24, color=WHITE),
            Text("Gauss-Jordan → extends elimination to find A⁻¹", font_size=24, color=WHITE),
            Text("Next: Lecture 4 — A = LU Factorization", font_size=24, color=GREY),
        ).arrange(DOWN, buff=0.5)
        takeaway.center()

        self.play(FadeOut(title), run_time=0.3)
        for t in takeaway:
            self.play(FadeIn(t), run_time=0.7)
        self.wait(2)


class Lecture3_MultiplicationAsComposition(Scene):
    """Matrix multiplication AB as applying B first, then A on a grid."""

    def construct(self):
        # Title with background
        title_text = Text(
            "Matrix Multiplication = Composition", font_size=36, color=YELLOW
        )
        title_bg = BackgroundRectangle(title_text, color=BLACK, fill_opacity=0.85, buff=0.2)
        title = VGroup(title_bg, title_text)
        title.to_edge(UP, buff=0.3)
        title.set_z_index(10)

        # Grid and basis vectors
        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-5, 5],
            background_line_style={"stroke_opacity": 0.4},
        )
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=5)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=5)

        self.play(Create(plane), GrowArrow(i_hat), GrowArrow(j_hat), run_time=1.5)
        self.play(FadeIn(title), run_time=0.6)
        self.wait(0.5)

        # Matrices
        # B = 90-degree rotation, A = shear
        B = [[0, -1], [1, 0]]
        A = [[1, 1], [0, 1]]
        # AB = [[1*0+1*1, 1*(-1)+1*0], [0*0+1*1, 0*(-1)+1*0]] = [[1,-1],[1,0]]

        # Step 1: Apply B (rotation)
        step1_text = Text("Apply B first (rotation):", font_size=26, color=BLUE)
        step1_bg = BackgroundRectangle(step1_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        step1 = VGroup(step1_bg, step1_text)
        step1.to_edge(DOWN, buff=0.8)
        step1.set_z_index(10)

        b_mat = MathTex(
            r"B = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}",
            font_size=28, color=BLUE,
        )
        b_mat_bg = BackgroundRectangle(b_mat, color=BLACK, fill_opacity=0.85, buff=0.15)
        b_group = VGroup(b_mat_bg, b_mat)
        b_group.next_to(step1, UP, buff=0.25)
        b_group.set_z_index(10)

        self.play(FadeIn(step1), FadeIn(b_group), run_time=0.7)
        self.play(
            ApplyMatrix(B, plane),
            ApplyMatrix(B, i_hat),
            ApplyMatrix(B, j_hat),
            run_time=3,
        )
        self.wait(1)

        # Step 2: Apply A (shear)
        step2_text = Text("Then apply A (shear):", font_size=26, color=ORANGE)
        step2_bg = BackgroundRectangle(step2_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        step2 = VGroup(step2_bg, step2_text)
        step2.to_edge(DOWN, buff=0.8)
        step2.set_z_index(10)

        a_mat = MathTex(
            r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}",
            font_size=28, color=ORANGE,
        )
        a_mat_bg = BackgroundRectangle(a_mat, color=BLACK, fill_opacity=0.85, buff=0.15)
        a_group = VGroup(a_mat_bg, a_mat)
        a_group.next_to(step2, UP, buff=0.25)
        a_group.set_z_index(10)

        self.play(
            FadeOut(step1), FadeOut(b_group),
            FadeIn(step2), FadeIn(a_group),
            run_time=0.7,
        )
        self.play(
            ApplyMatrix(A, plane),
            ApplyMatrix(A, i_hat),
            ApplyMatrix(A, j_hat),
            run_time=3,
        )
        self.wait(1)

        # Show combined result
        self.play(FadeOut(step2), FadeOut(a_group), run_time=0.5)

        result = MathTex(
            r"AB = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}"
            r"\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}"
            r"= \begin{bmatrix} 1 & -1 \\ 1 & 0 \end{bmatrix}",
            font_size=28, color=WHITE,
        )
        result_bg = BackgroundRectangle(result, color=BLACK, fill_opacity=0.85, buff=0.15)
        result_group = VGroup(result_bg, result)
        result_group.to_edge(DOWN, buff=1.0)
        result_group.set_z_index(10)
        self.play(FadeIn(result_group), run_time=0.8)
        self.wait(1.5)

        # Key insight
        insight_text = Text(
            "AB \u2260 BA in general \u2014 order matters!",
            font_size=30, color=YELLOW,
        )
        insight_bg = BackgroundRectangle(insight_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        insight = VGroup(insight_bg, insight_text)
        insight.next_to(result_group, UP, buff=0.3)
        insight.set_z_index(10)
        self.play(FadeIn(insight), run_time=0.8)
        self.wait(2)


class Lecture3_CompositionOrderMatters(Scene):
    """Shows that AB != BA by applying transformations in both orders."""

    def construct(self):
        title_text = Text(
            "Does Order Matter? AB vs BA", font_size=36, color=YELLOW
        )
        title_text.to_edge(UP, buff=0.3)
        self.play(Write(title_text), run_time=0.8)
        self.wait(0.5)

        A = [[1, 1], [0, 1]]  # shear
        B = [[0, -1], [1, 0]]  # 90-degree rotation

        # --- Left side: AB (apply B first, then A) ---
        left_label = Text("AB: B first, then A", font_size=22, color=BLUE)
        left_label.shift(LEFT * 3.5 + UP * 2.2)

        left_plane = NumberPlane(
            x_range=[-4, 4], y_range=[-4, 4],
            background_line_style={"stroke_opacity": 0.3},
        ).scale(0.4).shift(LEFT * 3.5)
        left_i = Arrow(
            left_plane.get_center(),
            left_plane.get_center() + RIGHT * 0.4,
            buff=0, color=GREEN, stroke_width=3,
        )
        left_j = Arrow(
            left_plane.get_center(),
            left_plane.get_center() + UP * 0.4,
            buff=0, color=RED, stroke_width=3,
        )
        left_group = VGroup(left_plane, left_i, left_j)

        # --- Right side: BA (apply A first, then B) ---
        right_label = Text("BA: A first, then B", font_size=22, color=ORANGE)
        right_label.shift(RIGHT * 3.5 + UP * 2.2)

        right_plane = NumberPlane(
            x_range=[-4, 4], y_range=[-4, 4],
            background_line_style={"stroke_opacity": 0.3},
        ).scale(0.4).shift(RIGHT * 3.5)
        right_i = Arrow(
            right_plane.get_center(),
            right_plane.get_center() + RIGHT * 0.4,
            buff=0, color=GREEN, stroke_width=3,
        )
        right_j = Arrow(
            right_plane.get_center(),
            right_plane.get_center() + UP * 0.4,
            buff=0, color=RED, stroke_width=3,
        )
        right_group = VGroup(right_plane, right_i, right_j)

        self.play(
            Create(left_plane), Create(right_plane),
            GrowArrow(left_i), GrowArrow(left_j),
            GrowArrow(right_i), GrowArrow(right_j),
            FadeIn(left_label), FadeIn(right_label),
            run_time=1.5,
        )
        self.wait(0.5)

        # Left side: apply B then A
        step_left_1 = Text("B (rotate)", font_size=18, color=BLUE_C)
        step_left_1.next_to(left_group, DOWN, buff=0.2)
        self.play(FadeIn(step_left_1), run_time=0.4)
        self.play(
            ApplyMatrix(B, left_plane),
            ApplyMatrix(B, left_i),
            ApplyMatrix(B, left_j),
            run_time=2,
        )
        self.wait(0.3)

        step_left_2 = Text("then A (shear)", font_size=18, color=BLUE_C)
        step_left_2.next_to(step_left_1, DOWN, buff=0.15)
        self.play(FadeIn(step_left_2), run_time=0.4)
        self.play(
            ApplyMatrix(A, left_plane),
            ApplyMatrix(A, left_i),
            ApplyMatrix(A, left_j),
            run_time=2,
        )
        self.wait(0.5)

        # Right side: apply A then B
        step_right_1 = Text("A (shear)", font_size=18, color=ORANGE)
        step_right_1.next_to(right_group, DOWN, buff=0.2)
        self.play(FadeIn(step_right_1), run_time=0.4)
        self.play(
            ApplyMatrix(A, right_plane),
            ApplyMatrix(A, right_i),
            ApplyMatrix(A, right_j),
            run_time=2,
        )
        self.wait(0.3)

        step_right_2 = Text("then B (rotate)", font_size=18, color=ORANGE)
        step_right_2.next_to(step_right_1, DOWN, buff=0.15)
        self.play(FadeIn(step_right_2), run_time=0.4)
        self.play(
            ApplyMatrix(B, right_plane),
            ApplyMatrix(B, right_i),
            ApplyMatrix(B, right_j),
            run_time=2,
        )
        self.wait(1)

        # Show results
        # AB = [[1,-1],[1,0]], BA = [[0,-1],[1,1]]
        ab_result = MathTex(
            r"AB = \begin{bmatrix} 1 & -1 \\ 1 & 0 \end{bmatrix}",
            font_size=24, color=BLUE,
        )
        ab_result.next_to(step_left_2, DOWN, buff=0.3)

        ba_result = MathTex(
            r"BA = \begin{bmatrix} 0 & -1 \\ 1 & 1 \end{bmatrix}",
            font_size=24, color=ORANGE,
        )
        ba_result.next_to(step_right_2, DOWN, buff=0.3)

        self.play(FadeIn(ab_result), FadeIn(ba_result), run_time=0.8)
        self.wait(1)

        # Bottom conclusion
        conclusion = Text(
            "Matrix multiplication is NOT commutative",
            font_size=28, color=YELLOW,
        )
        conclusion.to_edge(DOWN, buff=0.4)
        self.play(Write(conclusion), run_time=1)
        self.wait(2)


class Lecture3_InverseUndoesTransformation(Scene):
    """Shows A inverse undoing A's transformation on the grid."""

    def construct(self):
        # Title
        title_text = Text(
            "Inverse = Undo the Transformation", font_size=36, color=YELLOW
        )
        title_bg = BackgroundRectangle(title_text, color=BLACK, fill_opacity=0.85, buff=0.2)
        title = VGroup(title_bg, title_text)
        title.to_edge(UP, buff=0.3)
        title.set_z_index(10)

        # Grid, basis vectors, and a tracked point
        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-5, 5],
            background_line_style={"stroke_opacity": 0.4},
        )
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=5)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=5)
        tracked_dot = Dot(point=[1, 2, 0], color=YELLOW, radius=0.1)
        dot_label = MathTex(r"\begin{bmatrix}1\\2\end{bmatrix}", font_size=22, color=YELLOW)
        dot_label.next_to(tracked_dot, UR, buff=0.1)
        dot_label.set_z_index(10)
        dot_label_bg = BackgroundRectangle(dot_label, color=BLACK, fill_opacity=0.7, buff=0.1)
        dot_label_bg.set_z_index(9)

        self.play(
            Create(plane), GrowArrow(i_hat), GrowArrow(j_hat),
            FadeIn(tracked_dot), FadeIn(dot_label_bg), FadeIn(dot_label),
            run_time=1.5,
        )
        self.play(FadeIn(title), run_time=0.6)
        self.wait(0.5)

        # A = [[2,1],[1,1]], A_inv = [[1,-1],[-1,2]]
        A = [[2, 1], [1, 1]]
        A_inv = [[1, -1], [-1, 2]]

        # Apply A
        apply_a_text = Text("Apply A", font_size=26, color=BLUE)
        apply_a_bg = BackgroundRectangle(apply_a_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        apply_a = VGroup(apply_a_bg, apply_a_text)
        apply_a.to_edge(DOWN, buff=0.8)
        apply_a.set_z_index(10)

        a_mat_label = MathTex(
            r"A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}",
            font_size=28, color=BLUE,
        )
        a_mat_bg = BackgroundRectangle(a_mat_label, color=BLACK, fill_opacity=0.85, buff=0.15)
        a_mat_group = VGroup(a_mat_bg, a_mat_label)
        a_mat_group.next_to(apply_a, UP, buff=0.25)
        a_mat_group.set_z_index(10)

        self.play(FadeIn(apply_a), FadeIn(a_mat_group), run_time=0.7)
        self.play(
            ApplyMatrix(A, plane),
            ApplyMatrix(A, i_hat),
            ApplyMatrix(A, j_hat),
            ApplyMatrix(A, tracked_dot),
            FadeOut(dot_label_bg), FadeOut(dot_label),
            run_time=3,
        )
        self.wait(1.5)

        # Apply A inverse
        apply_ainv_text = Text("Apply A\u207b\u00b9", font_size=26, color=TEAL)
        apply_ainv_bg = BackgroundRectangle(
            apply_ainv_text, color=BLACK, fill_opacity=0.85, buff=0.15
        )
        apply_ainv = VGroup(apply_ainv_bg, apply_ainv_text)
        apply_ainv.to_edge(DOWN, buff=0.8)
        apply_ainv.set_z_index(10)

        ainv_mat_label = MathTex(
            r"A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}",
            font_size=28, color=TEAL,
        )
        ainv_mat_bg = BackgroundRectangle(ainv_mat_label, color=BLACK, fill_opacity=0.85, buff=0.15)
        ainv_mat_group = VGroup(ainv_mat_bg, ainv_mat_label)
        ainv_mat_group.next_to(apply_ainv, UP, buff=0.25)
        ainv_mat_group.set_z_index(10)

        self.play(
            FadeOut(apply_a), FadeOut(a_mat_group),
            FadeIn(apply_ainv), FadeIn(ainv_mat_group),
            run_time=0.7,
        )
        self.play(
            ApplyMatrix(A_inv, plane),
            ApplyMatrix(A_inv, i_hat),
            ApplyMatrix(A_inv, j_hat),
            ApplyMatrix(A_inv, tracked_dot),
            run_time=3,
        )
        self.wait(1)

        # Show equation
        self.play(FadeOut(apply_ainv), FadeOut(ainv_mat_group), run_time=0.5)

        equation = MathTex(r"A^{-1} A = I", font_size=36, color=WHITE)
        eq_bg = BackgroundRectangle(equation, color=BLACK, fill_opacity=0.85, buff=0.15)
        eq_group = VGroup(eq_bg, equation)
        eq_group.to_edge(DOWN, buff=1.2)
        eq_group.set_z_index(10)
        self.play(FadeIn(eq_group), run_time=0.8)
        self.wait(1)

        # Key insight
        insight_text = Text(
            "The inverse transformation perfectly reverses the original",
            font_size=26, color=YELLOW,
        )
        insight_bg = BackgroundRectangle(insight_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        insight = VGroup(insight_bg, insight_text)
        insight.next_to(eq_group, UP, buff=0.3)
        insight.set_z_index(10)
        self.play(FadeIn(insight), run_time=0.8)
        self.wait(2)


class Lecture3_SingularNoInverse(Scene):
    """Shows why a singular matrix has no inverse — space gets squished."""

    def construct(self):
        # Title
        title_text = Text(
            "Singular Matrix: No Inverse", font_size=36, color=YELLOW
        )
        title_bg = BackgroundRectangle(title_text, color=BLACK, fill_opacity=0.85, buff=0.2)
        title = VGroup(title_bg, title_text)
        title.to_edge(UP, buff=0.3)
        title.set_z_index(10)

        # Grid and basis vectors
        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-5, 5],
            background_line_style={"stroke_opacity": 0.4},
        )
        i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN, stroke_width=5)
        j_hat = Arrow(ORIGIN, UP, buff=0, color=RED, stroke_width=5)

        # Several colored dots at different positions
        dot_positions = [
            ([1, 0, 0], BLUE),
            ([0, 1, 0], ORANGE),
            ([1, 1, 0], PURPLE),
            ([-1, 1, 0], TEAL),
            ([2, -1, 0], PINK),
            ([-1, -1, 0], MAROON),
        ]
        dots = VGroup()
        for pos, col in dot_positions:
            dots.add(Dot(point=pos, color=col, radius=0.08))

        self.play(
            Create(plane), GrowArrow(i_hat), GrowArrow(j_hat),
            *[FadeIn(d) for d in dots],
            run_time=1.5,
        )
        self.play(FadeIn(title), run_time=0.6)
        self.wait(0.5)

        # Singular matrix: [[1, 2], [0.5, 1]], det = 1*1 - 2*0.5 = 0
        S = [[1, 2], [0.5, 1]]

        mat_label = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 0.5 & 1 \end{bmatrix}",
            font_size=28, color=WHITE,
        )
        mat_bg = BackgroundRectangle(mat_label, color=BLACK, fill_opacity=0.85, buff=0.15)
        mat_group = VGroup(mat_bg, mat_label)
        mat_group.to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        mat_group.set_z_index(10)
        self.play(FadeIn(mat_group), run_time=0.7)

        # Apply singular matrix
        self.play(
            ApplyMatrix(S, plane),
            ApplyMatrix(S, i_hat),
            ApplyMatrix(S, j_hat),
            *[ApplyMatrix(S, d) for d in dots],
            run_time=3,
        )
        self.wait(1)

        # Show det = 0
        det_text = MathTex(
            r"\det(A) = 1 \cdot 1 - 2 \cdot 0.5 = 0",
            font_size=28, color=RED,
        )
        det_bg = BackgroundRectangle(det_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        det_group = VGroup(det_bg, det_text)
        det_group.to_edge(DOWN, buff=1.5)
        det_group.set_z_index(10)

        squish_text = Text(
            "Space squished to a line!", font_size=26, color=RED
        )
        squish_bg = BackgroundRectangle(squish_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        squish_group = VGroup(squish_bg, squish_text)
        squish_group.next_to(det_group, UP, buff=0.25)
        squish_group.set_z_index(10)

        self.play(FadeIn(det_group), FadeIn(squish_group), run_time=0.8)
        self.wait(1.5)

        # Information lost
        self.play(FadeOut(squish_group), run_time=0.4)

        lost_text = Text(
            "Can't un-squish! Information is lost",
            font_size=26, color=ORANGE,
        )
        lost_bg = BackgroundRectangle(lost_text, color=BLACK, fill_opacity=0.85, buff=0.15)
        lost_group = VGroup(lost_bg, lost_text)
        lost_group.next_to(det_group, UP, buff=0.25)
        lost_group.set_z_index(10)
        self.play(FadeIn(lost_group), run_time=0.8)
        self.wait(1)

        # Show that multiple inputs map to same output
        arrow_note = Text(
            "Multiple input vectors \u2192 same output point",
            font_size=22, color=GREY,
        )
        arrow_note_bg = BackgroundRectangle(arrow_note, color=BLACK, fill_opacity=0.85, buff=0.1)
        arrow_group = VGroup(arrow_note_bg, arrow_note)
        arrow_group.next_to(lost_group, UP, buff=0.25)
        arrow_group.set_z_index(10)
        self.play(FadeIn(arrow_group), run_time=0.7)
        self.wait(1.5)

        # Conclusion
        self.play(
            FadeOut(lost_group), FadeOut(arrow_group),
            FadeOut(det_group), FadeOut(mat_group),
            run_time=0.5,
        )

        conclusion = Text(
            "No inverse exists for singular matrices",
            font_size=30, color=YELLOW,
        )
        conclusion_bg = BackgroundRectangle(conclusion, color=BLACK, fill_opacity=0.85, buff=0.2)
        conclusion_group = VGroup(conclusion_bg, conclusion)
        conclusion_group.to_edge(DOWN, buff=1.0)
        conclusion_group.set_z_index(10)
        self.play(FadeIn(conclusion_group), run_time=0.8)
        self.wait(2)
