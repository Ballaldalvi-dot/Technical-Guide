from django.core.management.base import BaseCommand
from django.utils import timezone
from todoapp.models import Todo
from django.core.mail import send_mail  # Use any other notification method if preferred

class Command(BaseCommand):
    help = 'Check for overdue reminders and send notifications'

reminder_datetime = timezone.make_aware(timezone.get_current_timezone())

# When retrieving a datetime
reminder_datetime_utc = reminder_datetime.astimezone(timezone.utc)

def handle(self, *args, **kwargs):
        now = timezone.now()
        todos = Todo.objects.filter(reminder__lte=now, notified=False, completed=False)

        for todo in todos:
            # Send an email or any other notification
            send_mail(
                'Reminder: {}'.format(todo.title),
                'Reminder for your task: {}. Description: {}'.format(todo.title, todo.description),
                'from@example.com',
                ['to@example.com'],  # You can use todo.assigned_to if it's an email
                fail_silently=False,
            )
            todo.notified = True
            todo.save()

        self.stdout.write(self.style.SUCCESS('Successfully checked and notified overdue reminders'))
