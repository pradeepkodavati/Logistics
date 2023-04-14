from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import RegisterForm, MyPasswordResetForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import routeLogistics
from .forms import routeLogisticsForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    return redirect('login')



class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    def form_valid(self, form):
        UserModel = get_user_model()
        username = form.cleaned_data.get('username')
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return redirect('register')
        user.set_password(form.cleaned_data['new_password1'])
        user.save()
        return super().form_valid(form)


class MyPasswordResetDoneView(TemplateView):
    template_name = 'password_reset_done.html'



# Create
@login_required
def routeLogistics_create(request):
    form = routeLogisticsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'routeLogistics/routelogistics_form.html', {'form': form})

# Read
@login_required
def routeLogistics_list(request):
    routes = routeLogistics.objects.all()
    return render(request, 'routeLogistics/routelogistics_list.html', {'routes': routes})
@login_required
def routeLogistics_detail(request, pk):
    route = get_object_or_404(routeLogistics, pk=pk)
    return render(request, 'routeLogistics/routelogistics_detail.html', {'route': route})

# Update
@login_required
def routeLogistics_update(request, pk):
    route = get_object_or_404(routeLogistics, pk=pk)
    form = routeLogisticsForm(request.POST or None, instance=route)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'routeLogistics/routelogistics_form.html', {'form': form})

# Delete
@login_required
def routeLogistics_delete(request, pk):
    route = get_object_or_404(routeLogistics, pk=pk)
    if request.method == 'POST':
        route.delete()
        return redirect('home')
    return render(request, 'routeLogistics/routelogistics_confirm_delete.html', {'route': route})

