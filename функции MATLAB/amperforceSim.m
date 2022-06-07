% amperforce - �������, ����������� �������� ����  ������ 
%(������� - Fa = IBLsin(alpha))
% graphic - �������, ������������ �������� I, B, L � �������� ������ ��
% ������� ���������
% label - �������, ���������� �����, ���������� ��� � ������ �������
% �������
% �������� ����� ����� �������� �������� alpha, ������������� ���������
% �������� I, B, L � ��� ����� ��� ������� �������
%%
hold on
alpha = 0:0.2:10;
coef = 1; 
lines = ["r-x","g-s","y-*","b-o"];
legendItems = strings;
listAns = [ans1; ans195; ans337; ans535];
for i = 1:(length(lines))
    a = listAns(i*2,1:51);
    legendItems(i) = num2str(graphic(alpha, a, coef, lines(i)))+"sin(alpha)";
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

function F = graphic(x,answer,coef,str)
I = 1*coef;
B = 2*coef;
L = 0.5*coef;
F = I*B*L;
plot(x,answer,str);
end