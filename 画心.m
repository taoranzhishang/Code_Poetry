syms x y;
f = sym('(x ^ 2 + y ^ 2 - 1) ^ 3 = x ^ 2 * y ^ 3');
h = ezplot(f, [-1.5, 1.5, -1.5, 1.5]);