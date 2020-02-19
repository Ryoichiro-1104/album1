from django.shortcuts import render,redirect,reverse
from django import views
from musics import CreateMusicForm

# Create your views here.


 class ListMusics(views.View):
    def get(self, request, *args, **kwargs):
        context = {'message': 'Hello world'}
        return render(request, 'music_list.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateMusicForm(request.POST)
        if form.is_valid():
            context = {'message': 'Hello world'}
            return redirect(reverse('musics:index'), context)
        else:
            context = {'form': CreateMusicForm()}
            return render(request, 'musics/form.html', context)

class NewMusic(views.View):
    def get(self, request, *args, **kwargs):
        context = {'form': CreateMusicForm()}
        return render(request, 'musics/form.html', context)
