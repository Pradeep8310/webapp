from django.urls import path

urlpatterns = [
    path("/",),
    path("/about",views.about,name='about'),
    path("/services",views.services,name='services'),
    path("/contact",views.contact,name='contact'),
    path("/login",views.login,name='login'),
    path("/signup",views.signup,name='signup'),
]