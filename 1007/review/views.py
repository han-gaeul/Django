from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'review/index.html', context)

