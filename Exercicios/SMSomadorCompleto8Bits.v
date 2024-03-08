module SomadorCompleto1Bit(x, y, Cin , Cout, A);
input [7:0]x;
input [7:0]y;
input Cin;
output Cout;
output [7:0]A;
wire [7:0]p;
wire [7:0]r;
wire [7:0]s;
genvar i, j, k;

for(i = 0; i<8; i=i+1) begin
  for(j = 0; j<8; j=j+1) begin
    for(k = 0; k<8; k=k+1) begin
      xor(p[i], x[j], y[k]);
    end
  end
end

for(i = 0; i<8; i=i+1) begin
  for(j = 0; j<8; j=j+1) begin
    xor(A[i], p[i], Cin);
  end
end

for(i = 0; i<8; i=i+1) begin
  for(j = 0; j<8; j=j+1) begin
    and(r[i], p[i], Cin);
  end
end

for(i = 0; i<8; i=i+1) begin
  for(j = 0; j<8; j=j+1) begin
    for(k = 0; k<8; k=k+1) begin
      and(s[i], x[j], y[y]);
    end
  end
end

for(i = 0; i<8; i=i+1) begin
  for(j = 0; j<8; j=j+1) begin
    or(Cout, r[i], s[j]);
  end
end


endmodule
