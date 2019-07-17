% ------define lattice------
period_length = 26e-3;
l_und = 2.86;
n_period = l_und/period_length;
beamenergy = 10e9;
B = 0.4;
magneticgap = 0.006;

UND = atundulator(l_und,n_period,'B0andEnergy',[B beamenergy],'magnetmodel','rectangularbend','PoleGap',magneticgap);
%UND = atdrift('Dr',1.6,'DriftPass');

QF = atquadrupole( 'QF', 0.2/2, 1.2,'QuadLinearFPass');
QD = atquadrupole( 'QD', 0.2, -1.3,'QuadLinearFPass');

D1 = atdrift('Dr',0.2,'DriftPass');

FODOcell = [{QF;D1};UND;{D1;QD;D1};UND;{D1;QF}];

FODO = repmat(FODOcell,5,1);

RP = atringparam('fel',6e9);
FEL = [{RP};FODO];

% generate tracking initial conditions

%transversal spread
epsilon_in = 0.9e-6;
E_in = 140e6;
E_out = 10e9;
epsilon = epsilon_in*E_in/E_out;
beta_x = 14;
beta_y = 5.8;
n_particle = 3000;

p_exp = makedist('Exponential','mu',(2*epsilon));
ex = random(p_exp,n_particle,1);

phi0 = 2*pi*rand(n_particle,1);

x = sqrt(ex*beta_x).*cos(phi0);
px = sqrt(ex/beta_x).*sin(phi0);

y = sqrt(ex*beta_y).*cos(phi0);
py = sqrt(ex/beta_y).*sin(phi0);


sz = [n_particle,length(FEL)+1];

rin = zeros(6,n_particle);
rin(1,:) = x';
rin(2,:) = px';
rin(3,:) = y';
rin(4,:) = py';
%rin(5,:) = delta';

R_tracking = linepass(FEL,rin,1:length(FEL)+1);
X_tracking = reshape(R_tracking(1,:),sz);
Y_tracking = reshape(R_tracking(3,:),sz);
Pos = findspos(FEL,1:length(FEL)+1);

sigma_x = std(X_tracking);
sigma_y = std(Y_tracking);

Beta_x = sigma_x.*sigma_x/epsilon;
Beta_y = sigma_y.*sigma_y/epsilon;
plot(Pos,Beta_x,'red',Pos,Beta_y);

