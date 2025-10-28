from manim import *
import numpy as np

# Utility: draw a 1-D signal (returns a Line mobject)
def plot_signal(ax, x, y, color=BLUE):
    # Create pairs of (x, y) as Points in data space
    points = [ax.c2p(xi, yi) for xi, yi in zip(x, y)]
    graph = VMobject()
    graph.set_points_smoothly(points)
    graph.set_stroke(color=color, width=3)
    return graph

class ConvolutionIdea(Scene):
    def construct(self):
        # Axes setup
        ax = Axes(
            x_range=[-4, 8, 1],
            y_range=[-1, 2, 0.5],
            tips=False,
            axis_config={"include_numbers": False}
        ).to_edge(DOWN)
        self.add(ax)

        # Time axis
        x = np.linspace(-4, 8, 600)
        f = np.exp(-0.5 * ((x - 1) / 0.8) ** 2)             # "signal" f(t)
        h = (x >= 0) * (x <= 3) * (1 - np.abs(x - 1.5) / 1.5)  # triangular "impulse" h(t)

        f_graph = plot_signal(ax, x, f, color=YELLOW)
        h_graph = plot_signal(ax, x, h, color=BLUE)

        legend = VGroup(
            Tex("f(t)", color=YELLOW),
            Tex("h(t)", color=BLUE)
        ).arrange(RIGHT, buff=0.6).to_edge(UP)

        self.add(f_graph, h_graph, legend)

        # Define a tracker for time shift τ
        tau_tracker = ValueTracker(-2.0)

        def shifted_h_points():
            tau = tau_tracker.get_value()
            y_shifted = (x - tau >= 0) * (x - tau <= 3) * (1 - np.abs((x - tau) - 1.5) / 1.5)
            return plot_signal(ax, x, y_shifted, color=BLUE_E)

        h_shifted_graph = always_redraw(shifted_h_points)
        self.add(h_shifted_graph)

        # Animate the shift across f(t)
        self.play(tau_tracker.animate.set_value(5.0), run_time=6, rate_func=linear)
        self.wait()
