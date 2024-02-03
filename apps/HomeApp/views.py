from django.shortcuts import render
from django.views.generic import View,DetailView


class HomeView(View):

    def get(self,request):


        return render(request,"HomeApp/index.html")


class AboutMeView(View):

    def get(self,request):

        return render(request,"HomeApp/about.html")


class MoreInformationView(View):

    def get(self,request):

        return render(request,"HomeApp/credentials.html")


class WorksView(View):

    def get(self,request):


        return render(request,"HomeApp/works.html")



class ContactView(View):


    def get(self,request):

        return render(request,"HomeApp/contact.html")


class WorkDetail(View):

    def get(self,request):

        return render(request,"HomeApp/work-details.html")
