from blueforge.apis.facebook import CreateFacebookApiClient, RequestDataFormat, Recipient, Message, QuickReplyTextItem, \
    QuickReply

client = CreateFacebookApiClient(
    access_token='d')



recipient = Recipient(recipient_id='1053565541409779')
quick_replies = [QuickReplyTextItem(title='예', payload='yes', image_url=None),
                 QuickReplyTextItem(title='아니요', payload='no', image_url=None)]

message = Message(text='Hard Study', quick_replies=QuickReply(quick_reply_items=quick_replies))
final_message = RequestDataFormat(recipient=recipient, message=message)
print(client.send_message(final_message))

