from django.shortcuts import render,get_object_or_404,redirect
from .models import Notes
from .forms import NoteForm

# Create your views here.
def list_view(request):
    notes_list = Notes.objects.order_by('-pinned','-created')
    return render(request,'notes/notes_list.html',{'notes':notes_list})
def  edit(request,id):
    
    note = get_object_or_404(Notes,id = id)
    if request.method == "POST":
        form = NoteForm(request.POST,instance = note)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    else:
        form = NoteForm(instance = note)
    return render(request,'notes/note_form.html',{'note_form':form})

def add(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    else:
        form = NoteForm()
    return render(request,'notes/note_form.html',{'note_form':form})

def delete(request, id):
    note = get_object_or_404(Notes, id=id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')

    return render(request, 'notes/note_confirm_delete.html', {'note': note})





