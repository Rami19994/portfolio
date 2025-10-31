from django.shortcuts import render,redirect
from .models import Home, About, Profile, Category, Skills, Portfolio, Message
from django.contrib import messages

def index(request):
    # Home
    home = Home.objects.order_by('-update').first()

    # About
    about = About.objects.order_by('-update').first()
    profiles = Profile.objects.filter(about=about) if about else []

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

 
    def contact_view(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            message_text = request.POST.get('message')

        if name and phone and message_text:
            Message.objects.create(
                name=name,
                phone=phone,
                address=address,
                message=message_text
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # اسم المسار في urls
        else:
            messages.error(request, "Please fill in all required fields.")

    
    
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }

    return render(request, 'index.html', context)


