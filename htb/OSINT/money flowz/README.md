# Exploration #
The prompt given is:
> Frank Vitalik is a hustler, can you figure out where the money flows?

My first thoguht is to Google this person and see what information I can find on them.

# Frank Vitalik #
Just doing a regular search for Frank Vitalik on Google, the first result contains a user on reddit with the description
> Cryptocurrency enthusiast @htb My Twitter account @frankvitalik was restricted

Taking a look at their profile, I see that one of their posts has a link in it
> Incredible SCAM giveaway! you can get free coins!
>
> Follow the link to get free fake coins!!
>
> https://steemit.com/htb/@freecoinz/freecoinz

Following the link goes to a page with a post claiming to double your ETH.
> Super Ethereum SCAM Giveaway
> 
>(?)Deposit 10X ETH to this address and get 20X ETH back!!(?)
> 
>0x1b3247Cd0A59ac8B37A922804D150556dB837699
> 
>you can get free coinz!

There is also one comment that says
> Wow! I can't believe they are giving free coins into the ropsten net!

which is also created by the same user that made the post.

Etherium's block chain is public, so I can see the transaction history of the given address. I went to etherscan.io to see the transaction history of `0x1b3247Cd0A59ac8B37A922804D150556dB837699`. The immediate page says "There are no mathcing entries" but we can see that there are 2 other accounts on the block chain.

Checking what they are we see there are 2 accounts:
1. Ropsten Testnet
2. Georli Testnet

Ropsten Testnet is similar to what I saw in the comments above. Going to the page we can see there are a lot of incoming transactions to this account.

Using the website GUI to filter only outgoing transactions, we can see that there are two outgoing transactions. Checking the first one there is input data connected to it. Changing the view to UTF-8 we can find the flag!

Checking the other outgoing transaction and its input gives us the same flag!