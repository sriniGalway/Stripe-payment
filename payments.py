import stripe

#usage for Debit / credit card 
#python -c 'import payments; payments.request_stripe_payment(50, "usd", "tok_visa", "sk_test_BQokikJOvBiI2HlWgH4olfQ2")'
#usage for apple pay 
#python -c 'import payments; payments.request_stripe_payment(50, "gbp", "tok_1APClXCsWauvTIpZDdalC4Sg", "sk_test_BQokikJOvBiI2HlWgH4olfQ2")'

'''
Payments using stripe API for credit / debit card and apple pay
Documentation : https://stripe.com/docs

'''
#test stripe_key = sk_test_BQokikJOvBiI2HlWgH4olfQ2
cust_token = 'tok_1ATtP92eZvKYlo2C6gfGn1cR'   #test token
def create_token(number,exp_month,exp_year,cvc):
    try:
        stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
        cust_token = stripe.Token.create(
            card={
            "number": number,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc
            },
        )
        print cust_token.id
    except Exception, e:
        # This will handle any issue occurred
        body = e.json_body
        err = body['error']
        print "Message is: %s" % err['message']

def request_stripe_payment(value,currency,cust_token, charity_key):
    stripe.api_key = charity_key
    try:
        # Charge the user's card:
        charge = stripe.Charge.create(
            amount=value,
            currency=currency,
            description='Payment was done using stripe',
            source=cust_token
        )
        print charge
        status = charge.status
        if status == 'succeeded':
            print "The payment was made successfully by Open Mobile Payment using " + charge.source.brand
        else:
            print "The payment was not succeded by Open Mobile payment"
    except stripe.error.CardError, e:
        #Card related error is handled in this exception
        print "There was an issue in payments"
        body = e.json_body
        err = body['error']
        print "Status is: %s" % e.http_status
        print "Type is: %s" % err['type']
        print "Code is: %s" % err['code']
        print "Message is: %s" % err['message']
    except Exception, e:
        # This will handle any issue occurred
        body = e.json_body
        err = body['error']
        print "Message is: %s" % err['message']
