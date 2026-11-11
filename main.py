
import csv
from pathlib import Path


def clean_csv(input_path):
    """Clean a CSV file and save a new cleaned version."""

    file_path = Path(input_path).expanduser()

    # Check whether the file exists
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError("The selected file does not exist.")

    # Create the output filename
    output_path = file_path.with_name(
        f"{file_path.stem}_cleaned.csv"
    )

    # Read the original CSV file
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        # Read column names
        try:
            headers = next(reader)
        except StopIteration:
            raise ValueError("The CSV file is empty.")

        headers = [header.strip() for header in headers]

        if not headers or all(not header for header in headers):
            raise ValueError("The CSV file has no valid column names.")

        cleaned_rows = []
        seen_rows = set()

        blank_rows = 0
        duplicate_rows = 0

        # Process each record
        for row_number, row in enumerate(reader, start=2):

            # Remove completely empty rows
            if not row or all(not cell.strip() for cell in row):
                blank_rows += 1
                continue

            # Check that every row has the correct number of columns
            if len(row) != len(headers):
                raise ValueError(
                    f"Invalid number of columns at row {row_number}."
                )

            # Remove unnecessary spaces
            cleaned_row = [cell.strip() for cell in row]

            # Identify duplicate records
            row_key = tuple(cleaned_row)

            if row_key in seen_rows:
                duplicate_rows += 1
                continue

            seen_rows.add(row_key)
            cleaned_rows.append(cleaned_row)

    # Export the cleaned data
    with open(output_path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(headers)
        writer.writerows(cleaned_rows)

    # Display the results
    print("\n========== CLEANING COMPLETE ==========")
    print(f"Original file: {file_path.name}")
    print(f"Cleaned file:  {output_path.name}")
    print(f"Records saved: {len(cleaned_rows)}")
    print(f"Blank rows removed: {blank_rows}")
    print(f"Duplicate rows removed: {duplicate_rows}")
    print("=======================================")

    return output_path


def main():
    print("================================")
    print("       PYTHON CSV CLEANER")
    print("================================")

    input_path = input("\nEnter your CSV file path: ").strip().strip('"')

    try:
        clean_csv(input_path)

    except (FileNotFoundError, ValueError, PermissionError, csv.Error, OSError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
