
module SomadorCompleto8Bits_tb;
    reg [7:0] x;
    reg [7:0] y;
    reg Cin;
    wire [7:0] S;
    wire Cout;
    
    // Instanciando o m�dulo a ser testado
    SomadorCompleto8BitsDF UUT (
        .x(x),
        .y(y),
        .Cin(Cin),
        .A(S),
        .Cout(Cout)
    );
    initial begin
        // Inicializa��o das entradas
        x = 8'b00000000;
        y = 8'b00000000;
        Cin = 0;
        
        // Espera alguns ciclos antes de come�ar
        #80;
        
        // A soma de 255 + 1 + 1, que deve resultar em 1 com Cout 1
        x = 8'b11111111;
        y = 8'b00000001;
        Cin = 1;

        #80;

	// A soma de 8 + 1 + 1, que deve resultar em 10 com Cout 10
        x = 8'b00001000;
        y = 8'b00000001;
        Cin = 1;
        
    end
    
endmodule