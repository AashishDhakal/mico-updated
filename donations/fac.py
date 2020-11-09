import zeep
from zeep import Client
import time
import hashlib
import base64
import datetime

from django.conf import settings


passwd = settings.FAC_MERCHANT_PASSWORD
fac_id =  settings.FAC_MERCHANT_ID
acquirer_id = settings.FAC_ACQUIRER_ID
currency = settings.FAC_CURRENCY_CODE

test_endpoint = 'https://ecm.firstatlanticcommerce.com/PGService/Services.svc?wsdl'
live_endpoint = 'https://marlin.firstatlanticcommerce.com/PGService/Services.svc?wsdl'

def msTimeStamp():
    return int(round(time.time() * 1000))

def authorize(cvv, expiry, card_no, amount, order_number, issue_number='', start_date=''):
    
    string_to_hash = f'{passwd}{fac_id}{acquirer_id}{order_number}{amount}{currency}'
    string_to_hash = str.encode(string_to_hash)
    hash = hashlib.sha1(string_to_hash)
    signature = base64.b64encode(hash.digest())
    signature = signature.decode('utf-8')
   
    card_details = {
        'CardCVV2': f'{cvv}',
        'CardExpiryDate': f'{expiry}',
        'CardNumber': f'{card_no}',
        'IssueNumber': f'{issue_number}',
        'StartDate': f'{start_date}',
    }

    transaction_details = {
        'AcquirerId': f'{acquirer_id}',
        'Amount': amount,
        'Currency': f'{currency}',
        'CurrencyExponent': 2,
        'IPAddress': '',
        'MerchantId': fac_id,
        'OrderNumber': f'{order_number}',
        'Signature': signature,
        'SignatureMethod': 'SHA1',
        'TransactionCode': '0',
    }

    AuthorizeRequest = {
        'CardDetails': card_details,
        'TransactionDetails': transaction_details,
        'MerchantResponseURL': settings.MERCHANT_RESPONSE_URL
    }
    try:
        client = Client(wsdl= live_endpoint if settings.FAC_MODE_PROD else test_endpoint)
        result = client.service.Authorize3DS(AuthorizeRequest)
    except zeep.exceptions.Fault as fault:
        result = client.wsdl.types.deserialize(fault.detail[0])
    return result['HTMLFormData']
