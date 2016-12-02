# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        # {
        #	"module_name": "Climbforce",
        #	"color": "orange",
        #	"icon": "octicon octicon-file-directory",
        #	"type": "module",
        #	"label": _("Climbforce")
        # }
        {
            "module_name": "Custom General Ledger",
            "color": "#F39C12",
            "icon": "octicon octicon-file-directory",
            "label": _("Custom General Ledger"),
             "link": "query-report/Climbforce General Ledger",
            "_doctype": "GL Entry",
            "type": "link"
        },
    ]
