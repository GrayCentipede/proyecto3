from django_seed import Seed
from myapp.models import Affiliation, Person, Journal, Publication, ExternalAuthor, Grant, Group

seeder = Seed.seeder()

inserted_pks = seeder.execute()