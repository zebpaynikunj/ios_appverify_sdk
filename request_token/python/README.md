pygenjwt
===============

Basic JSON Web Token Generator for python 2.x

Please note that this sample is designed for basic functionality 
testing, and is not suitable for use in production. 

==============

Dependencies:

- bottle
- pyjwt


Installation
------------

    git clonehttps://github.com/TeleSign/ios_appverify_sdk.git
    cd ios_appverify_sdk/request_token/python
    python setup.py develop
    
Configuration
-------------

    cd ios_appverify_sdk/request_token/python/pygenjwt
    Open settings.py in an IDE

<b>Required</b>
<ol>
<li>Update customer_id to the one obtained from Telesign</li>
<li>Update api_key to the one obtained from Telesign</li>
</ol>

<b>Optional</b>
<ol>
<li>Update the rate limit as per your requirements</li>
<li>Set DEV=False if using in non-testing environment</li>
</ol>
