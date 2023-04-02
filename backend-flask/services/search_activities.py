from datetime import datetime, timezone


class SearchActivities:
    @staticmethod
    def run(search_term: str):
        model = {
            'errors': None,
            'data': None
        }

        now = datetime.now(timezone.utc).astimezone()

        if search_term is None or len(search_term) < 1:
            model['errors'] = ['search_term_blank']
        else:
            results = [{
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'handle': 'Andrew Brown',
                'message': 'Cloud is fun!',
                'created_at': now.isoformat()
            }]
            model['data'] = results
        return model
