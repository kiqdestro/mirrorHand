<!-- # [Mirror Hand](SoftwareInt.md) -->

# Software e integração dos dispotivivos

O software do projeto é divido em duas partes: software de recebimento e envio via serial dos dados recebidos pelos sensores da luva realizado no Arduino Mega 2560 em linguagem C e o software de controle da mão robótica que roda no Raspberry Pi Zero W responsável por receber os dados via serial e realizar os comandos de controle dos servomotores, programado em linguagem Python

O fluxograma do código presente no Arduino Mega 2560 está apresentado na figura \ref{diagramasoftwarearduino}. Os dados dos sensores são lidos pelas 9 portas analógicas e os valores correspondentes às rotações x, y e z via I2C. Uma string é então montada e enviada para as portas Serial (USB) e Serial1(Bluetooth). Os dados enviados via USB podem ser recebidos por um computador para debug ou para visualização em software 3D.

![diagrama software arduino](/diagramas/diagramasoftwarearduino.jpg)

Já o código presente no Raspberry Pi Zero W recebe os bytes enviados via Bluetooth e os trata para obter os valores para cada sensor, os valores são então normalizados em um intervalos de 0 a 180 para comandos enviados aos servomotores ou 0 a 90 para comandos enviados ao Software 3D. O fluxograma do software pode ser visto na figura \ref{diagramasoftwarepi}.

![diagrama software pi](/diagramas/diagramasoftwarepi.jpg)

O software 3D utilizado para visualização dos movimentos virtualmente é o Autodesk Maya. O método utilizado para transmissão de dados é via TCP/IP. Isso permite que um dispositivo conectado a mesma rede LAN do computador onde está rodando o Maya possa conectar ao mesmo facilmente e enviar comandos. No software desenvolvido para esse projeto foi utilizado o módulo Python socket, onde basta a abertura de uma conexão no respectivo endereço IP para envio de comandos. Dessa forma é possível a visualização dos movimentos capturados pela luva em tempo real em uma mão virtual, com a adição de movimentos não replicados pela mão robótica. Caso não esteja sendo o utilizado o software 3D ou a conexão não seja realizada por algum motivo, o software de controle continua sem a opção de visualização. A figura \ref{maya1} apresenta a visualização da mão virtual em software 3D.

![visualização maya](/componentes/maya1.JPG)
