import random
import string
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import GeneratedPassword
import json


def home(request):
    """Main page view"""
    return render(request, 'generator/home.html')


@csrf_exempt
@require_http_methods(["POST"])
def generate_password(request):
    """API endpoint to generate password"""
    try:
        data = json.loads(request.body)
        
        # Get parameters with defaults
        length = int(data.get('length', 12))
        include_uppercase = data.get('include_uppercase', True)
        include_lowercase = data.get('include_lowercase', True)
        include_numbers = data.get('include_numbers', True)
        include_symbols = data.get('include_symbols', True)
        
        # Validate length
        if length < 4 or length > 128:
            return JsonResponse({'error': 'Password length must be between 4 and 128 characters'}, status=400)
        
        # Build character set
        chars = ''
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'
        
        if not chars:
            return JsonResponse({'error': 'At least one character type must be selected'}, status=400)
        
        # Generate password
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Save to database
        GeneratedPassword.objects.create(
            password=password,
            length=length,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase,
            include_numbers=include_numbers,
            include_symbols=include_symbols
        )
        
        return JsonResponse({
            'password': password,
            'length': length,
            'include_uppercase': include_uppercase,
            'include_lowercase': include_lowercase,
            'include_numbers': include_numbers,
            'include_symbols': include_symbols
        })
        
    except (ValueError, KeyError) as e:
        return JsonResponse({'error': 'Invalid input data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'An error occurred while generating password'}, status=500)


def password_history(request):
    """View to show password generation history"""
    passwords = GeneratedPassword.objects.all()[:50]  # Show last 50 passwords
    return render(request, 'generator/history.html', {'passwords': passwords})
