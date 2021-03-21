import pytest

from typing import List
from mimesis.random import Random
from databases import Database

from tests.common.constants import INGREDIENT_NAME_LENGTH, INGREDIENT_DESCRIPTION_LENGTH
from app.db.repositories.ingredient_repository import IngredientRepository
from app.models.ingredient import IngredientModel


@pytest.fixture
async def test_ingredient(db: Database, random_generator: Random) -> IngredientModel:
    repo = IngredientRepository(db)

    return await repo.create_ingredient(
        IngredientModel(
            name=random_generator.randstr(length=INGREDIENT_NAME_LENGTH),
            description=random_generator.randstr(length=INGREDIENT_DESCRIPTION_LENGTH),
        )
    )


@pytest.fixture
async def test_multiple_ingredients(
    db: Database, random_generator: Random
) -> List[IngredientModel]:
    repo = IngredientRepository(db)
    ingredients = []

    for _ in range(0, 500):
        ingredient = await repo.create_ingredient(
            IngredientModel(
                name=random_generator.randstr(length=INGREDIENT_NAME_LENGTH),
                description=random_generator.randstr(
                    length=INGREDIENT_DESCRIPTION_LENGTH
                ),
            )
        )

        ingredients.append(ingredient)

    return ingredients
