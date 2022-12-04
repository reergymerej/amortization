#!/usr/bin/env python

from typing import List, Tuple


def get_monthly_payment(
    annual_interest: float,
    loan_amount: int,
    years: int,
) -> float:
    monthly_interest_payment = annual_interest / 12
    number_of_payments = years * 12
    n = number_of_payments
    i = monthly_interest_payment

    group = ((1 + i)**n)
    top = i * group
    bottom = group - 1
    formula = top / bottom
    return loan_amount * formula


def get_principle_payment(
    total_monthly_payment: float,
    outstanding_loan_balance: float,
    annual_interest: float,
) -> float:
    monthly_interest_rate = annual_interest / 12
    return total_monthly_payment - (
        outstanding_loan_balance * monthly_interest_rate
    )

def get_interest_and_principle_from_payment(
    total_monthly_payment: float,
    outstanding_loan_balance: float,
    annual_interest: float,
) -> Tuple[float, float]:
    principle_payment = get_principle_payment(
        total_monthly_payment,
        outstanding_loan_balance,
        annual_interest,
    )
    return (
        total_monthly_payment - principle_payment,
        principle_payment,
    )


def split_into_chunks(value: str, chunk_size: int) -> List[str]:
    start = 0
    end = len(value)
    chunks = []
    for i in range(start, end, chunk_size):
        chunks.append(
            value[i:i+chunk_size]
        )
    return chunks

def add_commas(value: str) -> str:
    rev = value[::-1]
    chunks = split_into_chunks(rev, 3)
    joined = ','.join(chunks)
    return joined[::-1]

def currency(value: float, width: int) -> str:
    with_commas = add_commas(str(int(value)))
    space_needed = width - len(with_commas) - 1
    space = ' ' * space_needed
    return f'${space}{with_commas}'

def print_col(
    value: float,
    width: int,
) -> None:
    print(f'\t{currency(value, width)}', end='')

def main():
    annual_interest_rate = 0.07
    loan_amount = 500000
    years = 30
    total_payment = (
        get_monthly_payment(annual_interest_rate, loan_amount, years)
    )
    loan_balance = loan_amount

    for period in range(years * 12):
        print(f'{period + 1}', end='')
        print_col(loan_balance, 10)
        print_col(total_payment, 8)
        interest, principle = get_interest_and_principle_from_payment(
            total_payment,
            loan_balance,
            annual_interest_rate,
        )
        print_col(interest, 8)
        print_col(principle, 8)
        next_balance = loan_balance - principle
        print_col(next_balance, 10)
        print('')
        loan_balance = next_balance


if __name__ == '__main__':
    main()
