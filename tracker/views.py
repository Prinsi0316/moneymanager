from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expense, Income
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Rating
from .models import Note
from django.views.decorators.http import require_POST


def index(request):
    if request.method == 'POST':
        income = request.POST.get('income')
        expense = request.POST.get('expense')
        balance = request.POST.get('balance')

        # Save to session
        request.session['income'] = income
        request.session['expense'] = expense
        request.session['balance'] = balance

        return redirect('reports')  # Redirect to reports page after submission

    return render(request, 'tracker/index.html')
def records(request):
    if request.method == "POST":
        category = request.POST.get('category')
        amount = request.POST.get('amount')

        # Save the expense to the database
        Expense.objects.create(category=category, amount=amount)

        return redirect('records')  # Redirect to records page after submission

    # Handle GET request: fetch and display records
    records = Expense.objects.all()  # Fetch all records from the Expense model
    return render(request, 'tracker/records.html', {'records': records})  # Make sure to use the correct app name


def notes_view(request):
    if request.method == 'POST':
        note_name = request.POST.get('note_name', 'Note')
        note_content = request.POST.get('note_content')

        # Create or update the note
        if note_content:
            Note.objects.create(name=note_name, content=note_content)  # Save the note to the database
            return JsonResponse({'message': 'Note submitted successfully!'})

    notes = Note.objects.all()  # Get all notes to display
    return render(request, 'tracker/notes.html', {'notes': notes})  # Render the notes page
def reports(request):
    income = float(request.session.get('income', 0))
    expense = float(request.session.get('expense', 0))
    balance = float(request.session.get('balance', 0))

    context = {
        'income': income,
        'expense': expense,
        'balance': balance
    }
    return render(request, 'tracker/reports.html', context)
def profile(request):
    return render(request, 'tracker/profile.html')
def add_new(request):
    return render(request, 'tracker/add_new.html')

def payment(request):
    return render(request,'tracker/payment.html')


@csrf_exempt
def submit_rating(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            rating_value = data.get('rating')

            # Save the rating
            rating = Rating(stars=rating_value)
            rating.save()

            return JsonResponse({'status': 'success', 'message': 'Thank you for your rating!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@require_POST
def rename_note_view(request):
    note_id = request.POST.get('note_id')
    new_name = request.POST.get('note_name')
    note = Note.objects.get(id=note_id)
    note.name = new_name
    note.save()
    return JsonResponse({'message': 'Note renamed successfully!'})

@require_POST
def delete_note_view(request):
    note_id = request.POST.get('note_id')
    Note.objects.filter(id=note_id).delete()
    return JsonResponse({'message': 'Note deleted successfully!'})
