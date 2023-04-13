from import_export import resources
from .models import Diary
class DiaryResource(resources.ModelResource):
     class Meta:
         model = Diary