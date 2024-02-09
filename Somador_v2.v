
module Somador_v2(
  input a, b, Cin,
  output s, Cout
);

wire w1, w2, w3;
xor(w1, a, b);
xor(s, w1, Cin);
and(w2, w1, Cin);
and(w3, a, b);
or(Cout, w2, w3);

endmodule