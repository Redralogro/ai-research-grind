"""
MIT 18.06 Lecture 5: Transposes, Permutations, Vector Spaces
Permutation matrices, transpose operation, symmetric matrices,
and introduction to vector spaces / subspaces.

Style: 3Blue1Brown inspired
"""

from manim import *


class Lecture5_Permutations(Scene):
    """All 3x3 permutation matrices and PA = LU"""

    def construct(self):
        title = Text("Permutation Matrices", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        intro = Text(
            "A permutation matrix P has exactly one 1 in each row and column",
            font_size=22, color=GREY
        )
        intro.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(intro), run_time=0.8)
        self.wait(0.8)

        # All 6 = 3! permutation matrices
        perm_data = [
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], "I (no exchange)"),
            ([[0, 1, 0], [1, 0, 0], [0, 0, 1]], "Swap rows 1, 2"),
            ([[0, 0, 1], [0, 1, 0], [1, 0, 0]], "Swap rows 1, 3"),
            ([[1, 0, 0], [0, 0, 1], [0, 1, 0]], "Swap rows 2, 3"),
            ([[0, 1, 0], [0, 0, 1], [1, 0, 0]], "Cycle 1->2->3"),
            ([[0, 0, 1], [1, 0, 0], [0, 1, 0]], "Cycle 1->3->2"),
        ]

        count_text = MathTex(
            r"3! = 6 \text{ permutation matrices for } 3 \times 3",
            font_size=28, color=BLUE
        )
        count_text.shift(UP * 1.5)
        self.play(Write(count_text), run_time=0.8)
        self.wait(0.6)

        self.play(FadeOut(intro), run_time=0.3)

        # Show them in a grid (2 rows of 3)
        perm_group = VGroup()
        for i, (mat_vals, label_text) in enumerate(perm_data):
            mat = Matrix(
                mat_vals,
                h_buff=0.8, v_buff=0.6,
                element_to_mobject_config={"font_size": 24}
            )
            label = Text(label_text, font_size=16, color=GREY)
            label.next_to(mat, DOWN, buff=0.15)
            pair = VGroup(mat, label)
            perm_group.add(pair)

        perm_group.arrange_in_grid(rows=2, cols=3, buff=0.5)
        perm_group.scale(0.75)
        perm_group.shift(DOWN * 0.5)

        self.play(
            *[FadeIn(p, shift=UP * 0.3) for p in perm_group],
            run_time=2
        )
        self.wait(2)

        # Clear and show key property
        self.play(FadeOut(perm_group), FadeOut(count_text), run_time=0.5)

        # P^{-1} = P^T demonstration
        prop_title = Text("Key Property: P^(-1) = P^T", font_size=30, color=GREEN)
        prop_title.shift(UP * 2)
        self.play(Write(prop_title), run_time=0.8)

        # Example: swap rows 1,2
        p_mat = Matrix(
            [[0, 1, 0], [1, 0, 0], [0, 0, 1]],
            h_buff=0.8, v_buff=0.6,
            element_to_mobject_config={"font_size": 28}
        )
        p_label = MathTex("P =", font_size=30)

        pt_mat = Matrix(
            [[0, 1, 0], [1, 0, 0], [0, 0, 1]],
            h_buff=0.8, v_buff=0.6,
            element_to_mobject_config={"font_size": 28}
        )
        pt_label = MathTex("P^T =", font_size=30)

        result_mat = Matrix(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            h_buff=0.8, v_buff=0.6,
            element_to_mobject_config={"font_size": 28}
        )
        eq_sign = MathTex("=", font_size=30)
        i_label = MathTex("= I", font_size=30)

        product_group = VGroup(
            p_label, p_mat,
            pt_label, pt_mat,
            eq_sign, result_mat, i_label
        ).arrange(RIGHT, buff=0.2)
        product_group.scale(0.7)
        product_group.center()

        self.play(Write(product_group), run_time=2)
        self.wait(1)

        check_text = MathTex(
            r"P^T P = I \implies P^{-1} = P^T \quad \checkmark",
            font_size=28, color=GREEN
        )
        check_text.shift(DOWN * 1.8)
        self.play(Write(check_text), run_time=1)
        self.wait(1.5)

        # PA = LU
        self.play(
            FadeOut(product_group), FadeOut(check_text), FadeOut(prop_title),
            run_time=0.5
        )

        palu_title = Text("The General Factorization", font_size=30, color=ORANGE)
        palu_title.shift(UP * 2)
        self.play(Write(palu_title), run_time=0.7)

        palu = MathTex(r"PA = LU", font_size=48, color=WHITE)
        palu.center()
        self.play(Write(palu), run_time=1)
        self.wait(0.5)

        palu_note = VGroup(
            Text("P = permutation matrix (row exchanges needed)", font_size=22, color=BLUE),
            Text("L = lower triangular (multipliers below diagonal)", font_size=22, color=GREEN),
            Text("U = upper triangular (pivot rows)", font_size=22, color=ORANGE),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        palu_note.shift(DOWN * 1.5)

        for note in palu_note:
            self.play(FadeIn(note), run_time=0.5)
        self.wait(2)

        self.play(FadeOut(title), FadeOut(palu_title), FadeOut(palu), FadeOut(palu_note), run_time=0.5)


class Lecture5_TransposeDefinition(Scene):
    """The transpose operation: rows <-> columns"""

    def construct(self):
        title = Text("The Transpose", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Definition
        defn = MathTex(
            r"(A^T)_{ij} = A_{ji}",
            font_size=36, color=WHITE
        )
        defn.shift(UP * 2.5)
        self.play(Write(defn), run_time=1)
        self.wait(0.6)

        note = Text("Rows become columns, columns become rows", font_size=22, color=GREY)
        note.next_to(defn, DOWN, buff=0.25)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(0.5)

        # Original matrix A with color-coded entries
        colors = [
            [RED, GREEN, BLUE],
            [ORANGE, PURPLE, TEAL],
            [PINK, GOLD, MAROON],
        ]
        a_vals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        at_vals = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        a_mat = Matrix(
            a_vals,
            h_buff=1.0, v_buff=0.8,
            element_to_mobject_config={"font_size": 32}
        )
        a_label = MathTex("A =", font_size=32)
        a_label.next_to(a_mat, LEFT, buff=0.2)

        a_group = VGroup(a_label, a_mat)
        a_group.shift(LEFT * 2.5 + DOWN * 0.5)

        # Color code entries of A
        for i in range(3):
            for j in range(3):
                a_mat.get_entries()[i * 3 + j].set_color(colors[i][j])

        self.play(FadeOut(note), Write(a_group), run_time=1.2)
        self.wait(0.5)

        # Transpose matrix
        at_mat = Matrix(
            at_vals,
            h_buff=1.0, v_buff=0.8,
            element_to_mobject_config={"font_size": 32}
        )
        at_label = MathTex("A^T =", font_size=32)
        at_label.next_to(at_mat, LEFT, buff=0.2)

        at_group = VGroup(at_label, at_mat)
        at_group.shift(RIGHT * 2.5 + DOWN * 0.5)

        # Color code entries of A^T (transposed colors)
        for i in range(3):
            for j in range(3):
                at_mat.get_entries()[i * 3 + j].set_color(colors[j][i])

        self.play(Write(at_group), run_time=1.2)
        self.wait(0.8)

        # Draw the diagonal reflection line
        diag_label = Text("reflect across diagonal", font_size=20, color=YELLOW)
        diag_label.shift(DOWN * 2.5)
        self.play(FadeIn(diag_label), run_time=0.5)

        # Animate: highlight matching entries (show the flip)
        # Highlight off-diagonal pair (0,1) and (1,0): entries 2 and 4
        rect1 = SurroundingRectangle(a_mat.get_entries()[1], color=YELLOW, buff=0.1)
        rect2 = SurroundingRectangle(a_mat.get_entries()[3], color=YELLOW, buff=0.1)
        rect1t = SurroundingRectangle(at_mat.get_entries()[3], color=YELLOW, buff=0.1)
        rect2t = SurroundingRectangle(at_mat.get_entries()[1], color=YELLOW, buff=0.1)

        swap_text = MathTex(
            r"A_{12} = 2 \leftrightarrow A^T_{21} = 2", font_size=24, color=YELLOW
        )
        swap_text.shift(DOWN * 3.2)

        self.play(
            Create(rect1), Create(rect2),
            Create(rect1t), Create(rect2t),
            FadeIn(swap_text),
            run_time=1
        )
        self.wait(1.5)

        self.play(
            FadeOut(rect1), FadeOut(rect2),
            FadeOut(rect1t), FadeOut(rect2t),
            FadeOut(swap_text), FadeOut(diag_label),
            run_time=0.5
        )

        # Diagonal entries stay the same
        diag_entries_a = [a_mat.get_entries()[0], a_mat.get_entries()[4], a_mat.get_entries()[8]]
        diag_entries_at = [at_mat.get_entries()[0], at_mat.get_entries()[4], at_mat.get_entries()[8]]
        diag_rects = VGroup(
            *[SurroundingRectangle(e, color=WHITE, buff=0.1) for e in diag_entries_a],
            *[SurroundingRectangle(e, color=WHITE, buff=0.1) for e in diag_entries_at],
        )
        diag_note = Text("Diagonal entries stay the same", font_size=22, color=WHITE)
        diag_note.shift(DOWN * 2.5)

        self.play(Create(diag_rects), FadeIn(diag_note), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(defn), FadeOut(a_group), FadeOut(at_group),
            FadeOut(diag_rects), FadeOut(diag_note),
            run_time=0.5
        )


class Lecture5_TransposeGridVisualization(Scene):
    """3B1B-style grid visualization comparing A and A^T"""

    def construct(self):
        title = Text("Visualizing A vs A^T", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # --- Left side: apply A ---
        left_plane = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.5},
        )
        left_plane.shift(LEFT * 3.5)

        # Basis vectors on left plane
        left_i = Arrow(
            left_plane.c2p(0, 0), left_plane.c2p(1, 0),
            buff=0, color=GREEN, stroke_width=3
        )
        left_j = Arrow(
            left_plane.c2p(0, 0), left_plane.c2p(0, 1),
            buff=0, color=RED, stroke_width=3
        )

        a_label = MathTex(
            r"A = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}",
            font_size=26, color=BLUE
        )
        a_label.next_to(left_plane, DOWN, buff=0.3)

        # --- Right side: apply A^T ---
        right_plane = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.5},
        )
        right_plane.shift(RIGHT * 3.5)

        right_i = Arrow(
            right_plane.c2p(0, 0), right_plane.c2p(1, 0),
            buff=0, color=GREEN, stroke_width=3
        )
        right_j = Arrow(
            right_plane.c2p(0, 0), right_plane.c2p(0, 1),
            buff=0, color=RED, stroke_width=3
        )

        at_label = MathTex(
            r"A^T = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix}",
            font_size=26, color=ORANGE
        )
        at_label.next_to(right_plane, DOWN, buff=0.3)

        # Show both planes
        self.play(
            Create(left_plane), Create(right_plane),
            run_time=1
        )
        self.play(
            Create(left_i), Create(left_j),
            Create(right_i), Create(right_j),
            FadeIn(a_label), FadeIn(at_label),
            run_time=1
        )
        self.wait(0.5)

        # Apply A to left plane
        a_matrix = [[2, 1], [0, 1]]
        at_matrix = [[2, 0], [1, 1]]

        self.play(
            ApplyMatrix(a_matrix, left_plane),
            ApplyMatrix(a_matrix, left_i),
            ApplyMatrix(a_matrix, left_j),
            ApplyMatrix(at_matrix, right_plane),
            ApplyMatrix(at_matrix, right_i),
            ApplyMatrix(at_matrix, right_j),
            run_time=3,
        )
        self.wait(1)

        # Determinant insight
        det_text = VGroup(
            MathTex(r"\det(A) = 2 \cdot 1 - 1 \cdot 0 = 2", font_size=24, color=BLUE),
            MathTex(r"\det(A^T) = 2 \cdot 1 - 0 \cdot 1 = 2", font_size=24, color=ORANGE),
        ).arrange(DOWN, buff=0.2)

        bg = BackgroundRectangle(det_text, fill_opacity=0.85, buff=0.15)
        det_group = VGroup(bg, det_text)
        det_group.to_edge(UP, buff=0.8)

        self.play(FadeIn(det_group), run_time=1)
        self.wait(0.5)

        insight = Text(
            "A and A^T always have the same determinant!",
            font_size=24, color=YELLOW
        )
        insight_bg = BackgroundRectangle(insight, fill_opacity=0.85, buff=0.15)
        insight_group = VGroup(insight_bg, insight)
        insight_group.next_to(det_group, DOWN, buff=0.2)

        self.play(FadeIn(insight_group), run_time=0.8)
        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(left_plane), FadeOut(right_plane),
            FadeOut(left_i), FadeOut(left_j),
            FadeOut(right_i), FadeOut(right_j),
            FadeOut(a_label), FadeOut(at_label),
            FadeOut(det_group), FadeOut(insight_group),
            run_time=0.5
        )


