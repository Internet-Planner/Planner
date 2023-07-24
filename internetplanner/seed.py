from django_seed import Seed

seeder = Seed.seeder()

from api.models import Events, Video
seeder.add_entity(Events, 5)
seeder.add_entity(Video, 10)

inserted_pks = seeder.execute()

seeder.add_entity(Video, 10, {
        'my_field': 'https://www.youtube.com/watch?v=P1UqJBNQ1EI',
    })