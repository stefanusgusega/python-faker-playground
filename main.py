"""
This module is used as the main entry for the project
"""

from faker import Faker
from icecream import ic

if __name__ == "__main__":
    LOCALE_USED = "id_ID"
    SEED = 42

    faker = Faker(LOCALE_USED)
    faker.seed_instance(SEED)
    names = [faker.unique.name() for _ in range(10)]
    ic(names)
