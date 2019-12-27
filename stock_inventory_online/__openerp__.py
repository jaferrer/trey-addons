# -*- coding: utf-8 -*-
##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2018-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
##############################################################################
{
    'name': 'Stock Inventory Online',
    'summary': 'Define stock inventory for users and product seasons',
    'description': '',
    'author': 'Trey (www.trey.es)',
    'license': 'AGPL-3',
    'website': 'https://www.trey.es',
    'category': 'Product',
    'version': '8.0.1.0.0',
    'depends': [
        'base',
        'product_season',
        'stock'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stock_inventory_online.xml',
    ],
    'installable': True,
}
