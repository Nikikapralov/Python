amount_guests = int(input())
regular = set()
vip = set()
for _ in range(amount_guests):
    guest = input()
    if len(guest) == 8:
        if guest[0].isdigit():
            vip.add(guest)
        else:
            regular.add(guest)
while True:
    arrival = input()
    if arrival == 'END':
        break
    elif arrival in regular:
        regular.remove(arrival)
    elif arrival in vip:
        vip.remove(arrival)

guests_who_never_came = len(regular) + len(vip)
print(guests_who_never_came)
regular = sorted(regular)
vip = sorted(vip)
[print(vip_skipper) for vip_skipper in vip]
[print(regular_no_show) for regular_no_show in regular]
