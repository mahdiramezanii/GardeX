from django.urls import path
from apps.HomeApp import views
app_name="HomeApp"
urlpatterns=[
    path("",views.HomeView.as_view(),name="HomeView"),
    path("about/",views.AboutMeView.as_view(),name="about"),
    path("credentials/",views.MoreInformationView.as_view(),name="credentials"),
    path("work/",views.WorksView.as_view(),name="work"),
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("work-detail/",views.WorkDetail.as_view(),name="work-detail")

]