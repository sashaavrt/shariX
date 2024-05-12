from django.contrib.auth.decorators import user_passes_test


# Функция позволяющая определить принадлежность к группе, перенаправляет на авторизацию
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_names).exists() or u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)