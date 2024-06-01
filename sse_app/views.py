import time
import json
from django.http import StreamingHttpResponse
from sse_app.schema import schema

def sse_view(request):
    def event_stream():
        while True:
            time.sleep(1)
            query = '''
                query {
                    allModels {
                        id
                        name
                        description
                    }
                }
            '''
            result = schema.execute(query)
            data = json.dumps(result.data)
            yield f'data: {data}\n\n'
    
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response
