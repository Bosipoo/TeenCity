from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum


from .models import *
from django.contrib.auth.models import User
from .forms import Teens
from .filters import TeenFilter

def dashboard(request):
    teens = Teen.objects.count()
    admins = User.objects.count()
    profile = User.objects.all()
    birthdays = Teen.objects.all()

    datetime_now = timezone.now()
    now_day, now_month = datetime_now.day, datetime_now.month
    datetime_tomorrow = datetime_now + timedelta(days=1)
    tomorrow_day, tomorrow_month = datetime_tomorrow.day, datetime_tomorrow.month
    datetime_nexttomorrow = datetime_now + timedelta(days=2)
    nexttomorrow_day, nexttomorrow_month = datetime_nexttomorrow.day, datetime_nexttomorrow.month
    
    labels = []
    data = []

    queryset = Teen.objects.values('age').annotate(teen_age=Sum('age')).order_by('-teen_age')
    for entry in queryset:
        labels.append(entry['age'])
        data.append(entry['teen_age'])

    context = {
        'teens': teens,
        'admins': admins,
        'profile': profile,
        'birthdays': birthdays,
        'now_day': now_day,
        'now_month': now_month,
        'tomorrow_day': tomorrow_day,
        'tomorrow_month': tomorrow_month,
        'nexttomorrow_day': nexttomorrow_day,
        'nexttomorrow_month': nexttomorrow_month,
        'labels': labels,
        'data': data,
    }

    return render(request,'dashboard.html',context)

class addTeen(CreateView):
    form_class = Teens
    template_name = "add-teen.html"
    success_url = reverse_lazy('dashboard')

class teenLanding(ListView):
    template_name = 'teen-details.html'
    model = Teen
    context_object_name = 'teendisps'
    paginate_by = 10
    queryset = Teen.objects.all()

class view_teen_in_detail(DetailView):
    template_name = "view-teen.html"
    model = Teen
    context_object_name = 'teend'

class edit_teen_details(UpdateView):
    model = Teen
    template_name = "update-teen.html"
    fields = ['firstname','lastname','othername','email','gender','dob','age',
                    'phone','school','level','cclass','address','ambition','bornagain','hobbies']
    context_object_name = 'teenu'

    def form_valid(self, form):
        instance = form.save()
        # messages.success(self.request, 'Teen has been updated!')
        return redirect('/teens')

class delete_teen(DeleteView):
    model = Teen
    template_name = "delete-teen.html"
    success_url = reverse_lazy('teenlanding')
    context_object_name = "del"

def search_date(request):
    data = Teen.objects.all()
    myFilter = TeenFilter(request.GET, queryset=data)
    return render(request, 'search-with-date.html', {'filter': myFilter})

class UserDetailView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "profile.html"
    fields = ['username','email','first_name','last_name']
    context_object_name = 'userdet'

    def form_valid(self, form):
        instance = form.save()
        # messages.success(self.request, 'Teen has been updated!')
        return redirect('/teens')

    def get_object(self):
        object = get_object_or_404(User, username=self.kwargs.get("username"))

        #only the owner can view this page
        if self.request.user.username == object.username:
            return object
        else:
            #redirect to 404 page
            print("You are not the owner?!!")
