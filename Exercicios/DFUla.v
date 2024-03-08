module DataFlowModelUlda (
  input A, B, Ainv, Binv, Cinv,
  input [2:0] op,
  output S,
  output Cout
);

// Fazendo o Mux 2 -> 1 para o A
wire cabo1 = A & ~Ainv;
wire cabo2 = ~A & Ainv;
wire cabo3 = cabo1 | cabo2;

// Fazendo o Mux 2 -> 1 para o B
wire b1 = B & ~Binv;
wire b2 = ~B & Binv;
wire b3 = b1 | b2;

// Portas l�gicas para p1, p2, p3, p4
wire p1 = cabo3 & b3;
wire p2 = cabo3 | b3;
wire p3 = cabo3 ^ b3;
wire p4 = ~(cabo3 | b3);

// Half Adder
wire sum = cabo3 ^ b3;
assign Cout = cabo3 & b3;

// Mux 5 to 1
assign S = (op == 3'b000) ? p1 :
           (op == 3'b001) ? p2 :
           (op == 3'b010) ? p3 :
           (op == 3'b011) ? p4 :
           (op == 3'b100) ? sum : 1'b0;

endmodule
