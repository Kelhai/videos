from manim import *

class OpeningManim(Scene):
    def construct(self):
        plot_axes = Axes(
            x_range=[0, 100, 0.05],
            y_range=[0, 100, 0.05],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": np.arange(0, 100, 10),
                "font_size": 12,
            },
            tips=False,
        )

        y_label = plot_axes.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = plot_axes.get_x_axis_label("x")
        plot_labels = VGroup(x_label, y_label)

        plots = VGroup()
        plots += plot_axes.plot(
            lambda x: 0.01 * (x**2), color=WHITE, use_smoothing=False
        )

        extras = VGroup()
        #extras += plot_axes.get_horizontal_line(plot_axes.c2p(1, 1, 0), color=BLUE)
        #extras += plot_axes.get_vertical_line(plot_axes.c2p(1, 1, 0), color=BLUE)
        #extras += Dot(point=plot_axes.c2p(1, 1, 0), color=YELLOW)
        title = Title(
            r"Graph of $y=x^2$",
            include_underline=False,
            font_size=40,
        )
        plot_axes.stroke_width = 0.01
        self.play(Write(title))
        self.play(Create(plot_axes)) #, Create(plot_labels)
        self.play(Create(plots[0]))