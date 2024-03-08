module DFFlipFlopSR(
    input S, R,
    output Q, Qbar
);
    assign Qbar = ~(S | Q);
    assign Q = ~(R | Qbar);
endmodule
