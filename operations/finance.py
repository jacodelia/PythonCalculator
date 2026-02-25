import math
from typing import Optional


class FinanceOperations:
    @staticmethod
    def simple_interest(principal: float, rate: float, time: float) -> float:
        return principal * (1 + (rate / 100) * time)

    @staticmethod
    def simple_interest_rate(principal: float, final_amount: float, time: float) -> Optional[float]:
        if time == 0:
            return None
        return ((final_amount / principal) - 1) / time * 100

    @staticmethod
    def compound_interest(principal: float, rate: float, time: float, n: int = 12) -> float:
        return principal * math.pow(1 + (rate / 100) / n, n * time)

    @staticmethod
    def effective_annual_rate(nominal_rate: float, n: int) -> float:
        return (math.pow(1 + (nominal_rate / 100) / n, n) - 1) * 100

    @staticmethod
    def present_value(future_value: float, rate: float, time: float, n: int = 12) -> float:
        return future_value / math.pow(1 + (rate / 100) / n, n * time)

    @staticmethod
    def future_value(present_value: float, rate: float, time: float, n: int = 12) -> float:
        return present_value * math.pow(1 + (rate / 100) / n, n * time)

    @staticmethod
    def net_present_value(rate: float, cash_flows: list) -> float:
        npv = 0
        for i, cf in enumerate(cash_flows):
            npv += cf / math.pow(1 + (rate / 100), i + 1)
        return npv

    @staticmethod
    def internal_rate_of_return(cash_flows: list, guess: float = 0.1) -> Optional[float]:
        def npv_at_rate(rate):
            return sum(cf / math.pow(1 + rate, i) for i, cf in enumerate(cash_flows))
        
        rate = guess
        for _ in range(100):
            npv = npv_at_rate(rate)
            if abs(npv) < 0.0001:
                return rate * 100
            derivative = sum(-i * cf / math.pow(1 + rate, i + 1) for i, cf in enumerate(cash_flows))
            if derivative == 0:
                return None
            rate = rate - npv / derivative
        return None

    @staticmethod
    def payment(principal: float, rate: float, n_periods: int) -> Optional[float]:
        if rate == 0:
            return principal / n_periods
        r = rate / 100 / 12
        return principal * (r * math.pow(1 + r, n_periods)) / (math.pow(1 + r, n_periods) - 1)

    @staticmethod
    def total_payment(principal: float, rate: float, n_periods: int) -> Optional[float]:
        pmt = FinanceOperations.payment(principal, rate, n_periods)
        return pmt * n_periods if pmt else None

    @staticmethod
    def total_interest(principal: float, rate: float, n_periods: int) -> Optional[float]:
        total = FinanceOperations.total_payment(principal, rate, n_periods)
        return total - principal if total else None

    @staticmethod
    def remaining_balance(principal: float, rate: float, n_periods: int, payments_made: int) -> Optional[float]:
        if payments_made >= n_periods:
            return 0
        r = rate / 100 / 12
        pmt = FinanceOperations.payment(principal, rate, n_periods)
        if pmt is None:
            return None
        return principal * math.pow(1 + r, payments_made) - pmt * (math.pow(1 + r, payments_made) - 1) / r

    @staticmethod
    def depreciation_straight_line(cost: float, salvage: float, life: float) -> float:
        return (cost - salvage) / life

    @staticmethod
    def depreciation_declining_balance(cost: float, rate: float, life: float, period: int) -> float:
        factor = rate / 100
        return cost * math.pow(1 - factor, period - 1) * factor

    @staticmethod
    def depreciation_double_declining_balance(cost: float, life: float, period: int) -> float:
        factor = 2 / life
        if period == 1:
            return cost * factor
        prev = cost * factor
        for _ in range(1, period):
            prev *= (1 - factor)
        return prev

    @staticmethod
    def depreciation_sum_of_years(cost: float, salvage: float, life: float, period: int) -> Optional[float]:
        if period > life:
            return None
        depreciable_base = cost - salvage
        sum_of_years = life * (life + 1) / 2
        return depreciable_base * (life - period + 1) / sum_of_years

    @staticmethod
    def break_even(fixed_costs: float, variable_cost_per_unit: float, price_per_unit: float) -> Optional[float]:
        if price_per_unit <= variable_cost_per_unit:
            return None
        return fixed_costs / (price_per_unit - variable_cost_per_unit)

    @staticmethod
    def profit_margin(revenue: float, costs: float) -> float:
        if revenue == 0:
            return 0
        return ((revenue - costs) / revenue) * 100

    @staticmethod
    def markup(costs: float, selling_price: float) -> float:
        if costs == 0:
            return 0
        return ((selling_price - costs) / costs) * 100

    @staticmethod
    def roi(initial_investment: float, final_value: float) -> float:
        if initial_investment == 0:
            return 0
        return ((final_value - initial_investment) / initial_investment) * 100

    @staticmethod
    def cagr(start_value: float, end_value: float, periods: float) -> Optional[float]:
        if start_value <= 0 or periods == 0:
            return None
        return (math.pow(end_value / start_value, 1 / periods) - 1) * 100

    @staticmethod
    def pmt_loan(principal: float, annual_rate: float, years: int) -> Optional[float]:
        if annual_rate == 0:
            return principal / (years * 12)
        monthly_rate = annual_rate / 100 / 12
        n_payments = years * 12
        return principal * (monthly_rate * math.pow(1 + monthly_rate, n_payments)) / (math.pow(1 + monthly_rate, n_payments) - 1)

    @staticmethod
    def future_value_annuity(pmt: float, rate: float, years: int) -> float:
        if rate == 0:
            return pmt * years * 12
        r = rate / 100 / 12
        n = years * 12
        return pmt * (math.pow(1 + r, n) - 1) / r

    @staticmethod
    def present_value_annuity(pmt: float, rate: float, years: int) -> float:
        if rate == 0:
            return pmt * years * 12
        r = rate / 100 / 12
        n = years * 12
        return pmt * (1 - math.pow(1 + r, -n)) / r

    @staticmethod
    def tip_calculator(bill: float, tip_percent: float, num_people: int) -> Optional[float]:
        if num_people == 0:
            return None
        tip = bill * (tip_percent / 100)
        total = bill + tip
        return total / num_people

    @staticmethod
    def tax_calculator(amount: float, tax_rate: float) -> float:
        return amount * (1 + tax_rate / 100)

    @staticmethod
    def discount(original_price: float, discount_percent: float) -> float:
        return original_price * (1 - discount_percent / 100)

    @staticmethod
    def sales_tax(amount: float, tax_rate: float) -> float:
        return amount * (tax_rate / 100)
