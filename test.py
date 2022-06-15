import discord
from discord.ext import commands
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
opts.add_argument('--headless')

lanes = ["上路TOP","中路AP","打野JG","輔助SUP","下路ADC"]
stars = [":star:",":star::star:",":star::star::star:",":star::star::star::star:",":star::star::star::star::star:"]
hearts = [":heart_on_fire:",":heart_on_fire::heart_on_fire:",":heart_on_fire::heart_on_fire::heart_on_fire:",":heart_on_fire::heart_on_fire::heart_on_fire::heart_on_fire:",":heart_on_fire::heart_on_fire::heart_on_fire::heart_on_fire::heart_on_fire:"]
names = ["呂諺","大腸腸","阿熙","韋頡","小智","桀煾"]

TOP = ["厄薩斯","卡蜜兒","古拉格斯","弗力貝爾","伊瑞莉雅","伊羅旖","汎","克雷德","吶兒","犽宿","犽凝","辛吉德","杰西","阿卡莉","科加斯","約瑞科","剛普朗克","悟空","泰達米爾","烏爾加特","納瑟斯","貪啃奇","凱能","凱爾","提摩","斯溫","菲歐拉","鄂爾","慎","葛雷夫","葵恩","賈克斯","達瑞斯","雷尼克頓","雷玟","漢默丁格","蒙多醫生","蓋倫","歐拉夫","墨菲特","賽恩","賽特","藍寶","關","魔鬥凱薩"]
AP = ["加里歐","卡特蓮娜","卡莎碧雅","卡薩丁","弗拉迪米爾","伊瑞莉雅","安妮","艾克","艾妮維亞","劫","犽宿","犽凝","妮可","拉克絲","阿卡莉","阿祈爾","阿璃","星朵拉","柔伊","飛斯","剛普郎克","埃可尚","姬亞娜","庫奇","逆命","馬爾札哈","勒布朗","斯溫","塔莉雅","塔隆","奧莉安娜","雷茲","漢默丁格","維克特","維迦","齊勒斯","翱銳龍獸","薇可絲","賽勒斯","麗珊卓"]
JG = ["卡力斯","卡爾瑟斯","史加納","史瓦妮","弗力貝爾","札克","伊芙琳","伊莉絲","艾克","努努和威朗普","劫","希瓦娜","李星","沃維克","貝爾薇斯","夜曲","奈德麗","拉姆斯","易大師","波比","阿姆姆","埃爾文","悟空","烏迪爾","特朗德","莉莉亞","慨影","菲艾","費德提克","塔莉雅","塔隆","葛雷夫","雷珂煞","雷葛爾","嘉文四世","維爾戈","赫克林","趙信","歐拉夫","黛安娜","薩科","鏡爪"]
AD = ["伊澤瑞爾","吉茵珂絲","好運姐","汎","艾希","克黎思妲","希格斯","希維爾","犽宿","亞菲利歐","法洛士","剎雅","婕莉","寇格魔","崔絲塔娜","凱特琳","凱莎","煞蜜拉","路西恩","達瑞文","圖奇","燼"]
SUP = ["巴德","卡瑪","布里茨","布朗姆","布蘭德","艾希","亞歷斯塔","珊娜","拉克斯","威寇茲","枷蘿","派克","珍娜","茂凱","娜米","納帝魯斯","索拉卡","索娜","悠咪","斯溫","塔里克","極靈","瑟菈紛","瑟雷西","雷歐娜","睿娜妲•格萊斯克","齊勒斯","潘森","銳兒","銳空","露璐","魔甘娜"]
Hero = ["厄薩斯","卡蜜兒","古拉格斯","弗力貝爾","伊瑞莉雅","伊羅旖","汎","克雷德","吶兒","犽宿","犽凝","辛吉德","杰西","阿卡莉","科加斯","約瑞科","剛普朗克","悟空","泰達米爾","烏爾加特","納瑟斯","貪啃奇","凱能","凱爾","提摩","斯溫","菲歐拉","鄂爾","慎","葛雷夫","葵恩","賈克斯","達瑞斯","雷尼克頓","雷玟","漢默丁格","蒙多醫生","蓋倫","歐拉夫","墨菲特","賽恩","賽特","藍寶","關","魔鬥凱薩","加里歐","卡特蓮娜","卡莎碧雅","卡薩丁","弗拉迪米爾","安妮","艾克","艾妮維亞","劫","妮可","拉克絲","阿祈爾","阿璃","星朵拉","柔伊","飛斯","剛普郎克","埃可尚","姬亞娜","庫奇","逆命","馬爾札哈","勒布朗","塔莉雅","塔隆","奧莉安娜","雷茲","維克特","維迦","齊勒斯","翱銳龍獸","薇可絲","賽勒斯","麗珊卓","卡力斯","卡爾瑟斯","史加納","史瓦妮","札克","伊芙琳","伊莉絲","艾克","努努和威朗普","劫","希瓦娜","李星","沃維克","貝爾薇斯","夜曲","奈德麗","拉姆斯","易大師","波比","阿姆姆","埃爾文","烏迪爾","特朗德","莉莉亞","慨影","菲艾","費德提克","塔莉雅","塔隆","雷珂煞","雷葛爾","嘉文四世","維爾戈","赫克林","趙信","黛安娜","薩科","鏡爪","伊澤瑞爾","吉茵珂絲","好運姐","艾希","克黎思妲","希格斯","希維爾","亞菲利歐","法洛士","剎雅","婕莉","寇格魔","崔絲塔娜","凱特琳","凱莎","煞蜜拉","路西恩","達瑞文","圖奇","燼","巴德","卡瑪","布里茨","布朗姆","布蘭德","艾希","亞歷斯塔","珊娜","拉克斯","威寇茲","枷蘿","派克","珍娜","茂凱","娜米","納帝魯斯","索拉卡","索娜","悠咪","塔里克","極靈","瑟菈紛","瑟雷西","雷歐娜","睿娜妲•格萊斯克","齊勒斯","潘森","銳兒","銳空","露璐","魔甘娜"]

