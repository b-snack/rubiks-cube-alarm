# Rubik's Cube Alarm Clock

An alarm clock that only turns off when you solve a Rubik's Cube! Built with Raspberry Pi and OpenCV computer vision.

## What It Does

This alarm clock goes off at 7:30 AM and **won't stop** until you:

1. Show a Rubik's Cube to the camera
2. Solve at least 3 faces of the cube

Perfect for people who need an extra push to get out of bed in the morning!

---

## 🛠️ Hardware Requirements

### Required Components:

- **Raspberry Pi** (tested on Pi 3/4/5)
- **USB Webcam** or **Raspberry Pi Camera Module**
- **Speaker** (USB speaker, HDMI audio, or 3.5mm audio jack)
- **Rubik's Cube** (MUST be **stickerless** - colored plastic, not stickers)
- **Power supply** for Raspberry Pi
- **MicroSD card** (16GB+) with Raspberry Pi OS installed

### Why Stickerless?

The color detection algorithm works best with **stickerless cubes** (solid colored plastic) because:

- Consistent color under different lighting
- No wear/fading like stickers
- Better HSV color range detection

---

## 📷 Camera Setup

### Camera Positioning:

The camera should capture **three faces at once** from a corner angle - All edges should meet at the centre at 120 degree angles.

```
        TOP FACE
           ↓
         ┌───┐
         │ Y │
    ┌────┼───┼────┐
    │ B  │ R │  G │  ← FRONT & SIDE FACES
    └────┼───┼────┘
         │ W │
         └───┘

    [Camera] ← Position here
       ↗
     /
   45° angle from corner
```

### Optimal Camera Setup:

1. **Distance**: 8-15 inches from the cube
2. **Angle**: Position camera to see corner of cube (capturing 3 faces simultaneously)
3. **Height**: Slightly above cube level, angled down
4. **Lighting**: Good, even lighting - avoid shadows or direct sunlight
5. **Background**: Plain, non-colorful background works best

### Correct vs Incorrect Camera Angles:

```
✓ GOOD - Corner View (3 faces visible)

         [Camera]
            ↘
             ↘ 45°
              ↘
                [Cube]
       (3 faces visible)


✗ BAD - Front View (1 face only)

         [Camera]
            |
            ↓
          [Cube]
       (only 1 face)
```

**Pro Tip**: Hold the cube so you can see the top face, front face, and one side face all at once. This is the view the camera needs!

---

## 💾 Software Installation

### Step 1: Clone the Repository

```bash
cd ~
git clone https://github.com/yourusername/rubiks-cube-alarm.git
cd rubiks-cube-alarm
```

Or download and extract the ZIP file to your Raspberry Pi.

### Step 2: Install System Dependencies

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install OpenCV and dependencies
sudo apt install python3-opencv python3-pip vlc -y
```

### Step 3: Install Python Packages

```bash
pip3 install numpy matplotlib pygame --break-system-packages
```

Or use a virtual environment (recommended):

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install opencv-python numpy matplotlib pygame
```

### Step 4: Add Your Alarm Sound (if not pleased with provided one)

Place your alarm audio file in the `media/` folder:

```bash
mkdir -p media
```

Name it alarm.mp3.

Supported formats: MP3, WAV, OGG

---

## 🚀 Usage

### Test Components First

**Test the camera:**

```bash
python3 capture.py
```

This should capture a photo from your camera.

**Test cube detection:**

```bash
python3 detection.py
```

Make sure your cube is detected and faces are identified correctly. You should see output like:

```
4 corners found
[side color 1] face solved
[side color 2] face solved
[top color] solved
(not necessarily in that order)
3 True
```

### Run the Alarm Clock

```bash
python3 main.py
```

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

## ⚙️ Configuration

### Change Alarm Time

Edit `main.py`:

```python
if now.hour == 7 and now.minute == 30:  # Change these values
    play_alarm()
```

Example for 6:00 AM:

```python
if now.hour == 6 and now.minute == 0:
```

### Adjust Photo Interval

Edit `main.py`:

```python
while not is_there(photo()):
    time.sleep(5)  # Change from 5 to desired seconds

while is_solved(photo()) != True:
    time.sleep(5)  # Change from 5 to desired seconds
```

**Note**: Lower values = faster detection but more CPU usage. Raspberry Pi may struggle with values below 3 seconds.

### Adjust Detection Sensitivity

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
  'red': (None, None)  # Red uses special handling
}
```

Values are in HSV format: `[Hue, Saturation, Value]`

---

## 🔧 Autostart on Boot (Optional)

To make the alarm run automatically when your Pi starts:

### Step 1: Create Service File

```bash
sudo nano /etc/systemd/system/rubiks-alarm.service
```

### Step 2: Add This Content

```ini
[Unit]
Description=Rubiks Cube Alarm Clock
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/rubiks-cube-alarm/main.py
WorkingDirectory=/home/pi/rubiks-cube-alarm
User=pi
Restart=always

[Install]
WantedBy=multi-user.target
```

**Note**: Adjust the path if your project is in a different location.

### Step 3: Enable and Start

```bash
sudo systemctl enable rubiks-alarm.service
sudo systemctl start rubiks-alarm.service
```

### Step 4: Check Status

```bash
sudo systemctl status rubiks-alarm.service
```

### Step 5: View Logs (if troubleshooting)

```bash
journalctl -u rubiks-alarm.service -f
```

### To Stop/Disable Autostart:

```bash
sudo systemctl stop rubiks-alarm.service
sudo systemctl disable rubiks-alarm.service
```

---

## 📁 Project Structure

```
rubiks-cube-alarm/
├── main.py              # Main alarm logic and scheduler
├── detection.py         # Cube detection and solving verification
├── capture.py           # Camera interface
├── alarm.py             # Audio playback control
├── media/
│   └── alarm.mp3        # Your alarm sound
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

