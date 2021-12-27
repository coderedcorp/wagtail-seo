# Generated by Django 3.2.10 on 2021-12-27 13:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211227_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='struct_org_actions',
            field=wagtail.core.fields.StreamField([('actions', wagtail.core.blocks.StructBlock([('action_type', wagtail.core.blocks.ChoiceBlock(choices=[('OrderAction', 'OrderAction'), ('ReserveAction', 'ReserveAction'), ('SearchAction', 'SearchAction')], verbose_name='Action Type')), ('target', wagtail.core.blocks.URLBlock(help_text='e.g. http://example.com/search?&q={query}', verbose_name='Target URL')), ('query', wagtail.core.blocks.ChoiceBlock(choices=[('required', 'required')], help_text="Is the search `query` parameter required for your search engine. Optional for 'Action Type' SearchAction", required=False, verbose_name='Search query required')), ('language', wagtail.core.blocks.CharBlock(default='en-US', help_text='If the action is offered in multiple languages, create separate actions for each language.', verbose_name='Language')), ('result_type', wagtail.core.blocks.ChoiceBlock(choices=[('Reservation', 'Reservation'), ('BusReservation', 'BusReservation'), ('EventReservation', 'EventReservation'), ('FlightReservation', 'FlightReservation'), ('FoodEstablishmentReservation', 'FoodEstablishmentReservation'), ('LodgingReservation', 'LodgingReservation'), ('RentalCarReservation', 'RentalCarReservation'), ('ReservationPackage', 'ReservationPackage'), ('TaxiReservation', 'TaxiReservation'), ('TrainReservation', 'TrainReservation')], help_text='Leave blank for OrderAction and SearchAction', required=False, verbose_name='Result Type')), ('result_name', wagtail.core.blocks.CharBlock(help_text='Example: "Reserve a table", "Book an appointment", etc.', required=False, verbose_name='Result Name')), ('extra_json', wagtail.core.blocks.RawHTMLBlock(form_classname='monospace', help_text='Additional JSON-LD inserted into the Action dictionary. Must be properties of https://schema.org/Action.', required=False, verbose_name='Additional action markup'))]))], blank=True, verbose_name='Actions'),
        ),
        migrations.AlterField(
            model_name='seopage',
            name='struct_org_actions',
            field=wagtail.core.fields.StreamField([('actions', wagtail.core.blocks.StructBlock([('action_type', wagtail.core.blocks.ChoiceBlock(choices=[('OrderAction', 'OrderAction'), ('ReserveAction', 'ReserveAction'), ('SearchAction', 'SearchAction')], verbose_name='Action Type')), ('target', wagtail.core.blocks.URLBlock(help_text='e.g. http://example.com/search?&q={query}', verbose_name='Target URL')), ('query', wagtail.core.blocks.ChoiceBlock(choices=[('required', 'required')], help_text="Is the search `query` parameter required for your search engine. Optional for 'Action Type' SearchAction", required=False, verbose_name='Search query required')), ('language', wagtail.core.blocks.CharBlock(default='en-US', help_text='If the action is offered in multiple languages, create separate actions for each language.', verbose_name='Language')), ('result_type', wagtail.core.blocks.ChoiceBlock(choices=[('Reservation', 'Reservation'), ('BusReservation', 'BusReservation'), ('EventReservation', 'EventReservation'), ('FlightReservation', 'FlightReservation'), ('FoodEstablishmentReservation', 'FoodEstablishmentReservation'), ('LodgingReservation', 'LodgingReservation'), ('RentalCarReservation', 'RentalCarReservation'), ('ReservationPackage', 'ReservationPackage'), ('TaxiReservation', 'TaxiReservation'), ('TrainReservation', 'TrainReservation')], help_text='Leave blank for OrderAction and SearchAction', required=False, verbose_name='Result Type')), ('result_name', wagtail.core.blocks.CharBlock(help_text='Example: "Reserve a table", "Book an appointment", etc.', required=False, verbose_name='Result Name')), ('extra_json', wagtail.core.blocks.RawHTMLBlock(form_classname='monospace', help_text='Additional JSON-LD inserted into the Action dictionary. Must be properties of https://schema.org/Action.', required=False, verbose_name='Additional action markup'))]))], blank=True, verbose_name='Actions'),
        ),
    ]
