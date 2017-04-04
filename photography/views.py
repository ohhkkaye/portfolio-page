from django.shortcuts import render

def index(request):

  return render(request, 'photography/home.html')

	#return HttpResponse("hello")


# from django.http import HttpResponse
# import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


