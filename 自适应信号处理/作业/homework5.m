clc
clear
x = [0,1,2,3,4,5,6,7,8,9];
y1 = cos(x) + rand(length(x),1);
y2 = cos(2*x) + rand(length(x),1);
y3 = cos(x) + rand(length(x),1);
pxy = corrcoef(y1,y2);
pxx = corrcoef(y1,y3);
[z,lambdaxy] = eig(pxy);
[z2, lambdaxx] = eig(pxx);
lambdaxy = [lambdaxy(1,1),lambdaxy(2,2)]
lambdaxx = [lambdaxx(1,1),lambdaxx(2,2)]
spreadxy = max(lambdaxy)/min(lambdaxy)
spreadxx = max(lambdaxx)/min(lambdaxx)