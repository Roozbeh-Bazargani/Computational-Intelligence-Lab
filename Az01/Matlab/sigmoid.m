function [ result ] = sigmoid( x )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    result = 2 / (1 + exp(-x)) - 1;

end

