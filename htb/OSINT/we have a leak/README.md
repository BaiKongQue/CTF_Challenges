# Exploration #
The Prompt is as follows:
> Super Secure Startup's private information is being leaked; can you find out how?

We also get a file to download. Opening the file has a few zips nested inside. The last zip is password protected. The `Username` file (when being extracted) requires a password.

# Username #
Googling "Super Secure Startup" we find their twitter page. Looking at their page one of their posts mentions that "@JTerranwald" is a new employee.

I tried differnt combinations of "JTerranwald" and how it would be a username. I found out that `j.terrandwald` worked! and extracted the folder.

Inside that folder is a `Password` zip that requires a password.

# Password #
Going back to the google result, I see that a Bianka Phelps is a sub result to the first one.

After looking at their twitter page for a while, I found that their post "Our nerds are working hard today! 🤓" has a image that is showing their brainstorm session or something. I almost went passed this because it looked like a poor stock photo, but in this image we can see that their brainstorm session contains the "New Hire" -> "SSH DEFAULT PW" that is "SupSecStart#Winter2018!". Trying this out as the password did not work though.

Going back to the first companies twitter page, I stared at the post when they hired JTerranwald, and realized the date was Mar 25, 2019. So I tried "SupSecStart#Spring2019!" for the time he was hired, and it worked! The folder extracted and contained a txt file with the flag!