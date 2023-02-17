from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, ListView, UpdateView
from users.forms import UserCreationForm, UserUpdateForm
from users.models import CustomUser


class Register(View):
    template_name = 'register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'detailview.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user_s'] = CustomUser.objects.get(pk=self.request.user.pk)
        # context['company'] = Company.objects.get(id=user_s)
        context['customusers'] = CustomUser.objects.all()
        return context


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('mainapp:mainpage')


class UsersListView(ListView):
    model = CustomUser
    template_name = 'userlist.html'
    context_object_name = 'users'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['useri'] = CustomUser.objects.all()

    def get(self, request):
        users = CustomUser.objects.all()
        context = {
            'users': users
        }
        return render(request, template_name='userlist.html', context=context)