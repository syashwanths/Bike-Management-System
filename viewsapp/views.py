from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from viewsapp.models import Company
from django.urls import reverse_lazy
from viewsapp.models import Products 

# Create your views here.
# class Myclass(View):
#     def get(self,request):
#         return HttpResponse("<h1>This is Class Based View</h1>")

class htmlpage(TemplateView):
    template_name = 'index.html'


class Allcompanies(ListView):
    model = Company

class CompanyDetail(DetailView):
    model = Company
    context_object_name = 'companies_detail'

class Addcompany(CreateView):
    model = Company
    fields = "__all__"

class EditCompany(UpdateView):
    model = Company
    fields = ['company_name','ceo']

class DeleteCompany(DeleteView):
    model = Company
    success_url = reverse_lazy('list')

def EmiCalulator(request,id= 0):
    product_details = Products.objects.get(id=id)
    if request.method == 'POST':
        amount = int(request.POST['Amount'])
        tenure = int(request.POST['tenure'])
        interest = int(request.POST['interest'])
        r = interest / (interest * 100)
        numerator = amount * r * (1 + r) ** tenure
        denominator = (1 + r)**tenure - 1
        emi_per_month = numerator / denominator
        return render(request,"emi_calculator.html",{'emi_per_month':emi_per_month})
    
    return render(request,'emi_calculator.html',{'product_details': product_details})