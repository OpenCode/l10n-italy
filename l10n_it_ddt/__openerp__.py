# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Apulia Software s.r.l. (http://www.apuliasoftware.it)
#    @author Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'DDT',
    'version': '1.0',
    'category': 'Localization/Italy',
    'summary': 'Documento di Trasporto',
    'author': 'Francesco Apruzzese, Odoo Community Association (OCA), '
              'Apulia Software',
    'website': 'http://www.odoo-italia.org/',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'stock_picking_package_preparation',
        'stock_picking_package_preparation_line',
        ],
    'data': [
        'data/ddt_data.xml',
        'views/stock_picking_package_preparation.xml',
        'views/partner.xml',
        'views/sale.xml',
        ],
    'test': [],
    'installable': True,
}
