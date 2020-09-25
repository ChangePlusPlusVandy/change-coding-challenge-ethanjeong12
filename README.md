# Change++ 2020 Coding Challenge

## TweetGame - Elon or Kanye?

## Framework
I used Django framework to create this game.
In game/views.py, I have four functions: get_random_text, determineAnswer, index, and result.
<ol>
<li> get_random_text() loads tweets from each user, merges the total tweets from two users, and returns the randomtweet to the index function.</li>
<li> Then, determineAnswer() function determines the answer of the game using Tweeppy search function. And, it returns that answer to the index function
<li> index function returns the random tweet with 'index.html' in GET method. </li>
<li> Whenever the user submits their answer, we read the user input with POST method and the let the user know if he or she got the answer correctly or incorrectly with an URL(end of url, there's msg). </li>
<li> User can repeat this process until the user decides to view the result. If the result button is hit, my program will redirect the user to 'result.html' page and display the statistics. </li>
</ol>

## How to run the game on your local server
<ul>
<li> First, start your local server, and type "yourlocalserver/tweets/display" (i.e. "http://127.0.0.1:8000/tweets/display" </li>
<li> The way I did it was I ran a server with "python manage.py runserver" on my terminal and typed "http://127.0.0.1:8000/tweets/display"</li>
<li> Then, you'll see the main page where you can play the game. The result after each submission will be shown
at the end of each url after msg, and the final result will be shown at "yourlocalserver/tweets/end"</li>
</ul>

## Feedback on the project
<ul>
<li>I've only done web developing as a backend developer, so the concept of returning the result in django with separate HTML files and forms was fairly new to me. Since I have little experience with frontend developing, I wish I had more time to learn React so that I could make prettier website.</li>

<li> The reason why I used Django is because it's the framework that I'm most comfortable at. I know very basics about Node.js, and I actually wanted to try Node.js, but with the given time, I decided to use Django framework.</li>
<li> I spent a long time trying to figure out how to return the HttPmessage with HttpResponseDirect, but I couldn't figure out how to return both, so I ended up returning the answer in the URL, which is less than ideal. If I had more time, I would have used Django.messages, return the message first and then redirect the page.</li>
<li> Also for counting the total play time and the correct time, I created the model and was going to create a query in my databse and update the query everytime the user plays the game or the user gets it right. And, delete my DB and reset the PK every time user finishes the game. But, eventually, I decided that it was unnecessary to save the records and there was an easier way: creating global variables and updating them.</li>
</ul>

## Finally,
I think my biggest strength is that I know how to teach myself new concepts. I've already done small projects in the past where I had to learn a new language or new framework, so I know what to google or where to look for. I'm aware ChangePlusPlus usually use Node.js and React, and even though I don't know anything about React and only basics about Node.js, I'm very confident that I can teach myself those pretty quickly.  
