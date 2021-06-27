from django.shortcuts import render, redirect

from Notes.my_notes.forms import NoteForm, ProfileForm
from Notes.my_notes.models import Note, Profile


# Create your views here.
def set_fields_of_form_to(form, field_to_set, set_to):
    for name, field in form.fields.items():
        field.widget.attrs[field_to_set] = set_to
    return form

def home_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    context_profile = {
        'notes': notes
    }
    # No profile has been created
    if not profile:
        form = ProfileForm()
        context_no_profile = {
            "form": form
        }
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'home-with-profile.html', context_profile)
            return render(request, 'home-no-profile.html', context_no_profile)
        return render(request, 'home-no-profile.html', context_no_profile)
    # A profile has been created
    context_profile = {
        'notes': notes
    }
    return render(request, 'home-with-profile.html', context_profile)


def profile_page(request):
    notes = Note.objects.all()
    amount = len(notes)
    profile = Profile.objects.first()
    context = {
        'notes': notes,
        'profile': profile,
        'amount': amount
    }
    return render(request, 'profile.html', context)


def profile_delete(request):
    notes = Note.objects.all()
    profile = Profile.objects.first()
    profile.delete()
    [note.delete() for note in notes]
    return redirect('home_page')


def add_note(request):
    context = {'form': NoteForm()}
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        return render(request, 'note-create.html', context)
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note_to_edit = Note.objects.get(pk=pk)
    context = {
        'form': NoteForm(instance=note_to_edit, initial=note_to_edit.__dict__)
    }
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note_to_edit)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        return render(request, 'note-edit.html', context)
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note_to_delete = Note.objects.get(pk=pk)
    form = set_fields_of_form_to(NoteForm(instance=note_to_delete, initial=note_to_delete.__dict__),
                                 'disabled', 'disabled')
    context = {'form': form}

    if request.method == 'POST':
        note_to_delete.delete()
        return redirect('home_page')
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {'note': note}
    return render(request, 'note-details.html', context)






