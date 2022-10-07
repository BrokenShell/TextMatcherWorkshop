from app.model import TextMatcher
from app.test_data import biographies
from app.train_data import archetypes


matcher = TextMatcher(archetypes)
for name, description in biographies.items():
    print(f"{name}: {matcher(description)}")
