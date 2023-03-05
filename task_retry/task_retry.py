"""Main module."""

import time
import functools



class RetryOptions:
    def __init__(self, delay_factor=0.2, randomization_factor=0.25, max_delay=30, max_attempts=8):
        """
        Initializes a new instance of the RetryOptions class.

        :param delay_factor: The delay factor to use when calculating the delay time between retries.
        :param randomization_factor: The randomization factor to use when calculating the delay time between retries.
        :param max_delay: The maximum delay time between retries.
        :param max_attempts: The maximum number of attempts to retry the function.
        """
        self.delay_factor = delay_factor
        self.randomization_factor = randomization_factor
        self.max_delay = max_delay
        self.max_attempts = max_attempts

    def delay(self, attempt):
        """
        Calculates the delay time between retries.

        :param attempt: The number of the current retry attempt.
        :return: The delay time in seconds.
        """
        delay_time = pow(2, attempt) * self.delay_factor * (1 + self.randomization_factor * random.random())
        return min(delay_time, self.max_delay)

    def retry(self, fn, retry_if=None, on_retry=None):
        """
        Retries the specified function if it fails.

        :param fn: The function to retry.
        :param retry_if: An optional function that determines whether to retry the function based on the exception that was thrown.
        :param on_retry: An optional function that is called each time the function is retried.
        :return: The return value of the function if it succeeds.
        :raises: Exception if the maximum number of attempts is reached and the function still fails.
        """
        attempt = 1
        while attempt <= self.max_attempts:
            try:
                return fn()
            except Exception as e:
                if retry_if is None or retry_if(e):
                    if on_retry is not None:
                        on_retry(e, attempt)
                    delay_time = self.delay(attempt)
                    time.sleep(delay_time)
                    attempt += 1
                else:
                    raise e
        raise Exception('Max attempts reached, function still failing.')


class RetryOptionsDecorator:
    def __init__(self, delay_factor=0.2, randomization_factor=0.25, max_delay=30, max_attempts=8):
        """
        Initializes a new instance of the RetryOptions class.

        :param delay_factor: The delay factor to use when calculating the delay time between retries.
        :param randomization_factor: The randomization factor to use when calculating the delay time between retries.
        :param max_delay: The maximum delay time between retries.
        :param max_attempts: The maximum number of attempts to retry the function.
        """
        self.delay_factor = delay_factor
        self.randomization_factor = randomization_factor
        self.max_delay = max_delay
        self.max_attempts = max_attempts

    def delay(self, attempt):
        """
        Calculates the delay time between retries.

        :param attempt: The number of the current retry attempt.
        :return: The delay time in seconds.
        """
        delay_time = pow(2, attempt) * self.delay_factor * (1 + self.randomization_factor * random.random())
        return min(delay_time, self.max_delay)

    def __call__(self, fn, retry_if=None, on_retry=None):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= self.max_attempts:
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    if retry_if is None or retry_if(e):
                        if on_retry is not None:
                            on_retry(e, attempt)
                        delay_time = self.delay(attempt)
                        time.sleep(delay_time)
                        attempt += 1
                    else:
                        raise e
            raise Exception('Max attempts reached, function still failing.')
        return wrapper
