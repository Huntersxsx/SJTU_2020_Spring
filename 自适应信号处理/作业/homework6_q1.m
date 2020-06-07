clc;clear variables;
length=10000;   % sequence length
var_v=10;   % initial noise variance
sd_v=sqrt(var_v);
u=zeros(length+3,1);    %input u(n)
a1=0.1; % AR coefficient
a2=-0.8;
error_boundary=0.001; % maximum error
iteration_num=300; % iteration number
error=error_boundary+1; % an initial error 
mu=0.02; % step-size
k=1; % number of iteration
while(abs(error)>error_boundary && k<iteration_num)
sd_v=sqrt(var_v);
for n=3:(length+3)
u(n)=-a1*u(n-1)-a2*u(n-2)+randn(1)*sd_v;
end
error=(1-var(u(3:length+3))); 
var_v=var_v+mu*error; % adjust the noise variance 
k=k+1; 
end
if abs(error)>error_boundary 
fprintf('increase the iteration numbers')
sample_variance_u=var(u(3:length+3))
var_v
else
sample_variance_u=var(u(3:length+3))
var_v
k
end