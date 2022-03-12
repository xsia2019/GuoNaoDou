# -*- coding: utf-8 -*-

import sys
from dingtalkchatbot.chatbot import DingtalkChatbot
from Lib.DailySentence import EduicContent
from Lib.qWeatherAPI import QWeatherApi

# 取得天气信息
# 取得系统传入KEY
qweather_key = sys.argv[3]
# 实例化qWeatherAPI
qWeather = QWeatherApi(qweather_key, 'Beihai')
# 取得天气信息
forcast = qWeather.get_weather_forecast()

# 取得每日图片
# 实例化Euic
euic = EduicContent()
# 取得每日图片
image = euic.get_daily_content()[1]
# 编辑要发送的信息
md_message = '### 平果现在天气  \n  ' \
             '##### {forcast}  \n  ' \
             '![picture]({image})  \n  ' \
             '##### from GitHub Actions.  \n  '\
    .format(forcast=forcast, image=image,)

# 接收系统传入的webhook和secret
chatbot_webhook = sys.argv[1]
chatbot_secret = sys.argv[2]

# 实例化DingtalkChatbot
chatbot = DingtalkChatbot(chatbot_webhook, secret=chatbot_secret)

# 发送消息
chatbot.send_markdown(title="实时天气", text=md_message, is_at_all=False)
