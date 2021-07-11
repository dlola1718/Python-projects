
fid = fopen ('data1.xlsx', 'r')
fid = fopen ('reg1.txt', 'w')
A = []
for i = 1:4
  x = data1(:,i);
  for j = 2:5
      y = data1(:,j);
      p = polyfit(x,y,1);
      yfit = polyval(p,x);
      yresid = y - yfit;
      ssresid = sum(yresid.^2);
      A(:,end+1) = ([i; j; ssresid]);
  end
en
reg1 = xlswrite('reg.xlsx', A);