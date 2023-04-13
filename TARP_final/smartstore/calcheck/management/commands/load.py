from django.core.management.base import BaseCommand
import pandas as pd
from smartstore.calcheck.models import Diary

class Command(BaseCommand):
    help = "A command to add data from csv file"

    def handle(self, *args , **options):

        df = pd.read_csv('../../../food_data.csv')
        Diary.objects.all().delete()
        products = [
                    Diary(food=row[1],
                        energy=row[2],
                        protein=row[3],
                         carbs=row[4],
                         sugar=row[5],
                         calcium=row[6],
                         potassium=row[7],
                         sodium=row[8],
                         fa_sat=row[9],
                         fa_mono=row[10],
                         fa_poly=row[11],
                         cholest=row[12],
                         )
        for row in tmp_data.iterrows()
        ]

        Diary.objects.bulk_create(products)