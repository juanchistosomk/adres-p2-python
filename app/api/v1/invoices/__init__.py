from flask import Blueprint
from flask_restx import Namespace


invoices_bp = Blueprint('invoices', __name__)
invoices_ns = Namespace('invoices', description='Invoices API operation')
from . import invoices_api