# readx

A micro-library for safe file reading and size inspection. Protects your terminal and memory from crashing when accidentally reading huge or binary files.

## Features

- **Safe Reading**: Automatically stops and raises an error if the file is binary or too large.
- **Smart Size**: Converts bytes to KB, MB, or GB into clean integer or float values.
- **No Dependencies**: Built entirely using Python's standard library.

## Installation

Just drop the script into your project folder or install it:
```bash
pip install readx
```

## Usage

### 1. Safe Content Reading
By default, `readContent` blocks files larger than 200MB or files with binary structures.

```python
import readx

# Reading a safe text file
text = readx.readContent("logs.txt")

# Trying to read a 1GB database or a .png image without ignoreWarns=True
# Will safely raise TooBig or BinaryFile exceptions instead of freezing your PC
binary_data = readx.readContent("photo.png", ignoreWarns=True)
```

### 2. Smart File Size Conversion
Convert file size into any format without messy `if/else` lines.

```python
import readx

# Returns an exact integer if there is no remainder, or float if there is
mb_size = readx.size("video.mp4", type="MB")  # e.g., 45 or 45.23
gb_size = readx.size("archive.zip", type="GB")
```

## Custom Exceptions

The library provides clear exceptions you can handle with `try/except`:
- `FileNotFound` - Raised when the path does not exist.
- `TooBig` - Raised when the file exceeds the threshold.
- `BinaryFile` - Raised when trying to read a binary file in text mode.
- `InvalidType` - Raised when a wrong size format is requested.

## License
MIT
