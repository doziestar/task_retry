=================
Python Task Retry
=================


.. image:: https://img.shields.io/pypi/v/task_retry.svg
        :target: https://pypi.python.org/pypi/task_retry

.. image:: https://img.shields.io/travis/doziestar/task_retry.svg
        :target: https://travis-ci.com/doziestar/task_retry

.. image:: https://readthedocs.org/projects/task-retry/badge/?version=latest
        :target: https://task-retry.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/doziestar/task_retry/shield.svg
     :target: https://pyup.io/repos/github/doziestar/task_retry/
     :alt: Updates



 this package offers an easy-to-use and flexible solution for implementing retry functionality in Python programs, helping to reduce the impact of transient errors and improve the reliability of the software.


* Free software: MIT license
* Documentation: https://task-retry.readthedocs.io.

Usage
-----
```python
# Define the function to be retried
def my_function():
    # Do some stuff that might fail
    pass

# Create an instance of RetryOptions with default options
options = RetryOptions()

# Retry the function until it succeeds or reaches the maximum number of attempts
result = options.retry(my_function)

# You can also specify a retry_if function and an on_retry function
def retry_if_exception(e):
    return isinstance(e, MyException)

def on_retry_exception(e, attempt):
    print(f'Function failed on attempt {attempt}, error: {e}')

options.retry(my_function, retry_if=retry_if_exception, on_retry=on_retry_exception)
```

Or Use As Decorator
-------------------
```python
@RetryOptionsDecorator()
def my_function():
    # code to retry

@RetryOptionsDecorator(max_attempts=5)
def my_function():
    # code to retry


@RetryOptionsDecorator(retry_if=retry_if_exception, on_retry=on_retry_exception)
def my_function():
    # code to retry
```


Features
--------

## Class Methods
__init__(self, delay_factor=0.2, randomization_factor=0.25, max_delay=30, max_attempts=8)
Initializes a new instance of the RetryOptions class with the specified parameters.

**delay_factor** : The delay factor to use when calculating the delay time between retries.

**randomization_factor** : The randomization factor to use when calculating the delay time between retries.

**max_delay** : The maximum delay time between retries.

**max_attempts** : The maximum number of attempts to retry the function.

delay(self, attempt)
Calculates the delay time between retries based on the current attempt number.

**attempt** : The number of the current retry attempt.

**Returns** : The delay time in seconds.

retry(self, fn, retry_if=None, on_retry=None)
Retries the specified function if it fails.

**fn** : The function to retry.

**retry_if** : An optional function that determines whether to retry the function based on the exception that was thrown.

**on_retry** : An optional function that is called each time the function is retried.

**Returns** : The return value of the function if it succeeds.

**Raises** : Exception if the maximum number of attempts is reached and the function still fails.

* TODO

Credits
-------


