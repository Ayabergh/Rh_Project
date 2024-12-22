from django.shortcuts import render, get_object_or_404, redirect
from .models import Personnel
from .forms import PersonnelForm
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
