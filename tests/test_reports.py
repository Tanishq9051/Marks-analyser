import unittest
import tempfile
import os

from reports import export_student_report


class TestReports(unittest.TestCase):

    def test_report_creation(self):
        student = (1, "Test Student")

        exams = [
            (
                1,
                1,
                "Test Exam",
                100,
                100,
                100,
                80,
                85,
                90
            )
        ]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt"
        ) as file:
            filename = file.name

        try:
            result = export_student_report(
                student,
                exams,
                filename
            )

            self.assertTrue(result)
            self.assertTrue(os.path.exists(filename))

            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            self.assertIn("MARKS ANALYSER REPORT", content)
            self.assertIn("Test Student", content)
            self.assertIn("Test Exam", content)

        finally:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == "__main__":
    unittest.main()