# Blog
#### Blog Application created on 14/09/2018
#### Author: **Tony Kioko**
## Description
The Blog is a web application where you can create and share your opinions and other users can read and comment on them. The user can also subscribe to the app to be informed of a new post via their email.

## User Stories
* As a user, I would like to view the blog posts submitted
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to alerted when a new post is made by joining a subscription.
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Create user account | **Click Sign Up button** | New user registered |
| Welcome email | **On sign Up** | sends welcome email to new user|
| Display posts | **On the Home page** | Posttches by writers displayed per time of posting |
| See full post | **Click reaf full post/post title** | Read full post and view comments |
| Comment on Post | **Click comment on Post**  | Comment created for that specific post |
| Create post | **Click New Post**  | Directed to form where writer fill post title and content  |
| Update Post | **Click Update button** | Post created directed to form to update post |
| Delete post | **Click Delete Post button** | Post deleted |


## Setup/Installation Requirements.
* Git clone https://github.com/TonyKioko/TheBlog or download and unzip the repository from github.
* Have python3.6 installed in your machine
* Navigate into cloned file using the terminal.
* Run python3.6 -m venv --without-pip virtual to create a virtual environment.
* Run source virtual/bin/activate to activate the above created virtual environment.
* To run the app, type ./start.sh from your virtual environment on the terminal. In your favorite browser, open the link provided by the local host.

### Live Link ###
https://terabyte.herokuapp.com/

## Technologies used ##

* Python 3.6
* Flask
* PostgreSQL - Database
* Bootstrap

## Test Driven Development
* Testing was done using python inbuild test tool called unittest


## Known Bugs 
There are no known bugs.

 
### License
This project is licensed under the MIT Open Source license,Copyright (c) 2018 [Tony Kioko](https://github.com/tonykioko/)