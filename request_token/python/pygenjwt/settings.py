# coding=utf-8

# This flag is set for development usage
DEV = True

# Any compensation to be subtracted in seconds between generator and end server
TIMESTAMP_DELTA = 10

# Duration in seconds that the token should be valid for
VALID_DURATION = 90

# Customer ID used as the "iss" claim Replace with actual customer
# ID. Looks like: 554b1467-3cf3-43ca-94a7-b30bf69f2fc6
CUSTOMER_ID = "your_telesign_customer_id"

# Base64-encoded APIKey that you received from TeleSign
# CustomerServices/TeleMaster for this product. Looks like:
# BOKg05XbCBh8iZ1fB/NjHSKItsR54OvO+nMPH6RJQCRaPI/qcM23c9lxGsxz/Cg7k6xYKEdqqKybqz+41MBYmdOj
API_KEY = "eW91cl90ZWxlc2lnbl9hcGlfa2V5" # "your_telesign_api_key"

# Size of the rate limit cache. The maximum number of key/value
# pairs you want the cache to hold for rate limiting.
CACHE_SIZE = 10

# Number of requests per second to allow with rate limiting
RATE_LIMIT = 1