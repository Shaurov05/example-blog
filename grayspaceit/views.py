from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def IndexTemplateView(request):
    # login_url = '/auth/login/'
    if settings.DEBUG:
        template_name = "vue/vue_index_dev.html"
    else:
        template_name = "vue/vue_index.html"

    # token = localStorage.getItem('token');
    # print("token", token)
    # if token != "initial":
    #     response = HttpResponse(request)
    #     response.set_cookie('token', 'cookie_value')
    #     # request.COOKIES["token"] = "initial"
    #     print("initialied token ", request.COOKIES.get("token"))
    # else:
    #     print("new token ", request.COOKIES.get("token"))
    # print("new token ", request.COOKIES.get("token"))
    return render(request, template_name, {})
