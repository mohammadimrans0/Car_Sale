from django.http import HttpResponseRedirect
from car.forms import CarForm, CommentForm
from car.models import Car
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create_car.html'
    success_url = reverse_lazy('main')
    def form_valid(self, form):
        return super().form_valid(form)

class DetailCarView(DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to save a new comment.
        """
        # Get the car object (this will be the object being viewed in the template)
        self.object = self.get_object()  
        comment_form = CommentForm(request.POST)
        
        # Check if the form is valid
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = self.object  # Associate the comment with the car object
            new_comment.name = request.user.get_full_name()  # Set the user's name
            new_comment.email = request.user.email  # Set the user's email
            new_comment.save()

            # Redirect back to the car details page
            return HttpResponseRedirect(reverse('car_details', args=[self.object.pk]))

        # If the form is invalid, render the page with the form errors
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Add comments and the comment form to the context.
        """
        # Get the default context data from the parent class
        context = super().get_context_data(**kwargs)
        
        # Fetch the current car and related comments
        car = self.object
        comments = car.comments.all()  # Assuming 'comments' is the related_name for comments
        
        # Add the comments and the empty (or filled) comment form to the context
        context['comments'] = comments
        context['comment_form'] = kwargs.get('comment_form', CommentForm())

        return context


@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if car.quantity > 0:
        car.quantity -= 1
        car.purchased_by.add(request.user)
        car.save()
        messages.success(request, "Car purchased successfully!")
    else:
        messages.error(request, "Sorry, this car is out of stock.")
    
    return redirect('car_details', pk=car.id)

    
class EditCarView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'update_car.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


class DeleteCarView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'delete_car.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

