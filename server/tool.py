from dotenv import load_dotenv
import os, json

from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.client import Token

import spl.token.instructions as spl_token

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction


load_dotenv()

OWNER_ADDRESS = PublicKey(os.getenv("OWNER_ADDRESS"))
MINT_ADDRESS = PublicKey(os.getenv("MINT_ADDRESS"))
TOKEN_HOLDER = PublicKey(os.getenv("TOKEN_HOLDER"))
KEYPAIR = json.loads(os.getenv("KEYPAIR"))

MINT_ADDRESS = PublicKey(MINT_ADDRESS)
TOKEN_HOLDER = PublicKey(TOKEN_HOLDER)
keypair = Keypair.from_secret_key(bytes(KEYPAIR))

# rpc cluster endpoint for figment
http_client = Client("https://solana--devnet.datahub.figment.io/apikey/3fcb206da8578cfe75045bed0e1126cf", timeout=10)
http_token = Token(conn=http_client, pubkey=MINT_ADDRESS, program_id=PublicKey(TOKEN_PROGRAM_ID), payer=keypair)

def check_for_associaton(user_wallet_address):
    pass

def transfer_tokens(amount, user_wallet_address):
    resp = http_token.transfer(
        source=TOKEN_HOLDER,
        dest=PublicKey(user_wallet_address),
        owner=keypair,
        amount=int(amount*1e9)
    )
    return resp

# Maybe implement some kind of check to see if the account already has association.
def create_associated(user_wallet_address):
    new_account = http_token.create_associated_token_account(
        owner=user_wallet_address,
    )
    return new_account
