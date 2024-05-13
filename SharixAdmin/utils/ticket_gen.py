from datetime import datetime, timedelta

from tickets.models import Ticket, TicketList


def create_ticket_partner_activation(user, сompany):
    """
    Создание тикета на активацию партнера.
    
    Список: 2101, METASERVICE-ADMIN: Активация партнеров (NEG_REQUEST)
    Тип: 4, NEG_REQUEST
    """
    # FIXME: Возможно нужно автоматически создавать содержимое поля json
    return Ticket.objects.create(
        title=f"Создание нового Партнера '{сompany.legal_name}'",
        ticket_list=TicketList.objects.get(pk=2101),
        ticket_type=4,
        due_date=datetime.now().date() + timedelta(days=30),
        created_by=user,
        
        note=f"""
            Пользователь {user} #{user.pk} отправил заявку на становление партнером сервиса:\n
            - Имя: {сompany.legal_name}\n
            - ИНН: {сompany.inn}\n
            - Юридический адрес: {сompany.address}\n
            <a href="{сompany.get_admin_url()}">Полная информация</a>\n
            \n
            Проверьте всю информацию и для активации партнера измените статус заявки на ACCEPTED.
            Это будет означать, что договорные отношения между сервисом и партнером, вступают в силу.
        """
    )

    