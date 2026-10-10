
import unittest


def calculate_average(marks):
    if not marks:
        raise ValueError("List cannot be empty")
    for mark in marks:
        get_grade(mark)
    return sum(marks) / len(marks)


def get_grade(mark):
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100")

    if mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


def is_pass(mark):
    get_grade(mark)
    return mark >= 40


def get_highest_mark(marks):
    if not marks:
        raise ValueError("List cannot be empty")
    for mark in marks:
        get_grade(mark)
    return max(marks)


class TestGradeCalculator(unittest.TestCase):

    def test_get_grade(self):
        self.assertEqual(get_grade(85), "A+")

    def test_fail_grade(self):
        self.assertEqual(get_grade(35), "F")

    def test_grade_100(self):
        self.assertEqual(get_grade(100), "A+")

    def test_negative_mark(self):
        with self.assertRaises(ValueError):
            get_grade(-5)

    def test_mark_over_100(self):
        with self.assertRaises(ValueError):
            get_grade(110)

    def test_pass(self):
        self.assertTrue(is_pass(40))

    def test_fail(self):
        self.assertFalse(is_pass(25))

    def test_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_highest_mark(self):
        self.assertEqual(get_highest_mark([45, 88, 67]), 88)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])


if __name__ == "__main__":
    unittest.main()