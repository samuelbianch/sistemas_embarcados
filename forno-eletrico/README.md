# Forno Elétrico simplificado

1. Este projeto deverá utilizar leds para mostrar os sinais de saída do controlador e botões de pressão (Push buttons) ou liga/desliga para enviar comandos ao controlador;

2. Será utilizado um sensor de temperatura do tipo DTH11 para informar ao controlador a temperatura interna do forno;

3. Um botão será utilizado para ligar/desligar o forno;

4. Haverá 3 opções de temperatura para o forno: 180°, 220° e 250°, as quais deverão ser escolhidas por um botão do tipo push button. Além dessas três opções de temperatura, há uma opção que indica forno desabilitado, e esta deve ser a opção inicial quando o forno é ligado. Uma vez escolhido um valor de temperatura, o forno começa a aquecer imediatamente. Para desligar o aquecimento pode-se selecionar a opção desabilitado ou acionar o botão de
liga/desliga;

5. O aquecimento do forno ocorre por meio de uma resistência elétrica que
deve ser ligada e desligada pelo controlador, a fim de manter a temperatura
desejada.

6. A resistência deverá ser ligada/desligada da seguinte forma:



| Atuação 	| Temperatura escolhida 	                |
|           |-----------------------	|-----	|-----	|
|-----------| 180                   	| 220 	| 250 	|
| Liga    	| 179                   	| 219 	| 249 	|
| Desliga 	| 181                   	| 221 	| 251 	|
|         	|                       	|     	|     	|


essas temperaturas poderão ser alteradas para temperaturas em uma faixa mais baixa para que os testes em laboratório sejam possíveis;

7. Para qualquer uma das temperaturas selecionadas no item f, haverá a possibilidade de se estabelecer um tempo de funcionamento. Para isso, haverá um botão do tipo push button para a seleção do tempo desejado que pode ser de: 30, 60, 90 e 120 minutos. Uma vez transcorrido esse tempo, o forno será desligado;

8. Independentemente de estar ligado ou desligado, por segurança, o sistema de controle do forno deverá sinalizar num led piscante que o forno estiver com temperatura interna acima de 40°;

9. Deverá haver também uma opção de resfriamento rápido, em que um sistema de exaustão aspira o ar quente do forno. Para acioná-la deverá haver um botão do tipo liga/desliga, mas o motor do exaustor somente será ligado quando o forno for desligado e a temperatura estiver acima de 180°;

10. Faz parte do desenvolvimento do projeto, a correta interpretação do que está sendo solicitado, o levantamento de todas as entradas e saídas necessárias, bem como um desenho ilustrativo do forno com o circuito elétrico correspondente.