# Coded by Sebastian Gonzalez Ramirez
# email to sebastiang1493@gmail.com

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from customtypes import BotSettings


class SpotifyBot:
    def __init__(self):
        print("Starting SpotifyBot.")
        print("Remember, to cancel this bot at any time just press ctrl+c")
        self.settings = BotSettings()
        self.settings.load()
        self.DRIVER = webdriver.Chrome()

    def Login(self, usernamein, passwordin):
        print("Loading and sending credentials payload...")
        driver = self.DRIVER
        print("URL to visit", self.settings.login_url)
        driver.get(self.settings.login_url)
        username = driver.find_element(By.ID, value="login-username")
        username.clear()
        username.send_keys(usernamein)
        password = driver.find_element(By.ID, value="login-password")
        password.clear()
        password.send_keys(passwordin)
        driver.find_element(By.ID, value="login-button").click()
        window_before = driver.window_handles[0]
        print("Done!")
        self.WINDOW = window_before

    def OpenArtistSite(self):
        print("Opening artist's site...")
        driver = self.DRIVER
        driver.execute_script("window.open('" + self.settings.artist_url + "');")
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(3)
        driver.refresh()
        print("Loading songs...")
        time.sleep(3)
        playbtn = driver.find_element(
            by=By.XPATH, value=self.settings.buttons.get("PLAYBTNXPATH")
        )
        time.sleep(3)
        print("Playing.")
        playbtn.click()
        repeatbtn = driver.find_element(
            by=By.XPATH, value=self.settings.buttons.get("RPTBTNCLASSNAME")
        )
        time.sleep(2)
        try:
            cookiepolicybutton = driver.find_element(
                by=By.XPATH, value=self.settings.buttons.get("COOKIEPOLICYBTN")
            )
            cookiepolicybutton.click()
        except:
            pass
        finally:
            if repeatbtn.get_attribute("aria-checked") == "false":
                print("Checking repeat button...")
                repeatbtn.click()
                print("Clicked.")
        time.sleep(2)

    def StartCycling(self, trange):
        driver = self.DRIVER
        print("Random switching started...")
        print(
            "The switch time range is from ", trange[0], " to ", trange[1], " seconds."
        )
        nextbtn = driver.find_element(By.XPATH, self.settings.buttons.get("NEXTBTN"))
        while True:
            randran = random.randint(int(trange[0]), int(trange[1]))
            print("It will switch the song in ", randran, " seconds.")
            time.sleep(randran)
            print("Switching song.")
            nextbtn.click()


def StartBot():
    bot = SpotifyBot()
    bot.Login(
        usernamein=bot.settings.username,
        passwordin=bot.settings.password,
    )
    bot.OpenArtistSite()
    bot.StartCycling((bot.settings.start_time, bot.settings.end_time))


StartBot()
