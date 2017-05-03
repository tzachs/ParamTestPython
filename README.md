# Parameterized test python example

This is an example on how to create a test with dynamic parameters

## How to use

Create a directory (or just clone this project)
Download both 'TestParam.py' and 'data.json'
Run using 'python TestParam.py'

You should see the following output:

```
Setup
test1
test2
F
======================================================================
FAIL: test_loop (__main__.TestParam)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestParam.py", line 14, in test_loop
    self.assertEqual(item["number1"] + item["number2"], item["result"])
AssertionError: 5 != 6

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

## Limitations

If one of the tests fails, the method stops running
