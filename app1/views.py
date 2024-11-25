from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def set_session(request):
    request.session['username']="adithya"
    return HttpResponse('session created successfully')



def get_session(request):
    adithya=request.session.get('username','session not created for specified user')
    return HttpResponse(f"user name is {adithya}")


def set_cookies(request):
    response=HttpResponse('cookie set')
    response.set_cookie("city","hyderabad",)
    return response

def get_cookie(request):
  city=request.COOKIES.get("city",'no city')
  return HttpResponse(f"city is {city}")






