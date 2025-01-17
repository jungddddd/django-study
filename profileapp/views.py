from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from profileapp.templates.profileapp.decorators import profile_ownership_required


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    #model에는 user 구현했는데 formd에는 user 빼고 3개만 구현했었음. 그래서 여기에 user 코드 추가해줘야함.
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    #메서드 재정의. urls에 path('detail/<int:pk>' 받아오는 것. pk는 kwargs로 받아옴
    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

def get_success_url(self):
    return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

