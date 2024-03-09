module ContadorAssincrono(
    input clk, // Sinal de clock
    input reset, // Botão de reset
    output reg [3:0] count // Saída do contador de 4 bits
);

    // Flip-flops D para cada bit do contador
    reg [3:0] next_count; 

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            // Reiniciar a contagem se o botão de reset estiver pressionado
            next_count <= 4'b0101; // Iniciar a contagem em 5 (0101)
        end 
	if ( c == 4'b1111) begin
		c <= 4'b0101;
	end else begin
            // Incrementar o contador
            next_count <= count + 4'b0001;
        end
    end

	assign count = next_count;

    // Atribuir o próximo estado ao estado atual do contador
    always @(posedge clk) begin
        if (!reset) begin
            count <= next_count;
        end
    end

endmodule
