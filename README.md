# Ticketmaster, News, & Google Maps Embed APIs

The Google Maps API challenge made making requests to a 3rd Party API very easy. All we needed to do was copy and paste. We mentioned that it would actually be much more difficult to actually make requests in real life and this challenge is for that.

Typically, when you make a request to a 3rd Party API, you read through the documentation, make a [Request](https://realpython.com/python-requests/) (you'll need that link later), and get a [Response](https://realpython.com/python-requests/#the-response). Once you parse through the response, you can use that data to achieve your application goals.

This challenge is going to be rather nebulous and that's by design. Most software engineering features are going to come as a laundry list of wants from your client. It is up to you to figure out how it works and implement it.

# Agile Development
When developing an app or feature using the Agile Methodology, you want to write the new feature from the perspective of the end user. This is called a __User Story__ in agile developement.

For example: __As a user, I want to be able to search for artist's concerts from the Home Page and be redirected to a list where their next 5 concerts will be displayed on a map and the 10 most recent news about that artist sorted by article popularity.__

Each app has multiple __User Stories__.

[Agile User Story Overview](https://www.atlassian.com/agile/project-management/user-stories)

# Client Request (Group Project)

You've been contacted by a client to build a new application. They'll pay you **_\$50,000_** to build a Minimum Viable Product (MVP) over the next 4 days. If all goes well, they want to hire you and your team to continue building out the application for 6 months. They have a budget of **_\$400,000_**, which will go to you and your team.

### High Level Overview from the client

Your client would like to build an application which allows users to search for concerts and news.

![](https://github.com/oscarplatoon/curriculum/blob/master/page-resources/concerts_and_news_app.gif)

Here are some __MUST HAVES__ from the client regarding the functionality of the MVP. (Required functionality)
1. Must be able to search artist's concerts.
2. Must be able to display the concert's locations on a map.
3. Must be able to display news related to the artist that the user searched for.
4. Must be able to search for news independently from the artist. Ex: Search for news about `Coding Bootcamps`.
5. Must be 'pretty'.

Here are some __NICE TO HAVES__ from the client. (Not required but if you implement these features the more likelihood they'll hire you and your team)
1. The ability to create Users
2. The ability for Users to login
3. The ability for Users to tag `I want to go` to their favorite artist's concerts.
4. The ability for Users to view a list of concerts they've tagged `I want to go`.

## User Stories
- #### Must haves
1. As a user, I want to be able to search for artist's concerts from the Home Page and be redirected to a list where their next 5 concerts will be displayed on a map and the 10 most recent news about that artist sorted by article popularity. (Each concert will have it's own Google Map, don't display multiple points on a single map)
2. As a user, I can search for news based on a search query/topic from the NavBar, the search bar should be on every page of the application. After typing in my search query and pressing 'search news' I should be redirected to a dedicated page showing the 20 most recent news article for input search query/topic.
3. As a user, I can navigate to a __dedicated search news page__ from the Nav Bar where it displays the Top Headlines in the US by default.
4. As a user, I can filter news based on categories `business`, `entertainment` `general` `health` `science` `sports` `technology` on the __dedicated search news page__.
5. As a user, I can search for news based on a search query/topic on the on the __dedicated search news page__ and sort by `relevancy` & `popularity`.
- #### Nice to haves
6. As a user, I can navigate to a dedicated signup page and type in a username and password and click `Signup` and an alert will show if I successfully signed up with a link to redirect me to the `Login` page.
7. As a user, I can navigate to a dedicated login page and type in a username and password and click `Login` and be redirected to the Home Page upon successfull login.
8. As an Authenticated User, after searching for artist's concerts I can tag `I want to go` to a specific concert (similar to a `like` button on Facebook or `heart` on Twitter).
9. As an Authenticated User, I can navigate to dedicated `My Concerts` page that will display a list of concerts I've tagged `I want to go`.

## Resources
Look up the available endpoints on [Ticketmaster's Free API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/). Which ones do you need to figure out the next 5 concerts of the artist in question? You'll be making lots of requests and getting lots of responses. Ticketmaster gives you 5000 free calls per day.
<details>
<summary>Ticketmaster API Hint </summary>
Look at the <strong>'keyword'</strong> query parameter.
</details>
<br>

Use the [News API](https://newsapi.org/) to search for News articles based off several criteria. Research the available endpoints and `request parameters`. This API has great documentation and is pretty straight forward. (NOTE: You DON'T need to use a Client Library!)

Use the Google Maps Embed API from the lecture to display concert locations.

Use Python's [Request](https://realpython.com/python-requests/) library and know what to do after you get the [Response](https://realpython.com/python-requests/#the-response).

### Example Request/Response Flow

![](https://github.com/oscarplatoon/curriculum/blob/master/page-resources/ticketmaster_req_res.png)

## How to start?
__Get organized!__
- Have one person in your group create a Github repository on their personal Github or fork over this repository and create a template Django Project and push it to the newly created or forked repository.
- In your repository settings, under `Manage access` invite your Group Members.
- Other Group Members, DON'T FORK the group member who created the repository to your own Github, just clone it to your machine so you're all working on the same repository.
- When working on features, work on seperate `branches`. Never work directly on the `master` branch. You can add `Branch protection rules` for your repository to prevent you from pushing code straight to the `master` branch.
- Look into Trello or another project management tool to stay organized.
- __Pair Program!__

