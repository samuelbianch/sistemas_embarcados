module DataFlowModelUlda_tb;

    // Par�metros
    parameter PERIOD = 10;

    // Sinais de Entrada
    reg A, B, Ainv, Binv, Cinv;
    reg [2:0] op;

    // Sinais de Sa�da
    wire S, Cout;

    // Inst�ncia do M�dulo a ser testado
    DataFlowModelUlda dut (
        .A(A),
        .B(B),
        .Ainv(Ainv),
        .Binv(Binv),
        .Cinv(Cinv),
        .op(op),
        .S(S),
        .Cout(Cout)
    );

    // Est�mulo
    initial begin
        A = 0; B = 0; Ainv = 0; Binv = 0; Cinv = 0; op = 0;

        // Teste 1
        #20 A = 1; B = 0; Ainv = 1; Binv = 1; Cinv = 0; op = 0;
        #20 A = 0; B = 1; Ainv = 1; Binv = 1; Cinv = 0; op = 1;
        #20 A = 1; B = 1; Ainv = 0; Binv = 0; Cinv = 1; op = 2;
        #20 A = 0; B = 0; Ainv = 0; Binv = 0; Cinv = 1; op = 3;
        #20 A = 1; B = 1; Ainv = 1; Binv = 0; Cinv = 1; op = 4;
        #20;
    end

endmodule
