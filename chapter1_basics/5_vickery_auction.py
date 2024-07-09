# Chapter : 1 - item : 5 - vickrey auction

# จงสร้าง vickrey auction แบบจำลอง
# Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

# word
# "Enter All Bid : "
# "not enough bidder"
# "error : have more than one highest bid"
# "winner bid is $ need to pay $"

input_string = input("Enter All Bid : ")

bids = [int(n) for n in input_string.split(" ")]

if bids.__len__() < 2:
    print("not enough bidder")
    exit(1)

bids.sort(reverse=True)
max_bid = bids[0]
max_bid_count = 0
for i in bids:
    if i == max_bid:
        max_bid_count += 1
    elif max_bid_count > 1:
        print("error : have more than one highest bid")
        exit(1)
    elif max_bid_count == 1:
        print(f"winner bid is {max_bid} need to pay {i}")
        exit(0)
