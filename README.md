# Spotify Looping Bot

API-Less Python3 Spotify bot which reproduces an Artist's songs list or album for the minimum amount of time in order to be considered as 'listened' by Spotify. This will be running on your machine using your browser and a command prompt which will be executing this project.

## Prerequisites

This project was built with [Python3](https://www.python.org/), get the latest version from [here](https://www.python.org/downloads/).
In order to run succesfully this project you'll need to install  [Selenium](https://www.selenium.dev/) python language bindings for its Webdriver. Also, you must have an account registered in [Spotify](https://www.spotify.com/). Without these requirements the project won't run.

To install the Python language bindings for Selenium WebDriver, we will use [pip](https://pypi.org/project/pip/). You must run this on the command prompt to install it 
```
pip install selenium
```
right after it is installed, you must download your favorite browser web driver. Here I leave a list for Chrome and Firefox web drivers, keep in mind you must download one that works with the current version of your browser.

* [Chrome WebDrivers](https://chromedriver.chromium.org/downloads).
* [Firefox WebDrivers](https://github.com/mozilla/geckodriver/releases) (right from Mozilla's repository).

## Environment File

You must create an environment file `.env`, in here you must declare the constants that the project is going to need to be able to play our desired Artist's content.

Here is an example of the contents of `.env` : 

```python
LOGINURL = 'https://accounts.spotify.com/es/login/' #URL where we are going to log in.
DRIVERURL = './Resources/chromedriver' # Path for the webdriver of your choice.
ARTISTURL = 'https://open.spotify.com/artist/36QJpDe2go2KgaRleHCDTp'  # Artist URL.
USERNAME = "your@spotify_email.com" # Email registered in Spotify.
PASSWORD = "spotifypassword" # Password of the registered email.
```

## Executing the project

Now, we arrived to the fun part.  Before executing this project I strongly recommend to use a [VPN](https://en.wikipedia.org/wiki/Virtual_private_network) to avoid the posibility of your account being flagged and your ip being banned from the this unfortunate event. It's pure speculation since I don't really know how do they manage this kind of behavior. 

Anyway, to execute this project simply run ```spotify.bot``` on the command prompt. Here is the line you must run :
```python
python3 spotifybot.py
```
You must leave the mouse pointer on the web browser launched by the bot, don't alt+tab or switch windows right after you execute the bot. Wait until you start listening your artist's content, then you can switch or minimize the window.

## Authors

* [**Sebastián González Ramírez**](https://github.com/sgonzalezr94) 

Contact information : sebastiang1493@gmail.com.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details.

## Pending improvements

- Add logging instead of prints.
- Scalability, we could launch several instances of SpotifyBot therefore some refactoring could be done.
- Secure the execution of the Bot
    - Proxy Switching (Take a look to [Python-Proxy-Switcher](https://github.com/sgonzalezr94/python-proxy-switcher)!)
    - VPN usage
## Random Information

* This project was a product of a challenge from a co-worker.
* I don't profit by any means from this project.

