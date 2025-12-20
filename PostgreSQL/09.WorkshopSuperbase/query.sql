ALTER TABLE students
ADD CONSTRAINT
   students_name_unique UNIQUE (name);

ALTER TABLE attendance
ADD COLUMN comment TEXT;

CREATE OR REPLACE FUNCTION get_absence_students_by_session_id
(session_id INT)
RETURNS TABLE (name TEXT)
AS
$$
  BEGIN
     RETURN QUERY
        SELECT
        s.name
        FROM absences AS a
        JOIN students AS s
        ON s.id=a.student_id
        WHERE a.session_id = get_absence_students_by_session_id.session_id;

  END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE mark_student_absent
(p_student_id INT, p_session_id INT)
AS
$$
  BEGIN
      IF NOT EXISTS (SELECT 1 FROM students WHERE id=p_student_id) THEN
        RAISE EXCEPTION 'Student with id % does not exist.', p_student_id;
      END IF;

      IF NOT EXISTS (SELECT 1 FROM sessions WHERE id=p_session_id) THEN
        RAISE EXCEPTION 'Session with id % does not exist.', p_session_id;
      END IF;

      INSERT INTO attendance(student_id, session_id, attended)
      VALUES (p_student_id, p_session_id, FALSE)
      ON CONFLICT (student_id, session_id) DO UPDATE SET attended = FALSE;
  END
$$
LANGUAGE plpgsql;

 CREATE INDEX concurrently IF NOT EXISTS
 idx_sessions_session_date
 ON sessions(session_date);

ALTER TABLE absences
ADD CONSTRAINT absences_students_fk FOREIGN KEY (student_id) REFERENCES students(id),
ADD CONSTRAINT absences_sessions_fk FOREIGN KEY (session_id) REFERENCES sessions(id)