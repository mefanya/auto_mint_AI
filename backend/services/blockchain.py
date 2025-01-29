from web3 import Web3
import json
from ..models.token_model import TokenDetails
import os
from dotenv import load_dotenv

load_dotenv()

WEB3_PROVIDER = "https://rpc.sonicchain.com"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")

w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
account = w3.eth.account.from_key(PRIVATE_KEY)

def deploy_token(details: TokenDetails) -> str:
    with open("contracts/TokenABI.json") as f:
        abi = json.load(f)
    with open("contracts/TokenBytecode.txt") as f:
        bytecode = f.read()

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx = contract.constructor(details.name, details.symbol, details.supply).build_transaction({
        "from": ACCOUNT_ADDRESS,
        "gas": 2000000,
        "gasPrice": w3.to_wei("5", "gwei"),
        "nonce": w3.eth.get_transaction_count(ACCOUNT_ADDRESS),
    })

    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.to_hex(tx_hash)
