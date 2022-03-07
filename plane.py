from manim import *

class Plain(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-28, 28, 4],
            y_range=[-16, 16, 4],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
            }, faded_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 8
            }, faded_line_ratio=1,
            x_length=7 * 3 / 2,
            y_length=4 * 3 / 2,
        ).add_coordinates()
        func = plane.plot(lambda x: 8 * np.sin(0.25 * x), [-28, 28], color=GOLD_D)
        matrix = [[1, 1], [0.3, -0.5]]
        inv = [[0.625, 1.25], [0.375, -1.25]]
        m_matrix = Matrix(matrix)
        group = VGroup(plane, func)
        self.play(Create(m_matrix))
        self.play(m_matrix.animate.to_corner(DL))
        self.play(Create(plane), run_time=2)
        self.play(Write(func), run_time=2)
        self.play(Uncreate(m_matrix))
        self.wait()

        
        self.wait(2)
        self.play(group.animate.apply_matrix(matrix))
        self.wait(2)
        self.play(group.animate.apply_matrix(inv))
        self.wait(1)
        self.play(group.animate.apply_complex_function(np.exp, run_time=5))
        self.play(group.animate.apply_complex_function(np.log, run_time=5))
        self.wait(2)
