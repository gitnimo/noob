from urllib import parse
stre="我是一隻小鳥"
A=parse.quote(stre)
B=parse.unquote(A)
print(A)
print(B)