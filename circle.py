from manim import *

class Cir(Scene):
    def construct(self):
        val = ValueTracker(0)
        polar_plane = PolarPlane(
            azimuth_step=24,
            size=5, azimuth_label_font_size=36,
            radius_step=0.25, radius_max=1
        ).add_coordinates()

        func = polar_plane.plot_polar_graph(lambda x : 1, color=BLUE_E)

        hyp = always_redraw(
            lambda: Line(
                start=polar_plane.get_origin(),
                end=func.get_point_from_function(val.get_value()),
                color=RED_E
            )
        )

        sine_line = always_redraw(
            lambda: polar_plane.get_line_from_axis_to_point(
                0, func.get_point_from_function(val.get_value()),
            ).set_color(GREEN_D)
        )

        cosine_line = always_redraw(
            lambda: polar_plane.get_line_from_axis_to_point(
                1, func.get_point_from_function(val.get_value()),
            ).set_color(TEAL_E)
        )

        dot = always_redraw(
            lambda: Dot(color=GOLD_E).move_to(
                func.get_point_from_function(val.get_value())
            )
        )

        theta_value_text = (
            MathTex(r"\theta: ")
            .next_to(polar_plane, DOWN, buff=0.1)
            .set_color(WHITE)
        ).add_background_rectangle()
        theta_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=3, unit=r"\pi")
            .set_value(val.get_value() / PI)
            .next_to(theta_value_text, RIGHT, buff=0.1)
            .set_color(BLUE_C)
        ).add_background_rectangle()

        sine_value_text = (
            Tex("Sine: ")
            .next_to(theta_value, RIGHT, buff=1.0)
            .set_color(WHITE)
        ).add_background_rectangle()
        sine_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=3)
            .set_value(np.sin(val.get_value()))
            .next_to(sine_value_text, RIGHT, buff=0.1)
            .set_color(GREEN_D)
        )

        cos_value_text = (
            Tex("Cosine: ")
            .next_to(theta_value, LEFT * 2, buff=1.0)
            .set_color(WHITE)
        ).add_background_rectangle()
        cos_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=3)
            .set_value(np.sin(val.get_value()))
            .next_to(cos_value_text, RIGHT, buff=0.1)
            .set_color(TEAL_E)
        )

        self.add(
            polar_plane, func, hyp, cosine_line, 
            sine_line, theta_value, theta_value_text, 
            sine_value_text, sine_value, cos_value, 
            cos_value_text, dot
        )
        self.play(val.animate.set_value(PI * 2), run_time=15, rate_func=linear)
        self.play(val.animate.set_value(0), run_time=15, rate_func=linear)

        self.wait(2)