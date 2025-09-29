"""Django management command to populate the database with historical Pirate Queens."""
from django.core.management.base import BaseCommand
from django.core.management.color import Style
from pirates.models import PirateQueen


class Command(BaseCommand):
    """Management command to populate PirateQueen data."""
    help = 'Populate the database with historical Pirate Queens'

    def handle(self, *args, **options):
        pirate_queens_data = [
            {
                'name': 'Grace O\'Malley (Gráinne Mhaol)',
                'description': (
                    'Irish pirate leader and chieftain who commanded over 200 men '
                    'and controlled the western waters of Ireland. Known as the '
                    '"Pirate Queen of Connacht," she met with Queen Elizabeth I as an equal.'
                ),
                'historical_period': '1530-1603',
                'region': 'Ireland',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/'
                    'Grace_O%27Malley_statue.jpg/256px-Grace_O%27Malley_statue.jpg'
                )
            },
            {
                'name': 'Zheng Yi Sao (Shi Xianggu)',
                'description': (
                    'Chinese pirate leader who commanded over 80,000 outlaws on 1,800 vessels. '
                    'She was one of the most powerful pirate leaders in history and negotiated '
                    'her own amnesty with the Chinese imperial government.'
                ),
                'historical_period': '1775-1844',
                'region': 'South China Sea',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/'
                    'Shi_Xianggu.jpg/256px-Shi_Xianggu.jpg'
                )
            },
            {
                'name': 'Anne Bonny',
                'description': (
                    'Irish-born pirate who operated in the Caribbean. Known for her '
                    'fierce fighting skills and partnership with fellow female pirate '
                    'Mary Read aboard Calico Jack\'s ship.'
                ),
                'historical_period': '1697-1782',
                'region': 'Caribbean',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/'
                    'Anne_Bonny.jpg/256px-Anne_Bonny.jpg'
                )
            },
            {
                'name': 'Mary Read',
                'description': (
                    'English pirate who disguised herself as a man to join the crew. '
                    'She fought alongside Anne Bonny and was known for her sword '
                    'fighting prowess and naval tactics.'
                ),
                'historical_period': '1685-1721',
                'region': 'Caribbean',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/'
                    'Mary_Read.jpg/256px-Mary_Read.jpg'
                )
            },
            {
                'name': 'Jeanne de Clisson',
                'description': (
                    'French noblewoman turned pirate known as the "Lioness of Brittany." '
                    'She commanded a fleet of warships painted black with red sails, '
                    'seeking revenge against the French king.'
                ),
                'historical_period': '1300-1359',
                'region': 'English Channel',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/'
                    'Jeanne_de_Clisson.jpg/256px-Jeanne_de_Clisson.jpg'
                )
            },
            {
                'name': 'Sayyida al Hurra',
                'description': (
                    'Moroccan queen and pirate admiral who controlled the western '
                    'Mediterranean. She was the last person to legitimately hold the '
                    'title "al Hurra" (the free woman).'
                ),
                'historical_period': '1485-1561',
                'region': 'Mediterranean Sea',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/'
                    'Sayyida_al_Hurra.jpg/256px-Sayyida_al_Hurra.jpg'
                )
            },
            {
                'name': 'Rachel Wall',
                'description': (
                    'American pirate and the last woman to be hanged in Massachusetts. '
                    'She was the first American-born woman pirate and operated along '
                    'the New England coast.'
                ),
                'historical_period': '1760-1789',
                'region': 'New England Coast',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/'
                    'Rachel_Wall.jpg/256px-Rachel_Wall.jpg'
                )
            },
            {
                'name': 'Jacquotte Delahaye',
                'description': (
                    'French-Haitian pirate who allegedly faked her own death and '
                    'returned as a male pirate. Known as "Back from the Dead Red" for '
                    'her red hair and supposed resurrection.'
                ),
                'historical_period': '1656-1663',
                'region': 'Caribbean',
                'image_url': (
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/'
                    'Jacquotte_Delahaye.jpg/256px-Jacquotte_Delahaye.jpg'
                )
            }
        ]

        created_count = 0
        for queen_data in pirate_queens_data:
            queen, created = PirateQueen.objects.get_or_create(
                name=queen_data['name'],
                defaults=queen_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    Style.SUCCESS(f'Created Pirate Queen: {queen.name}')
                )
            else:
                self.stdout.write(
                    Style.WARNING(f'Pirate Queen already exists: {queen.name}')
                )

        self.stdout.write(
            Style.SUCCESS(f'Successfully created {created_count} new Pirate Queens')
        )
