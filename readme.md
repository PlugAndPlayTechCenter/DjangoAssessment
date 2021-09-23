# Introduction

Note: This scenario is based on the latest versions of Django and Django Rest Framework. You can get it up running by:
1. Migrate default database: python manage.py migrate
2. Create super user (currently) : email admin@assessment.com username: admin pwd: pnptc123
3. Run server: python manage.py runserver
4. App will be accessible at http://localhost:8000 and the admin panel at http://localhost:8000/admin/

## The Scenario
Our application, PlayBook is an innovation platform, a key aspect of innovation is being able to meet and analyze a large footprint of startups, for that purpose the team built an API to help manage the startups database for our staff.

The API has been in use for several months and our users have come several improvements to it.

Please help our staff by completing below tasks.

Please take your time to ask any question that can help you craft your software.


## The API

The current API can be accessed at http://localhost:8000 and presents 3 management endpoints:
```json
  {
    "users": "http://127.0.0.1:8000/users/",
    "groups": "http://127.0.0.1:8000/groups/",
    "startups": "http://127.0.0.1:8000/startups/"
  }
 ``` 
 The "startups" endpoint allow us to view, edit and remove a startup:

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```json
{
    "count": 11,
    "next": "http://127.0.0.1:8000/startups/?page=2",
    "previous": null,
    "results": [
        {
            "startup_name": "JetSon Engines",
            "website": "https://jetson.engines",
            "one_liner": "The best Jet Engines that New Zealand can produce.",
            "description": "New Zealand best engineers have created a fantastic engine that can run in low fuel.",
            "city": "Auckland",
            "founded": "2017",
            "money_raised_usd": "1000000.00",
            "country": {
                "country_name": "New Zealand",
                "country_code": "NZ"
            },
            "stage": {
                "stage_name": "Series A"
            },
            "created": "2021-09-16T17:41:28Z",
            "updated": "2021-09-16T17:41:28Z"
        }
 ...
 }
```


# Get the code

You can choose where to develop this project. Pick the IDE you are most confortable with. But make sure it runs.

If you are not sure, we recommend **forking** it on [GitHub](https://github.com/PlugAndPlayTechCenter/DjangoAssessment). Don't forget to click on the 'FORK' button!


# Tasks
## Task 1: Our team will like to have a logo and a list of contacts for the startups so please add them to the Startup model and to all places needed in order to be able to serialize the new info and deserialize it along with the rest of the startup info. The contacts model should contain at least position, company, email and full name of the contact. A contact cannot be in more than one startup.
Once you are done answer these questions:

1. How will yo ensure an optimal performance of the new serializer for startups?
2. How will you implement pagination? Why?
3. Please identify what UNIT and INTEGRATION tests will this API require.


## Task 2: Plug and Play partners with a huge list of mentors, corporate partners and other stakeholders. We want to be able to track which partner has introduced a startup to us. Create a new model named Prescriptor, this new model should contain the same info as a contact but in this case a contact can be linked to several startups. You will need fill up the new Prescriptor model with some sample data.

Note: You are allowed refactor the original contact model in order to create a clean and reusable design 

Nice to have: The Prescriptor serializer should include the total number of startups that the prescriptor has introduced to us.

Once you are done answer these questions:

1. Explain your design. What other options have you considered and why did you choose that one.
2. Do you know the content type framework? What use cases do you think is fit for purpose?
3. What tasks, other than coding, will you perform before sending to your peers for code review?


## Task 3: Plug and Play Compliance team has requested us that we introduce some security in the API so only admins and the users that have been added as "to be shared with" can get access to the startup info. Please improve the model and the endpoint to apply the required security.

Once you are done answer these questions:

1. How did you approach the new security needs? Why?
2. Mention some common API security issues and how will you mitigate or remove them.


# Wrap-up
We thank you very much for your time and wish you the best of luck in this process.




