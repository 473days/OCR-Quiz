# Quiz OCR Processor fur Praktikum

A Python script that extracts text from quiz screenshots using Optical Character Recognition (OCR). Processes images of quiz questions and answers, then saves them to a text file with automatic question numbering.

## Features

- Image preprocessing for better OCR accuracy
- Automatic question numbering
- Separation of questions and answers
- Support for German language text (modifiable)
- Appends results to a text file while maintaining previous entries

## Requirements

- Python 3.6+
- Tesseract OCR
- OpenCV
- Pillow
- pytesseract

## Installation

1. Install Tesseract OCR:
   - **Windows**: Download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux**: `sudo apt-get install tesseract-ocr`
   - **Mac**: `brew install tesseract`

2. Install Python dependencies:
   ```bash
   pip install opencv-python pillow pytesseract
