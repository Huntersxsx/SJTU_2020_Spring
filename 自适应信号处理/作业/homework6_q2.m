clc;
clear variables;
iteration_num=3000;
n=1:iteration_num;
a1=zeros(1,iteration_num);
a2=zeros(1,iteration_num);
for i=1:iteration_num
    [a1(i),a2(i)]=AR_coe_cal(i);
end
plot(n,a1,'b',n,a2,'r')
set(gca,'ygrid','on')
legend('a1','a2')
hold on

coe1=0.1*ones(1,iteration_num);
coe2=-0.8*ones(1,iteration_num);
plot(n,coe2,'-.','color',[0.5 0 1]);
hold on
plot(n,coe1,'-.','color',[1 0.5 0]);
axis([0 3000 -0.9 0.2])
xlabel('n/times')
ylabel('a1 & a2')
