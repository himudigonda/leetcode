class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        coupons = []
        for code, business, status in zip(code, businessLine, isActive):
            # if status and business in order and code and re.fullmatch(r"\w+", code):
            #     coupons.append((code, business))
            if status and business in order and code:
                if all(ch.isalnum() or ch == "_" for ch in code):
                    coupons.append((code, business))

        coupons = sorted(coupons, key=lambda x: (order[x[1]], x[0]))
        return [coupon[0] for coupon in coupons]
