#ALUNOS: PEDRO FERNANDO WIEZEL, CAROLYNE SOARES MIRANDA DA LUZ
#DATA: 30 DE ABRIL DE 2024
#TURMA 1

#Código para ESP-32 com sensor DHT-11. Passa informações de temperatura e umidade ambiente para a plataforma de IoT ThingSpeak.

import dht
import machine
import time
import urequests
from wifi_lib import conecta

#informações do Wi-Fi
WIFI_SSID = "" #inserir SSID do Wi-Fi
WIFI_SENHA = "" #inserir senha do Wi-Fi

#definição das chaves API para operar o thingspeak e configuração da URL para write
THINGSPEAK_WRITE_APIKEY = "" #inserir aqui a chave API
THINGSPEAK_URL = "https://api.thingspeak.com/update?api_key=" + THINGSPEAK_WRITE_APIKEY

#declaração do sensor e do relé conectados ao ESP32
sensor = dht.DHT11(machine.Pin(4))
rele = machine.Pin(2, machine.Pin.OUT)

def envio_dados_thingspeak(temperatura, umidade):
    conecta(WIFI_SSID, WIFI_SENHA)
    url_envio = THINGSPEAK_URL + "&field1={}&field2={}".format(temperatura, umidade)
    resposta = urequests.get(url_envio)
    print("Resposta do Thingspeak:" + resposta.text)

def monitoramento_rele(temperatura, umidade):
    if (temperatura > 31 or umidade > 70):
        rele.value(1)
    else:
        rele.value(0)

#verificações da temperatura e da umidade e envio ao Thingspeak
for i in range (10):
    sensor.measure()
    temperatura = sensor.temperature()
    umidade = sensor.humidity()
    print("Temperatura = {}ºC, Umidade = {}%".format(sensor.temperature(), sensor.humidity()))
    envio_dados_thingspeak(temperatura, umidade)
    monitoramento_rele(temperatura, umidade)
    time.sleep(12)

#desliga o relé, reboota o ESP32
rele.value(0)
machine.soft_reset()
