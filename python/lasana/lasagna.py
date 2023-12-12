
EXPECTED_BAKE_TIME =40
def lasagna(EXPECTED_BAKE_TIME):
        return EXPECTED_BAKE_TIME
        
def bake_time_remaining(ttime):
    if ttime < EXPECTED_BAKE_TIME:
       ttime=EXPECTED_BAKE_TIME -ttime
    else: 
        ttime=EXPECTED_BAKE_TIME   
    return ttime
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return elapsed_bake_time +preparation_time_in_minutes(number_of_layers)
def test_docstrings_were_written(self):
       functions = [bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes]

       for variant, function in enumerate(functions, start=1):
           with self.subTest(f'variation #{variant}', function=function):
               failure_msg = f'Expected a docstring for `{function.__name__}`, but received `None` instead.'
               self.assertIsNotNone(function.__doc__, msg=failure_msg)
                

import lasagna
print(lasagna.EXPECTED_BAKE_TIME)
from lasagna import bake_time_remaining
print(bake_time_remaining(30))
from lasagna import preparation_time_in_minutes
print(preparation_time_in_minutes(2))
from lasagna import elapsed_time_in_minutes
from lasagna import test_docstrings_were_written

print(test_docstrings_were_written())
