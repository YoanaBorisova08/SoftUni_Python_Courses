from project.senior_student import SeniorStudent
from unittest import TestCase, main

class SeniorStudentTest(TestCase):
    def setUp(self):
        self.student = SeniorStudent("1234", "Test name", 3.5)

    def test_init(self):
        self.assertEqual("1234", self.student.student_id)
        self.assertEqual("Test name", self.student.name)
        self.assertEqual(3.5, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_student_id_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_student_id_setter_valid(self):
        self.student.student_id = "  5678  "
        self.assertEqual("5678", self.student.student_id)

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_name_setter_valid(self):
        self.student.name = "  New Name  "
        self.assertEqual("  New Name  ", self.student.name)

    def test_gpa_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = -1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_gpa_setter_valid(self):
        self.student.student_gpa = 2.5
        self.assertEqual(2.5, self.student.student_gpa)

    def test_college_setter_raises(self):
        result = self.student.apply_to_college(4.0, "Harvard")
        self.assertEqual("Application failed!", result)
        self.assertEqual(set(), self.student.colleges)

    def test_college_setter_valid(self):
        result = self.student.apply_to_college(3.0, "Harvard")
        self.assertEqual("Test name successfully applied to Harvard.", result)
        self.assertEqual({"HARVARD"}, self.student.colleges)

        result = self.student.apply_to_college(2.5, "MIT")
        self.assertEqual("Test name successfully applied to MIT.", result)
        self.assertEqual({"HARVARD", "MIT"}, self.student.colleges)

    def test_update_gpa_raises(self):
        result = self.student.update_gpa(1.0)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(3.5, self.student.student_gpa)

        result = self.student.update_gpa(0.6)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(3.5, self.student.student_gpa)

    def test_update_gpa_valid(self):
        result = self.student.update_gpa(3.8)
        self.assertEqual("Student GPA was successfully updated.", result)
        self.assertEqual(3.8, self.student.student_gpa)

    def test_equality_true(self):
        other_student = SeniorStudent("5678", "Other name", 3.5)
        self.assertTrue(self.student == other_student)

    def test_equality_false(self):
        other_student = SeniorStudent("5678", "Other name", 4.0)
        self.assertFalse(self.student == other_student)




if __name__ == "__main__":
    main()