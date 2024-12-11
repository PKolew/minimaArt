from django.shortcuts import render, redirect
from django.contrib import messages
from minima_art.web.forms import ContactForm
from .forms import FeedbackForm

def home(request):
    form = ContactForm()
    return render(request, 'index.html', {'form':form})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Feedback received: {name}, {email}, {message}")
            messages.success(request, "Thank you for your feedback!")
            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
