from day_01 import calculate_distance, convert_line


class TestDay01:
    def test_case_1(self):
        # GIVEN
        line = "45257   55015\n"
        # [2,4,5,5,7], [0,1,5,5,5]
        result = abs(2 - 0) + abs(4 - 1) + abs(5 - 5) + abs(5 - 5) + abs(7 - 5)
        # result = 22
        print("result:", result)
        # WHEN
        l1, l2 = convert_line(line)
        distance = calculate_distance(l1, l2)
        # THEN
        assert distance == result