class Lecture5_SymmetricMatrices(Scene):
    """Symmetric matrices and A^T A is always symmetric"""

    def construct(self):
        title = Text("Symmetric Matrices: A = A^T", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # Example symmetric matrix
        s_label = MathTex("S =", font_size=32)
        s_mat = Matrix(
            [[2, 1], [1, 3]],
            h_buff=0.8, v_buff=0.6,
            element_to_mobject_config={"font_size": 30}
        )
        eq = MathTex("=", font_size=32)
        st_label = MathTex("S^T", font_size=32)

        sym_row = VGroup(s_label, s_mat, eq, st_label).arrange(RIGHT, buff=0.25)
        sym_row.shift(UP * 1.8)

        self.play(Write(sym_row), run_time=1.2)
        self.wait(0.5)

        note = Text("The matrix equals its own transpose", font_size=22, color=GREY)
        note.next_to(sym_row, DOWN, buff=0.25)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.8)

        # Highlight symmetry: color the off-diagonals the same
        entries = s_mat.get_entries()
        entries[1].set_color(GREEN)  # (0,1) = 1
        entries[2].set_color(GREEN)  # (1,0) = 1
        self.wait(0.5)

        self.play(FadeOut(sym_row), FadeOut(note), run_time=0.4)

        # A^T A is always symmetric
        ata_title = Text("A^T A is always symmetric", font_size=30, color=GREEN)
        ata_title.shift(UP * 2.2)
        self.play(Write(ata_title), run_time=0.8)

        # Proof
        proof_lines = VGroup(
            MathTex(r"\text{Is } (A^T A)^T = A^T A \text{ ?}", font_size=28, color=WHITE),
            MathTex(r"(A^T A)^T = A^T (A^T)^T", font_size=28, color=WHITE),
            MathTex(r"= A^T A \quad \checkmark", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        proof_lines.center().shift(DOWN * 0.2)

        for line in proof_lines:
            self.play(Write(line), run_time=1)
            self.wait(0.5)
        self.wait(0.8)

        # Rule used
        rule = MathTex(
            r"\text{Rule: } (AB)^T = B^T A^T",
            font_size=26, color=BLUE
        )
        rule.shift(DOWN * 2)
        self.play(FadeIn(rule), run_time=0.6)
        self.wait(0.5)

        # Importance note
        importance = Text(
            "This is key for least squares: the normal equations use A^T A",
            font_size=20, color=GREY
        )
        importance.shift(DOWN * 2.8)
        self.play(FadeIn(importance), run_time=0.6)
        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(ata_title), FadeOut(proof_lines),
            FadeOut(rule), FadeOut(importance),
            run_time=0.5
        )


class Lecture5_VectorSpaces(Scene):
    """Introduction to vector spaces and subspaces"""

    def construct(self):
        title = Text("Vector Spaces", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # R^2 as a plane
        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=6,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.scale(0.65)
        plane.shift(DOWN * 0.3)

        r2_label = MathTex(r"\mathbb{R}^2", font_size=36, color=BLUE)
        r2_label.next_to(plane, UP + RIGHT, buff=-0.5)
        r2_bg = BackgroundRectangle(r2_label, fill_opacity=0.8, buff=0.1)

        self.play(Create(plane), run_time=1)
        self.play(FadeIn(r2_bg), Write(r2_label), run_time=0.6)
        self.wait(0.5)

        # Rules
        rules_title = Text("Rules for a Vector Space:", font_size=24, color=WHITE)
        rules_title.to_edge(LEFT, buff=0.3).shift(UP * 2.5)

        rule1 = Text("1. Closed under addition: v + w in V", font_size=20, color=GREEN)
        rule2 = Text("2. Closed under scalar mult: cv in V", font_size=20, color=GREEN)
        rule3 = Text("3. Contains zero vector: 0 in V", font_size=20, color=GREEN)

        rules = VGroup(rules_title, rule1, rule2, rule3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rules.to_edge(LEFT, buff=0.3).shift(UP * 1.5)
        rules_bg = BackgroundRectangle(rules, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(rules_bg), FadeIn(rules), run_time=1)
        self.wait(1.5)

        self.play(FadeOut(rules_bg), FadeOut(rules), run_time=0.4)

        # Subspace example: line through origin
        sub_title = Text("Subspace: line through origin", font_size=24, color=GREEN)
        sub_title_bg = BackgroundRectangle(sub_title, fill_opacity=0.85, buff=0.1)
        sub_title_group = VGroup(sub_title_bg, sub_title)
        sub_title_group.to_edge(UP, buff=0.8)

        line_through = Line(
            plane.c2p(-3, -1.5), plane.c2p(3, 1.5),
            color=GREEN, stroke_width=4
        )

        v_arrow = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, color=GREEN_A, stroke_width=3
        )
        v_label = MathTex(r"\vec{v}", font_size=24, color=GREEN_A)
        v_label.next_to(v_arrow.get_end(), UP, buff=0.1)

        self.play(FadeIn(sub_title_group), run_time=0.5)
        self.play(Create(line_through), run_time=1)
        self.play(Create(v_arrow), FadeIn(v_label), run_time=0.7)
        self.wait(0.5)

        # Show scalar mult stays on line
        cv_arrow = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, -0.5),
            buff=0, color=YELLOW, stroke_width=3
        )
        cv_label = MathTex(r"-\tfrac{1}{2}\vec{v}", font_size=22, color=YELLOW)
        cv_label.next_to(cv_arrow.get_end(), DOWN, buff=0.1)

        self.play(Create(cv_arrow), FadeIn(cv_label), run_time=0.7)

        check1 = MathTex(r"\checkmark", font_size=32, color=GREEN)
        check1_bg = BackgroundRectangle(check1, fill_opacity=0.85, buff=0.1)
        check1_group = VGroup(check1_bg, check1)
        check1_group.next_to(sub_title_group, RIGHT, buff=0.3)
        self.play(FadeIn(check1_group), run_time=0.4)
        self.wait(1)

        self.play(
            FadeOut(line_through), FadeOut(v_arrow), FadeOut(v_label),
            FadeOut(cv_arrow), FadeOut(cv_label),
            FadeOut(sub_title_group), FadeOut(check1_group),
            run_time=0.5
        )

        # Counterexample: line NOT through origin
        bad_title = Text("NOT a subspace: line not through origin", font_size=24, color=RED)
        bad_title_bg = BackgroundRectangle(bad_title, fill_opacity=0.85, buff=0.1)
        bad_title_group = VGroup(bad_title_bg, bad_title)
        bad_title_group.to_edge(UP, buff=0.8)

        bad_line = Line(
            plane.c2p(-3, 0.5), plane.c2p(3, 2.5),
            color=RED, stroke_width=4
        )

        self.play(FadeIn(bad_title_group), run_time=0.5)
        self.play(Create(bad_line), run_time=1)
        self.wait(0.3)

        # The zero vector is at origin, which is NOT on this line
        zero_dot = Dot(plane.c2p(0, 0), color=YELLOW, radius=0.08)
        zero_label = MathTex(r"\vec{0}", font_size=24, color=YELLOW)
        zero_label.next_to(zero_dot, DOWN + LEFT, buff=0.1)
        zero_bg = BackgroundRectangle(zero_label, fill_opacity=0.85, buff=0.05)

        self.play(Create(zero_dot), FadeIn(zero_bg), FadeIn(zero_label), run_time=0.7)

        fail_text = Text("Zero vector is not on this line!", font_size=22, color=RED)
        fail_bg = BackgroundRectangle(fail_text, fill_opacity=0.85, buff=0.1)
        fail_group = VGroup(fail_bg, fail_text)
        fail_group.shift(DOWN * 2.5)
        self.play(FadeIn(fail_group), run_time=0.6)

        cross = MathTex(r"\times", font_size=36, color=RED)
        cross_bg = BackgroundRectangle(cross, fill_opacity=0.85, buff=0.1)
        cross_group = VGroup(cross_bg, cross)
        cross_group.next_to(bad_title_group, RIGHT, buff=0.3)
        self.play(FadeIn(cross_group), run_time=0.4)
        self.wait(2)

        self.play(
            FadeOut(plane), FadeOut(r2_bg), FadeOut(r2_label),
            FadeOut(bad_line), FadeOut(bad_title_group), FadeOut(cross_group),
            FadeOut(zero_dot), FadeOut(zero_bg), FadeOut(zero_label),
            FadeOut(fail_group), FadeOut(title),
            run_time=0.5
        )


