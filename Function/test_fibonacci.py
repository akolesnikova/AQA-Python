from FibonacciFunction import fibonacci


def test_message():

       print("Fibonacci sequence:")


def test_expected_result():

        assert fibonacci(3) == 2


def test_condition_for_negative():

        assert fibonacci(-1) == 1


def test_not_expected_result():

        assert fibonacci(5) != 1
