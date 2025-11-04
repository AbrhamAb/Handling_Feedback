from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm  
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView 

from .models import Review
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you/'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you/")
        
    #     return render(request, 'reviews/review.html', {"form": form})

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Thank you for your review!"
        return context

class ReviewsListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
class SingleReviewView(DetailView):
    model = Review
    template_name = 'reviews/single_review.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context
class FavoriteReviewView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect(f"/reviews/{review_id}/")