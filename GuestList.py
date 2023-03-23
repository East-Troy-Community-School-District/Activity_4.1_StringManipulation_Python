'''
Guest List
Pawelski
3/23/2023
Python II
'''

guest_list = "Mass Leising Pawelski Hoff Keuhn"
name = input("Enter your name >> ").strip()

if name in guest_list:
    print("You are on the guest list.")
if name not in guest_list:
    print("You are not on the guest list.")