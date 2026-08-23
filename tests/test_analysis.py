import unittest

from analysis import (
    subject_percentages,
    exam_percentage,
    calculate_subject_averages,
    calculate_student_average,
    find_strongest_weakest_subject,
    classify_performance,
    compare_exams
)


class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.exam = (
            1, 1, "Test Exam",
            100, 100, 100,
            80, 70, 90
        )

    def test_exam_percentage(self):
        self.assertAlmostEqual(
            exam_percentage(self.exam),
            80
        )

    def test_subject_percentages(self):
        self.assertEqual(
            subject_percentages(self.exam),
            (80.0, 70.0, 90.0)
        )

    def test_student_average(self):
        self.assertEqual(
            calculate_student_average([self.exam]),
            80
        )

    def test_classification(self):
        self.assertEqual(
            classify_performance(95),
            "Excellent"
        )

        self.assertEqual(
            classify_performance(80),
            "Good"
        )

    def test_strongest_weakest(self):
        strongest, weakest = (
            find_strongest_weakest_subject(
                [self.exam]
            )
        )

        self.assertEqual(strongest, "Biology")
        self.assertEqual(weakest, "Chemistry")

    def test_exam_comparison(self):
        second_exam = (
            2, 1, "Second Exam",
            100, 100, 100,
            90, 80, 95
        )

        first, second, difference = compare_exams(
            self.exam,
            second_exam
        )

        self.assertAlmostEqual(first, 80)
        self.assertAlmostEqual(
            second,
            88.3333333333
        )
        self.assertGreater(difference, 0)


if __name__ == "__main__":
    unittest.main()