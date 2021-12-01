# Exploration #
The prompt is as follows:
> Can you find something to help you break into the company 'Evil Corp LLC'. Recon social media sites to see if you can find any useful information.

Doing a quick google search for 'Evil Corp LLC' shows their linkedin page.

In their description they have `HTB{WW91IGNhbiBkbyB0aGlzLCBrZWVwIGdvaW5nISEh}` decoding it reveals `You can do this, keep going!!!`

The link to their website redirects to `whoismrrobot.com` which returns a 503 error.

returning to the google search the next link on the search result is a person's instagram page, and their profile says they work at Evil Corp LLC.

# Instagram #
Looking through all the images the person has, one of them is a images of their laptop and employee badge. Taking a closer look at the image we see that the employee tag contains the flag at the bottom of it!