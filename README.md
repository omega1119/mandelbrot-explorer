# Mandelbrot Explorer & Manim Animations

A dual-purpose educational and visualization toolkit:
- **`mandelbrot_explorer.ipynb`** — an *interactive Jupyter notebook* for exploring and zooming into the Mandelbrot set with NumPy + Matplotlib.  
- **Manim scenes** (`mandel.py`, `linear_demo.py`, `convolution_demo.py`) — high-quality mathematical animations built using [Manim](https://github.com/ManimCommunity/manim).

---

## Installation

### Step 1: Create a dedicated environment
```bash
conda create -n my-manim-environment python=3.11
conda activate my-manim-environment
````

### Step 2: Install Manim and dependencies

Using conda-forge (preferred for stability):

```bash
conda install -c conda-forge manim
```

### Step 3 (Optional): Install additional requirements

If you have a `requirements.txt` for the notebook or extra packages:

```bash
pip install -r requirements.txt
```

### Step 4 (macOS only): Install LaTeX for math rendering

Manim uses LaTeX for `Tex` and `MathTex` objects:

> Download and install:
> [https://www.tug.org/mactex/mactex-download.html](https://www.tug.org/mactex/mactex-download.html)

---

## Project Overview

### 1. Mandelbrot Explorer (`mandelbrot_explorer.ipynb`)

An interactive Jupyter notebook featuring:

* Pure NumPy computation of the Mandelbrot set
* Click-to-zoom interface using Matplotlib event handling
* Adjustable iteration count and export to PNG
* Optional high-resolution renders for deep zooms

**Run it in Jupyter:**

```bash
jupyter notebook mandelbrot_explorer.ipynb
```

Then execute all cells top-to-bottom.
Controls:

| Action              | Key / Mouse              |
| ------------------- | ------------------------ |
| Zoom in             | Left click               |
| Zoom out            | Right click / Ctrl-click |
| Reset view          | `r`                      |
| Increase iterations | ↑                        |
| Decrease iterations | ↓                        |
| Save PNG            | `s`                      |

---

### 2. Manim Animations

Each of these scripts renders a standalone mathematical animation using Manim.

| File                  | Class                 | Description                                                                 |
| --------------------- | --------------------- | --------------------------------------------------------------------------- |
| `mandel.py`           | `MandelbrotZoom`      | Smooth zoom into the Mandelbrot set using NumPy rendering per frame         |
| `linear_demo.py`      | `LinearTransformDemo` | Linear algebra demo showing a vector and grid undergoing a matrix transform |
| `convolution_demo.py` | `ConvolutionIdea`     | DSP visualization showing a sliding convolution process over time           |

---

## Rendering Animations

Render a scene to **4K quality** (`-qk`) or **1080p preview** (`-pqh`):

```bash
# 4K renders
manim -qk mandel.py MandelbrotZoom
manim -qk linear_demo.py LinearTransformDemo
manim -qk convolution_demo.py ConvolutionIdea

# High-quality previews (opens player after render)
manim -pqh mandel.py MandelbrotZoom
manim -pqh linear_demo.py LinearTransformDemo
manim -pqh convolution_demo.py ConvolutionIdea
```

| Option | Meaning                   |
| ------ | ------------------------- |
| `-p`   | Auto-preview after render |
| `-qk`  | Ultra-high (4K)           |
| `-qh`  | High (1080p)              |
| `-qm`  | Medium (720p)             |
| `-ql`  | Low (fast preview)        |

**Output videos** are saved under:

```
media/videos/<script_name>/<quality>/<scene_name>.mp4
```

---

## Repository Structure

```
mandelbrot-explorer/
├── mandelbrot_explorer.ipynb        # Jupyter interactive explorer
├── mandel.py                        # Manim: Mandelbrot zoom animation
├── linear_demo.py                   # Manim: Linear algebra transformation demo
├── convolution_demo.py              # Manim: DSP convolution visualization
├── requirements.txt                 # Optional dependencies
└── README.md                        # (this file)
```

---

## Notes & Tips

* You can use `%matplotlib notebook` in Jupyter for a fully interactive Mandelbrot view.
* To speed up Mandelbrot rendering, reduce `max_iter` or image resolution.
* On macOS, if LaTeX fails for `MathTex`, ensure `/Library/TeX/texbin` is on your PATH.
* Manim supports direct exports to `.mp4`, `.mov`, `.gif`, and `.png` sequences.

---

## Future Enhancements

* Smooth (continuous) Mandelbrot coloring
* Julia set generation
* Animated zoom path and orbit traps
* Audio-reactive DSP animations (link with your JUCE plugins)
* RAG/AI integration for scene narration (text-to-speech + subtitles)
