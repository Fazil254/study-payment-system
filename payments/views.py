from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment
import json
from django.views.decorators.csrf import csrf_exempt

COURSES = [
    {'id': 1, 'name': 'Python',          'desc': 'Learn Python from scratch.',        'price': 1999},
    {'id': 2, 'name': 'Web Development', 'desc': 'HTML, CSS, JavaScript and Django.', 'price': 2999},
    {'id': 3, 'name': 'Data Science',    'desc': 'Data analysis and visualization.',  'price': 3499},
]

def home(request):
    return render(request, 'payments/home.html', {'courses': COURSES})

def course_detail(request, course_id):
    course = next((c for c in COURSES if c['id'] == course_id), None)
    return render(request, 'payments/course_detail.html', {'course': course})

def payment_page(request, course_id):
    course = next((c for c in COURSES if c['id'] == course_id), None)
    return render(request, 'payments/payment.html', {'course': course})

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Payment.objects.create(
                name=data['name'],
                email=data['email'],
                course=data['course'],
                amount=data['amount'],
                payment_status='Success'
            )
            return JsonResponse({'success': True})
        except (KeyError, json.JSONDecodeError) as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    # FIX: was returning None (HTTP 500) for non-POST requests
    return JsonResponse({'error': 'Method not allowed'}, status=405)
