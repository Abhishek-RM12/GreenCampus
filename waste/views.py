from django.shortcuts import render, redirect
from .forms import WasteReportForm
from .models import WasteReport

def submit_report(request):
    if request.method == "POST":
        form = WasteReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reports')
    else:
        form = WasteReportForm()
    return render(request, 'waste/submit_report.html', {'form': form})

def home(request):
    return render(request, 'waste/reports.html', {'reports': WasteReport.objects.all().order_by('-date_reported')})

def reports(request):
    reports = WasteReport.objects.all().order_by('-date_reported')
    return render(request, 'waste/reports.html', {'reports': reports})
