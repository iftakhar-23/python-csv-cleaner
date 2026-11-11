
import unittest
import tempfile
import csv
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

from main import clean_csv


class TestCSVCleaner(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_clean_csv_removes_duplicates_and_spaces(self):
        input_file = self.folder / "customers.csv"

        input_file.write_text(
            "name,email\n"
            " Mahin , mahin@example.com \n"
            "Rahim,rahim@example.com\n"
            "Mahin,mahin@example.com\n"
            ",\n",
            encoding="utf-8"
        )

        with redirect_stdout(StringIO()):
            output_file = clean_csv(input_file)

        with open(output_file, encoding="utf-8-sig", newline="") as file:
            rows = list(csv.reader(file))

        self.assertEqual(
            rows,
            [
                ["name", "email"],
                ["Mahin", "mahin@example.com"],
                ["Rahim", "rahim@example.com"]
            ]
        )

    def test_original_file_remains_unchanged(self):
        input_file = self.folder / "original.csv"
        original_data = "name,email\nMahin,mahin@example.com\n"

        input_file.write_text(original_data, encoding="utf-8")

        with redirect_stdout(StringIO()):
            clean_csv(input_file)

        self.assertEqual(
            input_file.read_text(encoding="utf-8"),
            original_data
        )

    def test_empty_file_raises_error(self):
        input_file = self.folder / "empty.csv"
        input_file.write_text("", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "empty"):
            clean_csv(input_file)

    def test_inconsistent_columns_raise_error(self):
        input_file = self.folder / "invalid.csv"

        input_file.write_text(
            "name,email\n"
            "Mahin,mahin@example.com,extra\n",
            encoding="utf-8"
        )

        with self.assertRaisesRegex(ValueError, "row 2"):
            clean_csv(input_file)


if __name__ == "__main__":
    unittest.main()
