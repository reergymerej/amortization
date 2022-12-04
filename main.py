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

def align_left(value: str, width: int) -> str:
    space_needed = width - len(value)
    space = ' ' * space_needed
    return f'{value}{space}'


def justify(left: str, right: str, width: int) -> str:
    space_needed = width - len(right) - len(left)
    space = ' ' * space_needed
    return f'{left}{space}{right}'


def currency(value: float, width: int) -> str:
    with_commas = add_commas(str(int(value)))
    return justify('$', with_commas, width)

def print_col(
    value: float,
    width: int,
) -> None:
    prefix = '\t'
    print(f'{prefix}{currency(value, width)}', end='')


header_padding = 4

def print_header(columns: List[str]) -> None:
    for i, c in enumerate(columns):
        prefix = i != 0 and '\t' or ''
        print(f'{prefix}{align_left(c, len(c) + header_padding)}', end='')
    print('')


def main():
    annual_interest_rate = 0.07
    loan_amount = 500000
    years = 30
    total_payment = (
        get_monthly_payment(annual_interest_rate, loan_amount, years)
    )
    loan_balance = loan_amount

    columns = [
        'period',
        'beginning balance',
        'total payment',
        'interest',
        'principle',
        'next balance',
    ]
    print_header(columns)

    for period in range(years * 12):
        print(f'{align_left(str(period + 1), len(columns[0]) + header_padding)}', end='')

        print_col(loan_balance, len(columns[1]) + header_padding)
        print_col(total_payment, len(columns[2]) + header_padding)
        interest, principle = get_interest_and_principle_from_payment(
            total_payment,
            loan_balance,
            annual_interest_rate,
        )
        print_col(interest, len(columns[3]) + header_padding)
        print_col(principle, len(columns[4]) + header_padding)
        next_balance = loan_balance - principle
        print_col(next_balance, len(columns[5]) + header_padding)
        print('')
        loan_balance = next_balance
    print_header(columns)


if __name__ == '__main__':
    main()
