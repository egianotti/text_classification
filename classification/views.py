from django.shortcuts import render
from django.views import View


# Create your views here.
class TextClassificationView(View):
    template_name = "templates/text-classification.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
