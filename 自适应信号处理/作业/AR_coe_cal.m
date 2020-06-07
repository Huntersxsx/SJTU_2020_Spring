function [a1,a2]=AR_coe_cal(iteration_num)
length=10000;   % sequence length
var_v=0.27;   % initial noise variance
sd_v=sqrt(var_v);
u=zeros(length+3,1);    %input u(n)
mu=0.05; % step-size
k=1; % number of iteration
h0=0;
h1=0;
h=zeros(2,iteration_num);
for n=3:(length+3)
    if(k<iteration_num)
        v=randn(1)*sd_v;
        u(n)=-h0*u(n-1)-h1*u(n-2)+v;
        d=-0.1*u(n-1)+0.8*u(n-2)+v;
        e=d+h0*u(n-1)+h1*u(n-2)-v;
        h(1,k)=h0;
        h(2,k)=h1;
        h0=h0-mu*e*u(n-1);
        h1=h1-mu*e*u(n-2);
        k=k+1;
    end
end
a1=sum(h(1,:))/(iteration_num-1);
a2=sum(h(2,:))/(iteration_num-1);
