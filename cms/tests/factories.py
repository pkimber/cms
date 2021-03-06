# -*- encoding: utf-8 -*-
import factory

from block.tests.factories import SectionFactory
from cms.models import (
    Template,
    TemplateSection,
)


class TemplateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Template


class TemplateSectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = TemplateSection

    template = factory.SubFactory(TemplateFactory)
    section = factory.SubFactory(SectionFactory)
