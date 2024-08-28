// Mux 4 to 1

module Mux4to1(
  input in0, in1, in2, in3, s0, s1,
  output reg out
);

always @(s0 or s1) begin
  if(s0 == 0 & s1 == 0) out = in0;
  else if(s0 == 0 & s1 == 1) out = in2;
  else if(s0 == 1 & s1 == 0) out = in1;
  else out = in3;
end
endmodule
