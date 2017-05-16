# !/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode
import group_criteria_analysis
from car_text_analysis import data as car_text_analysis
from cellular_text_analysis import data as cellular_text_analysis
from nadlan_text_analysis import data as nadlan_text_analysis

min_specs = 2
text_analysis_files = {
    u'רכב': car_text_analysis,
    u'סלולר': cellular_text_analysis,
    u'נדלן': nadlan_text_analysis
}


def analyse_database_post(database_post, category_name):
    if should_be_ignore(database_post):
        database_post.set_ignore()
    else:
        specs = get_specs_from_post(database_post, category_name)
        if 'טלפון' in specs:
            database_post.set_phone(specs['טלפון'])
            del specs['טלפון']
        if 'מחיר' in specs:
            database_post.set_price(specs['מחיר'])
            del specs['מחיר']
        if 'מיקום' in specs and not database_post.has_location():
            database_post.set_location(specs['מיקום'])
            del specs['מיקום']
        if 'ק"מ' in specs:
            km = specs['ק"מ']
            if len(str(km)) <= 3:
                specs['ק"מ'] = km*1000
        if len(specs) >= min_specs:
            database_post.set_specs(specs)
        else:
            database_post.set_ignore()


def get_specs_from_post(database_post, category_name):
    message = database_post.get_message()
    # TODO: insert self-re as first option
    return group_criteria_analysis.analyse(message, text_analysis_files[category_name])


def should_be_ignore(post):
    words = ['מחפש', 'מחפשת', 'מחפשים', 'להחליף', 'החלפה', 'מתעניין', 'מתעניינת', 'מעוניין', 'למישהו', 'מעוניינת',
             'שתפו', 'לשתף', "ספינרים", 'מגוון']
    post_message = post.get_message()
    for word in words:
        if to_unicode(word) in post_message:
            return True
    return False
