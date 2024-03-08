module SomadorCompleto8Bits(
    input [7:0] x,
    input [7:0] y,
    input Cin,
    output reg [7:0] A,
    output reg Cout
);

reg [7:0] sum;
reg [7:0] carry;

always @(x, y, Cin) begin
  sum = x + y + Cin;
  Cout = carry[7];
  A = sum;
end

endmodule
