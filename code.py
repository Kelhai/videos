from manim import *

class CodeTest(Scene):
    def construct(self):
        eq1 = MathTex(r"{{a}}{{x}}^2 + {{b}}{{x}} + {{c}} = 0")
        eq2 = MathTex(r"{{a}}{{x}}^2 + {{{b}} \over a} {{x}} + {{{c}} \over a} = 0")
        eq3 = MathTex(r"{{a}}({{x}}^2 + {{{b}} \over a} {{x}}) = -{{{c}} \over a}")

        

        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2, eq3))

