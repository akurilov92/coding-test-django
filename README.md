# Coding Test Django Python


### Running locally

To run the project locally:
   1.  `docker-compose build`
   2.  `docker-compose up`

This should start both services on your machine.

the `user_birthday` service will be at `localhost:8001`

the `letter_digit` service will be at `localhost:8002`

### Tests


To run the tests for `birthday_service`:

    docker-compose run user_birthday_web python ./user_birthday/manage.py test user_birthday

To run the tests for `letter_digit`:

    docker-compose run letter_digit_web python ./letter_digit/manage.py test letter_digit



### Description
#### Birthday service

The first task was to create a service with the following endpoints:

*  endpoint which accepts a list of JSON objects as POST-payload("birthday" is unique)

    This endpoint is at `/users-insert-bulk`. 
    
    You can insert multiple users or a single user.
    
    As specified, `birthday` must be unique.
    
    Runnable example: 

        curl -d '[{"first_name": "alex", "last_name": "kurilov", "email": "akurilov92@gmail.com","birthday": "18.12.1992"}, {"first_name": "Bob", "last_name": "Smith", "email": "bob.smith@gmail.com","birthday": "01.02.1983"}]' -H "Content-Type: application/json"  -X POST '0.0.0.0:8001/users-insert-bulk'

* endpoint which returns a list of objects, filtered by the following parameters (birthday)
    - from (example: from=%d%m)
    - to (example: to=%d%m)

    I renamed `from` and `to` to `from_dt` and `to_dt` for convinience
    
    This endpoint is at `/users-from-to`. 
    
    As specified, it requires two parameters to filter the users by birthday.
    
    Runnable example:
    
        curl 'localhost:8001/users-from-to?from_dt=0112&to_dt=1812'
    
* endpoint which returns the average age of all records in the database

  This endpoint is at `/users-average-age`. 
  
  It requires no parameters and returns the average age of all users.
  
  The method uses simple in-build Django caching; the cache lives for 60 seconds.
  
  In a real production environment we would use something like Memcached and probably have a larger timeout value. 

  Runnable example:
    
        curl 'localhost:8001/users-average-age'
    
#### Letter digit service

  The second task was to create a service with a single endpoint that takes a string with letters and digits and returns a list of all
  possible upper & lowercase variations.
  
  This endpoint is at `/letter-permutation`. 
  
  It requires a single parameter, `input_string`.
  
    curl 'localhost:8002/letter-permutation?input_string=a2B'
  



