Coding Test Django Python
The challenge consists of creating two services:
- user_brithday
- letter_digit
Conditions:
- Make use of docker and docker-compose
- Make use of unit tests
1. User Birthday Service
a. Create an API endpoint which accepts a list of JSON objects as POST-payload.
- Store the data in a Postgres Database
- The email address should be unique
- All fields are required
Payload Example:
b. Create an API endpoint which returns a list of objects, filtered by the following
parameters (birthday)
- from (example: from=%d%m)
- to (example: to=%d%m)
c. Create an API endpoint which returns the average age of all records in the database.
Think about caching.
2. Letter Digit
Create an API-Endpoint taking a string with letters and digits and returning a list of all
possible upper & lowercase variations.
Example: (a2B => [a2b, a2B, A2b, A2B])