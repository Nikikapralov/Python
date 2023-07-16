from django.shortcuts import render, redirect

# Create your views here.
from ExamPrep.expenses.models import Profile, Expense
from ExamPrep.expenses.forms import ProfileForm, ExpenseForm


def get_money_left(profile, expenses):
    total_budget = profile.budget
    to_spend = sum([expense.price for expense in expenses])
    result = total_budget - to_spend
    return f"{result:.1f}"


def home_page(request):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses,
        'profile': profile,
    }
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
            # form is invalid
            context = {'form': ProfileForm()}
            return render(request, 'home-no-profile.html', context)
        # GET no profile
        context = {'form': ProfileForm()}
        return render(request, 'home-no-profile.html', context)
    # GET with profile
    money_left = get_money_left(profile, expenses)
    context = {
        'expenses': expenses,
        'profile': profile,
        'money_left': money_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    context = {'form': ExpenseForm()}
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        return render(request, 'expense-create.html', context)
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    context = {
        "form": ExpenseForm(instance=expense, initial=expense.__dict__),
    }
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        return render(request, 'expense-edit.html', context)
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense_to_delete = Expense.objects.get(pk=pk)
    form = ExpenseForm(instance=expense_to_delete, initial=expense_to_delete.__dict__)
    for name, field in form.fields.items():
        field.widget.attrs['disabled'] = 'disabled'
    context = {
        "form": form
    }
    if request.method == 'POST':
        expense_to_delete.delete()
        return redirect('home_page')
    return render(request, 'expense-delete.html', context)


def profile(request):
    expenses = Expense.objects.all()
    my_profile = Profile.objects.first()
    money_left = get_money_left(my_profile, expenses)
    if not my_profile:
        return redirect('home_page')
    context = {
        "profile": my_profile,
        "money_left": money_left,
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    my_profile = Profile.objects.first()
    context = {
        "form": ProfileForm(instance=my_profile, initial=my_profile.__dict__)
    }
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=my_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile-edit.html', context)
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    my_profile = Profile.objects.first()
    expenses = Expense.objects.all()
    if request.method == 'POST':
        my_profile.delete()
        [expense.delete() for expense in expenses]
        return redirect('home_page')
    return render(request, 'profile-delete.html')
