from django.http import FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from .report_utils import generate_evaluation_report
from .models import Evaluation, Personnel
from .forms import EvaluationForm, PersonnelForm
# Create your views here.

def main_page(request):
    return render(request, 'main/index.html')

def personnels(request):
    query = request.GET.get('q', '')  # Get the query from the GET request, default to empty string if not provided
    if query:
        # Filter the personnel based on the search query
        personnels = Personnel.objects.filter(name__icontains=query)  # Filter by name, can be expanded to other fields
    else:
        # If no query, return all personnel
        personnels = Personnel.objects.all()

    return render(request, 'employee/personnels.html', {'personnels': personnels})


# Update Personnel View
def update_personnel(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('personnels')
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'employee/update_personnel.html', {'form': form})

# Delete Personnel View
def delete_personnel(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    if request.method == 'POST':
        personnel.delete()
        return redirect('personnels')
    return render(request, 'employee/delete_personnel.html', {'personnel': personnel})


def add_personnel(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personnels')  # Redirect to the personnel list after saving
    else:
        form = PersonnelForm()
    return render(request, 'employee/add_personnel.html', {'form': form})


def evaluations(request, employee_id):
    employee = get_object_or_404(Personnel, id=employee_id)
    period = request.GET.get('period')
    if period:
        evaluations = Evaluation.objects.filter(employee=employee, period=period)
    else:
        evaluations = Evaluation.objects.filter(employee=employee)
    return render(request, 'evaluations/evaluations.html', {'employee': employee, 'evaluations': evaluations})


def add_evaluation(request, employee_id):
    employee = get_object_or_404(Personnel, id=employee_id)
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.employee = employee
            evaluation.save()
            return redirect('evaluations', employee_id=employee.id)
    else:
        form = EvaluationForm()
    
    return render(request, 'evaluations/add_evaluation.html', {'form': form, 'employee': employee})


def evaluation_report(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)
    filename = generate_evaluation_report(evaluation)
    return FileResponse(open(filename, 'rb'), as_attachment=True, filename=filename)