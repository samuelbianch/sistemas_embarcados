module BehaviorModelUlda (
  input A, B, Ainv, Binv, Cinv,
  input [2:0] op,
  output reg S,
  output reg Cout
);

reg cabo1, cabo2, cabo3;
reg b1, b2, b3;
reg p1, p2, p3, p4;
reg sum;

always @(*) begin
    // Fazendo o Mux 2 -> 1 para o A
    if (Ainv)
        cabo1 = A;
    else
        cabo1 = ~A;
    if (Ainv)
        cabo2 = ~A;
    else
        cabo2 = A;
    cabo3 = cabo1 | cabo2;

    // Fazendo o Mux 2 -> 1 para o B
    if (Binv)
        b1 = B;
    else
        b1 = ~B;
    if (Binv)
        b2 = ~B;
    else
        b2 = B;
    b3 = b1 | b2;

    // Portas lógicas para p1, p2, p3, p4
    p1 = cabo3 & b3;
    p2 = cabo3 | b3;
    p3 = cabo3 ^ b3;
    p4 = ~(cabo3 | b3);

    // Half Adder
    sum = cabo3 ^ b3;
    Cout = cabo3 & b3;

    // Mux 5 to 1
    case (op)
        3'b000: S = p1;
        3'b001: S = p2;
        3'b010: S = p3;
        3'b011: S = p4;
        3'b100: S = sum;
        default: S = 1'b0;
    endcase
end

endmodule