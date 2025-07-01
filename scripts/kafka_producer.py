import MetaTrader5 as mt5
from confluent_kafka import Producer
import time
import json

KAFKA_BROKER = 'localhost:9092'
TOPIC = 'market_ticks'
SYMBOL = 'EURUSD'

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def main():
    if not mt5.initialize():
        print("MT5 initialize() failed, error =", mt5.last_error())
        return
    
    producer = Producer({'bootstrap.servers': KAFKA_BROKER})
    
    print(f"Producing ticks for {SYMBOL} to Kafka topic '{TOPIC}'...")
    try:
        while True:
            tick = mt5.symbol_info_tick(SYMBOL)
            if tick is not None:
                data = {
                    "time": tick.time,
                    "bid": tick.bid,
                    "ask": tick.ask,
                    "last": tick.last,
                    "volume": tick.volume,
                    "symbol": SYMBOL
                }
                producer.produce(TOPIC, json.dumps(data), callback=delivery_report)
                producer.poll(0)
            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        mt5.shutdown()
        producer.flush()

if __name__ == "__main__":
    main()
