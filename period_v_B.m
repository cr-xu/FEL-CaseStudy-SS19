lambda = 0.5e-10;

E = 10e9;
m_e = 511e3;
gamma = E/m_e;

% K = 93.4*B*lambda_u[m];

period = 20:0.02:35.5;
period = period*10^-3; 

B = sqrt(2*((lambda*2*gamma^2)./period-1))./period/93.4;

plot(period*1000,B);
legend('beam energy 10GeV')
xlabel('\lambda_{u} [mm]')
ylabel('B [ T ]')

Bworking = 0.40;
Lambdau = 26e-3;
K = 93.4*Bworking*Lambdau;