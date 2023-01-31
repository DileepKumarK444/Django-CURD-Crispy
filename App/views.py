from App.models import Employee
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin # For Add/ Update
from django.contrib import messages # for Delete

# CREATE
class Create(SuccessMessageMixin,CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Employee %(name)s created successfully!"

# READ
class Read(ListView):
    model = Employee
    queryset = Employee.objects.all()
# UPDATE
class Update(SuccessMessageMixin,UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = 'Employee %(name)s updated successfully!'

# DELETE
class Delete(DeleteView):
    # queryset = Employee.objects.all()
    # success_url = reverse_lazy('read')
    model = Employee
    def get_success_url(self):
        messages.success(self.request, 'Employee Deleted successfully!')
        return reverse('read')
