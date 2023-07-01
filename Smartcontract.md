---
layout: default
title: Smartcontract for ICO
nav_exclude: false
nav_order: 7
child_nav_order: reversed
---

### Smart Contract ICO

This smart contract is designed to function as an Initial Coin Offering (ICO) contract on the CosmWasm platform, which is a framework for writing smart contracts on the Cosmos blockchain.

ICO is a type of token offering where new cryptocurrencies are pre-sold to investors in exchange for legally recognized currencies or other cryptocurrencies.

#### Here are the key features of the contract:

##### InstantiateMsg: This message is used to initialize the ICO with parameters such as the ICO start and end dates, soft cap, minimum investment, maximum investment, and token rate.

##### State: This represents the global state of the contract, which includes information such as the amount raised, list of investors, number of investors at different bonus levels, set of authorized addresses, and ICO parameters.

##### Investor: This structure stores information about an investor, including their address, investment amount, and whether they have been refunded or not.

##### ExecuteMsg: These are the messages that the contract can handle after initialization. It includes operations such as investment, token distribution, and investor refunds.

##### invest: This function allows an investor to participate in the ICO by investing a certain amount. It updates the contract state and calculates the number of tokens the investor will receive.

##### distribute_tokens: This function is used to distribute tokens to investors after the ICO ends, provided that the soft cap has been reached.

##### refund_investors: If the ICO fails to reach the soft cap, this function is used to refund investors.

##### calculate_token_amount: This function calculates the number of tokens each investor will receive based on their investment amount and eligibility for bonus tokens.

In summary, this smart contract represents an ICO that can accept investments, calculate the number of tokens to allocate to each investor, distribute tokens after the ICO ends, and refund investors if the soft cap is not reached.
