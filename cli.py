from predictor import predict_color_number
from database import log_trade, get_stats

def cli_loop():
    while True:
        inp = input("🔄 Press [Enter] to get prediction or type 'exit': ")
        if inp.lower() == 'exit':
            break
        result = predict_color_number()
        print(f"🎯 Predicted Color: {result['color']}")
        print(f"🎯 Predicted Number: {result['number']}")
        print(f"📈 Confidence: {result['confidence']*100:.1f}%")
        log_trade(result['color'], result['number'])

    print("\n📊 Final Stats:")
    print(get_stats())

if __name__ == "__main__":
    cli_loop()\n