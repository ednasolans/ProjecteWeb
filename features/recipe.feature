Feature: Gestión de recetas

  Scenario: Crear una receta
    Given estoy logueado como "user1" con la contraseña "testpass123"
    When creo una receta llamada "Tortilla" con la descripción "Tortilla de patatas"
    Then debería ver la receta con título "Tortilla"

  Scenario: Editar una receta existente
    Given estoy logueado como "user1" con la contraseña "testpass123"
    And ya tengo una receta llamada "Tortilla"
    When cambio el título a "Tortilla Española"
    Then debería ver la receta con título "Tortilla Española"

  Scenario: Eliminar una receta guardada
    Given estoy logueado como "user1" con la contraseña "testpass123"
    And tengo guardada una receta llamada "Tortilla Española"
    When elimino la receta guardada
    Then no debería ver "Tortilla Española" en mi colección
