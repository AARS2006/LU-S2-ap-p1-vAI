class CourseSelectionException(Exception):
    pass


class StudentNotFoundException(CourseSelectionException):
    pass


class StudentAlreadyExistsException(CourseSelectionException):
    pass


class ProfessorNotFoundException(CourseSelectionException):
    pass


class ProfessorAlreadyExistsException(CourseSelectionException):
    pass


class CourseNotFoundException(CourseSelectionException):
    pass


class CourseAlreadyExistsException(CourseSelectionException):
    pass


class CourseCapacityFullException(CourseSelectionException):
    pass


class CourseAlreadySelectedException(CourseSelectionException):
    pass