Path = "C:/Users/阿熙/Desktop/chromedriver.exe"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!')

@bot.event

async def on_ready():
    print(">> 熙掰Bot is Online <<")
    channel_siba = bot.get_channel(934050717008814121)
    #await channel_siba.send(f"熙掰Bot 天降伺服器")

    channel_luyan = bot.get_channel(985022431888551946)
    await channel_luyan.send(">> 熙掰Bot is Online <<")
    
    game = discord.Game('熙掰英雄聯盟')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event

async def on_message(message):
    channel_siba = bot.get_channel(971373450281226280)
    if message.content == '今天玩哪路':
        random.shuffle(lanes)
        await channel_siba.send(lanes[0])
    
    channel_luyan = bot.get_channel(985022431888551946)
    if message.content == '今天玩哪路':
        random.shuffle(lanes)
        await channel_luyan.send(lanes[0])
    
    if message.content == '今日手感':
        random.shuffle(hearts)
        await channel_siba.send(hearts[0])

    if message.content == '今日手感':
        random.shuffle(hearts)
        await channel_luyan.send(hearts[0])
    
    if message.content == '今日手感':
        random.shuffle(stars)
        await channel_siba.send(stars[0])

    if message.content == '今日運氣':
        random.shuffle(stars)
        await channel_luyan.send(stars[0])

    if message.content == '3v3隨機分隊':
        random.shuffle(names)
        team1 = "第一組:"+names[0]+" "+names[1]+" "+names[2]
        team2 = "第二組:"+names[3]+" "+names[4]+" "+names[5]
        await channel_luyan.send(team1)
        await channel_luyan.send(team2)
    
    if message.content == '上路玩誰':
        random.shuffle(TOP)
        Text_top = "為你選擇=>" + TOP[0]
        await channel_luyan.send(Text_top)
    
    if message.content == '中路玩誰':
        random.shuffle(AP)
        Text_AP = "為你選擇=>" + AP[0]
        await channel_luyan.send(Text_AP)

    if message.content == '下路玩誰':
        random.shuffle(AD)
        Text_AD = "為你選擇=>" + AD[0]
        await channel_luyan.send(Text_AD)

    if message.content == '打野玩誰':
        random.shuffle(JG)
        Text_JG = "為你選擇=>" + JG[0]
        await channel_luyan.send(Text_JG)

    if message.content == '輔助玩誰':
        random.shuffle(SUP)
        Text_SUP = "為你選擇=>" + SUP[0]
        await channel_luyan.send(Text_SUP)

    if message.content == "胖胖":
        fat = discord.File("C:/VScode/123.png")
        await channel_luyan.send(file=fat)

    if message.content in Hero:
        driver = webdriver.Chrome(Path,chrome_options=opts)
        driver.get("https://www.op.gg/")
        action = ActionChains(driver)
        element_search = driver.find_element(By.ID, 'searchSummoner')
        element_search.send_keys(message.content)
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH , '/html/body/div[1]/div[2]/div[2]/div/nav/a/div/small/em[1]'))
        )
        element_send = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/nav/a/div/small/em[1]')
        ActionChains(driver).move_to_element(element_send).perform()
        ActionChains(driver).click(element_send).perform()
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,600)')
        driver.get_screenshot_as_file("符文及裝備.png")
        driver.close()
        pic = discord.File("C:/VScode/Python Project/符文及裝備.png")
        await channel_luyan.send(file=pic)


bot.run("OTg0OTk2MTAwNzYxMDY3NTcw.GvqAjb.047zvvfBxk_oJxkNqVzdwFgr0SZ_WLZtcVBsnM")
