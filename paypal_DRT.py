#!/usr/bin/env python
#usage - python -c 'import paypal_DRT; paypal_DRT.DoReferenceTransaction(50, "gbp", "9AB055978X648820L")'
"""
PayPal utility class based on express checkout - Do Reference Transaction 
https://developer.paypal.com/docs/classic/api/#express-checkout
"""

import requests
import urlparse

def DoReferenceTransaction(value,currency,reference_id):
  data = {
    'USER': 'simon.king_api1.opencreates.com',
    'PWD': 'CZ2VRGYFJDLKKHY5',
    'SIGNATURE': 'AFcWxV21C7fd0v3bYYYRCpSSRl31A4Aqi.r5InxXS2IMBR23wu9L3MrG',
    'METHOD': 'DoReferenceTransaction',
    'VERSION': 78,
    'PAYMENTACTION': 'SALE',
    'AMT': value,
    'CURRENCYCODE': currency,
    'REFERENCEID' : reference_id,
  }
  response = requests.post('https://api-3t.sandbox.paypal.com/nvp', data=data)
  print response.text
