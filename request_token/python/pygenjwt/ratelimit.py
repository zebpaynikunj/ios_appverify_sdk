# coding=utf-8

"""
Module to rate limit JWT being generated to a specified value

This implementation is NOT thread safe, reliable or precise, and should not be used
in a production environment. The primary purpose of this is to emphasize the use
of a reliable rate limiting along with token generation on the server side.

"""

from time import time
from pylru import lrucache
from pygenjwt.settings import CACHE_SIZE

cache = lrucache(CACHE_SIZE)


class RateLimitExceeded(Exception):

    def __init__(self, key, limit,  *args, **kwargs):
        super(RateLimitExceeded).__init__(self, *args, **kwargs)
        self.message = "Rate limit exceeded for key: {}, limit: {}".format(key, limit)


def rate_limit(key, limit):
    if key is None:
        raise ValueError("rate_limit: parameter 'key' cannot be None")

    try:
        int(limit)
        if limit < 1:
            raise ValueError
    except:
        raise ValueError("rate_limit: parameter 'limit' is not a positive integer: {}".format(limit))

    # NOTE: The key is formed with the current seconds rounded
    # down. So each request inside of a 1 second block will create the
    # same key during that second, causing same cache key to be reused.
    rkey = "{}:{}".format(key, int(time()))

    if rkey in cache:
        cache[rkey] += 1
        curr = cache[rkey]
    else:
        curr = cache[rkey] = 1

    if curr > limit:
        raise RateLimitExceeded(rkey, limit)

    return True
