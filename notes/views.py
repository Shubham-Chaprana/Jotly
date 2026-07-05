from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Notes
from .forms import NoteForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('notes:list')

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes:list')
    else:
        form = SignUpForm()

    return render(request, 'notes/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('notes:list')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('notes:list')
    else:
        form = AuthenticationForm()

    return render(request, 'notes/login.html', {'form': form})

@login_required
def list_view(request):
    query = request.GET.get('q','')
    notes_list = Notes.objects.filter(user = request.user).order_by('-pinned','-created')
    if query:
        notes_list = notes_list.filter(
            Q(title__icontains = query) | Q(content__icontains = query)
            )
    return render(request,'notes/notes_list.html',{'notes':notes_list,'query':query})

@login_required
def  edit(request,id):
    
    note = get_object_or_404(Notes,user = request.user,id = id)
    if request.method == "POST":
        form = NoteForm(request.POST,instance = note)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    else:
        form = NoteForm(instance = note)
    return render(request,'notes/note_form.html',{'note_form':form})

@login_required
def add(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:list')
    else:
        form = NoteForm()
    return render(request,'notes/note_form.html',{'note_form':form})

@login_required
def delete(request, id):
    note = get_object_or_404(Notes, user = request.user,id=id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')

    return render(request, 'notes/note_confirm_delete.html', {'note': note})