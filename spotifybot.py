
# Coded by Sebastian Gonzalez Ramirez
# email to software@sgonzalezr.com

from selenium import webdriver
import time
import random
import botconfig as cfg


class SpotifyBot():
    def __init__(self):
        print("Starting SpotifyBot.")
        print("Remember, to cancel this bot at any time just press ctrl+c")
        self.LOGINURL = cfg.LOGINURL
        self.DRIVERURL = cfg.DRIVERURL
        self.ARTISTURL = cfg.ARTISTURL
        self.DRIVER = webdriver.Chrome(executable_path=self.DRIVERURL)
        self.WINDOW = ""

    def Login(self, usernamein, passwordin):
        print('Loading and sending credentials payload...')
        driver = self.DRIVER
        driver.get(self.LOGINURL)
        username = driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys(usernamein)
        password = driver.find_element_by_id("login-password")
        password.clear()
        password.send_keys(passwordin)
        driver.find_element_by_id("login-button").click()
        window_before = driver.window_handles[0]
        print("Done!")
        self.WINDOW = window_before

    def OpenArtistSite(self):
        print("Opening artist's site...")
        driver = self.DRIVER
        driver.execute_script("window.open('"+self.ARTISTURL+"');")
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.refresh()
        print("Loading songs...")
        time.sleep(3)
        playbtn = driver.find_element_by_xpath(cfg.PLAYBTNXPATH)
        time.sleep(3)
        print("Playing.")
        playbtn.click()
        repeatbtn = driver.find_element_by_class_name(cfg.RPTBTNCLASSNAME)
        time.sleep(3)
        print("Checking repeat button...")
        repeatbtn.click()
        print("Clicked.")

    def StartCycling(self, trange):
        driver = self.DRIVER
        print("Random switching started...")
        print("The switch time range is from ",
              trange[0], ' to ', trange[1], ' seconds.')
        nextbtn = driver.find_element_by_class_name(cfg.NEXTBTN)
        while(True):
            randran = random.randint(trange[0], trange[1])
            print("It will switch the song in ", randran, " seconds.")
            time.sleep(randran)
            print("Switching song. ")
            nextbtn.click()


def StartBot():
    bot = SpotifyBot()
    bot.Login(usernamein=cfg.USERNAME, passwordin=cfg.PASSWORD)
    bot.OpenArtistSite()
    bot.StartCycling([cfg.STARTTIME, cfg.ENDTIME])


StartBot()
