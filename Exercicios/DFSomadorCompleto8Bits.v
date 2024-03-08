module SomadorCompleto8BitsDF(
    input [7:0] x,
    input [7:0] y,
    input Cin,
    output [7:0] A,
    output Cout
);

wire [7:0] sum;
wire [7:0] carry;

assign sum = x + y + Cin;
assign Cout = carry[7];
assign A = sum;

endmodule