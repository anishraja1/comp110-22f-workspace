from __future__ import annotations

class Course:
    """Models the idea of a UNC course."""
    names: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, string: str) -> bool:
        if self.level >= 400 and string in self.prerequisites:
            return True
        return False


def find_courses(list_one: list[Course], search: str) -> list[str]:
    returned_list: list[str] = []
    for course in list_one:
        if course.level >= 400 and search in course.prerequisites:
            returned_list.append(course.name)
    return returned_list







