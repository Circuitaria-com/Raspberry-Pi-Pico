# Exibir texto em display OLED ssd1306 controlado por I2C 
from machine import Pin, I2C                            # importa a biblioteca para a I2C
from ssd1306 import SSD1306_I2C                         # importa a biblioteca para o display OLED1306
import utime                                            # importa a função de tempo

WIDTH  = 128                                            # largura da tela oled
HEIGHT = 32                                             # altura da tela oled

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)       # Init I2C usando pinos GP0 e GP1 (pinos I2C0 padrão)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Exibir endereço do dispositivo
print("I2C Configuration: "+str(i2c))                   # Exibir configuração I2C


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Inicializa o display OLED

while True:                                             # Laço de repetição
    # Limpe o display oled caso ele tenha algo nele.
    oled.fill(0)  

    # Adicione algum texto
    oled.text("CIRCUITARIA",5,8)
    oled.text("JA SOMOS 16K",5,18)

    # Por fim, atualize o display oled para que o texto sejam exibido.
    oled.show()
    utime.sleep(1)
    
    
