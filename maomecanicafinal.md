<!-- # [Mirror Hand](maomecanicafinal.md) -->

# A Mão Robótica

## Projeto mecânico da mão robótica

A mão robótica foi obtida de um projeto de fonte aberta encontrado na internet (Dextrus Hand), e foi construída com utilização de uma impressora 3D. Como material foi utilizado plático ABS. Nas juntas de cada articulação foram utilizados rolamentos miniatura e as peças foram fixadas com parafusos.

![mao robotica parcial](/maorobotica/maoparcial1.jpg)
<br>
<small>Figura 1 - Mão robótica parcialmente construída.</small>


Para movimentos dos dedos foram fixadas linhas nas extremidades de cada face do dedo e presas a seus respectivos servo motores. A mão robótica é capaz apenas de dobrar todas as articulações de cada dedo de forma dependente.

![dedo com linhas](/maorobotica/maoparcial3.jpg)
<br>
<small>Figura 2 - Dedo da mão robótica construído com as linhas.</small>

A mão robótica, os componentes e os servomotores foram então fixados em uma placa de madeira. O resultado final pode ser observado na figura 3.

![mao robotica pronta](/maorobotica/maoroboticafinal.jpg)
<br>
<small>Figura 3 - Mão robótica terminada</small>

## Projeto de hardware da mão robótica

O controlador principal da mão robótica é o Raspberry Pi Zero W, que é responsável por rodar todo o software de controle e receber as informações externas para controle da mão robótica. Seu modo de comunicação é serial via bluetooth e pode ser acessado por um computador por linha de comando via wifi.

Para controle do servomotores é utilizado a placa de controle PWM PCA9685. Os sinais recebidos via serial pelo Raspberry Pi Zero W são tratados e enviados para a placa, que é responsável por fazer o movimento dos servomotores. O Raspberry Pi Zero W é alimentado por uma fonte micro USB de 5V e a placa PWM PCA9685 é alimentada por uma fonte padrão de 5V. Foi decido não usar a mesma fonte para as duas placas para evitar comportamentos inesperados pelo Raspberry Pi Zero W devido a flutuações dos níveis de tensão causados pelo movimento dos servomotores. A figura 4 apresenta o diagrama de blocos do hardware da mão robótica.

Durante a construção da mão robótica foi necessário a simplicação do plano definido originalmente para as articulações

![diagrama mao robotica](/diagramas/diagramamaorobotica.jpg)
<br>
<small>Figura 4 - Diagrama de blocos do hardware da mão robótica</small>
