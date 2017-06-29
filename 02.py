#2-1
d = 89000 * 100
n = 751000 * 20
t = d + n
print(t)

#2-2
t2 = 89000 * 100 * 0.05 + 751000 * 20 * 0.1
print(t2)

#2-3
print((50 - 32)/1.8)

#2-4  
print('pizza\n' * 10)

#2-5
n = 1000000
n = n - (n * 0.3)
n = n - (n * 0.3)
n = n - (n * 0.3)
print(n)

#2-7
s = "Daum KaKao"
s = s[5:] + " " + s[:4]
print(s)

#2-8
a = "hello wowrld"
a = "hi " + a[6:]
print(a)

#2-9
x = "abcdef"
x = x[1:] + x[0]
print(x)

interest = ["삼성전자", "LG전자", "네이버"]

interest2 = interest
print(interest)
interest[0] = 1
print(interest)
print(interest2)

a = 1
b = a
a = 2
print(a)
print(b)

a = ['1'] * 10
a = [0,1,2,3,4,5,6,7,8,9]
print(a)
print(len(a))
print("a[11]", a[9])
c = a * 100
print(c)
print(len(c))

kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
print("시가총액 5위: ", kospi_top10[4])
kospi_top5 = kospi_top10[0:5]
print(kospi_top5)
kospi_top10[0] = kospi_top10[0] + "s"
print(kospi_top10[0:5])
print(kospi_top5)

str = "01234"
str2 = str[0:2]
print(str)
print("str2", str2)
print(str2[0])
# str2[0] = "k"
print("str:", str)
print(str2)


kospi_top10.append('SK텔레콤')
print(kospi_top10)