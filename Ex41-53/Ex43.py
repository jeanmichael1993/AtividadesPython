"""
Write a sales help program. From a total value read, show:
the total payable with a 10% discount.
the value of each installment, in 3 installments without interest.
the seller's commission, in case the sale is seen (5% of the discounted value).
the seller's commission, in case the sale is made in installments (5% of the total amount).
"""

total_value: float = float(input("Write a total value: "))
discount: float = total_value - (total_value*0.10)
print(f"The value payable with a 10% discont: {discount:.2f}")
print(f"The value of each installment is: {(total_value/3):.2f}")
print(f"The seller's commission, in case the sale is seen: {(discount*0.05):.2f}")
print(f"The seller's commission, in case the sale is made in installments is: {(total_value*0.05):.2f}")