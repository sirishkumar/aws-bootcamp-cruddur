import uuid
from datetime import datetime, timezone


class CreateMessage:
    @staticmethod
    def run(message: str, user_sender_handle: str, user_receiver_handle: str):
        model = {
            'errors': None,
            'data': None
        }
        if user_sender_handle is None or len(user_sender_handle) < 1:
            model['errors'] = ['user_sender_handle_blank']

        if user_receiver_handle is None or len(user_receiver_handle) < 1:
            model['errors'] = ['user_reciever_handle_blank']

        if message is None or len(message) < 1:
            model['errors'] = ['message_blank']
        elif len(message) > 1024:
            model['errors'] = ['message_exceed_max_chars']

        if model['errors']:
            # return what we provided
            model['data'] = {
                'display_name': 'Andrew Brown',
                'handle': user_sender_handle,
                'message': message
            }
        else:
            now = datetime.now(timezone.utc).astimezone()
            model['data'] = {
                'uuid': uuid.uuid4(),
                'display_name': 'Andrew Brown',
                'handle': user_sender_handle,
                'message': message,
                'created_at': now.isoformat()
            }
        return model
