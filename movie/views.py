from django.shortcuts import render
from django.http import HttpResponse
from .models import MOvie,Review
from django.shortcuts import get_object_or_404,redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies =MOvie.objects.filter(title__icontains=searchTerm)
    else:
        movies = MOvie.objects.all()
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})
def about(request):
    return render(request,'one.html')

def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})
def detail(request,movie_id):
    movie=get_object_or_404(MOvie,pk=movie_id)
    reviews=Review.objects.filter(movie=movie)
    return render(request,'detail.html',{'movie':movie,'reviews':reviews})
@login_required
def createreview(request,movie_id):
    movie=get_object_or_404(MOvie,pk=movie_id)
    if request.method=='GET':
        return render(request,'createreview.html',{'form':ReviewForm(),'movie':movie})
    else:
        try:
            form=ReviewForm(request.POST)
            newReview=form.save(commit=False)
            newReview.user=request.user
            newReview.movie=movie
            newReview.save()
            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request,'createreview.html',{'form':ReviewForm(),'error':"Bad Data Passed  In"})
@login_required
def updatereview(request,review_id):
    review=get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method=='GET':
        form=ReviewForm(instance=review)
        return render(request,'updatereview.html',{'review':review,'form':form})
    else:
        try:
            form=ReviewForm(request.POST,instance=review)
            form.save()
            return redirect('detail',review.movie_id)
        except ValueError:
            return render(request,'updatereview.html',{'review':review,'error':'bad data in form '})
@login_required        
def deletereview(request,review_id):
    review=get_object_or_404(Review,pk=review_id,user=request.user)
    review.delete()
    return redirect('detail',review.movie.id)        






