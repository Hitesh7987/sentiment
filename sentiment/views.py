from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import paralleldots
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt



paralleldots.set_api_key('npXLk6TDJ8BSrLqaKdndPViFxnmJnUSsQvpkosPhH0s')
text = "Chipotle in the north of Chicago is a nice outlet. I went to this place for their famous burritos but fell in love with their healthy avocado salads. Our server Jessica was very helpful. Will pop in again soon!"

def home(request):
    #paralleldots.sentiment(text)
   #print(apps.get_app_config('sentiment').getSentiment('Bad'))
    return render(request, 'page1.html', {})

@csrf_exempt
def model1(request):
    if request.method == "GET":
        return render(request,'model1.html')
    else:
        data = {}
        res = paralleldots.sentiment(request.POST['text'])
        #res ={'sentiment': {'negative': 1.003, 'neutral': 2.079, 'positive': 0.918}}
        if res :
            res = res['sentiment']
            key_max = max(res, key=res.get)
            data['status'] = 1
            data['success'] = key_max
            data['score'] = res[key_max]
            return JsonResponse(data)
        else :
            data['status'] = 2
            data['error'] = 'Unable to get your response'
            return JsonResponse(data)

@csrf_exempt
def model2(request):
    if request.method == "GET":
        return render(request,'model2.html')
    else:
        data = {}
        res = ''
        print(res)
        res = apps.get_app_config('sentiment').getSentiment(request.POST['text'])
        print(res)
        if res != '':
            data['status'] = 1
            data['success'] = int(res)
            return JsonResponse(data)
        else:
            data['status'] = 2
            data['error'] = 'Unable to get your response'
            return JsonResponse(data)
