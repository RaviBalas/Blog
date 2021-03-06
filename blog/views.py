from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from .models import PostModel
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import DetailView,ListView,UpdateView,DeleteView,CreateView
# Create your views here.
class PostModelListView(ListView):
    model = PostModel
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5
    # return render(request,"blog/index.html",{'posts':PostModel.objects.all()
class UserListView(ListView):
    model = PostModel
    context_object_name='posts'
    print("+ew++++++++++++")
    paginate_by=5
    template_name="blog/user_list.html"
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        print(user,"+++++++++++++")
        return PostModel.objects.filter(auther=user).order_by('-date_posted')
    
class PostModelDetailView(DetailView):
    model = PostModel

class PostModelUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = PostModel
    fields=('title','content')
    def form_valid(self, form):
        form.instance.auther =self.request.user
        return super().form_valid(form)
    def test_func(self):
        if self.request.user==self.get_object().auther:
            return True
        else:
            return False
class PostModelDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = PostModel
    success_url='/'

    def test_func(self):
        if self.request.user==self.get_object().auther:
            return True
        else:
            return False
    
class PostModelCreateView(LoginRequiredMixin,CreateView):
    model = PostModel
    fields=('title','content')
    def form_valid(self, form):
        form.instance.auther =self.request.user
        return super().form_valid(form)
    
    
    