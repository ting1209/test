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
                image_url='https://m1.aboluowang.com/uploadfile/2014/1224/20141224064255787.jpg',
                action=PostbackTemplateAction(
                    label='飯',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='http://pic.pimg.tw/anrine910070/1418824834-2716133969.jpg',
                action=PostbackTemplateAction(
                    label='麵',
                    text='麵',
                    data='action=buy&itemid=2'
                )
            )，
            ImageCarouselColumn(
                image_url='https://pic.pimg.tw/haruhii/1484636324-551661854.jpg',
                action=PostbackTemplateAction(
                    label='鍋',
                    text='鍋',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://pic.pimg.tw/kaohsiungtoeat/1525876557-3615106453_n.jpg',
                action=PostbackTemplateAction(
                    label='飲料',
                    text='飲料',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://pic.pimg.tw/cindy6732/1516363279-922751753.jpg',
                action=PostbackTemplateAction(
                    label='其他',
                    text='其他',
                    data='action=buy&itemid=1'
                )
            ),
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
