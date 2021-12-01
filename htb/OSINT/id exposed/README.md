# Exploration #
The prompt is as follows:
> We are looking for Sara Medson Cruz's last location, where she left a message. We need to find out what this message is! We only have her email: saramedsoncruz@gmail.com

One idea is that her location will correspond to being on google maps, and it may be a comment post.

Unfortunately, Google doesn't let you search for other contributors on Google maps, so we will need to extract her ID in order to search for her contributions.

# Extracting a Gmail ID #
These are the steps we will take to extract the ID:
1. login to our Gmail account
2. click the "+" to start a new Google Hangout
3. type `saramedsoncruz@gmail.com` in the search bar
4. open inspect element and inspect the `li` of the result that pops up
5. in the `li` that pops up, it should have a attribute `oid`, go ahead copy the value (`117395327982835488254`) to the clipboard

# Google Maps Contributor Page #
we will go directly to the contributor profile on google maps with the ID we got, so it will look like the following: `https://www.google.com/maps/contrib/117395327982835488254`

The user that we find is "Flag Watcher" showing that we are in the right place. Looking at the "Reviews" tab we see they made two reviews on different locations. Clicking on one of the reviews we find the flag in their description!