class Lecture5_SubspaceExamples(Scene):
    """Subspaces of R^2: examples and counterexamples"""

    def construct(self):
        title = Text("Subspaces of R^2", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # We will show 4 examples in sequence
        # ─── Example 1: All of R^2 ───
        ex1_title = Text("1) All of R^2 — a subspace", font_size=26, color=GREEN)
        ex1_title.shift(UP * 2.5)
        self.play(Write(ex1_title), run_time=0.6)

        plane1 = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane1.scale(0.7)
        plane1.shift(DOWN * 0.3)

        # Shade the whole plane
        shaded = Rectangle(
            width=plane1.get_width(), height=plane1.get_height(),
            fill_color=GREEN, fill_opacity=0.15, stroke_width=0
        )
        shaded.move_to(plane1)

        self.play(Create(plane1), FadeIn(shaded), run_time=1)

        check = MathTex(r"\checkmark \text{ subspace}", font_size=24, color=GREEN)
        check_bg = BackgroundRectangle(check, fill_opacity=0.85, buff=0.1)
        check_group = VGroup(check_bg, check)
        check_group.shift(DOWN * 2.5)
        self.play(FadeIn(check_group), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(plane1), FadeOut(shaded), FadeOut(ex1_title), FadeOut(check_group),
            run_time=0.4
        )

        # ─── Example 2: Line through origin ───
        ex2_title = Text("2) Line through origin — a subspace", font_size=26, color=GREEN)
        ex2_title.shift(UP * 2.5)
        self.play(Write(ex2_title), run_time=0.6)

        plane2 = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane2.scale(0.7)
        plane2.shift(DOWN * 0.3)

        subspace_line = Line(
            plane2.c2p(-3, -2), plane2.c2p(3, 2),
            color=GREEN, stroke_width=4
        )
        origin_dot = Dot(plane2.c2p(0, 0), color=YELLOW, radius=0.06)

        self.play(Create(plane2), run_time=0.6)
        self.play(Create(subspace_line), Create(origin_dot), run_time=0.8)

        check2 = MathTex(r"\checkmark \text{ contains } \vec{0}\text{, closed under +, } c\vec{v}",
                         font_size=22, color=GREEN)
        check2_bg = BackgroundRectangle(check2, fill_opacity=0.85, buff=0.1)
        check2_group = VGroup(check2_bg, check2)
        check2_group.shift(DOWN * 2.5)
        self.play(FadeIn(check2_group), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(plane2), FadeOut(subspace_line), FadeOut(origin_dot),
            FadeOut(ex2_title), FadeOut(check2_group),
            run_time=0.4
        )

        # ─── Example 3: Just the origin ───
        ex3_title = Text("3) Just {0} — the smallest subspace", font_size=26, color=GREEN)
        ex3_title.shift(UP * 2.5)
        self.play(Write(ex3_title), run_time=0.6)

        plane3 = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane3.scale(0.7)
        plane3.shift(DOWN * 0.3)

        zero_dot = Dot(plane3.c2p(0, 0), color=GREEN, radius=0.12)
        zero_label = MathTex(r"\{\vec{0}\}", font_size=28, color=GREEN)
        zero_label.next_to(zero_dot, UP + RIGHT, buff=0.15)
        zero_lbl_bg = BackgroundRectangle(zero_label, fill_opacity=0.85, buff=0.05)

        self.play(Create(plane3), run_time=0.6)
        self.play(Create(zero_dot), FadeIn(zero_lbl_bg), FadeIn(zero_label), run_time=0.7)

        check3 = MathTex(r"\checkmark \text{ subspace (trivially)}", font_size=22, color=GREEN)
        check3_bg = BackgroundRectangle(check3, fill_opacity=0.85, buff=0.1)
        check3_group = VGroup(check3_bg, check3)
        check3_group.shift(DOWN * 2.5)
        self.play(FadeIn(check3_group), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(plane3), FadeOut(zero_dot), FadeOut(zero_lbl_bg), FadeOut(zero_label),
            FadeOut(ex3_title), FadeOut(check3_group),
            run_time=0.4
        )

        # ─── Example 4: Line NOT through origin ───
        ex4_title = Text("4) Line not through origin — NOT a subspace", font_size=26, color=RED)
        ex4_title.shift(UP * 2.5)
        self.play(Write(ex4_title), run_time=0.6)

        plane4 = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane4.scale(0.7)
        plane4.shift(DOWN * 0.3)

        bad_line = Line(
            plane4.c2p(-3, 0), plane4.c2p(3, 2),
            color=RED, stroke_width=4
        )

        self.play(Create(plane4), run_time=0.6)
        self.play(Create(bad_line), run_time=0.8)

        # Show two vectors on the line and their sum leaving the line
        v1_start = plane4.c2p(0, 1.0 / 3)
        v1_end = plane4.c2p(1, 2.0 / 3)
        v2_start = plane4.c2p(0, 1.0 / 3)
        v2_end = plane4.c2p(2, 4.0 / 3)

        # Actually let's pick two points on the line and show their vector sum
        # Line goes from (-3,0) to (3,2), so parametrically: y = (x+3)/3
        # Point A at x=0: y=1, point B at x=1: y=4/3
        # As vectors from origin: a=(0,1), b=(1, 4/3)
        # a + b = (1, 7/3) -- is this on the line? y=(x+3)/3 = 4/3 != 7/3. Not on line!

        a_arrow = Arrow(
            plane4.c2p(0, 0), plane4.c2p(0, 1),
            buff=0, color=BLUE, stroke_width=3
        )
        a_lbl = MathTex(r"\vec{a}", font_size=22, color=BLUE)
        a_lbl.next_to(a_arrow.get_end(), LEFT, buff=0.1)

        b_arrow = Arrow(
            plane4.c2p(0, 0), plane4.c2p(1, 4.0 / 3),
            buff=0, color=ORANGE, stroke_width=3
        )
        b_lbl = MathTex(r"\vec{b}", font_size=22, color=ORANGE)
        b_lbl.next_to(b_arrow.get_end(), RIGHT, buff=0.1)

        self.play(
            Create(a_arrow), FadeIn(a_lbl),
            Create(b_arrow), FadeIn(b_lbl),
            run_time=1
        )
        self.wait(0.5)

        # Sum
        sum_arrow = Arrow(
            plane4.c2p(0, 0), plane4.c2p(1, 7.0 / 3),
            buff=0, color=YELLOW, stroke_width=3
        )
        sum_lbl = MathTex(r"\vec{a}+\vec{b}", font_size=22, color=YELLOW)
        sum_lbl.next_to(sum_arrow.get_end(), RIGHT, buff=0.1)

        self.play(Create(sum_arrow), FadeIn(sum_lbl), run_time=1)

        fail_text = Text("a + b is NOT on the line!", font_size=22, color=RED)
        fail_bg = BackgroundRectangle(fail_text, fill_opacity=0.85, buff=0.1)
        fail_group = VGroup(fail_bg, fail_text)
        fail_group.shift(DOWN * 2.5)
        self.play(FadeIn(fail_group), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(plane4), FadeOut(bad_line),
            FadeOut(a_arrow), FadeOut(a_lbl),
            FadeOut(b_arrow), FadeOut(b_lbl),
            FadeOut(sum_arrow), FadeOut(sum_lbl),
            FadeOut(ex4_title), FadeOut(fail_group),
            run_time=0.4
        )

        # ─── Example 5: First quadrant ───
        ex5_title = Text("5) First quadrant — NOT a subspace", font_size=26, color=RED)
        ex5_title.shift(UP * 2.5)
        self.play(Write(ex5_title), run_time=0.6)

        plane5 = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane5.scale(0.7)
        plane5.shift(DOWN * 0.3)

        # Shade first quadrant
        quadrant = Polygon(
            plane5.c2p(0, 0), plane5.c2p(3, 0),
            plane5.c2p(3, 2.5), plane5.c2p(0, 2.5),
            fill_color=RED, fill_opacity=0.2, stroke_width=0
        )

        self.play(Create(plane5), FadeIn(quadrant), run_time=0.8)

        # Show a vector in Q1
        q_arrow = Arrow(
            plane5.c2p(0, 0), plane5.c2p(1, 1.5),
            buff=0, color=GREEN, stroke_width=3
        )
        q_lbl = MathTex(r"\vec{v}", font_size=22, color=GREEN)
        q_lbl.next_to(q_arrow.get_end(), RIGHT, buff=0.1)

        self.play(Create(q_arrow), FadeIn(q_lbl), run_time=0.7)
        self.wait(0.3)

        # Multiply by -1: leaves first quadrant
        neg_arrow = Arrow(
            plane5.c2p(0, 0), plane5.c2p(-1, -1.5),
            buff=0, color=YELLOW, stroke_width=3
        )
        neg_lbl = MathTex(r"-\vec{v}", font_size=22, color=YELLOW)
        neg_lbl.next_to(neg_arrow.get_end(), LEFT, buff=0.1)

        self.play(Create(neg_arrow), FadeIn(neg_lbl), run_time=0.8)

        fail5 = Text("(-1)v leaves the first quadrant!", font_size=22, color=RED)
        fail5_bg = BackgroundRectangle(fail5, fill_opacity=0.85, buff=0.1)
        fail5_group = VGroup(fail5_bg, fail5)
        fail5_group.shift(DOWN * 2.5)
        self.play(FadeIn(fail5_group), run_time=0.6)

        closed_note = Text(
            "Closed under addition, but NOT under scalar multiplication",
            font_size=18, color=GREY
        )
        closed_bg = BackgroundRectangle(closed_note, fill_opacity=0.85, buff=0.1)
        closed_group = VGroup(closed_bg, closed_note)
        closed_group.shift(DOWN * 3.1)
        self.play(FadeIn(closed_group), run_time=0.6)
        self.wait(2)

        # Final summary
        self.play(
            FadeOut(plane5), FadeOut(quadrant),
            FadeOut(q_arrow), FadeOut(q_lbl),
            FadeOut(neg_arrow), FadeOut(neg_lbl),
            FadeOut(ex5_title), FadeOut(fail5_group), FadeOut(closed_group),
            run_time=0.4
        )

        summary = VGroup(
            Text("Subspaces of R^2:", font_size=28, color=YELLOW),
            Text("  All of R^2", font_size=22, color=GREEN),
            Text("  Any line through the origin", font_size=22, color=GREEN),
            Text("  Just the zero vector {0}", font_size=22, color=GREEN),
            Text("NOT subspaces:", font_size=28, color=RED),
            Text("  Line not through origin (fails zero vector)", font_size=22, color=RED_B),
            Text("  First quadrant (fails scalar mult by -1)", font_size=22, color=RED_B),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        summary.center()

        self.play(FadeOut(title), run_time=0.3)
        for item in summary:
            self.play(FadeIn(item), run_time=0.4)
        self.wait(3)
