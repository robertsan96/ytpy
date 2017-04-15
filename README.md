# Youtube Video Details to JSON (ytpy)
This is a simple Youtube Scraping script in Python that stores default data of a video in a separate json file. Stores the **url**, **title** and the **author**. 

### Usage

Clone the project (or download it) and install the dependencies from the *requirements.txt* file.

```sh
$ https://github.com/robertsan96/ytpy.git
$ cd ytpy
$ pip install -r requirements.txt
```

There are **2 different** modes to run this script: **Quick mode** and **Manual mode**. In the quick mode you'll only give the Youtube URL as an argument. In the manual mode, you pass the url when you're asked (the program will get the data of the video anyway) and asks you after to overwrite the other details if you wish.

**Quick Mode**
```sh
$ python script.py https://www.youtube.com/watch?v=1EBw_da7BZk
Stored. [./videos/video1.json]
```

**Manual Mode**
```sh
$ python script.py
$ URL: https://www.youtube.com/watch?v=1EBw_da7BZk
$ Title [Chris Rea - Road to Hell]: 
$ Author [gree47]: 
Stored. [./videos/video1.json]
```
**TIP: You can change the path of the storage directory, the file name prefix and the extension by changing the properties of *AppConfig* class.**

### Purpose

The main purpose of this script is to help me get used with Python and I didn't focus so much on special cases.
