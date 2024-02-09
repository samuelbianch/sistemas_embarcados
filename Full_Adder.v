
module FullAdder(
  input in0, in1, in2, in3, s0, s1
  output out
);

wire a0, a1, a2, a3, inv0, inv3;

not(inv0, s0);
not(inv1, s1);

and(a0, in0, inv0, inv1);
and(a1, in1, inv0, s1);
and(a2, in2, s0, inv1);
and(a3, in3, s0, s1);

xor(out, a0, a1, a2, a3);

endmodule