from project.student import Student
from unittest import TestCase, main

class TestStudent(TestCase):
    def setUp(self):
        self.student1 = Student("Student 1",
                                {"Python": ["n1", "n2", "n3"],
                                        "JS": ["n1", "n2"]})
        self.student2 = Student("Student 2")

    def test_init_with_courses(self):
        self.assertEqual("Student 1", self.student1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"],"JS": ["n1", "n2"]}, self.student1.courses)
        self.assertIsInstance(self.student1.name, str)
        self.assertIsInstance(self.student1.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual("Student 2", self.student2.name)
        self.assertEqual({}, self.student2.courses)
        self.assertIsInstance(self.student2.name, str)
        self.assertIsInstance(self.student2.courses, dict)

    def test_enroll_in_existing_course(self):
        result = self.student1.enroll("Python", ["n4", "n5"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["n1", "n2", "n3", "n4", "n5"], self.student1.courses["Python"])

    def test_enroll_in_new_course_with_notes(self):
        result = self.student2.enroll("Java", ["n1", "n2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn("Java", self.student2.courses)
        self.assertEqual(["n1", "n2"], self.student2.courses["Java"])

        result = self.student2.enroll("C++", ["n1"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn("C++", self.student2.courses)
        self.assertEqual(["n1"], self.student2.courses["C++"])

    def test_enroll_in_new_course_without_notes(self):
        result = self.student2.enroll("Java", ["n1", "n2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertIn("Java", self.student2.courses)
        self.assertEqual([], self.student2.courses["Java"])

    def add_notes_to_existing_course(self):
        result = self.student1.add_notes("Python", "n4")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2", "n3", "n4"], self.student1.courses["Python"])

    def test_add_notes_to_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("Java", "n1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student1.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student1.courses)

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))





if __name__ == "__main__":
    main()