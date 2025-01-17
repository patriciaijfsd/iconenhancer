# IconEnhancer

IconEnhancer is a Python application that allows users to customize the size and appearance of desktop icons for better visibility on Windows.

## Features

- Adjust the size of desktop icons.
- Simple and intuitive user interface.
- Immediate application of changes.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. Install Python 3.x from the official [Python website](https://www.python.org/).
2. Install PyQt5 using pip:

   ```bash
   pip install PyQt5
   ```

3. Download the `icon_enhancer.py` file from this repository.

## Usage

1. Run the `icon_enhancer.py` script:

   ```bash
   python icon_enhancer.py
   ```

2. Use the slider to select the desired icon size.
3. Click the "Apply" button to change the desktop icon size.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Note: This program uses `ctypes` to call Windows APIs, which may require administrative privileges to change system settings. Please ensure that you have the necessary permissions when running this program.