[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![QRcode](https://img.shields.io/badge/QRcode-v7.4.2-green.svg)](https://pypi.org/project/qrcode/)


## Python QR Code Generator

### Overview
This QRCode is a minimalistic Python script designed for generating QR codes. 
This script utilizes the `qrcode` library to create a QR code that encodes a specified URL. 
In this instance, the script generates a QR code for the URL "https://github.com/python-dev-og" and saves it as an image file. 
This README provides instructions on how to set up and run the script.

### Prerequisites
- Python (3.x)
- `qrcode` Python library

### Installation

1. **Clone the Repository**
   ```
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Install `qrcode` Library**
   You can install the `qrcode` library using pip. Run the following command:
   ```
   pip install qrcode
   ```

### Usage
To use this script, simply run it in your Python environment. The script will generate a QR code image (`qr.png`) in the script's directory.

1. **Run the Script**
   ```
   python qr_code_generator.py
   ```

   This will create a QR code image named `qr.png` in the current directory.

### Customization
To generate a QR code for a different URL, modify the URL string in the `qrcode.make()` method. For example:
```python
image = qrcode.make("https://your-custom-url.com")
```

### Features
- **Simple and Fast**: Quickly generates a QR code for any URL.
- **Customizable**: Easy to modify to encode different URLs.
- **Portable**: Generates a `.png` image file that can be used across various platforms.

### Contributing
Feel free to fork the repository and submit pull requests with any enhancements or additional features.

### License
This project is open source and available under the [MIT License](LICENSE).

### Final Look

![qr.png](qr.png)
