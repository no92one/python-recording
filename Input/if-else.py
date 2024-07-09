# x = 10
# y = 10

# if x > y:
#     print('X är större än Y')
# elif x == y:
#     print('X är lika mycket som Y')
# else:
#     print('X är mindre än Y')

print('Ange din ålder:')

age = int(input())

if age < 5 :
    print('Du ska gå på förskola.')
elif age < 12:
    print('Du ska gå på lågstadiet')
elif age < 16:
    print('Du ska gå på högstadiet')
elif age < 19:
    print('Du ska gå på gymnasiet')
else:
    print('Du kan kan få ansöka om att läsa på högskola eller universitet.')