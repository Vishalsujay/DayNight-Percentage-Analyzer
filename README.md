# DayNight-Percentage-Analyzer

**DayNight Percentage Analyzer** is a Python-based tool for analyzing videos and determining the percentage of Day, Evening, and Night periods in the footage. It utilizes the HSV (Hue, Saturation, Value) color model to classify frames and provides a summary of time periods as percentages.

---

## Features

- **Video Frame Analysis**: Processes videos frame by frame using the OpenCV library.
- **Time Period Classification**: Categorizes frames into Day, Evening, or Night based on brightness and hue distribution.
- **Percentage Summary**: Outputs the percentage of frames belonging to each time period.
- **Real-Time Visualization**: Displays both the original and HSV-transformed frames during the analysis.

---

## Requirements

Ensure you have the following installed:

- Python 3.7+
- OpenCV (`cv2`)
- Numpy

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/DayNight-Percentage-Analyzer.git
   cd DayNight-Percentage-Analyzer
