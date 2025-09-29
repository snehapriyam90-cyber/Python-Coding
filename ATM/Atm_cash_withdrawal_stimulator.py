amount=int(input())
if amount%100 != 0:
    print("Invalid Amount")
else:
    notes=[2000,500,100]
    for note in notes:
        count=amount//note
        if count>0:
            print(f"{note} x {count}")
            amount=amount%note
            