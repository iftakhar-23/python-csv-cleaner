
# Python CSV Cleaner

A lightweight Python application that cleans CSV files by removing duplicate records, trimming unnecessary whitespace, and removing completely empty rows.

## Features

- Removes duplicate records.
- Trims unnecessary whitespace from data.
- Removes completely empty rows.
- Validates CSV column consistency.
- Preserves the original CSV file.
- Exports cleaned data into a separate CSV file.
- Provides a summary of cleaning operations.
- Handles common file and data errors.

## Technologies

- Python 3
- Python CSV module
- pathlib

No external Python packages are required.

## Project Structure

csv-cleaner/
├── main.py
├── sample_customers.csv
└── README.md

## How to Run

1. Install Python 3.
2. Open a terminal inside the project folder.
3. Run:

   py main.py

4. Enter the path of your CSV file when prompted.
5. The program generates a new file with `_cleaned` added to its name.

## Example

Input:

name,email,city
 Mahin , mahin@example.com , Mymensingh
Rahim,rahim@example.com,Dhaka
Mahin,mahin@example.com,Mymensingh

Output:

name,email,city
Mahin,mahin@example.com,Mymensingh
Rahim,rahim@example.com,Dhaka

## Privacy

All processing takes place locally on the computer. No CSV data is uploaded to an external server.

## License

MIT License
