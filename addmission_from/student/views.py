from django.shortcuts import render,redirect
from .forms import AdmissionFrom
# Create your views here.
def admission_view(request):
    if request.method=='POST':
        form=AdmissionFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'student/success.html')
    else:
        form=AdmissionFrom()
    return render(request,'student/admission_from.html',{'from':form})