# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2015-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Enhace Marketing campaigns',
    'category': 'marketing',
    'summary': 'Enhace Marketing campaigns',
    'version': '8.0.0.1',
    'description': """
    """,
    'author': 'Trey (www.trey.es)',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'marketing_campaign',
        'product',
        'purchase',
        'survey',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_rules.xml',
        'views/marketing_campaign_workflow.xml',
        'views/campaign_view.xml',
        'views/partner_view.xml',
        'views/sale_view.xml',
        'views/marketing_campaign_view.xml',
        'views/survey_view.xml',
        'views/marketing_project_type_view.xml',
        'views/marketing_issue_type_view.xml',
        'views/collaboration_reason_view.xml',
        'wizards/survey_user_input_finalize.xml',
        'wizards/export_media_delivery.xml',
        'wizards/import_media_delivery.xml',
        'views/menu.xml'
    ],
    'installable': True,
}
