clc;
close all
clear variables;
length=100; % sequence length
iteration_num=100; % iteration number
a1=0.1; % AR coefficient
a2=-0.8; 
var_v=0.27;% noise variance
sd_v=sqrt(var_v);
mu=0.05;
u=zeros(length+3,1); 
f=zeros(length+3,1); 
epsilon1=zeros(length+3,1);
epsilon2=zeros(length+3,1);
g=zeros(length+3,1);
J=zeros(length+3,1);
weights=zeros(2,length+3); 
gsum = zeros(length+3,1);
for k=1:iteration_num % number of iteration
W=zeros(2,length+3); 
for n=3:length+3
    
u(n)=a1*u(n-1)+a2*u(n-2)+randn(1)*sd_v;

f(n)=u(n)-W(1,n-1)*u(n-1)-W(2,n-1)*u(n-2);

epsilon1(n)=a1-W(1,n-1);

epsilon2(n)=a2-W(2,n-1);

W(:,n)=W(:,n-1)+mu*f(n)*[u(n-1);u(n-2)];

end
g=g+f.^2; % accumulate squared error of estimation

end
g=g/iteration_num; % accumulate squared error of estimation
for n=3:length+3
    
 % theoretical cost function  
J(n)=(1-var_v*(1+mu/2))*(1-mu)^(2*n)+var_v*(1+mu/2);

end
index=1:length+3; 

subplot(2,2,1) 
plot(index,(abs((fft(f)))).^2)
xlim([0 length+3])
title('Power Spectral of f')
xlabel('Frequency') 
ylabel('Power Level') 

subplot(2,2,2) 
plot(index,(abs((fft(epsilon1)))).^2)
xlim([0 length+3])
title('Power Spectral of \epsilon_1')
xlabel('Frequency') 
ylabel('Power Level') 

subplot(2,2,3) 
plot(index,(abs((fft(epsilon2)))).^2)
xlim([0 length+3])
title('Power Spectral of \epsilon_2')
xlabel('Frequency') 
ylabel('Power Level') 

figure
plot(index,g(1:length+3),index,J)
xlim([0 length+3])
ylim([0 1])
legend('Experimental Results','Theoretical Results')
xlabel('Sequence length') 
ylabel('Squared Error')
title({'Comparison Plot of Theoretical Learning Curve';...
'to Observed MonteCarlo Results'})