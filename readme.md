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

If you are not sure, we recommend **forking** it on [StackBlitz](https://stackblitz.com/github/PlugAndPlayTechCenter/FrontPairScreening). Don't forget to click on the 'FORK' button!


# Tasks
## Task 1: Bring the data from the REST API to the component and show several users in a bootstrap grid.
Once you are done answer these questions:

1. How will you handle backend API errors? Describe in detail the approach and explain why you opted for it
2. How will you implement pagination? Why?
3. How will you store the data retrieved from the backend?
4. Please identify what UNIT and INTEGRATION tests will this component require.


## Task 2: Code the functionality of the "Mark as favourite" button. Design the calls to the backend service
Nice to have: A section showing only “my favorites” on the same page.

Once you are done answer these questions:

1. What calls to the backend API have you used? What data entities do you need? Why?
2. What tasks, other than coding, will you perform before sending to your peers for code review?
3. What type of security controls will this functionality require at both ends (client and server side)?
4. What improvements will you suggest to your team and customer for this solution? Why?

# Wrap-up
We thank you very much for your time and wish you the best of luck in this process.




