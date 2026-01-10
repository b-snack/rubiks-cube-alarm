# Rubik's Cube Alarm Clock

An alarm clock that only turns off when you solve a Rubik's Cube! Built with Raspberry Pi and OpenCV computer vision.

This is my first time making something like this, so I'm putting this here:

## SUPPORT

For questions, issues, or suggestions:

- Open an issue on GitHub
- Check the Troubleshooting section above
- Contact me at swuott2009@gmail.com

Anyways,

## What It Does

This alarm clock goes off at 7:30 AM and wont stop until you show a solved Rubik's Cube to the camera

Perfect for people who need an extra push to get out of bed in the morning!

---

## 🛠️ Hardware Requirements

### Required Components:

- Raspberry Pi (tested on Pi 3)
- USB Webcam or Raspberry Pi Camera Module
- Speaker (USB speaker, HDMI audio, or 3.5mm audio jack)
- **Rubik's Cube** (MUST be **STICKERLESS** - colored plastic, not stickers) - e.g. https://speedcubeshop.com/products/yuxin-little-magic-3x3
- Power supply for Raspberry Pi
- MicroSD card (16GB+) with Raspberry Pi OS installed - tested on a 32GB

### Why Stickerless?

The color detection algorithm works best with stickerless cubes (solid colored plastic) because
it detects each face and searches for a large quadrilateral shape on each face, and not individual
pieces. A rubik's brand or stickered cube will not work, as it splits the large quadrilateral per face
into smaller squares, hence rendering the code invalid.

---

## Camera Angle

The camera should be slightly slanted and pointing at the cube from above, where it captures three faces of the
cube (non white side) at roughly even areas. Should be adequately far such that the code can detect at least 5000
pixels, and that there are three large quadrilateral shapes (after applying the mask)

---

## TO INSTALL (do so on the pi)

### 1. Clone the Repository

#### Run:

```bash
cd ~
git clone https://github.com/yourusername/rubiks-cube-alarm.git
cd rubiks-cube-alarm
```

### 2, Install System Dependencies

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install OpenCV and dependencies
sudo apt install python3-opencv python3-pip vlc -y
```

### 3. Install Python Packages

```bash
pip3 install numpy matplotlib pygame --break-system-packages
```

Or use a virtual environment (recommended):

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install opencv-python numpy matplotlib pygame
```

### 4. Add Your Alarm Sound (if not pleased with provided one)

Place your alarm audio file in the `media/` folder:

```bash
mkdir -p media
```

Name it alarm.mp3.

Supported formats: MP3, WAV, OGG

---

## TO USE

### Run the Alarm Clock

```bash
python3 main.py
```

In the terminal of the raspberry pi.

The program will:

1. Wait until 7:30 AM
2. Play the alarm sound on loop
3. Take photos every 5 seconds to check for cube
4. Wait for you to show a Rubik's Cube (3 visible faces)
5. Keep playing until you solve at least 3 faces
6. Stop the alarm when solved

### Stop the Program

Press `Ctrl+C` in the terminal.

---

## Configuration

### Change Alarm Time

Edit `main.py`:

```python
if now.hour == 7 and now.minute == 30:
    play_alarm()
```

Change now.hour to the desired hour, and similarly for the desired minute.

E.g. for it to go off at 6:00 AM:

```python
if now.hour == 6 and now.minute == 0:
```

### Adjust Photo Interval

Edit `main.py`:

```python
while not is_there(photo()):
    time.sleep(5)

while is_solved(photo()) != True:
    time.sleep(5)
```

Change the value of **5** in time.sleep(5) to the amount of seconds.

**Note**: Lower values = faster detection, but results in more CPU usage. Raspberry Pi may struggle with values below 3 seconds.

### Adjusting detection sensitivity

Edit `detection.py`:

```python
# Change minimum area for face detection
if cv.contourArea(largest) > 5000:  # Lower number = more sensitive

# Change color threshold
threshold = 500  # in is_there() function - lower = more sensitive
```

### Adjust Color Ranges (if colors aren't detected)

Edit `COLOR_INFO` in `detection.py`:

```python
COLOR_INFO = {
  'blue': (np.array([100,150,0]), np.array([140,255,255])),
  'green': (np.array([40,50,50]), np.array([80,255,255])),
  'orange': (np.array([12, 150, 100]), np.array([18, 255, 255])),
  'yellow': (np.array([22,100,100]), np.array([38,255,255])),
  'red': (None, None)  # Red uses special handling for upper and lower
}
```

Values are in HSV format.

---

## Logic behind detection

### Color Detection

The program uses the HSV (Hue, Saturation, Value) color space to detect colors of the cube:

- Blue, Green, Orange, Yellow means a Single HSV range
- Red: Two HSV ranges (wraps around 0°/180° in Hue)
- White: Not detected due to possible complications that could arise w/ a white bg

### Cube Recognition

1. Converts image to HSV color space
2. Creates color masks for each cube color
3. Applies morphological operations (opening/closing) to reduce noise
4. Finds contours (shapes) in each color mask
5. Checks if contour is large enough and quadrilateral shaped
6. Counts how many valid faces are detected

### Solving Logic

A face is considered "solved" when:

- At least 5000 pixels of that color detected
- The shape is a quadrilateral (4 corners)
- At least 85% of the quadrilateral is one uniform detected color.

The alarm stops when:

- At least 3 faces are solved
- Opposite face pairs aren't both "solved" (blue/green, red/orange can't both be detected at once)

### Supported Cube Colors

- ✅ Blue
- ✅ Green
- ✅ Orange
- ✅ Yellow
- ✅ Red
- ❌ White (not detected due to issues with lighting & bg that could emerge)

---

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

This project is open source and available under the MIT License.

---

## Resources

- [OpenCV Morphological Operations](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)
- [Color Detection with OpenCV](https://www.youtube.com/watch?v=oXlwWbU8l2o)
- [Quadrilateral Detection Tutorial](https://nhuvan.github.io/blog/005-quadrilateral/)
- Other sources

---

**Happy Cubing!**
