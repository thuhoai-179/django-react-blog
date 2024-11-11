from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views as api_views

urlpatterns = [
    # Userauths API Endpoints
    path('user/token/', api_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', api_views.RegisterView.as_view(), name='auth_register'),
    path('user/profile/<user_id>/', api_views.ProfileView.as_view(), name='user_profile'),

    path('', api_views.index, name='home'),
    path('pages/', api_views.page, name='pages'),
    path('blog/', api_views.blog, name='blog'),
    path('login/', api_views.login, name='login'),
    path('register/', api_views.register, name='register'),
    path('baiviet/',api_views.blog,name='blog'),
    path('trangchu/',api_views.trangchu,name='trang_chu'),
    path('catalog/',api_views.catalog,name='catalog'),
    path('trang/',api_views.trang,name='trang'),
    path('vechungtoi/',api_views.vechungtoi,name='vechungtoi'),
    path('lienhe/',api_views.lienhe,name='lienhe')



]