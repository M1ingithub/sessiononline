from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, re_path, include
from apps.home.views import views
from apps.home.views.loginviews import LoginView, RegisterView, LogoutView
from apps.home.views.views import AddCommunityView, ReportView, AboutView
from apps.home.views.views import CommunityListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CommunityListView.as_view(), name='home'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    # path('addcommunity/', views.addcommunity, name='addcommunity'),
    path('addcommunity/', AddCommunityView.as_view(), name='addcommunity'),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("report/", ReportView.as_view(), name="report"),
    path("about/", AboutView.as_view(), name="about")
]

"""
urlpatterns += i18n_patterns(
    path("", include("apps.home.urls.urls")),
)

    path('i18n/', include('django.conf.urls.i18n')),
"""