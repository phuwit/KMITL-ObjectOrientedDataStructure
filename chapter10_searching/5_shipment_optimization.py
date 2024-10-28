"""
มีสินค้าอยู่ n ชิ้น โดยชิ้นที่ i (0 <= i < n) มีน้ำหนัก Wi กิโลกรัม  นำสินค้าบรรจุใส่กล่องไม่เกิน k ใบ โดยมีเงื่อนไขว่า
1. สิ่งของต้องมีน้ำหนักรวมกันไม่เกินน้ำหนักมากสุดที่กล่องรับไหว
2. หากสิ่งของชิ้นที่ a และชิ้นที่ b อยู่ในกล่องเดียวกัน (a <= b) สิ่งของทุกชิ้นที่อยู่ระหว่างสองชิ้นนี้ (ทุกชิ้นที่ i ที่ a < i < b) จะต้องอยู่ในกล่องนี้ด้วย (นั่นคือสิ่งที่ของในกล่องเดียวกันจะต้องเป็นสิ่งของที่ตำแหน่งติดกัน)

ถ้าทุกกล่องสามารถรับน้ำหนักได้เท่ากัน จงหาว่าเราสามารถใช้กล่องที่รับน้ำหนักได้น้อยสุดเท่าใด โดยที่ยังบรรจุของตามเงื่อนไขได้ และใช้กล่องครบทุกใบ

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง สินค้า n ชิ้น และแต่ละชิ้นมีน้ำหนัก W กิโลกรัม
    -   ด้านขวาหมายถึง จำนวนกล่อง k ใบ

คำใบ้  Optimization Problem

อธิบาย Test Case #1

มีสินค้าอยู่ 5 ชิ้น โดยมีน้ำหนักเป็น 6 2 4 3 7 ตามลำดับ และมีกล่องจำนวน 3 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 8 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 6 และ 2   กล่องใบที่ 2 จะใส่สินค้า 2 ชิ้นที่มำน้ำหนัก 4 และ 3  และกล่องใบที่ 3 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 7

อธิบาย Test Case #2

มีสินค้าอยู่ 10 ชิ้น โดยมีน้ำหนักเป็น 8 7 2 5 1 10 9 2 3 5 ตามลำดับ และมีกล่องจำนวน 5 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 14 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 8   กล่องใบที่ 2 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 7 2 และ 5   กล่องใบที่ 3 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 1 และ 10   กล่องใบที่ 4 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 9 2 และ 3    และกล่องใบที่ 5 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 5


psuedocode from daddy gpt

Binary Search on Maximum Weight:
We will use binary search to find the minimum possible maximum weight capacity that allows us to pack all items into k boxes.

Greedy Check:
For each candidate maximum weight (from the binary search), use a greedy algorithm to check if it's possible to pack all items into k boxes without exceeding the candidate weight.

function find_min_max_weight(weights, k):
    low = max(weights)
    high = sum(weights)

    while low < high:
        mid = (low + high) // 2
        if can_pack(weights, k, mid):
            high = mid
        else:
            low = mid + 1

    return low

function can_pack(weights, k, max_weight):
    current_weight = 0
    box_count = 1

    for weight in weights:
        if current_weight + weight > max_weight:
            box_count += 1
            current_weight = weight
            if box_count > k:
                return False
        else:
            current_weight += weight

    return True
"""


class Box:
    def __init__(self, weights) -> None:
        self.weights = weights
        self.weight = sum(weights)

    def __str__(self) -> str:
        return f"{str(self.weights)}: {self.weight}"

    def add_weight(self, weight: int):
        self.weights.append(weight)
        self.weight += weight


class Pallet:
    def __init__(self) -> None:
        self.boxes: list[Box] = []

    def get_max_weight(self):
        return max(map(lambda box: box.weight, self.boxes))


class Shipment:
    def __init__(self, all_weights, boxes_per_pallet: int) -> None:
        self.all_weights = all_weights
        self.boxes_per_pallet = boxes_per_pallet

    def can_pack(self, max_capacity: int):
        pallet = Pallet()
        accumulated_weight = 0
        box_used = 1

        for weight in self.all_weights:
            if weight + accumulated_weight > max_capacity:
                box_used += 1
                accumulated_weight = weight
                if box_used > self.boxes_per_pallet:
                    return False
                continue

            accumulated_weight += weight
            continue

        return True

    def find_min_max_weight(self):
        min_box_capacity = max(self.all_weights)
        max_box_capacity = sum(self.all_weights)

        while min_box_capacity < max_box_capacity:
            testing_max_capacity = (min_box_capacity + max_box_capacity) // 2
            if self.can_pack(testing_max_capacity):
                max_box_capacity = testing_max_capacity
                continue

            min_box_capacity = testing_max_capacity + 1
            continue

        return min_box_capacity


item_weights, boxes_count = input("Enter Input : ").split("/")
shipment = Shipment(list(map(int, item_weights.split())), int(boxes_count))
result = shipment.find_min_max_weight()
print(f"Minimum weigth for {boxes_count} box(es) = {result}")
