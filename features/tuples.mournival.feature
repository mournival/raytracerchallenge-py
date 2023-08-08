Feature: Mournival modificiations to Tuples, Vectors, and Points

  Scenario: Normalizing vector(1, 2, 3) (approximately)
    Given v ← vector(1/√14, 2/√14, 3/√14)
    When norm ← normalize(v)
    Then norm = approximately vector(0.26726, 0.53452, 0.80178)

  Scenario: The magnitude of a normalized vector
    Given v ← vector(1, 2, 3)
    When norm ← normalize(v)
    Then magnitude(norm) = 1

  Scenario: The magnitude of a normalized vector (approximately)
    Given v ← vector(1, 2, 3)
    When norm ← normalize(v)
    Then magnitude(norm) = approximately 1

  Scenario: Normalizing vector(4, 0, 0) gives (1, 0, 0)
    Given v ← vector(4, 0, 0)
    When norm ← normalize(v)
    Then norm = vector(1, 0, 0)

  Scenario: Normalizing vector(4, 0, 0) gives (1, 0, 0) (approximately)
    Given v ← vector(4, 0, 0)
    When norm ← normalize(v)
    Then norm = approximately vector(1, 0, 0)