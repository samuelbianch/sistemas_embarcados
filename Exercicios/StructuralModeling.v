module SomadorCompleto1Bit(x, y, Cin , Cout, A);
input x, y, Cin;
output Cout, A;
wire p, r, s;

xor(p, x, y);
xor(A, p, Cin);

and(r, p, Cin);
and(s, x, y);

or(Cout, r, s);

endmodule