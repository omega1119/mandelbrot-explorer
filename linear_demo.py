from manim import *

class LinearTransformDemo(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4,4,1], y_range=[-3,3,1],
                            background_line_style={"stroke_opacity":0.4})
        vec = Vector([1,2], color=YELLOW)
        label = MathTex(r"\vec{v}").next_to(vec.get_end(), UR, buff=0.2)
        self.add(plane, vec, label)

        # Transform matrix (shear + scale + rotation-ish)
        M = [[1.2, 0.6],
             [-0.4, 1.1]]

        self.play(ApplyMatrix(M, plane), run_time=2)
        self.play(ApplyMatrix(M, vec), run_time=2)
        self.wait()
