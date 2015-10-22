from populus.utils import wait_for_transaction


def test_withdrawing(deploy_client, deployed_contracts):
    bank = deployed_contracts.TestAccounting
    coinbase = deploy_client.get_coinbase()

    initial_balance = 1000

    txn_hash = bank.setAccountBalance(initial_balance)
    assert bank.getAccountBalance(coinbase) == initial_balance

    txn_hash = bank.withdraw(600)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == 400

    txn_hash = bank.withdraw(400)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == 0
