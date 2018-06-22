from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now, localdate


class Client(models.Model):
    name = models.CharField('nome', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class Raffle(models.Model):
    description = models.CharField('descrição', max_length=120)
    numbers = models.PositiveIntegerField('números')
    initial_number = models.IntegerField('número inicial', default=0)
    observation = models.TextField('observação', null=True, blank=True)
    price = models.DecimalField('preço', max_digits=15, decimal_places=2, default=0)
    draw_date = models.DateField('data do sorteio', blank=True, null=True)

    @property
    def reserved(self):
        return self.ticket_set.filter(client__isnull=False).count()

    @staticmethod
    def ticket_caption():
        return Ticket._meta.verbose_name

    def __str__(self):
        return "#" + str(self.id) + "-Rifa " + self.description

    class Meta:
        verbose_name = 'rifa'
        verbose_name_plural = 'rifas'


@receiver(post_save, sender=Raffle)
def generate_raffle_tickets(sender, instance, created, **kwargs):
    if created:
        numbers = []
        for x in range(instance.initial_number, instance.numbers):
            numbers.append(Ticket(raffle=instance, number=x))
        instance.ticket_set.bulk_create(numbers)


class Ticket(models.Model):
    raffle = models.ForeignKey('Raffle', on_delete=models.PROTECT, verbose_name=Raffle._meta.verbose_name)
    number = models.IntegerField('número', editable=False)
    client = models.ForeignKey('Client', on_delete=models.PROTECT, verbose_name=Client._meta.verbose_name, null=True,
                               blank=True)
    booking_date = models.DateField('data da reserva', null=True, blank=True)
    is_paid = models.BooleanField('pago?', default=False)

    def __str__(self):
        numbers = self.raffle.numbers
        if self.raffle.initial_number == 0:
            numbers -= 1
        numbers = len(str(numbers))
        return str(self.number).zfill(numbers)

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = (("raffle", "number"),)
        ordering = ('number',)
        verbose_name = 'bilhete'
        verbose_name_plural = 'bilhetes'


@receiver(post_save, sender=Ticket)
def ticket_post_save(sender, instance, created, **kwargs):
    if instance.client is not None and instance.booking_date is None:
        instance.booking_date = localdate()
        instance.save()
