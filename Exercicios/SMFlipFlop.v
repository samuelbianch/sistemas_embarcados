module SMFlipFlopSR(
    input S, R,
    reg Q, Qbar
);

    nor n1(Qbar, S, Q);
    nor n2(Q, R, Qbar);

endmodule