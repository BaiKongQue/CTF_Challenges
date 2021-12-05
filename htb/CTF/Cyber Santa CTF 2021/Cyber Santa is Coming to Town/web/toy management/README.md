# Exploration #
The Prompt:
> Toy Management
>
> The evil elves have changed the admin access to Santa's Toy Management Portal. Can you get the access back and save the Christmas?

The page is a simple login page.

# SQL Injection #
I tried to use the following SQL injection to gain access:
```
' or 1=1; -- 
```

and I successfully logged in! meaning that sql injection is working.

I was logged into the dashboard that had a list of toys, but I did not see the flag. After looking at the code for a while I found that the flag is in the list of toys but its `approved` field is set to `0`.

My next thought was to modify this with a sql injection, but after a while I forgot that the login was only using a SELECT to grab a user.

After I relooked at the code I realized that unaproved toys will appear for the Admin. So I tried the following SQL injection:
```
admin';-- 
```

It successfully logged in as admin and I was able to see the flag!