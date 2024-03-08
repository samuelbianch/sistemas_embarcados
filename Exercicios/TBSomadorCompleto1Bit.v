module SomadorCompleto1Bit_tb;
    reg x, y, Cin;
    wire Cout, A;
    integer i, j, k;
    // Instanciando o m�dulo a ser testado
    SomadorCompleto1Bit sum (
        .x(x),
        .y(y),
        .Cin(Cin),
        .Cout(Cout),
        .A(A)
    );
    
    // Testando todas as combina��es poss�veis de entrada
    initial begin
        for (i = 0; i <= 1; i = i+1) begin
            for (j = 0; j <= 1; j = j+1) begin
                for (k = 0; k <= 1; k = k+1) begin
                    x = i;
                    y = j;
                    Cin = k;
                    #20; // Aguarda alguns ciclos para as sa�das se estabilizarem
                end
            end
        end
    end
endmodule