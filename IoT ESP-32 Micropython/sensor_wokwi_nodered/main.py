import time
from wifi_lib import conecta
from umqttsimple import MQTTClient
from defs import *
from machine import I2C, Pin 
from i2c_lcd import I2cLcd 

TEMP_TOPICO = "pucpr/iot/temperatura"
UMIDADE_TOPICO = "pucpr/iot/umidade"
TOPICO_GERAL = "pucpr/#"
mensagens_gerais = 0

red_led = Pin(4, Pin.OUT) 
green_led = Pin(5, Pin.OUT)
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

def imprime_status(status, valor):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(status)
    lcd.move_to(0,1)
    lcd.putstr("Valor: " + str(valor))

def imprime_mensagem(linha1, linha2):
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(str(linha1))
    if linha2:
        lcd.move_to(0,1)
        lcd.putstr(str(linha2))
    time.sleep(1)

def processa_dados(topico, mensagem):
    mensagem = mensagem.decode()
    topico = topico.decode()

    if topico == TEMP_TOPICO:
        if int(valor) < 30:
            red_led.off()
            green_led.on()
            imprime_status("Temperatura OK", valor)
        else:
            red_led.on()
            green_led.off()
            imprime_status("Temperatura ALTA", valor)
    elif topico == UMIDADE_TOPICO:
        if int(valor) < 70:
            red_led.on()
            green_led.off()
            imprime_status("Umidade BAIXA", valor)
        else:
            red_led.off()
            green_led.on()
            imprime_status("Umidade OK", valor)
    else:
        imprime_mensagem("Spam: ", mensagem)

def conecta_wifi():
    imprime_mensagem("Rede Wi-Fi:", "conectando...")
    station = conecta("Wokwi-GUEST", "")
    if not station.isconnected():
       conecta_wifi()
    imprime_mensagem("Rede Wi-Fi:", "conectada!")
    return station

def main():
    conecta_wifi()
    client = MQTTClient(mqtt_client_id, mqtt_server, mqtt_port)

    imprime_mensagem("HiveMQ Broker:", "conectando...")
    client.connect()
    client.set_callback(processa_dados)
    imprime_mensagem("HiveMQ Broker:", "conectado!")

    client.subscribe(TEMP_TOPICO)
    client.subscribe(UMIDADE_TOPICO)
    client.subscribe(TOPICO_GERAL)
    imprime_mensagem("Esperando por", "dados do broker")

    while True:
        client.check_msg()
        time.sleep(0.1)

if __name__ == "__main__":
    main()