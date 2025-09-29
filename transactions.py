from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware

# Establish connection to a Polygon RPC endpoint
POLYGON_RPC_URL = "https://polygon-rpc.com/"
web3 = Web3(Web3.HTTPProvider(POLYGON_RPC_URL))

# Polygon uses a Proof-of-Authority consensus mechanism, so we need to inject this middleware
web3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

# Define the block number and the target contract address we want to inspect
block_number = 51866068
# For this example, we'll look at the exchange for multi-outcome markets
TARGET_ADDRESS = "0xc5d563a36ae78145c45a50134d48A1215220f80a" # NegRisk_CTFExchange address

# Fetch all logs for the target address within the specified block range
logs = web3.eth.get_logs({
    'fromBlock': block_number,
    'toBlock': block_number,
    'address': Web3.to_checksum_address(TARGET_ADDRESS)
})

print(logs)