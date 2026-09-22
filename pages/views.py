from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request): 
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3", "Widget 4"],
        "greeting" : "THAnk you FOR visitING."
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
class products_page_view(TemplateView):
    template_name = "products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = [
            {"name": "Bread", "sales_price": 9.99},
            {"name": "Soup", "sales_price": 3.99},
            {"name": "Dr.Pepper (12pk)", "sales_price": 5.99},
            {"name": "Napkins", "sales_price": 1.99},
        ]
        return context