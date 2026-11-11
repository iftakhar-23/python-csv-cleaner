# Python CSV Cleaner

A lightweight Python application for cleaning and organizing CSV files, featuring both a command-line interface and a desktop graphical interface.

## Features

- Remove duplicate records.
- Trim unnecessary whitespace.
- Remove completely empty rows.
- Validate CSV column consistency.
- Preserve original input files.
- Export cleaned CSV files.
- Display a summary of cleaning operations.
- Handle common file and data errors.
- Simple desktop interface using Tkinter.

## Technologies

- Python 3
- CSV module
- Tkinter
- pathlib
- unittest

No external Python packages are required.

## Project Structure

python-csv-cleaner/
├── main.py
├── gui.py
├── test_main.py
├── sample_customers.csv
├── README.md
└── .gitignore

## Getting Started

### Requirements

- Python 3 installed.
- No additional packages required.

### Command-Line Version

Open a terminal inside the project folder and run:

    py main.py

Enter the path to your CSV file when prompted.

### Desktop Application

Run:

    py gui.py

Use Browse Files to select a CSV file, then click Clean CSV File.

## Running Tests

Run the automated tests with:

    py -m unittest -v test_main.py

The tests cover duplicate removal, whitespace cleaning, original file preservation, empty files, and inconsistent column counts.

## Output

The application creates a new file with `_cleaned` added to the original filename.

For example:

    customers.csv
    customers_cleaned.csv

The original CSV file remains unchanged.

Generated cleaned files are excluded from Git through `.gitignore`.

## Privacy

All CSV processing takes place locally on the user's computer. No CSV data is uploaded to an external server.

## License

No license file has been added yet.

All processing takes place locally on the computer. No CSV data is uploaded to an external server.

## License

MIT License
