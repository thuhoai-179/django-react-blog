from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Sum

# Restframework
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


# Custom Imports
from api import serializer as api_serializer
from api import models as api_models
from django.shortcuts import render, redirect
from rest_framework.authentication import BasicAuthentication
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"base.html")
def trangchu(request):
    return render(request,"trangchu.html")
def blog(request):
    return render(request,'blog.html')
def catalog(request):
    return render(request,"catalog.html")
def vechungtoi(request):
    return render(request,'vechungtoi.html')
def lienhe(request):
    return render(request,'lienhe.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tài khoản {username} đã được tạo thành công!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'loggin.html')

def home(request):
    return render(request, 'home.html')

def trang(request):
    trending_posts = Post.objects.order_by('-views')[:5]
    categories = Post.objects.values('category').distinct()
    popular_posts = Post.objects.order_by('-likes')[:5]

    return render(request, 'home.html', {
        'trending_posts': trending_posts,
        'categories': categories,
        'popular_posts': popular_posts,
    })


def register(request):
    return render(request, 'register.html')

authentication_classes = [BasicAuthentication]
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = api_models.User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = api_serializer.RegisterSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = api_serializer.ProfileSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']

        user = api_models.User.objects.get(id=user_id)
        profile = api_models.Profile.objects.get(user=user)
        return profile