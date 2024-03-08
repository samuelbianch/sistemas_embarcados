
module SomadorCompleto1Bit(x, y, Cin , Cout, A);
input x, y, Cin;
output Cout, A;
assign A = (x ^ y) ^ Cin;
assign Cout = ((x ^ y) & Cin) | (x & y);
endmodule