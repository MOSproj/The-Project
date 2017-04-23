#!/usr/bin/env python
# -*- coding: utf-8 -*-


data = {
    'דגם': {
        'before': ['דגם', 'מסוג'],
    },
    'שנה': {
        'before': ['עלה לכביש', 'שנת', 'מודל'],
        'regex': [r'19[7-9]\d', r'20[0-1]\d'],
        'type': 'int'
    },
    'יד': {
        'before': ['יד', 'ידיים'],
        'after': ['ידיים'],
        'type': 'int'
    },
    'מחיר': {
        'before': ['מחיר', 'מבקש'],
        'after': ['שח', '₪'],
        'inside': ['שח', '₪'],
        'regex': [ur'[\u20aa]\d+[\,\d{3}]*'],
        'type': 'int'
    },
    'ק"מ': {
        'before': ['קמ', 'עשה', 'עשתה', 'ק.מ', 'קילומטראז'],
        'after': ['אלף', 'KM', 'קמ', 'קילומטר'],
        'type': 'int'
    },
    'נפח מנוע': {
        'before': ['מנוע'],
        'type': 'int'
    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'\d{3}-?\d{3}-?\d{4}'],
        'regex': [r'\d{3}-?\d{3}-?\d{4}'],
        'type': 'int'
    }

}