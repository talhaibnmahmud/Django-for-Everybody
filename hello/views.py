from django.http import HttpResponse


# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    if num_visits > 4: del (request.session['num_visits'])

    response = HttpResponse('view count=' + str(num_visits))
    response.set_cookie('dj4e_cookie', 'd58cc999', max_age=1000)
    return HttpResponse(response)


def cookie(request):
    oldval = request.COOKIES.get('zap', )
    response = HttpResponse('In a view - the zap cookie value is ' + str(oldval))

    response.set_cookie('dj4e_cookie', 'd58cc999', max_age=1000)
    return response


def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    if num_visits > 4: del (request.session['num_visits'])
    return HttpResponse('View Count = ' + str(num_visits))
