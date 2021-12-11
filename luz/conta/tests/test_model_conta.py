import pytest
from model_bakery import baker

from luz.conta.models import Conta


MOUNTH_NUMBER = 2


@pytest.fixture
def tow_bills(db):
    return baker.make(Conta, MOUNTH_NUMBER)


def test_number_of_months(tow_bills):

    assert Conta.objects.all().count() == MOUNTH_NUMBER


def test_models_attributes(tow_bills):

    tow_bills_from_db = list(Conta.objects.all())

    for bill, bill_from_db in zip(tow_bills, tow_bills_from_db):
        assert bill_from_db.date == bill.date
        assert bill_from_db.amount_paid == bill.amount_paid
        assert bill_from_db.mw == bill.mw
