import io
import base64
import threading

from flask import Flask, render_template, jsonify, request
from PIL import Image
import numpy as np

from lib.colors import generate_rgb_colors
from algorithm import run_algorithm

app = Flask(__name__, template_folder="templates")

state = {
    "pixels": None,
    "iteration": 0,
    "total": 0,
    "running": False,
    "lock": threading.Lock(),
}


def web_progress(iteration: int, total: int, pixels) -> None:
    """Progress callback for web preview - updates shared state."""
    with state["lock"]:
        state["iteration"] = iteration
        state["total"] = total
        state["pixels"] = pixels.copy()


def run_in_background(colors_list: list, width: int, height: int):
    """Run the algorithm in a background thread."""
    state["running"] = True
    state["iteration"] = 0
    state["total"] = len(colors_list)
    state["pixels"] = np.zeros((height, width, 3), dtype=np.int32)

    run_algorithm(colors_list, width, height, on_progress=web_progress)

    state["running"] = False


def get_image_base64() -> str:
    """Get current canvas as base64 PNG."""
    with state["lock"]:
        if state["pixels"] is None:
            return ""
        img_array = state["pixels"].astype(np.uint8)
    img = Image.fromarray(img_array)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


@app.route("/")
def index():
    return render_template("preview.html")


@app.route("/api/init", methods=["POST"])
def api_init():
    if state["running"]:
        return jsonify({"status": "already_running"})

    width, height = 256, 128
    colors = generate_rgb_colors(width, height)

    thread = threading.Thread(target=run_in_background, args=(colors, width, height))
    thread.daemon = True
    thread.start()

    return jsonify({"status": "ok"})


@app.route("/api/frame")
def api_frame():
    with state["lock"]:
        total = state["total"]
        iteration = state["iteration"]

    return jsonify({
        "image": get_image_base64(),
        "iteration": iteration,
        "total": total,
        "progress": iteration / total if total > 0 else 0,
        "running": state["running"],
    })


if __name__ == "__main__":
    print("Starting web preview at http://localhost:5000")
    print("Click 'Reset' in the browser to start the algorithm")
    app.run(debug=False, port=5000)
