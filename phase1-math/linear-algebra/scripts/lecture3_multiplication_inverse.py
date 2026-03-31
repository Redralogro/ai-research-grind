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
