from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('a')

    def test_constructor(self):
        self.assertEqual('a', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_course_already_added_updating_notes(self):
        self.student.courses = {'maths': ['ok']}
        self.assertEqual('Course already added. Notes have been updated.', self.student.enroll('maths', ['not ok']))
        self.assertEqual(['ok', 'not ok'], ['ok', 'not ok'])

    def test_enroll_add_course_notes_Y(self):
        self.student.courses = {'maths': ['ok']}
        self.assertEqual('Course and course notes have been added.', self.student.enroll('english', ['not ok'], 'Y'))
        self.assertEqual(['not ok'], self.student.courses['english'])

    def test_enroll_add_course_no_notes(self):
        self.assertEqual('Course has been added.', self.student.enroll('english', 'asfasd', 'String'))
        self.assertEqual([], self.student.courses['english'])

    def test_add_notes_course_already_in(self):
        self.student.courses = {'maths': ['ok']}
        self.assertEqual('Notes have been updated', self.student.add_notes('maths', 'not ok'))
        self.assertEqual(['ok', 'not ok'], self.student.courses['maths'])

    def test_add_notes_course_not_found(self):
        with self.assertRaises(Exception) as exc:
            self.student.add_notes('maths', 'not ok')
        self.assertEqual('Cannot add notes. Course not found.', str(exc.exception))

    def test_leave_course_successfully(self):
        self.student.courses = {'maths': 'ok'}
        self.assertEqual('Course has been removed', self.student.leave_course('maths'))
        self.assertEqual({}, self.student.courses)

    def test_leave_course_not_found(self):
        with self.assertRaises(Exception) as exc:
            self.student.leave_course('maths')
        self.assertEqual('Cannot remove course. Course not found.', str(exc.exception))

if __name__ == '__main__':
    unittest.main()