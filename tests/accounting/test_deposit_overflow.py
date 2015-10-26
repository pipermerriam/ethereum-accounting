def test_depositing_with_max_account_balance(deploy_client, deployed_contracts):
    bank = deployed_contracts.TestAccounting
    coinbase = deploy_client.get_coinbase()

    assert bank.getAccountBalance(coinbase) == 0

    initial_balance = 2 ** 256 - 20

    txn_hash = bank.setAccountBalance(initial_balance)
    deploy_client.wait_for_transaction(txn_hash)

    assert bank.getAccountBalance(coinbase) == initial_balance

    txn_hash = bank.deposit(value=10)
    deploy_client.wait_for_transaction(txn_hash)

    assert bank.getAccountBalance(coinbase) == initial_balance + 10

    txn_hash = bank.deposit(value=10)
    deploy_client.wait_for_transaction(txn_hash)

    assert bank.getAccountBalance(coinbase) == initial_balance + 10
