#DIP Sticker Generator
Script to help generate pinout images that can be printed and glued to any DIP package microcontroller.

##Dependencies
* svgwrite: `pip install svgwrite`

##Usage
```shell
$ python dipstickgen.py -h
usage: dipstickgen.py [-h] [-s STYLE] inputfile outputfile

Generate a pinout sticker for dual inline packages.

positional arguments:
  inputfile   name of the json pin definition file.
  outputfile  name of the image file.

optional arguments:
  -h, --help  show this help message and exit
  -s STYLE    define a different style to use for your sticker
```

##Contribute
Please fork, modify and issue a pull request. More styles and microcontroller data files are especially welcome.

##TODO
* Create a style that utilizes the aliases for pins.
* Add more processor definitions
* Make some nicer styles.