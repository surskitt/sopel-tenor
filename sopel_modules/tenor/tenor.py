# coding=utf-8

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)


from sopel import module
from sopel.config.types import StaticSection, ValidatedAttribute

import requests


class TenorSection(StaticSection):
    api = ValidatedAttribute('api_key', str)


def setup(bot):
    bot.config.define_section('tenor', TenorSection)


def configure(config):
    config.define_section('api_key', TenorSection)
    config.tenor.configure_setting('api_key', 'Tenor api key')


def template_endpoint(search_term, api_key):
    endpoint_template = 'https://api.tenor.com/v1/search?q={}&key={}&limit=10'
    endpoint = endpoint_template.format(search_term, api_key)

    return endpoint
