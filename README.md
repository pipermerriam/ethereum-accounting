# Ethereum Account Lib

Solididy Library for dealing with ethereum account balances within a contract.

## API

### Banks

The primary unit of storage in accounting is the `Bank` struct which contains a
single mapping from addresses to account balances at `Bank.accountBalances`.

### Deposits and Withdrawls

The following functions are *high* level account management functions that are
suitable for normal deposit and withdrawl operations on an account.

`function deposit(Bank storage self, address accountAddress, uint value) public returns (bool)`

The `deposit` function can be used to add funds to the given account.  It
returns a boolean as to whether the deposit was successful.

`function withdraw(Bank storage self, address accountAddress, uint value) public returns (bool)`

The `withdraw` function can be used to remove funds from an account.  The
corresponding amount in ether is sent to the account address.  Returns a
boolean as to whether the withdrawl was successful.

### Adding and Removing Funds

The following functions are *low* level functions for manipulating account
balances.


`function addFunds(Bank storage self, address accountAddress, uint value) public`

The `addFunds` function adds the given value to an accounts balance.  If the
addition would cause an overflow of the `uint256` account balance, an exception
is thrown.

`function deductFunds(Bank storage self, address accountAddress, uint value) public`

The `deductFunds` function subtracts the given value from an account's balance.
If the subtraction would cause an underflow of the `uint256` account balance,
an exception is thrown.

### Events

The following events are available.  Each event has a corresponding library
function that can be used to log the event.


* `event _Deposit(address indexed _from, address indexed accountAddress, uint value)`
* `event _Withdrawal(address indexed accountAddress, uint value)`
* `event _InsufficientFunds(address indexed accountAddress, uint value, uint balance)`


* `function Deposit(address _from, address accountAddress, uint value) public`
* `function Withdrawal(address accountAddress, uint value) public`
* `function InsufficientFunds(address accountAddress, uint value, uint balance) public`
