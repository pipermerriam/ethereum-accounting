import pytest

from ethereum.tester import TransactionFailed

from populus.utils import wait_for_transaction


def test_underflow_protection(deploy_client, deployed_contracts):
    bank = deployed_contracts.TestAccounting
    coinbase = deploy_client.get_coinbase()

    initial_balance = 1000

    txn_hash = bank.setAccountBalance(initial_balance)
    assert bank.getAccountBalance(coinbase) == initial_balance

    txn_hash = bank.deductFunds(600)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == 400

    with pytest.raises(TransactionFailed):
        bank.deductFunds(401)
