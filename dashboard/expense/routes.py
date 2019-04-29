from flask import Blueprint, request, jsonify
from dashboard.auth.utils import token_required
from dashboard import mongo
from dashboard.common.currency import Currency
from dashboard.common.tax import Tax

expense = Blueprint('expense', __name__)


@expense.route('/expense', methods=['POST'])
@token_required
def new_expense_entry(current_user):
    """
    Create new expense entry
    """
    request_data = request.get_json()
    expenses = mongo.db.expense
    expenses.insert(
        {
            "user_id": current_user.public_id,
            "employee": "{} {}".format(current_user.first_name, current_user.last_name),
            "date": request_data["date"],
            "expense_type": request_data["expense_type"],
            "project": request_data["project"],
            "purpose": request_data["purpose"],
            "payment_method": request_data["payment_method"],
            "currency": Currency.NZD,
            "tax_type": Tax.GST,
            "net_amount": request_data["net_amount"],
            "amount": request_data["amount"],
            "description": request_data["description"],
            "status": "Received"
        }
    )
    # TODO: quarter needs to be unique
    return jsonify({'message': 'Expense entry saved!'}), 200


@expense.route('/expense/<public_id>', methods=['GET'])
@token_required
def get_all_expenses(current_user, public_id):
    """
    Get all expense entries against user public id
    """
    expenses = mongo.db.expense
    entries = expenses.find({"user_id": public_id})
    # output = []

    # for entry in entries:
    #     expense_data = {}
    #     expense_data['user_id'] = entry["user_id"]
    #     expense_data['employee'] = entry["employee"]
    #     expense_data['date'] = entry["date"]
    #     expense_data['expense_type'] = entry["expense_type"]
    #     expense_data["project"] = entry["project"],
    #     expense_data["purpose"] = entry["purpose"],
    #     expense_data["payment_method"] = entry["payment_method"],
    #     expense_data["currency"] = entry["currency"],
    #     expense_data["tax_type"] = entry["tax_type"],
    #     expense_data["net_amount"] = entry["net_amount"],
    #     expense_data["amount"] = entry["amount"],
    #     expense_data["description"] = entry["description"],
    #     expense_data["status"] = entry["status"]
    #     output.append(expense_data)

    return jsonify({'expenses': entries})


@expense.route('/expense', methods=['PUT'])
@token_required
def update_expense_entry(current_user):
    """
    Update expense entry
    """
    pass


@expense.route('/expense/<entry_id>', methods=['DELETE'])
@token_required
def delete_expense_entry(current_user, entry_id):
    """
    Delete expense entry against id
    """
    pass
