# -*- coding: utf-8 -*-

import sys
from Lib.DailySentence import EduicContent
from dingtalkchatbot.chatbot import DingtalkChatbot

# 取得每日图片和每日一句
# 实例化Euic
euic = EduicContent()
# 取得每日内容
sentence = euic.get_daily_content()[0]
# 取得每日图片
image = euic.get_daily_content()[1]

# 编辑要发送的信息
md_message = '### 每日一句  \n  ' \
             '![picture]({image})  \n  ' \
             '##### {sentence}  \n  '\
             '##### from GitHub Actions.  \n  '\
    .format(image=image, sentence=sentence)

# 接收系统传入的webhook和secret
chatbot_webhook = sys.argv[1]
chatbot_secret = sys.argv[2]

# 实例化DingtalkChatbot
chatbot = DingtalkChatbot(chatbot_webhook, secret=chatbot_secret)

# 发送消息
chatbot.send_markdown(title="每日一句", text=md_message, is_at_all=False)
