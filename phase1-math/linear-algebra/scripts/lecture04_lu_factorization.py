"""
MIT 18.06 Linear Algebra — Lecture 4: Factorization into A = LU
Following Gilbert Strang's lecture content.

Scenes:
  1. Lecture4_EliminationToLU
  2. Lecture4_LUExample
  3. Lecture4_CostOfElimination
  4. Lecture4_PermutationMatrices

Manim Community Edition v0.20.1
Run:  manim -pql lecture04_lu_factorization.py <SceneName>
"""

from manim import *


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def matrix_tex(entries, label=None):
    """Return a MathTex string for a matrix given a 2-D list of strings."""
    rows = " \\\\ ".join(" & ".join(row) for row in entries)
    core = r"\begin{bmatrix} " + rows + r" \end{bmatrix}"
    if label:
        return MathTex(label + " = " + core)
    return MathTex(core)


def title_slide(self, text, wait=1.5):
    """Show a centred title then fade it up."""
    title = Text(text, font_size=42, weight=BOLD)
    self.play(Write(title))
    self.wait(wait)
    self.play(title.animate.scale(0.55).to_edge(UP))
    return title


# ===================================================================
# Scene 1 — From elimination to A = LU
# ===================================================================

class Lecture4_EliminationToLU(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 4: From Elimination to A = LU")

        # --- Step 1: elimination equation E_{32} E_{21} A = U ---
        eq1 = MathTex(
            r"E_{32}", r"E_{21}", r"A", r"=", r"U"
        ).scale(0.9).next_to(title, DOWN, buff=0.6)
        self.play(Write(eq1))
        self.wait(1)

        # --- Step 2: invert both sides ---
        eq2 = MathTex(
            r"A", r"=",
            r"E_{21}^{-1}", r"E_{32}^{-1}", r"U"
        ).scale(0.9).next_to(eq1, DOWN, buff=0.5)
        self.play(Write(eq2))
        self.wait(1)

        # --- Step 3: define L ---
        eq3 = MathTex(
            r"A", r"=", r"L", r"U"
        ).scale(0.9).next_to(eq2, DOWN, buff=0.5)
        brace = Brace(eq3[2], DOWN, buff=0.15)
        brace_text = brace.get_text(
            r"$L = E_{21}^{-1}\,E_{32}^{-1}$", buff=0.1
        ).scale(0.7)
        self.play(Write(eq3), GrowFromCenter(brace), Write(brace_text))
        self.wait(1.5)

        # --- Step 4: why L is nice — multipliers go straight in ---
        self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(brace), FadeOut(brace_text))

        explanation = VGroup(
            MathTex(
                r"E_{21} \text{ subtracts } \ell_{21} \times \text{row 1 from row 2}"
            ).scale(0.65),
            MathTex(
                r"E_{21}^{-1} \text{ adds it back: multiplier } \ell_{21} \text{ goes into } L"
            ).scale(0.65),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(eq3, DOWN, buff=0.6)
        for line in explanation:
            self.play(Write(line))
            self.wait(0.8)

        # 2x2 concrete mini-example
        example_title = Text("2×2 example", font_size=30).next_to(explanation, DOWN, buff=0.5)
        self.play(Write(example_title))

        e21 = MathTex(
            r"E_{21}=\begin{bmatrix}1&0\\-3&1\end{bmatrix}"
        ).scale(0.7)
        e21_inv = MathTex(
            r"E_{21}^{-1}=\begin{bmatrix}1&0\\3&1\end{bmatrix}"
        ).scale(0.7)
        pair = VGroup(e21, e21_inv).arrange(RIGHT, buff=0.8).next_to(example_title, DOWN, buff=0.4)
        self.play(Write(e21))
        self.wait(0.5)
        self.play(Write(e21_inv))
        self.wait(0.5)

        box = SurroundingRectangle(e21_inv, color=YELLOW, buff=0.1)
        note = MathTex(r"\text{Just flip the sign of the multiplier!}").scale(0.6).next_to(box, DOWN, buff=0.2)
        self.play(Create(box), Write(note))
        self.wait(2)


# ===================================================================
# Scene 2 — Concrete 3×3 LU factorization
# ===================================================================

class Lecture4_LUExample(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 4: 3×3 LU Factorization Example")

        # Matrix A
        A_label = MathTex(r"A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & -6 & 0 \\ -2 & 7 & 2 \end{bmatrix}").scale(0.75)
        A_label.next_to(title, DOWN, buff=0.4)
        self.play(Write(A_label))
        self.wait(1)

        # --- Step 1: eliminate (2,1) with multiplier l_{21}=2 ---
        step1 = MathTex(
            r"\ell_{21}=2: \; R_2 \leftarrow R_2 - 2R_1"
        ).scale(0.6).next_to(A_label, DOWN, buff=0.4)
        after1 = MathTex(
            r"\begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ -2 & 7 & 2 \end{bmatrix}"
        ).scale(0.7).next_to(step1, DOWN, buff=0.3)
        self.play(Write(step1))
        self.play(Write(after1))
        self.wait(0.8)

        # --- Step 2: eliminate (3,1) with multiplier l_{31}=-1 ---
        step2 = MathTex(
            r"\ell_{31}=-1: \; R_3 \leftarrow R_3 - (-1)R_1"
        ).scale(0.6).next_to(after1, DOWN, buff=0.3)
        after2 = MathTex(
            r"\begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 8 & 3 \end{bmatrix}"
        ).scale(0.7).next_to(step2, DOWN, buff=0.3)
        self.play(Write(step2))
        self.play(Write(after2))
        self.wait(0.8)

        # --- Step 3: eliminate (3,2) with multiplier l_{32}=-1 ---
        step3 = MathTex(
            r"\ell_{32}=-1: \; R_3 \leftarrow R_3 - (-1)R_2"
        ).scale(0.6).next_to(after2, DOWN, buff=0.3)
        U_mat = MathTex(
            r"U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 0 & 1 \end{bmatrix}"
        ).scale(0.7).next_to(step3, DOWN, buff=0.3)
        self.play(Write(step3))
        self.play(Write(U_mat))
        self.wait(1)

        # --- Clear and show L and verification ---
        self.play(*[FadeOut(m) for m in [A_label, step1, after1, step2, after2, step3, U_mat]])

        L_mat = MathTex(
            r"L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}"
        ).scale(0.75)
        U_mat2 = MathTex(
            r"U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 0 & 1 \end{bmatrix}"
        ).scale(0.75)
        result = VGroup(L_mat, U_mat2).arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.5)
        self.play(Write(L_mat), Write(U_mat2))
        self.wait(0.5)

        # Highlight multipliers in L
        note = MathTex(
            r"\text{Multipliers } \ell_{21}=2,\;\ell_{31}=-1,\;\ell_{32}=-1 "
            r"\text{ sit directly in } L"
        ).scale(0.55).next_to(result, DOWN, buff=0.5)
        self.play(Write(note))
        self.wait(1)

        verify = MathTex(r"A = L \, U \; \checkmark").scale(0.85).next_to(note, DOWN, buff=0.5)
        self.play(Write(verify))
        self.wait(2)


# ===================================================================
# Scene 3 — Cost of elimination: n³/3
# ===================================================================

class Lecture4_CostOfElimination(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 4: Cost of Elimination")

        # Build a visual picture of operations per pivot step
        desc1 = MathTex(
            r"\text{Column 1: operate on } (n-1) \text{ rows, } \sim n \text{ entries each}"
        ).scale(0.6)
        desc2 = MathTex(
            r"\text{Column 2: operate on } (n-2) \text{ rows, } \sim (n-1) \text{ entries}"
        ).scale(0.6)
        desc3 = MathTex(r"\vdots").scale(0.8)
        desc4 = MathTex(
            r"\text{Column } k: \;\sim (n-k)^2 \text{ operations}"
        ).scale(0.6)
        descs = VGroup(desc1, desc2, desc3, desc4).arrange(DOWN, buff=0.35).next_to(title, DOWN, buff=0.5)
        for d in descs:
            self.play(Write(d), run_time=0.7)
        self.wait(1)

        # Sum
        sum_eq = MathTex(
            r"\text{Total} \approx \sum_{k=1}^{n} k^2 \approx \frac{n^3}{3}"
        ).scale(0.8).next_to(descs, DOWN, buff=0.5)
        box = SurroundingRectangle(sum_eq, color=YELLOW, buff=0.15)
        self.play(Write(sum_eq), Create(box))
        self.wait(1)

        # Bar chart illustration
        self.play(FadeOut(descs))
        n = 6
        bars = VGroup()
        for k in range(1, n + 1):
            h = (n - k) ** 2 * 0.15 + 0.05
            bar = Rectangle(width=0.6, height=h, fill_opacity=0.7, fill_color=BLUE, stroke_width=1)
            bars.add(bar)
        bars.arrange(RIGHT, buff=0.15, aligned_edge=DOWN)
        bars.next_to(sum_eq, DOWN, buff=0.5)
        labels = VGroup()
        for k, bar in enumerate(bars, 1):
            lbl = MathTex(str(k), font_size=28).next_to(bar, DOWN, buff=0.1)
            labels.add(lbl)
        col_label = Text("pivot column k", font_size=24).next_to(labels, DOWN, buff=0.15)
        ops_label = Text("operations", font_size=24).rotate(PI / 2).next_to(bars, LEFT, buff=0.2)

        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.15),
            LaggedStart(*[Write(l) for l in labels], lag_ratio=0.15),
        )
        self.play(Write(col_label), Write(ops_label))
        self.wait(0.5)

        note = MathTex(
            r"\text{Not } n^3 \text{, but } \tfrac{n^3}{3} \text{ — the staircase shrinks!}"
        ).scale(0.6).next_to(col_label, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(2)


# ===================================================================
# Scene 4 — Permutation matrices and PA = LU
# ===================================================================

class Lecture4_PermutationMatrices(Scene):
    def construct(self):
        title = title_slide(self, "Lecture 4: Permutation Matrices")

        # All 3x3 permutation matrices
        perms = [
            ("I", [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            ("P_{12}", [[0, 1, 0], [1, 0, 0], [0, 0, 1]]),
            ("P_{13}", [[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
            ("P_{23}", [[1, 0, 0], [0, 0, 1], [0, 1, 0]]),
            ("P_{12}P_{23}", [[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
            ("P_{23}P_{12}", [[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
        ]

        mats = VGroup()
        for name, entries in perms:
            rows_str = " \\\\ ".join(" & ".join(str(e) for e in row) for row in entries)
            m = MathTex(
                name + r"=\begin{bmatrix}" + rows_str + r"\end{bmatrix}"
            ).scale(0.55)
            mats.add(m)
        mats.arrange_in_grid(rows=2, cols=3, buff=0.5).next_to(title, DOWN, buff=0.4)

        self.play(LaggedStart(*[Write(m) for m in mats], lag_ratio=0.2))
        self.wait(1.5)

        count_note = MathTex(
            r"n! = 3! = 6 \text{ permutation matrices for } 3\times3"
        ).scale(0.6).next_to(mats, DOWN, buff=0.4)
        self.play(Write(count_note))
        self.wait(1)

        # PA = LU
        self.play(FadeOut(mats), FadeOut(count_note))

        pa_lu = MathTex(r"P\,A = L\,U").scale(1.1).next_to(title, DOWN, buff=0.8)
        self.play(Write(pa_lu))
        self.wait(0.5)

        bullets = VGroup(
            MathTex(r"\text{When elimination needs row exchanges, } P \text{ records them}").scale(0.6),
            MathTex(r"\text{Choose } P \text{ so that } PA \text{ can be factored without row swaps}").scale(0.6),
            MathTex(r"\text{Every invertible } A \text{ has a } PA = LU \text{ factorization}").scale(0.6),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(pa_lu, DOWN, buff=0.6)

        for b in bullets:
            self.play(Write(b), run_time=0.8)
            self.wait(0.5)

        # Example needing permutation
        example = MathTex(
            r"A = \begin{bmatrix} 0 & 1 \\ 3 & 4 \end{bmatrix}"
            r"\;\;\Rightarrow\;\;"
            r"P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}"
        ).scale(0.7).next_to(bullets, DOWN, buff=0.5)
        note = MathTex(
            r"\text{Zero pivot } \Rightarrow \text{ must exchange rows}"
        ).scale(0.55).next_to(example, DOWN, buff=0.2)
        self.play(Write(example))
        self.play(Write(note))
        self.wait(2)
