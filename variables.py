from manim import *

class Variables(Scene):
    def construct(self):
        eq1 = MathTex(r"{{a}}{{x}}^2 + {{b}}{{x}} + {{c}} = 0")
        eq2 = MathTex(r"{{x}}^2 + {{{b}} \over {{a}}}{{x}} + {{{c}} \over {{a}}} = \frac{0}{a}")
        eq3 = MathTex(r"{{x}}^2 + {{{b}} \over {{a}}}{{x}} = -{{{c}} \over {{a}}}")
        eq4 = MathTex(r"{{x}}^2 + {{{b}} \over {{a}}}{{x}} + ({{{b}} \over 2{{a}}})^2 = -{{{c}} \over {{a}}} +({{{b}} \over 2{{a}}})^2")
        eq5 = MathTex(r"({{x}} + {{{b}} \over 2{{a}}})^2 = -{{{c}} \over {{a}}} + {{{b}}^2 \over 4{{a}}^2}")
        eq6 = MathTex(r"({{x}} + {{{b}} \over 2{{a}}})^2 = {-4{{a}}{{c}} \over 4{{a}}^2} + {{{b}}^2 \over 4{{a}}^2}")
        eq7 = MathTex(r"{{x}} + {{{b}} \over 2{{a}}} = sqrt{{-4{{a}}{{c}} + {{b}}^2} \over 4{{a}}^2}")
        eqs = [eq1, eq2, eq3, eq4, eq5, eq6, eq7]
        self.wait()
        self.play(Write(eq1))
        self.wait()
        eqs[0].scale(2.0)
        for i in range(len(eqs) - 1):
            eqs[i + 1].scale(2.0)
            self.play(TransformMatchingTex(eqs[i], eqs[i + 1]))
            self.wait(2)
