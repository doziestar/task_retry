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


Features
--------
## Class Methods
__init__(self, delay_factor=0.2, randomization_factor=0.25, max_delay=30, max_attempts=8)
Initializes a new instance of the RetryOptions class with the specified parameters.

**delay_factor** : The delay factor to use when calculating the delay time between retries.

**randomization_factor**: The randomization factor to use when calculating the delay time between retries.

**max_delay**: The maximum delay time between retries.

**max_attempts**: The maximum number of attempts to retry the function.

delay(self, attempt)
Calculates the delay time between retries based on the current attempt number.

**attempt**: The number of the current retry attempt.

**Returns**: The delay time in seconds.

retry(self, fn, retry_if=None, on_retry=None)
Retries the specified function if it fails.

**f**n: The function to retry.

**retry_if**: An optional function that determines whether to retry the function based on the exception that was thrown.

**on_retry**: An optional function that is called each time the function is retried.

**Returns**: The return value of the function if it succeeds.

**Raises**: Exception if the maximum number of attempts is reached and the function still fails.

* TODO

Credits
-------


