from .forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class ReviewView(FormView):
    template_name = 'review.html'
    from_clas = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review"
        return HttpResponse(msg)
    

    