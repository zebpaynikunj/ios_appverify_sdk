# coding=utf-8

"""
Module to generate TeleSign-compatible JWT strings for MobileVerification

Please check the output of your web services using a service such as
http://jwt.io/

"""

from json import dumps
from datetime import datetime
from base64 import b64decode
from uuid import uuid4

import jwt
from bottle import get, response

from pygenjwt.settings import *
from pygenjwt.ratelimit import *


@get('/v1/token/<phone_number>')
@get('/v1/token/<phone_number>/<xid>')
def get_token(phone_number, xid=None):
    """GET /v1/token/:phone_number/:xid

    Return a JWT auth token based on customer_id and associated secret key.
    This API is rate limited based on phone_number

    :param phone_number: The phone number associated with mobile device requesting token
    :param xid:
    """

    response.set_header('Content-Type', "text/plain")
    response.set_header('Allow', "GET")
    response.status = 200

    try:
        # Rate limit by phone_number as key, and limit specified in settings.
        # This is to emphasize the importance of rate limiting mobile devices requests.
        # This implementation is * NOT PRODUCTION READY *, and should use a reliable
        # store backend with appropriate configurations.
        rate_limit(key=phone_number, limit=RATE_LIMIT)

        # Set token claims
        # Define the token time stamp validity range in seconds
        iss = CUSTOMER_ID.upper()
        iat = int(time()) - TIMESTAMP_DELTA
        exp = iat + VALID_DURATION

        # Unique identifier to verify status of transaction completion from
        # Telesign's get status by xid service
        xid = xid or str(uuid4())

        payload = {
            'iss': iss,
            'iat': iat,
            'exp': exp,
            'phn': phone_number,
            'xid': xid,
        }
        if DEV:
            payload['bta'] = True

        key = b64decode(API_KEY)
        token = jwt.encode(payload, key)

    except RateLimitExceeded:
        # Add logging as required here
        token = ""
        response.status = 403

    except Exception:
        # Add logging as required here
        token = ""
        response.status = 500

    return token


@get('/ping')
def ping():
    """
    GET /ping

    Ping web server, return stuff
    """

    response.set_header('Content-Type', "application/json")
    response.set_header('Allow', "GET")
    return dumps({
        'pinged_on': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        'errors': [{'id': 0, 'description': ""}]
    })
