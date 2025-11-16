import pytest
from course_schedule import Solution

class TestCanFinish:
    def test_example1(self):
        sol = Solution()
        assert sol.canFinish(2, [[1, 0]]) == True

    def test_example2(self):
        sol = Solution()
        assert sol.canFinish(2, [[1, 0], [0, 1]]) == False

    def test_single_course(self):
        sol = Solution()
        assert sol.canFinish(1, []) == True

    def test_no_prerequisites(self):
        sol = Solution()
        assert sol.canFinish(3, []) == True

    def test_linear_dependencies(self):
        sol = Solution()
        assert sol.canFinish(3, [[0, 1], [1, 2]]) == True

    def test_circular_dependency(self):
        sol = Solution()
        assert sol.canFinish(3, [[0, 1], [1, 2], [2, 0]]) == False

    def test_multiple_paths(self):
        sol = Solution()
        assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True

    def test_disconnected_graph(self):
        sol = Solution()
        assert sol.canFinish(4, [[1, 0], [3, 2]]) == True

