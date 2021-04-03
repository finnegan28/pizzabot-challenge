import unittest
from commands import *


class ValidateArgs(unittest.TestCase):

    def test_valid_args_fail(self):
        args = ["1", "2"]
        with self.assertRaises(SystemExit):
            valid_args(args)


class ValidateGrid(unittest.TestCase):

    def test_invalid_grid_fail_no_x(self):
        size = "5d5"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_too_short(self):
        size = "5"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_negative(self):
        size = "5x-5"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_letters(self):
        size = "fxf"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_zero(self):
        size = "0x0"
        with self.assertRaises(SystemExit):
            valid_grid(size)

    def test_invalid_grid_fail_single_zero(self):
        size = "0x5"
        with self.assertRaises(SystemExit):
            valid_grid(size)


class ValidateLocation(unittest.TestCase):

    def test_invalid_location_brackets(self):
        size = "5x5"
        locations = "(5,5"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_brackets_2(self):
        size = "5x5"
        locations = "5,5)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_empty(self):
        size = "5x5"
        locations = "(,5)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_empty_2(self):
        size = "5x5"
        locations = "(5,)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_empty_3(self):
        size = "5x5"
        locations = "(5,4) (5,)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_letter(self):
        size = "5x5"
        locations = "(5,f)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_location_letter_2(self):
        size = "5x5"
        locations = "(f)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_coords_1(self):
        size = "5x5"
        locations = "(5)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_coords_2(self):
        size = "5x5"
        locations = "(5,4) (5)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_invalid_coords_3(self):
        size = "5x5"
        locations = "(-2,4)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_out_of_delivery_area_1(self):
        size = "5x5"
        locations = "(6,4)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)

    def test_out_of_delivery_area_2(self):
        size = "5x5"
        locations = "(1,7)"
        with self.assertRaises(SystemExit):
            valid_locations(size, locations)


class TestDelivery(unittest.TestCase):

    def test_delivery_success(self):
        locations = ['(5,5)']
        self.assertEqual(deliver_pizza(locations), "EEEEENNNNND")

    def test_delivery_success_2(self):
        locations = ['(1,3)', '(4,4)']
        self.assertEqual(deliver_pizza(locations), "ENNNDEEEND")

    def test_delivery_success_3(self):
        locations = ['(0,0)', '(1,3)', '(4,4)', '(4,2)', '(4,2)', '(0,1)', '(3,2)', '(2,3)', '(4,1)']
        self.assertEqual(deliver_pizza(locations), "DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD")

    def test_delivery_success_4(self):
        locations = ['(1,3)', '(1,3)']
        self.assertEqual(deliver_pizza(locations), "ENNNDD")

    def test_delivery_fail(self):
        locations = ['(5,5)']
        self.assertNotEqual(deliver_pizza(locations), "EEEENNNN")

    def test_delivery_fail_2(self):
        locations = ['(5,5)']
        self.assertNotEqual(deliver_pizza(locations), "")


if __name__ == '__main__':
    unittest.main()
