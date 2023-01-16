from django.http import HttpResponse
from django.template import loader

from .models import Food

# Create your views here.
def food_list(request):
    food_list = Food.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'food_list' : food_list,
    }
    return HttpResponse(template.render(context, request))
    