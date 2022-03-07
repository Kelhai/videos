from manim import *

class First(Scene):
    def construct(self):
        rect = Rectangle()
        self.wait()
        self.play(Create(rect))
        self.play(rect.animate.to_edge(DL))
        self.wait()

