from App.models import Employee
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# CREATE
class Create(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read')

# READ
class Read(ListView):
    model = Employee
    queryset = Employee.objects.all()
# UPDATE
class Update(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read')
# DELETE
class Delete(DeleteView):
    queryset = Employee.objects.all()
    success_url = reverse_lazy('read')