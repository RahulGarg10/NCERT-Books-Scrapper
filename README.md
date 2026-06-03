# NCERT Complete Library Downloader

An automated Python utility designed to stream, unpack, and catalog digital editions of Class 11 and Class 12 Mathematics and Physics textbooks directly from official NCERT infrastructure.

## Key Features

* **Automatic Volume Mapping**: Links human-readable book titles to specific NCERT server short-codes.
* **Storage Optimization**: Discards raw `.zip` containers instantly post-extraction to keep directories clean.
* **Resilient Downloader Pipeline**: Implements extended network timeouts via `httpx` to handle large archives.
* **Polite Scraping Architecture**: Incorporates rate-limiting cooldowns to protect government hosting infrastructure.

## Prerequisites

* Python 3.7 or newer.
* Stable internet connection.

## Installation

1. Clone or download this repository to your local machine.
2. Open your terminal inside the project directory.
3. Install the required `httpx` library:

```bash
pip install httpx
```

## Usage

Execute the script to start the automated download and extraction pipeline:

```bash
python ncert_books_scrapper.py
```

### Output Directory Structure

The script automatically generates a clean, structured library inside your active workspace directory:

```text
NCERT Books/
├── Class_11_Maths_Part1/
│   └── [Extracted PDF Chapters]
|
├── Class_11_Physics_Part1/
|    └── [Extracted PDF Chapters]
|
├── Class_11_Physics_Part2/
|    └── [Extracted PDF Chapters]
|
├── Class_12_Maths_Part1/
|    └── [Extracted PDF Chapters]
|
├── Class_12_Maths_Part2/
|    └── [Extracted PDF Chapters]
|
├── Class_12_Physics_Part1/
|    └── [Extracted PDF Chapters]
|
└── Class_12_Physics_Part2/
    └── [Extracted PDF Chapters]
```

## Supported Volumes

The script is pre-configured to fetch the following volumes:


| Book Identifier | NCERT Server Code |
| :--- | :--- |
| Class 11 Mathematics (Part 1) | `kemh1dd` |
| Class 11 Physics (Part 1) | `keph1dd` |
| Class 11 Physics (Part 2) | `keph2dd` |
| Class 12 Mathematics (Part 1) | `lemh1dd` |
| Class 12 Mathematics (Part 2) | `lemh2dd` |
| Class 12 Physics (Part 1) | `leph1dd` |
| Class 12 Physics (Part 2) | `leph2dd` |

## License

This project is open-source and free to use for personal educational purposes.

