from django.shortcuts import render, redirect

# from .forms import MedicineForm
from .models import Medicines


def index(request):
    medicines = Medicines.objects.all()
    return render(request, 'show.html', {'medicines': medicines})








    # if request.method == 'POST':
    #     form = MedicineForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('/show')
    #         except:
    #             pass
    # else:
    #     form = MedicineForm()
    #     return render(request, 'index.html', {'form': form})
#

# def med(request):
#     if request.method == 'POST':
#         form = MedicineForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = MedicineForm()
#         return render(request, 'index.html', {'form': form})
#
#
# def show(request):
#     medicines = Medicines.objects.all()
#     return render(request, 'show.html', {'medicines': medicines})
#
#
# def update(request, id):
#     medicine = Medicines.objects.get(id=id)
#     form = MedicineForm(request.POST, instance=medicine)
#
#     if form.is_valid():
#         form.save()
#         return redirect('/show')
#     return render(request, 'edit.html', {'medicine': medicine})
#
#
# def destroy(request, id):
#     medicine = Medicines.objects.get(id=id)
#     medicine.delete()
#     return redirect('/show')
