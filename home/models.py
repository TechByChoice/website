from django.db import models
from django import forms
from airtable import Airtable

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import CharBlock, FieldBlock, ListBlock, RawHTMLBlock, \
    RichTextBlock, StreamBlock, StructBlock, TextBlock
from wagtail.embeds.blocks import EmbedBlock


class WideImage(StructBlock):
    image = ImageChooserBlock()

    class Meta:
        icon = "image"

class BustoutBlock(StructBlock):
    image = ImageChooserBlock()
    text = RichTextBlock()

    class Meta:
        icon = "pick"

class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'),
        ('right', 'Wrap right'),
        ('mid', 'Mid width'),
        ('full', 'Full width'),
    ))

class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()
    link = CharBlock(required=False)

class DemoStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    h5 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image")
    wide_image = WideImage(label="Wide image")
    bustout = BustoutBlock()
    pullquote = PullQuoteBlock()
    raw_html = RawHTMLBlock(label='Raw HTML', icon="code")
    embed = EmbedBlock(icon="code")


class RawHtmlEntry(StreamBlock):
    raw_html = RawHTMLBlock(label='Raw HTML', icon="code")


class HomePage(Page):
    base_key = 'app2OXtbMVkriy7KX'
    table_name = 'TBC Directory'
    airtable = Airtable(base_key, 'table_name', api_key='keyCDI9g6pLU2Le5i')
    print(Page)

class CodeOfConductPage(Page):
    print("hey")
    template = "home/coc.html"

class AboutPage(Page):
    template = "home/about_page.html"

class TeamPage(Page):
    base_key = 'app2OXtbMVkriy7KX'
    table_name = 'TBC Directory'
    airtable = Airtable(base_key, 'table_name', api_key='keyCDI9g6pLU2Le5i')
    print(airtable)

    template = "home/team.html"

class DiversityStatementPage(Page):
    template = "home/diversity-statement.html"

class CurriculumPage(Page):
    template = "home/curriculum.html"

# Generic Page - Core Page


class GenericPage(Page):
    body_text = StreamField(DemoStreamBlock(), null=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = ['body_text', 'feed_image']


# Generic Page - Admin Panel Layout
GenericPage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body_text'),
]

GenericPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]
