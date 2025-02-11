from datetime import datetime, timedelta

from tickets.models import Ticket, TicketList
from dbsynce.models import DocumentFile
from dbsynce.lib.core import get_admin_url


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
            <a href="{get_admin_url(сompany)}">Полная информация</a>\n
            \n
            Проверьте всю информацию и для активации партнера измените статус заявки на ACCEPTED.
            Это будет означать, что договорные отношения между сервисом и партнером, вступают в силу.
        """
    )


def create_ticket_partner_docs_verification(user, company, doc):
    """
    Создание тикета на проверку документов партнера.
    
    Список: 2103, METASERVICE-ADMIN: Проверка документов (ST_REQUEST)
    Тип: 1, ST_REQUEST
    """
    doc_name = doc.get_doc_type_display()
    doc_files = DocumentFile.objects.filter(document=doc)

    note=f"Пользователь {user} #{user.pk} добавил новые файлы документа <a href='{get_admin_url(doc)}'>{doc_name}</a> партнера <a href='{get_admin_url(company)}'>{company.legal_name}</a> требующие проверки:<ul>"
    for file in doc_files:
        note += f"<li><a href='{file.file.url}' target='_blank'>{file}</a></li>"
    note += "</ul>"
    
    return Ticket.objects.create(
        title=f"Проверка документа '{doc_name}' партнера '{company.legal_name}'",
        ticket_list=TicketList.objects.get(pk=2103),
        ticket_type=1,
        due_date=datetime.now().date() + timedelta(days=30),
        created_by=user,
        note=note
    )    