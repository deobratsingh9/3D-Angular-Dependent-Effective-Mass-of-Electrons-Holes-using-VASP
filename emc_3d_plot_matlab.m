clc
clear

% ==========================================================
% ====== INPUT FILE ========================================
% ==========================================================
file = "EMC_B0004.dat";

% FIX: automatically ignores headers like "#Grid-size ..."
data = readmatrix(file);

% remove any empty / NaN rows (safety)
data = data(~any(isnan(data),2),:);

phi   = data(:,1) * pi/180;
theta = data(:,2) * pi/180;
R     = data(:,3);

% ==========================================================
% ====== GRID ==============================================
% ==========================================================
nphi = 500;
ntheta = 500;

phinew = linspace(0, pi, nphi);
thetanew = linspace(0, 2*pi, ntheta);

[yy, xx] = meshgrid(thetanew, phinew);

% interpolation (more stable than cubic in MATLAB for sparse grids)
Rnew = griddata(phi, theta, R, xx, yy, 'natural');

Rnew(isnan(Rnew)) = nanmean(Rnew(:));

% ==========================================================
% ====== SPHERICAL → CARTESIAN =============================
% ==========================================================
x = Rnew .* cos(yy) .* sin(xx);
y = Rnew .* sin(yy) .* sin(xx);
z = Rnew .* cos(xx);

% ==========================================================
% ====== PLOT ==============================================
% ==========================================================
figure
colormap jet

surf(x, y, z, abs(Rnew), ...
    'FaceColor','interp', ...
    'EdgeColor','none', ...
    'FaceLighting','gouraud')

shading interp

camlight headlight
lighting phong

axis equal
axis off
view(90,39)

set(gca,'FontSize',30)
set(gcf,'Position',[200,300,800,600])

% ==========================================================
% ====== COLORBAR ==========================================
% ==========================================================
h = colorbar;
h.Position = [0.85, 0.342, 0.03, 0.25];

ticks = linspace(min(Rnew(:)), max(Rnew(:)), 4);
h.Ticks = ticks;
h.TickLabels = arrayfun(@(x) sprintf('%.3f',x), ticks, 'UniformOutput', false);

% ==========================================================
% ====== ARROWS ============================================
% ==========================================================
flex_factor = 1.5;
maxR = max(R(:));

hold on

mArrow3([0 0 0], [flex_factor*maxR 0 0], ...
    'color','red','stemWidth',maxR/100,'facealpha',0.5);

mArrow3([0 0 0], [0 flex_factor*maxR 0], ...
    'color','green','stemWidth',maxR/100);

mArrow3([0 0 0], [0 0 flex_factor*maxR], ...
    'color','blue','stemWidth',maxR/100);

text(flex_factor*maxR,0,0,'x','FontSize',35)
text(0,flex_factor*maxR,0,'y','FontSize',35)
text(0,0,flex_factor*maxR,'z','FontSize',35)

hold off
