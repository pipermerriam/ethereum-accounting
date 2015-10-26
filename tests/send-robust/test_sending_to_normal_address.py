def test_sending_to_normal_address(deploy_client, deployed_contracts):
    bank = deployed_contracts.TestAccounting
    other = deployed_contracts.Other
    coinbase = deploy_client.get_coinbase()

    assert bank.getAccountBalance(coinbase) == 0

    txn_hash = bank.deposit(value=12345)
    deploy_client.wait_for_transaction(txn_hash)

    assert bank.getAccountBalance(coinbase) == 12345
    assert bank.get_balance() == 12345
    assert other.get_balance() == 0

    txn_hash = bank.sendRobust(other._meta.address, 12345)
    deploy_client.wait_for_transaction(txn_hash)

    assert bank.get_balance() == 0
    assert other.get_balance() == 12345
