from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_user_by_phone_number(request, phone_number):
    if request.method == 'GET':
        if phone_number:
            User = get_user_model()
            try:
                users_with_phone = User.objects.filter(phone_number=phone_number)
                if users_with_phone.exists():
                    user = users_with_phone.first()
                    user_info = {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                    }
                    return JsonResponse(user_info)
                else:
                    # Если пользователь не найден, возвращаем ошибку 404
                    return JsonResponse({'error': 'User not found'}, status=404)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'Phone number is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
