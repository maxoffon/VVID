% amperforce - ‘ункци€, вычисл€юща€ значение силы  ампера 
%(формула - Fa = IBLsin(alpha))
% graphic - функци€, определ€юща€ значени€ I, B, L и стро€ща€ график по
% текущим значени€м
% label - функци€, включающа€ сетку, называюща€ оси и дающа€ легенду
% графику
% ќсновна€ часть задаЄт интервал значений alpha, интенсивность изменени€
% значений I, B, L и тип линий дл€ каждого графика
%%
hold on
alpha = 0:0.2:10;
coef = 1; 
lines = ["r-x","g-s","y-*","b-o"];
legendItems = strings;
for i = 1:(length(lines))
    legendItems(i) = num2str(graphic(alpha,coef,lines(i)))+"sin(alpha)";
    coef = coef + 0.25;
end
label(legendItems);
hold off

function L = label(coefs)
xlabel("Alpha")
ylabel("Amper Force")
title("Fa = I*B*L*sin(alpha)")
grid("on")
legend(coefs);
end

function F = graphic(x,coef,str)
I = 1*coef;
B = 2*coef;
L = 0.5*coef;
F = I*B*L;
Fa = amperforceFunction(I,B,L,x);
plot(x,Fa,str);
end

function Fa = amperforceFunction(I,B,l,alpha)
Fa = I.*B.*l.*sin(alpha);
end