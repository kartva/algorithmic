## Overview

The **Rainbow Smoke Algorithm** fills a canvas by:
1. Starting from a seed point.
2. Iterating through a shuffled list of colors.
3. For each color, placing it next to an already-placed color that is most similar.

## Quick Start

### Dependencies

- Python 3.10+
- NumPy
- Pillow
- Flask (for web preview)

### Usage

```bash
python cli.py --rgb
python cli.py --image in/water_lilies_monet.jpg -o result.png
```

### Web Preview

```bash
python web_preview.py
```

Then open http://localhost:5000 in your browser.

## Command-line Options

| Option | Description |
|--------|-------------|
| `--rgb` | Generate uniform RGB cube (256×128) |
| `--image PATH` | Load colors from image |
| `-o, --output FILE` | Output filename (default: output.png) |
