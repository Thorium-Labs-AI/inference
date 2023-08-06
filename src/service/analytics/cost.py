import logging

model_token_pricing = {
    "gpt-3.5-turbo": {
        "request": 0.0015 / 1_000,
        "response": 0.002 / 1_000
    }
}


def handle_token_costs(request_token_count, response_token_count, model):
    pricing_info = model_token_pricing[model]
    if not pricing_info:
        logging.error(f"Cannot fetch pricing for model {model}")
    total_price = pricing_info['request'] * request_token_count + pricing_info['response'] * response_token_count
    logging.info(f"Cost: {request_token_count + response_token_count} tokens (appx. ${total_price})")
