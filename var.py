from manim import *
import numpy as np

class Var(Scene):
    def construct(self):
        text = Text("Fundamentals of Programming", font_size=48, should_center=True)

        self.play(Write(text))
        self.wait(duration=2)
        self.play(text.animate.to_edge(UP).scale(0.6), run_time=0.5)
        # variables
        # data types
        # data structures
        # control structures

        box1 = Square(side_length=2)
        box1.color = BLUE_E
        box2 = box1.copy()
        box2.color = GREEN_D
        box3 = box1.copy()
        box3.color = MAROON_E
        box4 = box1.copy()
        box4.color = LIGHT_PINK
        
        group = VGroup(box1, box2, box3, box4)
        group.arrange(buff=1.0)

        label1 = Text("Variables", font_size=24); label1.color = box1.color; label1.move_to(box1)
        label2 = Text("Data Types", font_size=24); label2.color = box2.color; label2.move_to(box2)
        label3 = Text("Data\nStructures", font_size=24); label3.color = box3.color; label3.move_to(box3)
        label4 = Text("Control\nStructures", font_size=24); label4.color = box4.color; label4.move_to(box4)
        label_group = Group(label1, label2, label3, label4)
        
        self.play(FadeIn(group, label_group))

        self.wait()

        arrow = Arrow()
        arrow.rotate_about_origin(PI / 2); arrow.color = GOLD_D; arrow.next_to(box1, DOWN)
        self.play(GrowArrow(arrow))
        self.wait(2)

        temp_box = Rectangle(height=8.5, width=14.5, color=BLUE_E)
        self.play(
            Uncreate(text), Uncreate(box2),
            Uncreate(box3), Uncreate(box4),
            Uncreate(label2), Uncreate(label3),
            Uncreate(label4), Uncreate(arrow)
        )
        self.play(Transform(box1, temp_box), label1.animate.move_to(ORIGIN).scale(7))
        self.wait(2)

        self.play(Unwrite(label1), run_time=2.0)

        consider_label = Tex(r"{{What is a variable}} in Math{{?}}", font_size=36)
        consider_label.to_edge(UP)
        sur_rect = SurroundingRectangle(consider_label, color=BLUE_D)

        self.play(Write(consider_label, run_time=0.7), Create(sur_rect, run_time=0.7))
        
        self.wait(2)

        # an unknown value
        eq1 = MathTex(r"{{x}} + {{5}} = {{9}}")
        eq2 = MathTex(r"{{x}} = {{9}} - {{5}}")
        eq3 = MathTex(r"{{x}} = 4")
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(3)
        self.play(Unwrite(eq3))
        # a variable can be many different things

        # a number that changes
        a = Axes(
            x_range=[-10, 10, 2],
            y_range=[-12, 12, 4],
            x_length=6,
            y_length=3,
            axis_config={
                "color": BLUE_A,
                "include_numbers": False,
                "include_ticks": True
            }, tips=False,
            y_axis_config={ "scaling": LinearBase(0.25) }
        )
        f = a.plot(lambda x : np.sin(x) * np.log(np.abs(x)), x_range=[-10, 10], use_smoothing=True).set_color(GREEN)

        a_labels = a.get_axis_labels(x_label="x", y_label="y").set_color(BLUE_D)

        self.play(Create(a), Create(a_labels))
        self.play(Create(f))
        self.wait(3)
        self.play(Uncreate(a), Uncreate(f), Uncreate(a_labels))

        self.wait()
        new_question = Tex(r"{{What is a variable}}{{?}}", font_size=36).to_edge(UP)
        new_rect = SurroundingRectangle(new_question, color=BLUE_D)

        self.play(TransformMatchingTex(consider_label, new_question), Transform(sur_rect, new_rect))
        self.wait(2)

        rect = Square(color=GREEN_E)
        cir = Circle(radius=0.5)
        cir.set_color(color=[BLUE_E, LIGHT_PINK])
        cir.set_fill(color=[BLUE_E, LIGHT_PINK], opacity=1.0)
        number_text = Tex("1, 2, 3, ...", font_size=24)
        rect2 = rect.copy()
        rect2.set_fill(color=GREEN_E, opacity=1.0)
        self.play(Create(rect))
        self.wait(4)
        self.play(DrawBorderThenFill(cir))
        self.wait()
        self.play(Uncreate(cir))
        self.play(DrawBorderThenFill(rect2))
        self.wait()
        self.play(Uncreate(rect2))
        self.play(Write(number_text))
        self.wait()
        self.play(Unwrite(number_text), Uncreate(rect))
        self.wait(3)

        
        self.wait()
        code_text = '''var x = 1\nx = 2\nvar y = 5\nvar z = x + y\nx = x * z'''
        code = Code(
            code=code_text, tab_width=4, background_stroke_color=WHITE,
            insert_line_no=True, style="monokai", language="swift", font="Consolas",
            background="window"
        )
        self.play(Write(code))
        self.play(code.animate.shift(ORIGIN + RIGHT * 3.5))
        boo1 = Square(side_length=1.0, color=GREEN_D)
        boo2 = boo1.copy()
        boo3 = boo1.copy()
        boo_group = VGroup(boo1, boo2, boo3)
        boo_group.arrange(DOWN).shift(ORIGIN + LEFT * 3.5)
        x_boo = Text("x", font_size=24).next_to(boo1, LEFT)
        y_boo = Text("y", font_size=24).next_to(boo2, LEFT)
        z_boo = Text("z", font_size=24).next_to(boo3, LEFT)
        self.play(Create(boo_group), Write(x_boo), Write(y_boo), Write(z_boo))
        self.wait(5)
        code_rect1 = SurroundingRectangle(code.code.chars[0])
        code_rect2 = SurroundingRectangle(code.code.chars[1])
        code_rect3 = SurroundingRectangle(code.code.chars[2])
        code_rect4 = SurroundingRectangle(code.code.chars[3])
        code_rect5 = SurroundingRectangle(code.code.chars[4])
        arrow1 = Arrow(start=boo1.get_right() + RIGHT, end=boo1.get_right(), color = RED)
        arrow2 = Arrow(start=boo2.get_right() + RIGHT, end=boo2.get_right(), color = RED)
        arrow3 = Arrow(start=boo3.get_right() + RIGHT, end=boo3.get_right(), color = RED)
        num_1 = Text("null", font_size=24, font="Mono").move_to(boo1)
        num_2 = Text("null", font_size=24, font="Mono").move_to(boo2)
        num_3 = Text("null", font_size=24, font="Mono").move_to(boo3)
        
        self.play(Write(num_1), Write(num_2), Write(num_3), GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3))
        self.wait(4)
        self.play(Create(code_rect1))
        self.wait(3)
        self.play(num_1.animate.become(Text("1", font_size=24, font="Mono").move_to(boo1)), Indicate(arrow1))
        self.wait(3)
        self.play(Transform(code_rect1, code_rect2))
        self.wait()
        self.play(num_1.animate.become(Text("2", font_size=24, font="Mono").move_to(boo1)), Indicate(arrow1))
        self.wait(3)
        self.play(Transform(code_rect1, code_rect3))
        self.play(num_2.animate.become(Text("5", font_size=24, font="Mono").move_to(boo2)), Indicate(arrow2))
        self.wait(3)
        self.play(Transform(code_rect1, code_rect4))
        self.wait()
        self.play(num_3.animate.become(Text("7", font_size=24, font="Mono").move_to(boo3)), Indicate(arrow3))
        self.wait(3)
        self.play(Transform(code_rect1, code_rect5))
        self.wait()
        self.play(num_1.animate.become(Text("14", font_size=24, font="Mono").move_to(boo1)), Indicate(arrow1))
        self.play(Uncreate(code_rect5))
        self.wait(3)

        self.play(Uncreate(boo2), Uncreate(boo3), Uncreate(num_2), Uncreate(num_3))
