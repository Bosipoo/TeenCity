from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Teen
from .forms import Teens

# Create your views here.
def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

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
