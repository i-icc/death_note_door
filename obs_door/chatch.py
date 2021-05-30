import time
import seeed_dht
def main():
    sensor = seeed_dht.DHT("22", 12)
    humi, temp = sensor.read()
    if not humi is None:
        print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))

if __name__ == '__main__':
    main()
