'''''''''
from unittest import mock as mk

# Creating a mock object
mocking = mk.Mock()

def me(value):
    print(str(value) + ' Hello')
    mocking()

for j in range(0, 10):
    if j == 4:
        me(j)
    else:
        print(j)

mocking.assert_any_call()
print(mocking.call_count)
print(mocking.call_args)
'''

'''''''''
from datetime import datetime
from unittest.mock import Mock

def is_weekday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)

# Check if today is in fact a weekday.  If you get no output your code worked, you will get an exception error
# if you ran this code during a weekend.
assert is_weekday()
'''


'''''''''
# We will now use the above code, import 'Mock' and start some tests
from datetime import datetime
from unittest.mock import Mock

tuesday = datetime(year=2021, month=1, day=1) # This implies that Monday is day '0'
saturday = datetime(year=2021, month=1, day=5) # This implies that Sunday is day '6'

# We are creating a mock of datetime so that we can control it for our test purposes
datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


# Mock .today() to return Tuesday, we are telling our 'Mock' datetime to return today as being Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday, we are telling our 'Mock' datetime to return today as being Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday, you will see you get an exception error here.  This is really cool.  By taking
# control of Python's 'datetime' library by making a 'Mock' of it, we can tell it that it should return today
# as being a day and then test our 'is_weekday()' function to see if it returns correctly.
assert not is_weekday()
'''

from itertools import combinations as cm
def Shortestpath(strArr):
    print(strArr)
    characters = int(strArr[0])
    dictionary = {}
    for j, val in enumerate(strArr):
        dictionary[val] = j
        if j >= 7:
            break
    del dictionary[str(characters)]
    options = strArr[characters + 1:]
    print(dictionary)
    print(options)
    combinations = cm(options, 2)
    for val in combinations:
        print(val)










Shortestpath(["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"])