---

## 🐛 Troubleshooting

### Camera Not Working

**Check if camera is detected:**

```bash
# For USB webcam
ls /dev/video*

# For Pi Camera Module
vcgencmd get_camera
```

**Test camera:**

```bash
# For Pi Camera Module
raspistill -o test.jpg

# For USB webcam
fswebcam test.jpg
```

**Fix permissions:**

```bash
sudo usermod -a -G video $USER
# Log out and back in for changes to take effect
```

**Enable Pi Camera in config:**

```bash
sudo raspi-config
# Navigate to: Interface Options > Camera > Enable
sudo reboot
```

### Cube Not Detected

**Issue**: Program says cube isn't there or isn't a quadrilateral

**Solutions**:

- Ensure you're using a **stickerless cube** (not stickers). A normal Rubik's brand WILL NOT WORK
- Check lighting - use bright, even lighting
- Position camera at **corner angle** to see 3 faces
- Hold cube 8-15 inches from camera
- Ensure background is plain (not colorful); the code detects for quadrilaterals but it can get confused.
- Try different cube orientations
- Check that at least 3 colors are visible in the frame and equally visible to the camera.

**Debug**: Run `python3 detection.py` to see which colors are detected and how many corners are found.

### Colors Detected Incorrectly

**Issue**: Wrong colors being identified

**Solution**: Calibrate color ranges for your specific cube and lighting.

1. Take a photo of your cube:

```bash
python3 capture.py
```

2. Use a color picker tool to find HSV values of your cube colors

3. Update `COLOR_INFO` in `detection.py` with correct ranges

**Example HSV ranges (you may need to adjust)**:

- Blue: H=100-140, S=150-255, V=0-255
- Green: H=40-80, S=50-255, V=50-255
- Orange: H=12-18, S=150-255, V=100-255
- Yellow: H=22-38, S=100-255, V=100-255

### No Sound

**Test audio output:**

```bash
speaker-test -t wav
```

**Check volume:**

```bash
alsamixer
# Use arrow keys to adjust volume
# Press M to unmute
```

**Select audio output (Pi 4/5):**

```bash
sudo raspi-config
# System Options > Audio > Select output device
```

**For VLC issues:**

```bash
sudo apt install vlc-plugin-base
```

**Alternative**: If pygame audio doesn't work, uncomment VLC method in `alarm.py`:

```python
# Uncomment these lines:
import subprocess

def play_alarm():
    subprocess.Popen(["cvlc", "--play-and-exit", "--loop", "media/alarm.mp3"])

def stop_alarm():
    subprocess.call(["pkill", "vlc"])
```

### Program Running Slow

**Solutions**:

- Increase photo interval in `main.py` (5 seconds → 10 seconds)
- Close other programs running on Pi
- Use a faster Raspberry Pi model (Pi 4/5 recommended)
- Reduce image resolution by adding to `capture.py`:

```python
def photo():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    # ... rest of code
```

### Alarm Doesn't Go Off

**Check**:

1. Is the program running? (`ps aux | grep main.py`)
2. Is the system time correct? (`date`)
3. Set system time if wrong:

```bash
sudo date -s "2024-01-10 14:30:00"
# Or enable NTP:
sudo timedatectl set-ntp true
```

### ImportError or Module Not Found

**Reinstall packages:**

```bash
pip3 install opencv-python numpy matplotlib pygame --break-system-packages --upgrade
```

**Or in virtual environment:**

```bash
source myenv/bin/activate
pip install opencv-python numpy matplotlib pygame --upgrade
```

---

## 🎨 How Detection Works

### Color Detection

The program uses HSV (Hue, Saturation, Value) color space to detect cube colors:

- **Blue, Green, Orange, Yellow**: Single HSV range
- **Red**: Two HSV ranges (wraps around 0°/180° in Hue)
- **White**: Not detected (uses opposite color logic instead)

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
- It's either the only contour OR represents >85% of that color

The alarm stops when:

- At least 3 faces are solved
- Opposite face pairs aren't both "solved" (blue/green, red/orange can't both be solved)

### Supported Cube Colors

- ✅ Blue
- ✅ Green
- ✅ Orange
- ✅ Yellow
- ✅ Red
- ❌ White (not detected due to issues with lighting & bg that could emerge)

---

## Tips for Best Results

1. **Lighting**: Use consistent, bright lighting. Morning sunlight works well!
2. **Cube Position**: Hold cube steady at corner angle showing 3 faces
3. **Background**: Use a plain wall or surface behind the cube
4. **Camera Placement**: Mount camera on a stand for consistent positioning
5. **Cube Type**: Stickerless cubes work MUCH better than stickered ones
6. **Practice**: Test the detection before relying on it as your alarm!

---

## 🎯 Future Improvements

Ideas for expanding this project:

- [ ] Multiple alarm times
- [ ] Web interface for remote control
- [ ] Statistics tracking (solve times, success rate)
- [ ] Gradual volume increase
- [ ] Weekend/weekday different schedules
- [ ] LED status indicators
- [ ] Backup alarm (stops after 10 minutes if not solved)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

**Resources Used:**

- [OpenCV Morphological Operations](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)
- [Color Detection with OpenCV](https://www.youtube.com/watch?v=oXlwWbU8l2o)
- [Quadrilateral Detection Tutorial](https://nhuvan.github.io/blog/005-quadrilateral/)
- Freecodecamp tutorial for openCV
- Other sources

---

## 📧 Support

For questions, issues, or suggestions:

- Open an issue on GitHub
- Check the Troubleshooting section above
- Contact me at swuott2009@gmail.com

**Happy Cubing! 🎲⏰**
