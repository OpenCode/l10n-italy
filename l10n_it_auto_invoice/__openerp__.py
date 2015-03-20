# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name': "Auto Invoice",
    'version': '0.1',
    'category': 'Account',
    'description': """Manage Invoice for Intra CEE supplier""",
    'author': 'Apulia software <info@apuliasoftware.it>',
    'website': 'http://www.apuliasoftware.it',
    'license': 'AGPL-3',
    "depends": ['base', 'account', 'account_voucher', 'account_cancel',
                'account_invoice_entry_date', 'l10n_it'],
    "init_xml": [],
    "data": [
        'data/account.tax.code.csv',
        'data/account.tax.csv',
        'company/company_view.xml',
        'account/account_view.xml',
        'account/account_data.xml',
        ],
    "demo_xml": [],
    "active": False,
    "installable": True
}
