from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
try:
    import json
except:
    import django.utils.simplejson as json
some_data_to_dump = {
    'some_var_1': 'foo',
    'some_var_2': 'bar',
}

data = json.dumps(some_data_to_dump)


def hello_world(request):
    print(request.method)
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

@csrf_exempt
def post_data(request):
    print(request.body)
    return HttpResponse(request.body, content_type='application/json')
