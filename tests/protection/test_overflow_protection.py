import pytest

from ethereum.tester import TransactionFailed

from populus.utils import wait_for_transaction


def test_depositing_overflow_protection(deploy_client, deployed_contracts):
    bank = deployed_contracts.TestAccounting
    coinbase = deploy_client.get_coinbase()

    assert bank.getAccountBalance(coinbase) == 0

    initial_balance = 2 ** 256 - 20

    txn_hash = bank.setAccountBalance(initial_balance)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == initial_balance

    txn_hash = bank.addFunds(10)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == initial_balance + 10

    with pytest.raises(TransactionFailed):
        bank.addFunds(10)
