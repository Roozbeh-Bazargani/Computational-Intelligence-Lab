function [ sig, sig_dot ] = MatrixSig( A, m, n )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
    sig = 0;
    sig_dot = 0;
    for i = 1:m
        for j = 1:n
            sig = sig + sigmoid(A(i,j));
            sig_dot = sig_dot + sigmoid_dot(A(i,j));
        end
    end
end

