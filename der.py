from manim import *

class Der(Scene):
    def construct(self):
        k = ValueTracker(-4)

        plane1 = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-1.2, 1.2, 1], y_length=5, x_length=5
        ).add_coordinates().to_edge(LEFT)

        func1 = plane1.plot(lambda x: np.sin(x), x_range=[-4, 4], color=RED_E)
        func1_lab = (
            MathTex(r"f(x) = sin(x)")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_E)
        )
        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=GREEN_B
            )
        )

        dot = always_redraw(
            lambda: Dot(color=GOLD_E).move_to(
                func1.get_point_from_function(k.get_value())
            )
        )

        plane2 = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-1.2, 1.2, 1], y_length=5, x_length=5
        ).add_coordinates().to_edge(RIGHT)

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x : np.cos(x), x_range=[-4, k.get_value()], color=GOLD_E
            )
        )
        func2_lab = (
            MathTex(r"f'(x) = cos(x)")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GOLD_E)
        )

        moving_h_line = always_redraw(
            lambda: plane2.get_horizontal_line(func2.get_point_from_function(k.get_value()), color=YELLOW)
        )
        
        slope_value_text = (
            Tex("Slope Value: ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(GOLD_E)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=3)
            .set_value(plane2.input_to_graph_coords(k.get_value(), graph=func2)[1])
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(GOLD_E)
        ).add_background_rectangle()

        dot2 = always_redraw(
            lambda: Dot(color=GOLD_E).move_to(
                func2.get_point_from_function(k.get_value())
            )
        )

        self.play(
            DrawBorderThenFill(plane1),
            DrawBorderThenFill(plane2),
            Create(func1),
            Write(func1_lab),
            Write(func2_lab),
            run_time=5,
            lag_ratio=0.5
        )
        self.add(moving_slope, moving_h_line, dot, func2, slope_value, slope_value_text, dot2)
        self.play(k.animate.set_value(4), run_time=15, rate_func=linear)
        self.wait()
