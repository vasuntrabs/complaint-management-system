from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm
from django.contrib import messages   # ✅ IMPORTANT

def home(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()

            # ✅ SUCCESS MESSAGE
            messages.success(request, "Complaint submitted successfully!")

            return redirect('home')   # redirect back to same page
    else:
        form = ComplaintForm()

    return render(request, 'tickets/home.html', {'form': form})


def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'tickets/list.html', {'complaints': complaints})