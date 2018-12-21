from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('erMPuj81XEFrc+GFQOaAXPCf8gIlU3ustq0ZdB+puOOH6WbPjtb6m3xER5yHyM/ODTKawpiBAJs3Z4bzGEn6ctyZDwK/P4bcnqqPuiaFI70yMm12FOf1GU91jrMdC2xdpZAWzn5H0PYJ3JUsHaPMXAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e8064ab6a153a869f41148e3021094db')

def handle_message(event):
    message = TextSendMessage(text='請撥打客服專線')
    line_bot_api.reply_message(event.reply_token, message)
	
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)