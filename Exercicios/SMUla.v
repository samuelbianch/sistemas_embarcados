module StructureModelUlda (
  input A, B, Ainv, Binv, Cinv,
  output reg [2:0] op,
  output Cout,
  reg S
);

wire cabo1, cabo2, cabo3;

// Fazendo o Mux 2 -> 1 para o A
and(cabo1, A, ~Ainv);
and(cabo2, ~A, Ainv);
or(cabo3, cabo1, cabo2);

wire b1, b2, b3;
// Fazendo o Mux 2 -> 1 para o A
and(b1, B, ~Binv);
and(b2, ~B, Binv);
or(b3, b1, b2);

wire p1, p2, p3, p4;
and(p1, cabo3, b3);
or(p2, cabo3, b3);
xor(p3, cabo3, b3);
nor(p4, cabo3, b3);

wire sum;
// Half Adder
xor(sum, cabo3, b3);
and(Cout, cabo3, b3);

// Mux 5 to 1
always @(op) begin
if (op[0] == 0 & op[1] == 0 & op[2] == 0) S = p1;
if (op[0] == 0 & op[1] == 0 & op[2] == 1) S = p2;
if (op[0] == 0 & op[1] == 1 & op[2] == 0) S = p3;
if (op[0] == 0 & op[1] == 1 & op[2] == 1) S = p4;
if (op[0] == 1 & op[1] == 0 & op[2] == 0) S = sum;
end

endmodule
