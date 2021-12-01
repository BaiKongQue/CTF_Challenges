# Exploration #
The prompt given says
> Customers of secure-startup.com have been recieving some very convincing phishing emails, can you figure out why?

Checking out the website shows nothing but a simple GoDaddy front page of related searches.

Because they are receiving phishing emails, they are not actually using the website, probably just the domain.

The next idea is to check their SPF, DMARC, and DKIM records.

# SPF, DMARC, and DKIM #
There are different ways to check these records, but I will use the `dig` command in the console
```
dig TXT secure-startup.com _dmarc.secure-startup.com _dkim.secure-startup.com
```

This will retrieve the TXT records of their SFP, DMARC and DKIM records.

This was the result:
```
; <<>> DiG 9.16.15-Debian <<>> TXT secure-startup.com _dmarc.secure-startup.com _dkim.secure-startup.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56911
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;secure-startup.com.            IN      TXT

;; ANSWER SECTION:
secure-startup.com.     1800    IN      TXT     "v=spf1 a mx ?all - HTB{THIS_IS_WHERE_TO"

;; Query time: 47 msec
;; SERVER: 75.75.75.75#53(75.75.75.75)
;; WHEN: Tue Nov 30 22:53:11 EST 2021
;; MSG SIZE  rcvd: 101

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 46925
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;_dmarc.secure-startup.com.     IN      TXT

;; ANSWER SECTION:
_dmarc.secure-startup.com. 1800 IN      TXT     "v=DMARC1;p=none;_FIND_THE_FLAG}"

;; Query time: 43 msec
;; SERVER: 75.75.75.75#53(75.75.75.75)
;; WHEN: Tue Nov 30 22:53:11 EST 2021
;; MSG SIZE  rcvd: 99

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 50541
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;_dkim.secure-startup.com.      IN      TXT

;; AUTHORITY SECTION:
secure-startup.com.     600     IN      SOA     ns69.domaincontrol.com. dns.jomax.net. 2020070800 28800 7200 604800 600

;; Query time: 19 msec
;; SERVER: 75.75.75.75#53(75.75.75.75)
;; WHEN: Tue Nov 30 22:53:11 EST 2021
;; MSG SIZE  rcvd: 121
```

After analyzing the results, we can see that the company has not properly configured their SPF, DMARC, and DKIM records. This could leave them suseptible to phishing attacks.

Also, it can be seen that parts of the flag is in the SFP and DMARC records, putting them together we get the full flag, completing the challenge.