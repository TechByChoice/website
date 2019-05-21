from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass

class CodeOfConductPage(Page):
    template = "home/coc.html"

class DiversityStatementPage(Page):
    template = "home/diversity-statement.html"

class CurriculumPage(Page):
    template = "home/curriculum.html"
