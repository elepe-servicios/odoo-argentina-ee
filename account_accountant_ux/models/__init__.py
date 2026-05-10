##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from . import bank_rec_widget
from . import account_move_line
from . import account_move
from . import res_partner
from . import account_journal_dashboard
from . import account_partner_ledger
# from . import account_report disabled because field require_custom_filter already exists in account_report module of account_reports, and it creates a conflict when both modules are installed. The field should be moved to account_report module of account_reports to avoid this conflict and then this import can be re-enabled.
