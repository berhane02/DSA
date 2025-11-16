import pytest
from course_schedule_ii import Solution

def is_valid_order(numCourses, prerequisites, result):
    """Helper to check if result is a valid topological order"""
    if len(result) != numCourses:
        return False
    
    # Check all prerequisites are satisfied
    pos = {course: i for i, course in enumerate(result)}
    for course, prereq in prerequisites:
        if pos[course] <= pos[prereq]:
            return False
    return True

class TestFindOrder:
    def test_example1(self):
        sol = Solution()
        result = sol.findOrder(2, [[1, 0]])
        assert len(result) == 2
        assert set(result) == {0, 1}
        assert is_valid_order(2, [[1, 0]], result)

    def test_example2(self):
        sol = Solution()
        result = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        assert len(result) == 4
        assert set(result) == {0, 1, 2, 3}
        assert is_valid_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]], result)

    def test_example3(self):
        sol = Solution()
        result = sol.findOrder(1, [])
        assert result == [0]

    def test_circular_dependency(self):
        sol = Solution()
        result = sol.findOrder(2, [[1, 0], [0, 1]])
        assert result == []

    def test_no_prerequisites(self):
        sol = Solution()
        result = sol.findOrder(3, [])
        assert len(result) == 3
        assert set(result) == {0, 1, 2}

    def test_linear_dependencies(self):
        sol = Solution()
        result = sol.findOrder(3, [[0, 1], [1, 2]])
        assert len(result) == 3
        assert set(result) == {0, 1, 2}
        assert is_valid_order(3, [[0, 1], [1, 2]], result)

