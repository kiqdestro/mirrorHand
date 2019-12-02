<!-- # [Mirror Hand](componentes.md) --> 
 
# Componentes utilizados no projeto

## Raspberry Pi Zero W

O Raspberry Pi Zero W é uma versão reduzida e de baixo custo da popular série de SoBs(System on a Board) Raspberry Pi. O sistema conta com um SoC(System On a Chip) com uma CPU single-core de frequência de 1GHz, 512 MB de RAM e recursos úteis para o projeto como USB OTG(On-The-Go), Bluetooth e Wifi integrados, portas GPIO(General Purpose In and Out) e comunicações serial I2C e UART possível via Bluetooth ou GPIO. A placa é alimentada por uma fonte Micro USB de 5V.

![pizerow](/componentes/pizerow.jpg)
<br>
<small>Figura 1 - Raspberry Pi Zero W.</small>

## PCA9685

Para controle dos atuadores é utilizada a placa PCA9685 em conjunto com o Raspberry Pi Zero W. Um controlador que permite enviar sinais PWM(Pulse Width Modulation) com um {\itshape duty cycle} ajustável de 0\% a 100\% para controle dos atuadores. Opera com uma tensão de 2.3V a 5.5V. A placa é controlada via protocolo serial I2C.


## Arduino Mega 2560

O Arduino Mega 2560 (figura 2) é uma placa microcontroladora baseada no chip ATmega2560. Em contraste com outras placas Arduino, ela é designada para projetos que requerem mais portas de entrada e saída ou memória. Possui 54 pinos de entrada e saída digitais, 16 entradas analógicas e 3 portas seriais UART, saídas PWM e comunicação serial via USB. A placa pode ser alimentada por uma fonte normal ou USB de 5V ou através dos pinos de 5V e GND presentes na placa.

Em conjunto com a placa Arduino Mega 2560 foi utilizado um adaptador Bluetooth HC-06 alimentado por tensão 5V. Utiliza protocolo serial UART para comunicação.

![pizerow](/componentes/mega.jpg)
<br>
<small>Figura 2 - Arduino Mega 2560.</small>

## Sensores

### Sensor óptico de flexão

Consiste em um tubo preto com um emissor de luz em uma extremidade e um sensor de luz em outra, ao ocorrer a dobra do tubo, menos luz do emissor alcança o sensor, o que causa um sinal que pode ser interpretado pelo microcontrolador. Um diagrama simplficado do sensor pode ser visto da figura. 3.

![pizerow](/componentes/ofs.jpg)
<br>
<small>Figura 3 - Sensor óptico de flexão.</small>

### Sensor Inercial (MPU6050)

O sensor inercial IMU (Inertial Measurement Unit) foi utilizado para medidas de rotação. É um sensor que combina um giroscópio de 3 eixos e um acelerômetro de 3 eixos e um processador digital de movimentos em um só pacote. Possui um conversor analógico digital integrado para conversão das leituras em e um buffer FIFO para menor consumo de energia. Utiliza comunicação I2C e alimentação entre 2.38V e 3.47V.

![pizerow](/componentes/mpu6050.jpg)
<br>
<small>Figura 4 - Placa do sensor inercial MPU 6050.</small>

## Atuadores

### Servomotores

Servomotor é um tipo de motor muito utilizado em automação para aplicações que exigem alta precisão no controle, torques altos, pouco ruído e boa manutenção. O servomotor em questão funciona de maneira que a posição do eixo é definida de acordo com o sinal PWM recebido pelo servo, para cada valor de {\itshape duty cycle} o motor assume uma única posição. Os servomotores utilizados são do modelo SG90. Um modelo compacto e leve com alto torque e rotação de aproximadamente 180 graus (90 graus para cada direção). Possui um torque de 1.8 kgf.cm, velocidade de 0.1s/60 graus e opera a uma tensão de aproximadamente 5V. O motor é controlado através de sinais PWM

## Sistemas de comunicação e controle

### Pulse Width Modulation

Sinais PWM consistem em sinais digitais com exemplos de aplicações sendo controle de motores e LEDs RGB. Uma onda retangular é cortada em vários pulsos digitais permitindo a variação(ou modulação) do valor médio de energia gerado pelo sinal. O {\itshape duty cycle} é o que determina o período de tempo em que o sinal está ligado e é expressado em porcentagem, com 100\% sendo sempre ligado. Exemplos de {\itshape duty cycles} e suas respectivas formas de onda resultantes podem ser vistos na figura 5

![pizerow](/componentes/pwmwave.JPG)
<br>
<small>Figura 5 - Onda PWM e diferentes duty sycles.</small>

### Comunicação Serial

Comunicação serial é o processo de mandar dados um bit por vez de forma sequencial e padronizada, diferente da comunicação paralela, onde a comunicação é feita com vários canais em paralelo enviando sinais simuntaneamente, uma comunicação serial precisa de apenas um canal de comunicação. No entanto, para que não haja conflito, normalmente para comunicação em duas vias são usados dois, um para receber dados e um para transmitir dados. Neste projeto, foram usadas comunicações seriais entre o Raspberry e o computador, entre o Arduino e o computador, entre o arduino e o dispositivo bluetooth (HC-06), entre o raspberry e o driver dos motores e entre o raspberry e o sensor inercial (MPU6050).

![pizerow](/componentes/Parallel_and_Serial_Transmission.png)
<br>
<small>Figura 6 - Transmissão paralela e serial.</small>

#### UART

UART é o dispositivo que faz a conversão entre comunicação serial e comunicação paralela, e está presente no HC-06 deste projeto. O protocolo bluetooth utiliza diversas diferentes frequências e sinais para fazer a comunicação, desta forma, precisa fazer a separação das diferentes informações através do dispositivo UART. A comunicação é feita através das portas TX e RX.

![pizerow](/componentes/UART.jpg)
<br>
<small>Figura 7 - Protocolo UART.</small>

#### I2C

I2C é um protocolo para interfaces de dois fios utilizado para conectar dispositivos de baixa velocidade. Utiliza as portas SDA(serial data) e SCL(serial clock) e transferêncis de 8 bits. Utiliza hierarquia mestre e escravo onde cada dispositivo possui um endereço de 7 bits. A comunicação é iniciada pelo dispositivo mestre com uma condição de início o que define se o mestre ou escravo irá escrever ou ler no barramento.