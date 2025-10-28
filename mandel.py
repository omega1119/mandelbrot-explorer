from manim import *
import numpy as np
import matplotlib.cm as cm

def mandelbrot_counts(xmin, xmax, ymin, ymax, w, h, max_iter=300, R=2.0):
    xs = np.linspace(xmin, xmax, w, dtype=np.float64)
    ys = np.linspace(ymin, ymax, h, dtype=np.float64)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j*Y
    Z = np.zeros_like(C, dtype=np.complex128)
    counts = np.zeros(C.shape, dtype=np.int32)
    mask = np.ones(C.shape, dtype=bool)
    for i in range(max_iter):
        Z[mask] = Z[mask]*Z[mask] + C[mask]
        escaped = np.abs(Z) > R
        newly_escaped = escaped & mask
        counts[newly_escaped] = i
        mask &= ~newly_escaped
        if not mask.any():
            break
    counts[mask] = max_iter
    return counts

def colorize(counts, max_iter=300, cmap_name="turbo"):
    # normalize to [0,1], map to RGB
    norm = np.clip(counts / max_iter, 0, 1)
    rgb = cm.get_cmap(cmap_name)(norm)[..., :3]  # drop alpha
    return (rgb * 255).astype(np.uint8)

class MandelbrotZoom(Scene):
    def construct(self):
        # Scene settings
        W, H = 640, 360   # render resolution for the fractal image
        max_iter = 600

        # Initial and target views
        xmin0, xmax0, ymin0, ymax0 = -2.5, 1.0, -1.25, 1.25
        # A classic minibrot target near Seahorse Valley:
        xmin1, xmax1 = -0.74877 - 0.001, -0.74877 + 0.001
        ymin1, ymax1 =  0.06505 - 0.0006,  0.06505 + 0.0006

        # A ValueTracker t ∈ [0,1] to lerp bounds over time
        t = ValueTracker(0.0)

        def lerp(a, b, t):
            return a*(1-t) + b*t

        def make_frame():
            tt = t.get_value()
            xmin = lerp(xmin0, xmin1, tt)
            xmax = lerp(xmax0, xmax1, tt)
            ymin = lerp(ymin0, ymin1, tt)
            ymax = lerp(ymax0, ymax1, tt)

            counts = mandelbrot_counts(xmin, xmax, ymin, ymax, W, H, max_iter=max_iter)
            img = colorize(counts, max_iter=max_iter, cmap_name="turbo")
            mobj = ImageMobject(img)
            # Fit to frame width while keeping aspect
            mobj.set_width(config.frame_width)
            return mobj

        image = always_redraw(make_frame)
        title = Tex(r"Mandelbrot Zoom").to_edge(UP)

        self.add(image, title)
        self.play(t.animate.set_value(1.0), run_time=6, rate_func=smooth)
        self.wait(0.5)
