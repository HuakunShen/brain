## Reentrance Vulnerability: Fallback function
2 variations:
- `fallback() external payable{}`
- `receive() external payable{}`

## Reentrance Vulnerability: Call function
Senders use call function to send ether to receiver. 
If gas limit not set, the call method execute is valnerable to reentrance attacks.

## Reentrance Valnerability: The Dao Attack
### Benefits of DAO
- Trustless: rules and processors of a DAO are encoded as smart contracts
- Cannot be shutdown
- Open Source
### Downsides of DAO
- No business secrets (due to open source)

### Overview of the Attack

## Prevention
- Gas limit on fallback function
- Check the balance
- Call external functions last, after any changes to state variables in contract, so they are not changed again later. 



