# [Valentine's Day Algorithmic Art Workshop](https://luma.com/22sxlnsx?tk=EC8Dwl)
<img align="right" src="https://github.com/user-attachments/assets/3521f856-6517-4e57-974e-47c833aefdfc" width="40%" />

A workshop for [Purdue Hackers](https://www.purduehackers.com/)! <br> <br>

> Roses are red, VSCode is blue... 💘 <br> <br>​
> Purdue Hackers is hosting a Valentine’s Day Algorithmic Art Workshop! <br> <br> You'll use code to generate heart-fluttering visuals and procedural patterns to create a digital Valentine's Day card with no prior experience required! <br> <br>
> ​By the end, you’ll leave with a digital valentine made of math and love \<3
> Join our Discord server: https://puhack.horse/discord !

## What's a workshop?

Workshops are our way to introduce folks to the magic of Purdue Hackers! Participants go through a short guided coding session, and then remix and hack their own modifications to make the project their own!
<!-- TODO: insert workshop page link once Notion CMS stuff is done -->

## Overview

This workshop covers implementing the algorithm by [József Fejes](http://codegolf.stackexchange.com/questions/22144/images-with-all-colors); I found it a few years ago while reading [Yuri Vishnevsky's beautiful blog post about making business cards with it](https://archive.yuri.is/cardcrafting/). The algorithm fills a canvas by:
1. Starting from a seed point.
2. Iterating through a shuffled list of colors.
3. For each color, placing it next to an already-placed color that is most similar.

Example output (run with four seeds in all four corners.)
<p align="center">
<img width="1280" height="640" alt="up-out" src="https://github.com/user-attachments/assets/809d1207-5e21-4615-9a51-04f8a4503bca" />
</p>

## Quick Start

Press `.` **on this Github page** to launch a [Github Codespace](https://github.com/features/codespaces) environment. The project has been tested to run on their default container image (which has Python pre-installed.)

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
