module SomadorCompleto1Bit_tb;
    reg x, y, Cin;
    wire Cout, A;
    integer i, j, k;
    // Instanciando o módulo a ser testado
    SomadorCompleto1Bit sum (
        .x(x),
        .y(y),
        .Cin(Cin),
        .Cout(Cout),
        .A(A)
    );
    
    // Testando todas as combinações possíveis de entrada
    initial begin
        for (i = 0; i <= 1; i = i+1) begin
            for (j = 0; j <= 1; j = j+1) begin
                for (k = 0; k <= 1; k = k+1) begin
                    x = i;
                    y = j;
                    Cin = k;
                    #20; // Aguarda alguns ciclos para as saídas se estabilizarem
                end
            end
        end
    end
endmodule