module FlipFlopSR_tb_structural;
    reg S, R;
    wire Q, Qbar;
    integer i, j;
    DFFlipFlopSR UUT (
        .S(S),
        .R(R),
        .Q(Q),
        .Qbar(Qbar)
    );
    // Testando o flip-flop SR
    initial begin
        for(i = 0; i<=1; i=i+1) begin
	   for(j = 0; j<=1; j=j+1) begin
        	S=i;
		R=j;       
		#30;
       	   end
        end
    end
endmodule