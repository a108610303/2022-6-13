#載入LineBot所需要的模組
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('PalTPBoHOha0gAvNfSCWOSSqkNvPryosbxwzIN7SBsZgGPNLUnN2v7WB1csrIr8oZWU1Z/yG9UlpWSdcCNZ2b+zbY6Qnk1L5bJK3El1sbWxEjl64kk9K15eaXuYS8tWLQD/mmEp8UUeNqLKDcoPsqwDnyilt='
)# 必須放上自己的Channel Secret
handler = WebhookHandler('3b9afa597807cf62bb855a059e7d0aa6')
line_bot_api.push_message('Ue6e5a2efeaf9e9052534905c1b043eba',TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:handler.handle(body, signature)
    except InvalidSignatureError:abort(400)
    
    return 'OK'
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
