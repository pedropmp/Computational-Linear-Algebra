clear; clc; close all;
syms t

f = @(t) 125*t;

 
odefun = @(t,y) [y(2); f(t)];

bcfcn = @(ya, yb) [ya(1); yb(1)];

N = 5
xmesh = linspace(0, 1, N);
yGuess = ones(2,N);

solinit.x = xmesh;
solinit.y = yGuess;

sol = bvp4c(odefun, bcfcn, solinit)
plot(sol.x, sol.y(1, :), 'o')
hold on

my_t = 0:.2:1;
my_y = [-5 -10 -14 -16 -15 -10];
plot(my_t, my_y, 'x')
hold off
