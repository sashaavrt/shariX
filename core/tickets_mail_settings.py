#LOGIN_REDIRECT_URL = "tickets:lists"
#LOGIN_URL = "/accounts/login/"
#LOGOUT_REDIRECT_URL = "/accounts/login/"
# tickets-specific settings
TICKETS_STAFF_ONLY = False
TICKETS_DEFAULT_LIST_SLUG = 'tickets'
TICKETS_DEFAULT_ASSIGNEE = None
TICKETS_PUBLIC_SUBMIT_REDIRECT = '/'

from tickets.mail.producers import imap_producer
from tickets.mail.consumers import tracker_consumer
from tickets.mail.delivery import smtp_backend, console_backend

# email notifications configuration
# each task list can get its own delivery method
IS_SEND_EMAIL = False
# TICKETS_MAIL_BACKENDS = {
#     # mail-queue is the name of the task list, not the worker name
#     "mail-queue": smtp_backend(
#         host="*********",
#         port=465,
#         use_ssl=True,
#         username="*********",
#         password="*********",
#         # used as the From field when sending notifications.
#         # a username might be prepended later on
#         from_address="*******",
#         # additionnal headers
#         headers={}
#     ),
# }