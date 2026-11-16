# Opensource_team6

## 2. Installation

### Install from TestPyPI

You can install the package from TestPyPI for testing purposes.

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ PACKAGE_NAME
```

### Install from PyPI

After the package is officially released, you can install it from PyPI.

```bash
pip install PACKAGE_NAME
```

## 3. Quick Start

SeeAllColors allows users to simulate how an image appears to people with different types of color vision deficiency.

### Example

Prepare an image file named `sample.png` in your working directory.

```python
from seeallcolors.core import load_image, simulate_colorblindness

image = load_image("sample.png")
result = simulate_colorblindness(image, "protanopia")
```

### Input
- An image file (JPG or PNG).
- A color vision deficiency type: `protanopia`, `deuteranopia`, or `tritanopia`.

### Output
- Image data processed to simulate the selected type of color vision deficiency.