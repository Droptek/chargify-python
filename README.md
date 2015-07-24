A [Chargify API](https://docs.chargify.com/api-introduction) client written in Python.

Basic Usage
-----------

See the test cases for a full list of examples for all supported API calls.

	chargify = Chargify('api_key','subdomain')

List products

    # GET http://subdomain.chargify.com/products.json
    res = chargify.products()

List customers

    # GET http://subdomain.chargify.com/customers.json
	res = chargify.customers()

List a specific customer

    # GET https://subdomain.chargify.com/customers/123.json
	res = chargify.customers(customer_id=123)

Create a customer

    # POST https://subdomain.chargify.com/customers.json
	res = chargify.customers.create(data={
        'customer':{
            'first_name':'Joe',
            'last_name':'Blow',
            'email':'joe@example.com'
        }
    })

Update a customer

    # PUT https://subdomain.chargify.com/customers/123.json
    res = chargify.customers.update(customer_id=123,data={
        'customer':{
            'email':'joe@example.com'
        }
    })

Create a subscription

    # POST https://subdomain.chargify.com/subscriptions.json
    res = chargify.subscriptions.create(data={
        'subscription':{
            'product_handle':'my_product',
            'customer_attributes':{
                'first_name':'Joe',
                'last_name':'Blow',
                'email':'joe@example.com'
            },
            'credit_card_attributes':{
                'full_number':'1',
                'expiration_month':'10',
                'expiration_year':'2020'
            }
        }
    })

Cancel a subscription

    # DELETE https://subdomain.chargify.com/subscriptions/123.json
    res = chargify.subscriptions.delete(subscription_id=123,data={
        'subscription':{
            'cancellation_message':'Goodbye!'
        }
    })

Migrate a subscription

    # POST https://subdomain.chargify.com/subscriptions/123/migrations.json
    res = chargify.subscriptions.migrations.create(subscription_id=123,data={
        'product_id':1234
    })

Add a one time charge to a subscription

    # POST https://subdomain.chargify.com/subscriptions/123/charges.json
    res = chargify.subscriptions.charges.create(subscription_id=123,data={
        'charge':{
            'amount':'1.00',
            'memo':'This is the description of the one time charge.'
        }
    })

List transactions for a subscription

    # GET https://subdomain.chargify.com/subscriptions/123/transactions.json
    res = chargify.subscriptions.transactions(subscription_id=123)

Get customer's subscritptions

    # GET https://subdomain.chargify.com/customers/123/subscriptions.json
    res = chargify.customers.subscriptions(customer_id=123)
