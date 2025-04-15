# 🖌️ Erase Canvas - Python Tkinter App 🎨

This repository contains a GUI-based **Eraser Canvas Application** built with **Tkinter**. It allows users to interactively erase parts of a grid using a draggable eraser. A great starting project to understand **canvas manipulation**, **event handling**, and **GUI development** in Python. 🚀

---

## 📌 Project Overview

A grid-based 400x400 pixel canvas is created using Tkinter. Each grid cell is initially filled with blue color. A draggable **pink eraser** allows users to erase cells (i.e., change their color to white) as it moves across the canvas.

---

## 🔹 Features & Functionalities

### 🎨 Canvas with Grid Cells
- 400x400 px canvas divided into 40x40 px blue-colored cells
- Efficient cell tracking using a dictionary

### 🖱️ Mouse-controlled Eraser
- Pink eraser (20x20 px) follows the mouse
- Erases (changes color) as it moves over cells while dragging

### 🛠️ Event Handling
- `<B1-Motion>` event captures dragging motion
- Real-time eraser tracking and cell color updates

### 🎯 Customizable Settings
- Easily change canvas size, cell size, eraser size, and colors

---

## 🏗️ Project Structure

Project-4-Assignments/ └── Assignments 00 to 05/ └── 02_lists/ └── 03_erase_canvas/ └── main.py


- `main.py`: Contains the full Tkinter app (canvas setup, eraser logic, and event handling)

---

## 🛠️ How It Works

1️⃣ **Initialize Tkinter Window**  
- Set up a canvas (400x400) with blue-filled cells  
- Cells stored in a dictionary

2️⃣ **Draw the Grid**  
- Loop to draw 40x40 px squares across canvas

3️⃣ **Create an Eraser**  
- A pink 20x20 px square positioned at the top-left

4️⃣ **Event Binding**  
- `<B1-Motion>` tracks mouse drag to move eraser  
- Eraser follows cursor coordinates

5️⃣ **Erase Cells**  
- Detects and updates overlapping cells to white

6️⃣ **Run App**  
- Launches Tkinter window and main loop

---

## ▶️ How to Run the Project

### 🔧 Prerequisites

- Python 3.x  
- Tkinter (pre-installed with Python)

### 🏃 Run the Application

```bash
python main.py

This opens the Eraser Canvas window. Drag the eraser to erase grid cells!


⚙️ Customization Options

Setting | Description | Default
CANVAS_WIDTH | Width of canvas | 400 px
CANVAS_HEIGHT | Height of canvas | 400 px
CELL_SIZE | Size of each grid cell | 40 px
ERASER_SIZE | Size of the eraser | 20 px
fill="blue" | Initial color of grid cells | Blue
fill="pink" | Eraser color | Pink
bg="white" | Canvas background color | White

📌 Learning Outcomes
✅ GUI Programming with Tkinter
✅ Real-time Mouse Event Handling
✅ Canvas Drawing Techniques
✅ Dictionary-based Cell Tracking


📜 Future Enhancements
🚀 Dynamically adjustable eraser size
🚀 Add a "Reset Canvas" button
🚀 Support for multiple brush/eraser types


🎯 Final Thoughts
This Eraser Canvas App is a fun and educational Python GUI project. It’s perfect for beginners learning how to work with Tkinter, canvas drawing, and event-driven programming. 🐍💡
