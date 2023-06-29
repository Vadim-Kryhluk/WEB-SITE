from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .utils import *


#Головний клас представлення
class WebHome(DataMixin, ListView):
    model = Web
    template_name = 'shop/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Головна сторінка')
        return context | c_def #dict(list(context.items()) + list(c_def.items()))


class AboutShop(DataMixin, ListView):
    model = Web
    template_name = 'shop/about_shop.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Про нас')
        return context | c_def


class AddItem(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'shop/add_item.html'
    success_url = reverse_lazy('home')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Додати товар')
        return context | c_def


class OurContacts(DataMixin, ListView):
    model = Web
    template_name = 'shop/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наші контакти')
        return context | c_def

def pay_page(request, price=None):
    posts = Web.objects.all()

    context = {
        'posts': posts,
        'price': price,
        'menu': menu,
        'title': 'Сторінка оплати',
        'cat_selected': price,
    }
    return render(request, 'shop/pay_page.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Чуєш друг, тут якби помилково введений url-адреса сторінОчки</h1>')


class ShowPost(DataMixin, DetailView):
    model = Web
    template_name = 'shop/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


#---Категорії---#
class WebCategory(DataMixin, ListView):
    model = Web
    template_name = 'shop/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self): # Отримати набір запитів
        return Web.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        posts = Web.objects.all()
        context = super().get_context_data(**kwargs)
        if len(posts) == 0:
            raise Http404
        c_def = self.get_user_context(title='Категорія - ' + str(context['posts'][0].cat),
                                            cat_selected = context['posts'][0].cat.id)
        return context | c_def


    #*** Доробити пошук товарів ***#

class Search(DataMixin, ListView):
    '''Пошук запчастин'''

    paginate_by = 2

    def get_queryset(self):
        return Web.objects.filter(title__icontains=self.request.GET.get("search"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title=('Результати за пошуком'))
        context["q"] = self.request.GET.get("q")
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


class UserProfile(DataMixin, ListView):
    model = Web
    template_name = 'shop/user_profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Профіль")
        return context | c_def



def logout_user(request):
    logout(request)
    return redirect('login')

def template(request):
    return render(request, 'shop/template_for_web.html')

