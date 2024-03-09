module ContadorAssincrono_tb;
    // Sinais
    reg clk;       // Sinal de clock
    reg reset;     // Botão de reset
    wire [3:0] count; // Saída do contador de 4 bits

    // Instância do módulo a ser testado
    ContadorAssincrono dut (
        .clk(clk),
        .reset(reset),
        .count(count)
    );

    // Teste
    initial begin
	clk = 0;
	forever #5 clk = ~clk;
    end
    initial begin
	reset = 0;
	forever #40 reset = ~reset;
    end

endmodule
