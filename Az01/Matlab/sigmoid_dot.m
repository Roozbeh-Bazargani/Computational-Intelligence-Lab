function [ result ] = sigmoid_dot( x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    result = (1 - sigmoid(x)^2) / 2;

end

