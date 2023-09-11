from django.shortcuts import render

chickens = [
    {'name': 'Nugget', 'breed': 'Buff Orpington', 'description': 'very friendly, loves mealworms', 'age': 3},
    {'name': 'Colonel', 'breed': 'Rhode Island Red', 'description': 'fiesty, likes to peck at any visitors', 'age': 3}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chickens_index(request):
    return render(request, 'chickens/index.html', {
        'chickens': chickens
    })