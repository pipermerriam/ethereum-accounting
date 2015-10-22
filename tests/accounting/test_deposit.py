from populus.utils import wait_for_transaction


def test_depositing(deploy_client, deployed_contracts):
    bank = deployed_contracts.TestAccounting
    coinbase = deploy_client.get_coinbase()

    assert bank.getAccountBalance(coinbase) == 0

    txn_hash = bank.deposit(value=1234)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == 1234

    txn_hash = bank.deposit(value=1234)
    wait_for_transaction(deploy_client, txn_hash)

    assert bank.getAccountBalance(coinbase) == 2468
