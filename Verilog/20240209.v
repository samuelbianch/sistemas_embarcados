/*
module circuito(a, b, c, xor1, s);

	input a, b, c;
	output xor1, s;

	xor(xor1, a, b);
	and(s, xor1, c);

endmodule
*/

module circuito(
  input a, b, c,
  output s
);

wire w1;
xor(w1, a, b);
and(s, w1, c);

endmodule