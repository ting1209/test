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
line_bot_api = LineBotApi('GcXT0hcdzVX8y0VopCEgHKKRKhZL1jKsALAkwxTV49W7dLbq2myIAj3RErrz2rEtt22mDnnTqZOLlqHYCuN6Aw7TMJ6qkS0cmvICHR5ZcgeczP6VbqCaQz9ezdAy/zsJV6nJSWoFntlnzQMTui9yzQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a7f676f0726586e8fe40d2a58227ca8a')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://thumbs.dreamstime.com/z/%E7%B1%B3%E5%92%8C%E9%87%91%E6%9E%AA%E9%B1%BC%E8%89%B2%E6%8B%89-75530860.jpg',
                action=PostbackTemplateAction(
                    label='飯',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='http://image.tupian114.com/20141117/14260194.jpg.238.jpg',
                action=PostbackTemplateAction(
                    label='麵',
                    text='麵',
                    data='action=buy&itemid=2'
                )
            )，
            ImageCarouselColumn(
                image_url='http://image.tupian114.com/20120424/09013375.jpg',
                action=PostbackTemplateAction(
                    label='鍋',
                    text='鍋',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://thumbs.dreamstime.com/z/%E4%B8%8E%E9%A5%AE%E6%96%99%E7%9A%84%E4%B8%80%E5%9D%97%E7%8E%BB%E7%92%83-%E5%9C%A8%E4%B8%80%E7%BA%B8%E6%9D%AF%E7%9A%84%E6%9F%A0%E6%AA%AC%E6%B0%B4-%E5%9C%A8%E6%88%8F%E9%99%A2%E7%9A%84%E8%8B%8F%E6%89%93-118454707.jpg',
                action=PostbackTemplateAction(
                    label='飲料',
                    text='飲料',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://thumbs.dreamstime.com/z/%E8%A2%AB%E8%AE%BE%E7%BD%AE%E7%9A%84%E6%B0%B4%E5%BD%A9%E7%94%9C%E7%82%B9-121468949.jpg',
                action=PostbackTemplateAction(
                    label='其他',
                    text='其他',
                    data='action=buy&itemid=1'
                )
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
